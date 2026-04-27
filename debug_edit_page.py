"""
Script để debug trang /edit và xem tất cả textarea fields
"""

from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import time

TICA_USERNAME = "thinhdt"
TICA_PASSWORD = "Th09051989@"

def debug_edit_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
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
            print("✅ Đã đăng nhập\n")
            
            # Vào trang edit của bài cụ thể
            problem_id = "nuocep_hoaqua"  # Thay bằng bài bạn muốn test
            edit_url = f"https://oj.tica.edu.vn/problem/{problem_id}/edit"
            print(f"Vào trang: {edit_url}\n")
            
            page.goto(edit_url)
            page.wait_for_load_state("networkidle")
            time.sleep(2)
            
            # Lấy HTML và parse
            content = page.content()
            soup = BeautifulSoup(content, 'html.parser')
            
            # Tìm TẤT CẢ textarea
            print("="*60)
            print("TẤT CẢ TEXTAREA TRÊN TRANG:")
            print("="*60)
            
            textareas = soup.find_all('textarea')
            for i, textarea in enumerate(textareas, 1):
                name = textarea.get('name', 'NO NAME')
                id_attr = textarea.get('id', 'NO ID')
                content_preview = textarea.get_text()[:100]
                
                print(f"\n[Textarea #{i}]")
                print(f"  name: {name}")
                print(f"  id: {id_attr}")
                print(f"  Content length: {len(textarea.get_text())} ký tự")
                print(f"  Preview: {content_preview}...")
                print("-"*60)
            
            # Tìm TẤT CẢ input fields
            print("\n" + "="*60)
            print("TẤT CẢ INPUT FIELDS:")
            print("="*60)
            
            inputs = soup.find_all('input', {'type': ['text', 'hidden']})
            for i, inp in enumerate(inputs, 1):
                name = inp.get('name', 'NO NAME')
                id_attr = inp.get('id', 'NO ID')
                value = inp.get('value', '')
                
                print(f"\n[Input #{i}]")
                print(f"  name: {name}")
                print(f"  id: {id_attr}")
                print(f"  value: {value[:50]}...")
                print("-"*60)
            
            # Lưu HTML về file
            html_path = f"edit_page_{problem_id}.html"
            with open(html_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"\n💾 HTML saved: {html_path}")
            
            # Tạo screenshot
            screenshot_path = f"edit_page_{problem_id}.png"
            page.screenshot(path=screenshot_path)
            print(f"📸 Screenshot saved: {screenshot_path}")
            
            # Giữ browser mở để user xem
            print("\n💡 Browser sẽ đóng sau 5 giây...")
            time.sleep(5)
            
        finally:
            browser.close()

if __name__ == "__main__":
    debug_edit_page()
