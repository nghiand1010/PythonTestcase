#!/usr/bin/env python3
"""Lấy HTML và phân tích lỗi chi tiết"""

from playwright.sync_api import sync_playwright
import time

problem_id = "thangmay"
url = f"https://oj.tica.edu.vn/problem/{problem_id}/test_data"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    
    # Login
    print("🔐 Đăng nhập...")
    page.goto("https://oj.tica.edu.vn/accounts/login/")
    page.fill('input[name="username"]', 'thinhdt')
    page.fill('input[name="password"]', 'Th09051989@')
    page.click('button[type="submit"]')
    time.sleep(2)
    
    # Mở test_data page
    print(f"🌐 Mở: {url}")
    page.goto(url)
    time.sleep(3)
    
    # Lấy HTML
    html = page.content()
    
    # Lưu HTML
    html_file = f"debug_html_{problem_id}.html"
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"💾 Đã lưu HTML: {html_file}")
    
    # Phân tích lỗi
    print("\n📊 PHÂN TÍCH LỖI:")
    print("="*60)
    
    # 1. Kiểm tra console.error
    if 'console.error("Failed to open as ZIP file"' in html:
        print("❌ Error: Failed to open as ZIP file")
    
    # 2. Kiểm tra errorlist
    if 'ul.errorlist' in html or 'class="errorlist"' in html:
        print("❌ Error: errorlist CSS found")
    
    # 3. Kiểm tra các dòng có "does not exist"
    import re
    errors = re.findall(r'(Input file for case \d+ does not exist|Output file for case \d+ does not exist)', html)
    if errors:
        print(f"❌ File errors ({len(errors)}):")
        for err in errors[:5]:  # Show first 5
            print(f"   - {err}")
    
    # 4. Đếm input fields
    input_fields = page.locator('input[name*="input_file"]').all()
    print(f"\n📊 Tổng số input fields: {len(input_fields)}")
    
    output_fields = page.locator('input[name*="output_file"]').all()
    print(f"📊 Tổng số output fields: {len(output_fields)}")
    
    # 5. Kiểm tra có bao nhiêu testcases
    checkboxes = page.locator('input[type="checkbox"][name*="cases-"]')
    test_count = 0
    for i in range(checkboxes.count()):
        name = checkboxes.nth(i).get_attribute('name')
        if '__prefix__' not in name:
            test_count += 1
    print(f"📊 Số testcases: {test_count}")
    
    # 6. Tìm các đoạn HTML chứa error message
    print("\n🔍 TÌM ERROR MESSAGES:")
    error_lines = [line for line in html.split('\n') if 'does not exist' in line.lower() or 'error' in line.lower()]
    for line in error_lines[:10]:  # Show first 10
        line = line.strip()
        if line and len(line) < 200:
            print(f"   {line[:150]}")
    
    print(f"\n⏸️  Đợi 30s để bạn xem trang...")
    time.sleep(30)
    
    browser.close()
