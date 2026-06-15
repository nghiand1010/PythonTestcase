"""
Scrape và tạo testcase cho 3 bài có lỗi: bdsochia2, sodep2, stickers
"""
import os
import time
from pathlib import Path
from playwright.sync_api import sync_playwright

# Thông tin đăng nhập
LOGIN_URL = "https://oj.tica.edu.vn/accounts/login/"
USERNAME = "thinhdt"
PASSWORD = "Th09051989@"

# 3 bài cần fix
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

def scrape_problem(page, problem_code):
    """Scrape thông tin bài toán"""
    print(f"📥 Scraping {problem_code}...")
    
    # Tạo thư mục
    problem_dir = Path(f"problems/{problem_code}")
    problem_dir.mkdir(parents=True, exist_ok=True)
    
    # Lấy editorial
    editorial_url = f"https://oj.tica.edu.vn/problem/{problem_code}/editorial"
    page.goto(editorial_url, timeout=15000)
    
    # Kiểm tra có editorial không
    content = page.content()
    if "No editorial is available" in content or "Editorial is not public" in content:
        print(f"   ⚠️  Không có editorial!")
        return False
    
    # Tìm tất cả editorial languages
    language_tabs = page.locator('a[data-toggle="tab"]').all()
    
    if len(language_tabs) == 0:
        print(f"   ⚠️  Không có editorial!")
        return False
    
    # In ra các ngôn ngữ có sẵn
    print(f"   📝 Các ngôn ngữ: ", end="")
    for tab in language_tabs:
        print(tab.text_content().strip(), end=" | ")
    print()
    
    # Ưu tiên Python, nếu không có thì lấy bất kỳ
    python_found = False
    for tab in language_tabs:
        lang_name = tab.text_content().strip().lower()
        if 'python' in lang_name or 'py' in lang_name:
            tab.click()
            time.sleep(0.5)
            python_found = True
            print(f"   ✅ Dùng Python editorial")
            break
    
    if not python_found:
        # Lấy ngôn ngữ đầu tiên
        language_tabs[0].click()
        time.sleep(0.5)
        lang = language_tabs[0].text_content().strip()
        print(f"   ⚠️  Không có Python, lấy {lang}")
    
    # Lấy code
    code_element = page.locator('pre code').first
    if code_element.count() == 0:
        print(f"   ⚠️  Không tìm thấy code!")
        return False
    
    editorial_code = code_element.text_content()
    
    # Lưu editorial
    with open(problem_dir / "editorial.txt", "w", encoding="utf-8") as f:
        f.write(editorial_code)
    
    print(f"   ✅ Đã lưu editorial")
    return True

def main():
    print("=" * 70)
    print("🔧 FIX 3 BÀI CÓ LỖI TESTCASE")
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
            if scrape_problem(page, problem_code):
                success_count += 1
            time.sleep(1)
        
        browser.close()
    
    print()
    print("=" * 70)
    print(f"📊 KẾT QUẢ: {success_count}/{len(PROBLEMS)} bài scrape thành công")
    print("=" * 70)

if __name__ == "__main__":
    main()
