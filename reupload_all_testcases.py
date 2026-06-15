#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
XÓA VÀ UPLOAD LẠI TESTCASES
Xóa toàn bộ testcases cũ và upload lại ZIP
"""

from playwright.sync_api import sync_playwright
import time
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent.absolute()
PROBLEMS_DIR = SCRIPT_DIR / "problems"
USERNAME = "thinhdt"
PASSWORD = "Th09051989@"

# 5 bài đã upload ZIP nhưng chưa nhấn Apply
PROBLEMS = [
    "bupbe", "chon_2stong", "cuahang_sohoc", "nhonhatchia36", "tuikeo_nguyenkhoa"
]

def check_for_errors(page):
    """Kiểm tra có error trên trang không"""
    html = page.content()
    
    # Kiểm tra error message trong HTML
    if 'Failed to open as ZIP file' in html:
        print("  ⚠️  Error: Failed to open as ZIP file")
        return True
    
    # Kiểm tra errorlist
    if 'ul.errorlist' in html or 'class="errorlist"' in html:
        print("  ⚠️  Error: errorlist found in HTML")
        return True
    
    # Kiểm tra input/output fields bị error (có ô đỏ)
    error_inputs = page.locator('input[type="text"].errorlist, input[type="text"][style*="border-color: red"], input[type="text"][style*="border: 1px solid red"]')
    if error_inputs.count() > 0:
        print(f"  ⚠️  Error: {error_inputs.count()} input fields có lỗi (border đỏ)")
        return True
    
    # Kiểm tra input file không tồn tại
    if 'Input file for case' in html and 'does not exist' in html:
        print("  ⚠️  Error: Input file does not exist")
        return True
    
    if 'Output file for case' in html and 'does not exist' in html:
        print("  ⚠️  Error: Output file does not exist")
        return True
    
    return False

def delete_and_upload(page, problem_id, retry=False):
    """Chỉ nhấn Apply để xử lý ZIP đã upload trước đó"""
    print(f"\n{'='*60}")
    print(f"🔄 {problem_id}")
    print(f"{'='*60}")
    
    # Mở test_data page
    url = f"https://oj.tica.edu.vn/problem/{problem_id}/test_data"
    print(f"🌐 Mở: {url}")
    page.goto(url)
    page.wait_for_load_state("networkidle")
    
    # Chỉ nhấn Apply để xử lý ZIP đã upload trước đó
    print("🔘 Nhấn Apply để xử lý ZIP đã upload...")
    apply_button = page.locator('input[type="submit"][value="Apply!"]')
    apply_button.click()
    print("   ✓ Đã nhấn Apply, đợi xử lý...")
    time.sleep(5)
    page.wait_for_load_state("networkidle")
    
    # Reload và kiểm tra testcases đã có chưa
    print("🔍 Reload và kiểm tra testcases...")
    page.reload()
    time.sleep(2)
    page.wait_for_load_state("networkidle")
    
    all_checkboxes = page.locator('input[type="checkbox"][name*="cases-"]')
    test_count = 0
    for i in range(all_checkboxes.count()):
        name = all_checkboxes.nth(i).get_attribute('name')
        if '__prefix__' not in name and 'DELETION' not in name:
            test_count += 1
    
    print(f"   📊 Số testcases: {test_count}")
    
    if test_count > 0:
        print("✅ THÀNH CÔNG - Testcases đã xuất hiện!")
        return True
    else:
        print("❌ THẤT BẠI - Chưa có testcases")
        return False

def main():
    print("="*60)
    print("🔄 XÓA VÀ UPLOAD LẠI TESTCASES")
    print("="*60)
    print(f"\n📋 Xử lý {len(PROBLEMS)} bài\n")
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        # Login
        print("🔐 Đăng nhập TICA OJ...")
        page.goto("https://oj.tica.edu.vn/accounts/login/")
        page.fill('input[name="username"]', USERNAME)
        page.fill('input[name="password"]', PASSWORD)
        page.click('button[type="submit"]')
        page.wait_for_load_state('networkidle')
        print("✅ Đã đăng nhập\n")
        
        success = []
        failed = []
        
        for i, problem_id in enumerate(PROBLEMS, 1):
            print(f"\n[{i}/{len(PROBLEMS)}] Processing: {problem_id}")
            
            try:
                if delete_and_upload(page, problem_id):
                    success.append(problem_id)
                else:
                    failed.append(problem_id)
            except Exception as e:
                print(f"❌ Lỗi: {e}")
                failed.append(problem_id)
            
            print("⏸️  Đợi 2s trước bài tiếp theo...")
            time.sleep(2)
        
        browser.close()
    
    # Summary
    print("\n" + "="*60)
    print("📊 KẾT QUẢ")
    print("="*60)
    print(f"✅ Thành công: {len(success)}/{len(PROBLEMS)}")
    print(f"❌ Thất bại: {len(failed)}/{len(PROBLEMS)}")
    
    if failed:
        print("\n❌ Các bài thất bại:")
        for p in failed:
            print(f"  - {p}")

if __name__ == "__main__":
    main()
