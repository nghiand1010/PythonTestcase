"""
Kiểm tra trang edit của stickers
"""
import time
from playwright.sync_api import sync_playwright

LOGIN_URL = "https://oj.tica.edu.vn/accounts/login/"
USERNAME = "thinhdt"
PASSWORD = "Th09051989@"

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        # Đăng nhập
        print("🔐 Đăng nhập...")
        page.goto(LOGIN_URL, timeout=30000)
        page.fill('input#id_username', USERNAME)
        page.fill('input#id_password', PASSWORD)
        page.click('button[type="submit"]')
        page.wait_for_load_state('networkidle')
        print("✅ Đã đăng nhập")
        
        # Vào trang edit
        print("\n📝 Kiểm tra trang edit của stickers...")
        page.goto("https://oj.tica.edu.vn/problem/stickers/edit", timeout=15000)
        
        # Kiểm tra có Python solutions không
        print("\n🔍 Tìm Python solutions...")
        
        # Tìm textarea chứa solution
        textarea = page.locator('textarea#id_description').first
        if textarea.count() > 0:
            content = textarea.input_value()
            print(f"\n📄 Description length: {len(content)} chars")
            print(f"First 500 chars:\n{content[:500]}")
        
        # Kiểm tra editorial section
        editorial_textarea = page.locator('textarea').all()
        print(f"\n📝 Tổng số textarea: {len(editorial_textarea)}")
        
        for i, ta in enumerate(editorial_textarea):
            try:
                val = ta.input_value()
                if len(val) > 50:  # Chỉ in những textarea có nội dung
                    print(f"\nTextarea {i+1}: {len(val)} chars")
                    print(f"Preview: {val[:200]}")
            except:
                pass
        
        print("\n⏳ Giữ trình duyệt mở 30s để bạn xem...")
        time.sleep(30)
        
        browser.close()

if __name__ == "__main__":
    main()
