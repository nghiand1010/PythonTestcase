#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kiểm tra chi tiết trang test_data của chiavo_oc
"""

from playwright.sync_api import sync_playwright
import time

TICA_BASE = "https://oj.tica.edu.vn"
TICA_LOGIN = f"{TICA_BASE}/accounts/login/"
USERNAME = "thinhdt"
PASSWORD = "Th09051989@"

def login_tica(page):
    """Đăng nhập TICA OJ"""
    print("🔐 Đăng nhập TICA OJ...")
    page.goto(TICA_LOGIN)
    page.fill('input[name="username"]', USERNAME)
    page.fill('input[name="password"]', PASSWORD)
    page.click('button[type="submit"]')
    page.wait_for_load_state('networkidle')
    print("✅ Đã đăng nhập\n")

def main():
    problem_id = "chiavo_oc"
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        
        try:
            login_tica(page)
            
            url = f"{TICA_BASE}/problem/{problem_id}/test_data"
            print(f"📖 Mở: {url}")
            page.goto(url, timeout=15000)
            page.wait_for_load_state('networkidle')
            
            # Check tất cả input checkboxes
            print("\n" + "="*60)
            print("PHÂN TÍCH CHECKBOXES")
            print("="*60)
            
            all_checkboxes = page.locator('input[type="checkbox"]').all()
            print(f"\nTổng số checkboxes: {len(all_checkboxes)}")
            
            for i, checkbox in enumerate(all_checkboxes, 1):
                name = checkbox.get_attribute('name') or 'NO_NAME'
                id_attr = checkbox.get_attribute('id') or 'NO_ID'
                print(f"  {i}. name='{name}', id='{id_attr}'")
            
            # Check selector pattern khác nhau
            print("\n" + "="*60)
            print("TEST CÁC SELECTOR PATTERNS")
            print("="*60)
            
            patterns = [
                'input[type="checkbox"][name*="-DELETE"]',
                'input[type="checkbox"][name^="cases-"][name$="-DELETE"]',
                'input[type="checkbox"][name="delete-all"]',
                'input[type="checkbox"][id^="id_cases-"]'
            ]
            
            for pattern in patterns:
                count = page.locator(pattern).count()
                print(f"  {pattern}: {count} matches")
            
            # Check table rows
            print("\n" + "="*60)
            print("TEST TABLE STRUCTURE")
            print("="*60)
            
            rows = page.locator('table tr').all()
            print(f"\nTổng số table rows: {len(rows)}")
            
            # Look for "No testcases" message
            content = page.content()
            if "No testcases" in content or "Không có testcase" in content:
                print("\n⚠️  PHÁT HIỆN: Trang có thông báo 'No testcases'")
            
            # Screenshot
            page.screenshot(path="chiavo_oc_testdata.png")
            print(f"\n📸 Đã chụp screenshot: chiavo_oc_testdata.png")
            
            print("\n⏸️  Đợi 5s để xem browser...")
            time.sleep(5)
            
        finally:
            browser.close()

if __name__ == "__main__":
    main()
