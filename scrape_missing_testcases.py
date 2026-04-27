"""
Script lấy CHỈ những bài có editorial MÀ CHƯA có testcase trên server
Kết hợp: scrape_tica.py + check_missing_problems.py
"""
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
from pathlib import Path
import time
import os

SCRIPT_DIR = Path(__file__).parent.absolute()
PROBLEMS_DIR = SCRIPT_DIR / "problems"
USERNAME = "thinhdt"
PASSWORD = "Th09051989@"

def login_tica(page):
    """Đăng nhập TICA OJ"""
    print("🔐 Đăng nhập TICA OJ...")
    page.goto("https://oj.tica.edu.vn/accounts/login/")
    page.wait_for_load_state("networkidle")
    
    page.fill('input[name="username"]', USERNAME)
    page.fill('input[name="password"]', PASSWORD)
    page.click('button[type="submit"]')
    
    page.wait_for_load_state("networkidle")
    time.sleep(2)
    print("✅ Đã đăng nhập\n")

def check_has_testcase(page, problem_id):
    """Kiểm tra bài có testcase trên server chưa"""
    test_data_url = f"https://oj.tica.edu.vn/problem/{problem_id}/test_data"
    
    try:
        page.goto(test_data_url, timeout=10000)
        page.wait_for_load_state("networkidle")
        time.sleep(0.3)
        
        # Check tbody có <tr data-type> không
        testcase_rows = page.locator('#case-table > tbody:not(.extra-row-body) > tr[data-type]').all()
        return len(testcase_rows) > 0
    except:
        return False

def scrape_problem_with_editorial(page, problem_url, problem_id):
    """Scrape 1 bài và kiểm tra có editorial Python không"""
    try:
        # Vào trang edit để lấy editorial
        edit_url = f"{problem_url}/edit"
        page.goto(edit_url, timeout=15000)
        page.wait_for_load_state("networkidle")
        time.sleep(1)
        
        html_content = page.content()
        soup = BeautifulSoup(html_content, 'lxml')
        
        # Lấy editorial
        editorial_textarea = soup.find('textarea', {'name': 'solution-0-content'})
        if not editorial_textarea or not editorial_textarea.get_text(strip=True):
            return None, "Không có editorial"
        
        editorial_code = editorial_textarea.get_text()
        
        # Kiểm tra có phải Python không (loại C++)
        if '#include' in editorial_code or 'using namespace std' in editorial_code:
            return None, "Editorial C++"
        
        # Lấy problem description
        problem_textarea = soup.find('textarea', {'name': 'description'})
        problem_text = problem_textarea.get_text() if problem_textarea else ""
        
        return {
            'id': problem_id,
            'url': problem_url,
            'editorial': editorial_code,
            'problem': problem_text
        }, "OK"
        
    except Exception as e:
        return None, f"Lỗi: {e}"

def scrape_problems_list(page, max_pages=50):
    """Lấy danh sách problem IDs từ trang problems với filter"""
    print("📋 Đang lấy danh sách bài toán...\n")
    
    all_problem_ids = []
    page_num = 1
    
    while page_num <= max_pages:
        if page_num == 1:
            # Trang 1: Navigate và apply filter
            page.goto("https://oj.tica.edu.vn/problems/")
            page.wait_for_load_state("networkidle")
            time.sleep(1)
            
            # Check filter checkbox
            filter_checkbox = page.locator('input#hide_solved')
            if not filter_checkbox.is_checked():
                filter_checkbox.check()
                page.wait_for_load_state("networkidle")
                time.sleep(2)
        else:
            # Trang 2+: Direct URL với filter
            url = f"https://oj.tica.edu.vn/problems/?hide_solved=1&page={page_num}"
            page.goto(url, timeout=15000)
            page.wait_for_load_state("networkidle")
            time.sleep(1)
        
        print(f"  📄 Trang {page_num}...")
        
        # Parse HTML
        html_content = page.content()
        soup = BeautifulSoup(html_content, 'lxml')
        
        # Tìm problem rows - tìm tất cả <a> có href="/problem/..."
        problem_links = soup.find_all('a', href=True)
        page_problems = []
        
        for link in problem_links:
            href = link['href']
            # Chỉ lấy link dạng /problem/{id} (không có /edit, /data, etc)
            if href.startswith('/problem/') and href.count('/') == 2:
                problem_id = href.split('/problem/')[1].rstrip('/')
                if problem_id and problem_id not in page_problems:
                    page_problems.append(problem_id)
        
        if not page_problems:
            print(f"  ⚠️  Không parse được bài nào, dừng tại trang {page_num}")
            break
        
        if not page_problems:
            print(f"  ⚠️  Không parse được bài nào, dừng")
            break
        
        all_problem_ids.extend(page_problems)
        print(f"  ✅ Lấy được {len(page_problems)} bài")
        
        page_num += 1
        time.sleep(1)
    
    print(f"\n📊 Tổng cộng: {len(all_problem_ids)} bài từ {page_num-1} trang\n")
    return all_problem_ids

