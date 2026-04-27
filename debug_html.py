# -*- coding: utf-8 -*-
"""
Script debug để lấy HTML của trang test_data
"""

from playwright.sync_api import sync_playwright
import time

TICA_USERNAME = "thinhdt"
TICA_PASSWORD = "Th09051989@"

def get_html():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        # Đăng nhập
        print("Đang đăng nhập...")
        page.goto("https://oj.tica.edu.vn/accounts/login/")
        page.wait_for_load_state("networkidle")
        page.fill('input[name="username"]', TICA_USERNAME)
        page.fill('input[name="password"]', TICA_PASSWORD)
        page.click('button[type="submit"]')
        page.wait_for_load_state("networkidle")
        time.sleep(2)
        
        # Vào trang test_data
        print("Vào trang test_data...")
        page.goto("https://oj.tica.edu.vn/problem/muahang_qnam/test_data")
        page.wait_for_load_state("networkidle")
        time.sleep(2)
        
        # Lấy HTML
        html = page.content()
        
        # Save HTML
        with open("test_data_page.html", "w", encoding="utf-8") as f:
            f.write(html)
        
        print("✅ Đã lưu HTML vào test_data_page.html")
        
        # Tìm tất cả buttons
        print("\n=== Tất cả buttons trên trang: ===")
        buttons = page.locator('button').all()
        for i, btn in enumerate(buttons):
            try:
                text = btn.inner_text()
                print(f"Button {i+1}: '{text}'")
            except:
                pass
        
        # Tìm tất cả inputs type=submit
        print("\n=== Tất cả input type=submit: ===")
        submits = page.locator('input[type="submit"]').all()
        for i, submit in enumerate(submits):
            try:
                value = submit.get_attribute('value')
                print(f"Submit {i+1}: value='{value}'")
            except:
                pass
        
        # Tìm form
        print("\n=== Forms trên trang: ===")
        forms = page.locator('form').all()
        for i, form in enumerate(forms):
            try:
                action = form.get_attribute('action')
                method = form.get_attribute('method')
                print(f"Form {i+1}: action='{action}', method='{method}'")
            except:
                pass
        
        print("\nGiữ browser mở 30 giây để bạn inspect...")
        time.sleep(30)
        
        browser.close()

if __name__ == "__main__":
    get_html()
