"""
Script khám phá cấu trúc trang TICA OJ
Chạy script này để xem các elements, filters có trên trang
"""

from playwright.sync_api import sync_playwright
import time

TICA_USERNAME = "thinhdt"  # Thay bằng username
TICA_PASSWORD = "Th09051989@"  # Thay bằng password

def explore_page():
    """Khám phá cấu trúc trang problems"""
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)  # Chậm để xem
        context = browser.new_context()
        page = context.new_page()
        
        try:
            # Đăng nhập
            print("Đang đăng nhập...")
            page.goto("https://oj.tica.edu.vn/accounts/login/")
            page.wait_for_load_state("networkidle")
            
            page.fill('input[name="username"]', TICA_USERNAME)
            page.fill('input[name="password"]', TICA_PASSWORD)
            page.click('button[type="submit"]')
            page.wait_for_load_state("networkidle")
            time.sleep(2)
            
            # Đi đến trang problems
            print("\nĐang mở trang problems...")
            page.goto("https://oj.tica.edu.vn/problems/")
            page.wait_for_load_state("networkidle")
            time.sleep(2)
            
            # Lấy HTML để phân tích
            content = page.content()
            
            # Tìm các checkbox/toggle
            print("\n" + "="*60)
            print("TÌM KIẾM CÁC FILTERS:")
            print("="*60)
            
            # Tìm tất cả checkbox
            checkboxes = page.query_selector_all('input[type="checkbox"]')
            print(f"\n📋 Tìm thấy {len(checkboxes)} checkboxes:")
            for i, cb in enumerate(checkboxes):
                label = cb.evaluate('el => el.labels ? el.labels[0]?.innerText : null')
                name = cb.get_attribute('name')
                id_attr = cb.get_attribute('id')
                checked = cb.is_checked()
                print(f"  {i+1}. ID: {id_attr}, Name: {name}, Label: {label}, Checked: {checked}")
            
            # Tìm "Hide solved problems"
            print("\n🔍 Tìm 'Hide solved problems':")
            hide_solved = page.query_selector_all('text=/hide.*solved/i')
            print(f"  Tìm thấy {len(hide_solved)} elements")
            for elem in hide_solved:
                print(f"  - Text: {elem.inner_text()}")
                print(f"    Tag: {elem.evaluate('el => el.tagName')}")
                print(f"    ID: {elem.get_attribute('id')}")
            
            # Tìm tất cả filters/dropdowns
            selects = page.query_selector_all('select')
            print(f"\n📑 Tìm thấy {len(selects)} dropdown menus:")
            for i, sel in enumerate(selects):
                name = sel.get_attribute('name')
                id_attr = sel.get_attribute('id')
                options = sel.query_selector_all('option')
                print(f"  {i+1}. ID: {id_attr}, Name: {name}")
                print(f"     Options: {[opt.inner_text() for opt in options[:5]]}")  # In 5 option đầu
            
            # Tìm buttons/links liên quan đến filter
            print("\n🔘 Tìm các buttons:")
            buttons = page.query_selector_all('button')
            for btn in buttons[:10]:  # In 10 button đầu
                text = btn.inner_text()
                if text and len(text) < 50:
                    print(f"  - {text}")
            
            # Screenshot để xem
            print("\n📸 Đang chụp màn hình...")
            page.screenshot(path="tica_problems_page.png", full_page=True)
            print("  Đã lưu: tica_problems_page.png")
            
            # Pause để xem trang
            print("\n⏸️  Trang web đang mở, hãy:")
            print("  1. Kiểm tra các filters trên trang")
            print("  2. Xem console output ở trên")
            print("  3. Xem file tica_problems_page.png")
            print("\nNhấn Enter để đóng browser...")
            input()
            
        finally:
            browser.close()

if __name__ == "__main__":
    print("🔍 TICA OJ Page Explorer")
    print("="*60)
    
    if TICA_USERNAME == "your_username":
        print("⚠️  Cập nhật username/password ở đầu file này!")
        exit(1)
    
    explore_page()