def save_problem(problem_data):
    """Lưu bài toán vào thư mục"""
    problem_id = problem_data['id']
    problem_folder = PROBLEMS_DIR / problem_id
    problem_folder.mkdir(parents=True, exist_ok=True)
    
    # Lưu editorial
    editorial_file = problem_folder / "editorial.txt"
    with open(editorial_file, 'w', encoding='utf-8') as f:
        f.write(problem_data['editorial'])
    
    # Lưu problem
    problem_file = problem_folder / "problem.txt"
    with open(problem_file, 'w', encoding='utf-8') as f:
        f.write(problem_data['problem'])

def main():
    print("="*60)
    print("🎯 SCRAPE BÀI CÓ EDITORIAL NHƯNG CHƯA CÓ TESTCASE")
    print("="*60 + "\n")
    
    # Tạo thư mục
    PROBLEMS_DIR.mkdir(exist_ok=True)
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        # Login
        login_tica(page)
        
        # 1. Lấy danh sách tất cả problems
        all_problem_ids = scrape_problems_list(page, max_pages=50)
        
        print("="*60)
        print("🔍 BƯỚC 1: Kiểm tra testcases hiện có")
        print("="*60 + "\n")
        
        # 2. Kiểm tra từng bài xem có testcase chưa
        problems_no_testcase = []
        problems_has_testcase = []
        
        for i, problem_id in enumerate(all_problem_ids, 1):
            print(f"[{i}/{len(all_problem_ids)}] Checking {problem_id}...", end=" ")
            has_testcase = check_has_testcase(page, problem_id)
            
            if has_testcase:
                problems_has_testcase.append(problem_id)
                print("✅ Có testcase")
            else:
                problems_no_testcase.append(problem_id)
                print("❌ CHƯA có testcase")
            
            time.sleep(0.3)
        
        print(f"\n📊 Kết quả:")
        print(f"  ✅ Đã có testcase: {len(problems_has_testcase)} bài")
        print(f"  ❌ Chưa có testcase: {len(problems_no_testcase)} bài\n")
        
        if not problems_no_testcase:
            print("🎉 Tất cả bài đã có testcase!")
            browser.close()
            return
        
        print("="*60)
        print("📥 BƯỚC 2: Scrape bài CHƯA có testcase")
        print("="*60 + "\n")
        
        # 3. Scrape chỉ những bài chưa có testcase
        scraped_count = 0
        skipped_no_editorial = 0
        skipped_cpp = 0
        failed = []
        
        for i, problem_id in enumerate(problems_no_testcase, 1):
            problem_url = f"https://oj.tica.edu.vn/problem/{problem_id}"
            print(f"[{i}/{len(problems_no_testcase)}] {problem_id}...", end=" ")
            
            problem_data, status = scrape_problem_with_editorial(page, problem_url, problem_id)
            
            if problem_data:
                save_problem(problem_data)
                scraped_count += 1
                print("✅ Có Python editorial")
            elif status == "Không có editorial":
                skipped_no_editorial += 1
                print("⏭️  Skip (không có editorial)")
            elif status == "Editorial C++":
                skipped_cpp += 1
                print("⏭️  Skip (C++)")
            else:
                failed.append(problem_id)
                print(f"❌ {status}")
            
            time.sleep(0.5)
        
        browser.close()
        
        print("\n" + "="*60)
        print("🏁 KẾT QUẢ CUỐI CÙNG")
        print("="*60)
        print(f"✅ Đã scrape: {scraped_count} bài (có Python editorial, chưa có testcase)")
        print(f"⏭️  Bỏ qua (không có editorial): {skipped_no_editorial} bài")
        print(f"⏭️  Bỏ qua (C++): {skipped_cpp} bài")
        print(f"❌ Lỗi: {len(failed)} bài")
        
        if failed:
            print(f"\nBài lỗi: {', '.join(failed)}")
        
        print(f"\n💾 Đã lưu vào: {PROBLEMS_DIR}")

if __name__ == "__main__":
    main()
