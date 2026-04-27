"""
Script kiểm tra bài nào CHƯA có testcase trên TICA OJ
"""
from playwright.sync_api import sync_playwright
from pathlib import Path
import time

SCRIPT_DIR = Path(__file__).parent
PROBLEMS_DIR = SCRIPT_DIR / "problems_ready_to_upload"

def get_all_problems():
    """Lấy danh sách tất cả problem IDs từ thư mục"""
    problems = []
    if PROBLEMS_DIR.exists():
        for item in PROBLEMS_DIR.iterdir():
            if item.is_dir():
                problems.append(item.name)
    return sorted(problems)

def login_tica(page):
    """Đăng nhập TICA OJ"""
    page.goto("https://oj.tica.edu.vn/accounts/login/")
    page.wait_for_load_state("networkidle")
    
    page.fill('input[name="username"]', 'thinhdt')
    page.fill('input[name="password"]', 'Th09051989@')
    page.click('button[type="submit"]')
    
    page.wait_for_load_state("networkidle")
    time.sleep(2)
    
    if "login" not in page.url.lower():
        return True
    return False

def check_testcases(page, problem_id):
    """Kiểm tra bài có testcase chưa. Return True nếu ĐÃ có, False nếu CHƯA có"""
    test_data_url = f"https://oj.tica.edu.vn/problem/{problem_id}/test_data"
    
    try:
        page.goto(test_data_url, timeout=10000)
        page.wait_for_load_state("networkidle")
        time.sleep(0.5)
        
        # Kiểm tra tbody của #case-table có chứa <tr> data không
        # Cách check: Tìm <tr data-type="C"> trong tbody chính (không phải extra-row-body)
        try:
            # Tìm tbody chính (không có class extra-row-body)
            testcase_rows = page.locator('#case-table > tbody:not(.extra-row-body) > tr[data-type]').all()
            
            if len(testcase_rows) > 0:
                return True  # Có testcase rows = có data
            else:
                return False  # Không có rows = chưa có data
        except:
            return False  # Lỗi thì coi như chưa có
        
    except Exception as e:
        print(f"  ⚠️  Lỗi khi check {problem_id}: {e}")
        return None  # Không xác định

def main():
    problems = get_all_problems()
    
    print(f"📊 Tổng cộng: {len(problems)} bài trong problems_ready_to_upload/\n")
    print("Đang kiểm tra...\n")
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        # Đăng nhập
        print("🔐 Đang đăng nhập...")
        if not login_tica(page):
            print("❌ Đăng nhập thất bại!")
            return
        print("✅ Đã đăng nhập\n")
        
        # Kiểm tra từng bài
        has_testcases = []
        missing_testcases = []
        errors = []
        
        for i, problem_id in enumerate(problems, 1):
            print(f"[{i}/{len(problems)}] Checking {problem_id}...", end=" ")
            result = check_testcases(page, problem_id)
            
            if result is True:
                has_testcases.append(problem_id)
                print("✅ Có testcase")
            elif result is False:
                missing_testcases.append(problem_id)
                print("❌ THIẾU testcase")
            else:
                errors.append(problem_id)
                print("⚠️  Lỗi")
            
            time.sleep(0.5)  # Delay nhẹ
        
        browser.close()
    
    # Báo cáo
    print(f"\n{'='*60}")
    print(f"📊 KẾT QUẢ KIỂM TRA:")
    print(f"  ✅ Đã có testcase: {len(has_testcases)}/{len(problems)} bài")
    print(f"  ❌ THIẾU testcase: {len(missing_testcases)} bài")
    print(f"  ⚠️  Lỗi khi check: {len(errors)} bài")
    
    if missing_testcases:
        print(f"\n🔴 DANH SÁCH BÀI THIẾU ({len(missing_testcases)} bài):")
        for pid in missing_testcases:
            print(f"  - {pid}")
    
    if errors:
        print(f"\n⚠️  BÀI LỖI KHI CHECK:")
        for pid in errors:
            print(f"  - {pid}")

if __name__ == "__main__":
    main()
