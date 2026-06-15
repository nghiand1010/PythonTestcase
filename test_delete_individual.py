#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TEST: Thử xóa từng testcase thay vì delete-all
"""

from playwright.sync_api import sync_playwright
import time

USERNAME = "thinhdt"
PASSWORD = "Th09051989@"
PROBLEM = "bupbe"

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        # Login
        print("🔐 Đăng nhập...")
        page.goto("https://oj.tica.edu.vn/accounts/login/")
        page.fill('input[name="username"]', USERNAME)
        page.fill('input[name="password"]', PASSWORD)
        page.click('button[type="submit"]')
        page.wait_for_load_state("networkidle")
        print("✅ Đã đăng nhập\n")
        
        # Mở test_data
        url = f"https://oj.tica.edu.vn/problem/{PROBLEM}/test_data"
        print(f"🌐 Mở: {url}")
        page.goto(url)
        time.sleep(2)
        
        # Đếm testcases
        all_checkboxes = page.locator('input[type="checkbox"][name*="cases-"]')
        test_count = 0
        delete_checkboxes = []
        
        for i in range(all_checkboxes.count()):
            name = all_checkboxes.nth(i).get_attribute('name')
            if '__prefix__' not in name and 'DELETION' not in name:
                test_count += 1
            elif 'DELETION_DELETE' in name and '__prefix__' not in name:
                delete_checkboxes.append(i)
        
        print(f"📊 Tìm thấy {test_count} testcases")
        print(f"📊 Tìm thấy {len(delete_checkboxes)} delete checkboxes")
        
        if len(delete_checkboxes) == 0:
            print("❌ Không có checkbox delete nào!")
            browser.close()
            return
        
        # Thử check tất cả delete checkboxes
        print(f"\n🗑️  Check {len(delete_checkboxes)} checkboxes...")
        for idx in delete_checkboxes:
            all_checkboxes.nth(idx).check()
        print("✓ Đã check tất cả")
        
        # Nhấn Apply
        print("\n🔘 Nhấn Apply...")
        apply_button = page.locator('input[type="submit"][value="Apply!"]')
        apply_button.click()
        print("✓ Đợi 5s...")
        time.sleep(5)
        page.wait_for_load_state("networkidle")
        
        # Reload và kiểm tra
        print("\n🔍 Reload và kiểm tra...")
        page.reload()
        time.sleep(2)
        
        all_checkboxes = page.locator('input[type="checkbox"][name*="cases-"]')
        test_count_after = 0
        for i in range(all_checkboxes.count()):
            name = all_checkboxes.nth(i).get_attribute('name')
            if '__prefix__' not in name and 'DELETION' not in name:
                test_count_after += 1
        
        print(f"📊 Còn lại: {test_count_after} testcases")
        
        if test_count_after == 0:
            print("✅ XÓA THÀNH CÔNG!")
        else:
            print(f"❌ VẪN CÒN {test_count_after} testcases")
        
        browser.close()

if __name__ == "__main__":
    main()
