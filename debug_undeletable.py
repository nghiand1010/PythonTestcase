#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DEBUG: Kiểm tra tại sao 5 bài không xóa được
"""

from playwright.sync_api import sync_playwright
import time

USERNAME = "thinhdt"
PASSWORD = "Th09051989@"

# So sánh 2 bài: 1 xóa được, 1 không xóa được
PROBLEM_SUCCESS = "dem_chia3"  # Xóa được
PROBLEM_FAIL = "bupbe"  # Không xóa được

def analyze_page(page, problem_id):
    """Phân tích trang test_data"""
    url = f"https://oj.tica.edu.vn/problem/{problem_id}/test_data"
    print(f"\n🔍 Phân tích: {problem_id}")
    print(f"   URL: {url}")
    page.goto(url)
    time.sleep(2)
    
    # Kiểm tra delete all checkbox
    delete_all = page.locator('input#delete-all')
    print(f"   Delete all checkbox: visible={delete_all.is_visible()}, enabled={delete_all.is_enabled()}")
    
    # Kiểm tra Apply button
    apply_btn = page.locator('input[type="submit"][value="Apply!"]')
    print(f"   Apply button: visible={apply_btn.is_visible()}, enabled={apply_btn.is_enabled()}")
    
    # Đếm số testcases
    testcase_rows = page.locator('table tbody tr').count()
    print(f"   Số testcases: {testcase_rows}")
    
    # Kiểm tra các checkbox delete của từng testcase
    delete_checkboxes = page.locator('input[name*="DELETION_DELETE"]')
    delete_count = delete_checkboxes.count()
    print(f"   Số checkbox delete: {delete_count}")
    
    # Lấy HTML của form
    form_html = page.locator('form').first.inner_html()
    
    # Debug: lấy toàn bộ page HTML
    full_html = page.content()
    
    # Lưu HTML để so sánh
    filename = f"debug_{problem_id}.html"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(full_html)
    print(f"   ✅ Đã lưu HTML: {filename}")

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        # Login
        print("🔐 Đăng nhập...")
        page.goto("https://oj.tica.edu.vn/accounts/login/")
        time.sleep(1)
        page.fill('input[name="username"]', USERNAME)
        page.fill('input[name="password"]', PASSWORD)
        page.click('button[type="submit"]')
        page.wait_for_load_state("networkidle")
        print("✅ Đã đăng nhập\n")
        
        # Phân tích bài xóa được
        analyze_page(page, PROBLEM_SUCCESS)
        
        # Phân tích bài không xóa được
        analyze_page(page, PROBLEM_FAIL)
        
        print("\n" + "="*60)
        print("📝 So sánh 2 file HTML để tìm khác biệt:")
        print(f"   - debug_{PROBLEM_SUCCESS}.html (xóa được)")
        print(f"   - debug_{PROBLEM_FAIL}.html (không xóa được)")
        
        browser.close()

if __name__ == "__main__":
    main()
