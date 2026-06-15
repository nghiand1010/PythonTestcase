#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Check HTML error on test_data page
"""

from playwright.sync_api import sync_playwright
import sys

TICA_BASE = "https://oj.tica.edu.vn"
TICA_LOGIN = f"{TICA_BASE}/accounts/login/"
USERNAME = "thinhdt"
PASSWORD = "Th09051989@"

def check_problem(problem_id):
    """Check HTML của trang test_data"""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        
        # Login
        print("🔐 Đăng nhập...")
        page.goto(TICA_LOGIN)
        page.fill('input[name="username"]', USERNAME)
        page.fill('input[name="password"]', PASSWORD)
        page.click('button[type="submit"]')
        page.wait_for_load_state('networkidle')
        print("✅ Đã đăng nhập")
        
        # Go to test_data page
        test_data_url = f"{TICA_BASE}/problem/{problem_id}/test_data"
        print(f"\n🌐 Mở: {test_data_url}")
        page.goto(test_data_url)
        page.wait_for_load_state('networkidle')
        
        # Get HTML content
        html = page.content()
        
        # Check for errors
        if "Input file for case" in html and "does not exist" in html:
            print("\n⚠️  PHÁT HIỆN LỖI:")
            # Extract error messages
            lines = html.split('\n')
            for line in lines:
                if "Input file for case" in line and "does not exist" in line:
                    # Try to extract the error message
                    import re
                    matches = re.findall(r'Input file for case \d+ does not exist: \w+\.in', line)
                    for match in matches:
                        print(f"  - {match}")
        
        # Check số lượng testcases
        all_checkboxes = page.locator('input[type="checkbox"][name*="-DELETE"]')
        test_count = all_checkboxes.count()
        print(f"\n📊 Số testcases hiện tại: {test_count}")
        
        # List all testcases
        print("\n📋 Danh sách testcases:")
        for i in range(test_count):
            checkbox = all_checkboxes.nth(i)
            name = checkbox.get_attribute('name')
            print(f"  {i+1}. {name}")
        
        browser.close()

if __name__ == "__main__":
    problem_id = sys.argv[1] if len(sys.argv) > 1 else "nhonhatchia36"
    check_problem(problem_id)
