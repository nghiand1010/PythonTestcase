"""
Debug script để check chi tiết 1 bài
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

def check_problem_detail(page, problem_id):
    """Check chi tiết 1 bài"""
    test_data_url = f"https://oj.tica.edu.vn/problem/{problem_id}/test_data"
    
    print(f"Đang vào: {test_data_url}\n")
    page.goto(test_data_url, timeout=10000)
    page.wait_for_load_state("networkidle")
    time.sleep(1)
    
    # Kiểm tra DELETE checkboxes
    print("📊 Tìm DELETE checkboxes...")
    delete_checkboxes = page.locator('input[name^="cases-"][name$="-DELETE"]').all()
    print(f"  → Tìm thấy {len(delete_checkboxes)} DELETE checkboxes\n")
    
    # Kiểm tra input files (để xem có testcase data không)
    print("📊 Tìm input files...")
    input_files = page.locator('input[name^="cases-"][name$="-input_file"]').all()
    print(f"  → Tìm thấy {len(input_files)} input file fields\n")
    
    # Kiểm tra output files
    print("📊 Tìm output files...")
    output_files = page.locator('input[name^="cases-"][name$="-output_file"]').all()
    print(f"  → Tìm thấy {len(output_files)} output file fields\n")
    
    # Kiểm tra xem có link "Download all test data" không
    print("📊 Tìm download link...")
    try:
        download_link = page.locator('a:has-text("Download all test data")').first
        if download_link.is_visible():
            print(f"  ✅ Có link download → BÀI CÓ TESTCASE\n")
        else:
            print(f"  ❌ Không thấy link download\n")
    except:
        print(f"  ❌ Không có link download → BÀI CHƯA CÓ TESTCASE\n")
    
    # Screenshot để xem
    page.screenshot(path=f"debug_{problem_id}.png")
    print(f"💾 Đã lưu screenshot: debug_{problem_id}.png")

def main():
    problem_id = "hcmdep"
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        print("🔐 Đăng nhập...\n")
        login_tica(page)
        print("✅ Đã đăng nhập\n")
        
        check_problem_detail(page, problem_id)
        
        input("\nNhấn Enter để đóng browser...")
        browser.close()

if __name__ == "__main__":
    main()
