"""
Download HTML của 2 bài để so sánh
"""
from playwright.sync_api import sync_playwright
import time

def login_tica(page):
    """Đăng nhập TICA OJ"""
    page.goto("https://oj.tica.edu.vn/accounts/login/")
    page.wait_for_load_state("networkidle")
    
    page.fill('input[name="username"]', 'thinhdt')
    page.fill('input[name="password"]', 'Th09051989@')
    page.click('button[type="submit"]')
    
    page.wait_for_load_state("networkidle")
    time.sleep(2)

def download_html(page, problem_id):
    """Download HTML của trang test_data"""
    test_data_url = f"https://oj.tica.edu.vn/problem/{problem_id}/test_data"
    
    print(f"Đang vào: {test_data_url}")
    page.goto(test_data_url, timeout=15000)
    page.wait_for_load_state("networkidle")
    time.sleep(2)
    
    # Lấy HTML content
    html_content = page.content()
    
    # Lưu file
    filename = f"html_{problem_id}.html"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"✅ Đã lưu: {filename}\n")

def main():
    problems = [
        "contest1_caudo",  # CÓ testcase
        "hcmdep"           # KHÔNG có testcase
    ]
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        print("🔐 Đăng nhập...\n")
        login_tica(page)
        print("✅ Đã đăng nhập\n")
        
        for problem_id in problems:
            download_html(page, problem_id)
            time.sleep(1)
        
        print("🎉 Hoàn thành! Kiểm tra 2 file HTML để so sánh.")
        input("\nNhấn Enter để đóng browser...")
        browser.close()

if __name__ == "__main__":
    main()
