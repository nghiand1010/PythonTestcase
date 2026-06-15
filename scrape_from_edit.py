"""
Lấy editorial từ trang edit của 3 bài
"""
import time
from pathlib import Path
from playwright.sync_api import sync_playwright

LOGIN_URL = "https://oj.tica.edu.vn/accounts/login/"
USERNAME = "thinhdt"
PASSWORD = "Th09051989@"

PROBLEMS = ["bdsochia2", "sodep2", "stickers"]

def login(page):
    """Đăng nhập vào TICA OJ"""
    print("🔐 Đăng nhập...")
    page.goto(LOGIN_URL, timeout=30000)
    page.fill('input#id_username', USERNAME)
    page.fill('input#id_password', PASSWORD)
    page.click('button[type="submit"]')
    page.wait_for_load_state('networkidle')
    print("✅ Đã đăng nhập\n")

def scrape_from_edit_page(page, problem_code):
    """Lấy editorial từ trang edit"""
    print(f"📥 Scraping {problem_code}...")
    
    # Tạo thư mục
    problem_dir = Path(f"problems/{problem_code}")
    problem_dir.mkdir(parents=True, exist_ok=True)
    
    # Vào trang edit
    edit_url = f"https://oj.tica.edu.vn/problem/{problem_code}/edit"
    page.goto(edit_url, timeout=15000)
    
    # Lấy tất cả textarea
    textareas = page.locator('textarea').all()
    
    # Tìm textarea chứa code (thường là textarea cuối hoặc textarea dài nhất có code)
    editorial_code = None
    for ta in textareas:
        try:
            val = ta.input_value()
            # Kiểm tra có phải Python code không
            if len(val) > 100 and ('def ' in val or 'import ' in val or 'with open' in val or 'input()' in val):
                editorial_code = val
                print(f"   ✅ Tìm thấy code ({len(val)} chars)")
                break
        except:
            pass
    
    if editorial_code:
        # Lưu editorial
        with open(problem_dir / "editorial.txt", "w", encoding="utf-8") as f:
            f.write(editorial_code)
        print(f"   ✅ Đã lưu editorial")
        return True
    else:
        print(f"   ⚠️  Không tìm thấy code!")
        return False

def main():
    print("=" * 70)
    print("🔧 SCRAPE EDITORIAL TỪ TRANG EDIT")
    print("=" * 70)
    print()
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        # Đăng nhập
        login(page)
        
        # Scrape từng bài
        success_count = 0
        for problem_code in PROBLEMS:
            if scrape_from_edit_page(page, problem_code):
                success_count += 1
            time.sleep(1)
        
        browser.close()
    
    print()
    print("=" * 70)
    print(f"📊 KẾT QUẢ: {success_count}/{len(PROBLEMS)} bài scrape thành công")
    print("=" * 70)

if __name__ == "__main__":
    main()
