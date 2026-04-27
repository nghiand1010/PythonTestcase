# -*- coding: utf-8 -*-
"""
Script để upload testcases lên TICA OJ bằng ZIP file
Yêu cầu: pip install playwright
"""

from playwright.sync_api import sync_playwright
from pathlib import Path
import time
import sys

# CẤU HÌNH
TICA_USERNAME = "thinhdt"
TICA_PASSWORD = "Th09051989@"
SCRIPT_DIR = Path(__file__).parent.absolute()
PROBLEMS_DIR = SCRIPT_DIR / "problems_ready_to_upload"  # Upload 67 bài đã test thành công

def login_tica(page):
    """Đăng nhập vào TICA OJ"""
    print("Đang đăng nhập...")
    page.goto("https://oj.tica.edu.vn/accounts/login/")
    page.wait_for_load_state("networkidle")
    
    page.fill('input[name="username"]', TICA_USERNAME)
    page.fill('input[name="password"]', TICA_PASSWORD)
    page.click('button[type="submit"]')
    
    page.wait_for_load_state("networkidle")
    time.sleep(2)
    print("✅ Đã đăng nhập thành công!")

def upload_testcases(page, problem_id):
    """Upload testcases cho một problem bằng ZIP file"""
    print(f"\n{'='*60}")
    print(f"Đang xử lý bài: {problem_id}")
    
    problem_dir = PROBLEMS_DIR / problem_id
    
    # Tìm file ZIP
    zip_file = problem_dir / f"{problem_id}_testcases.zip"
    
    if not zip_file.exists():
        print(f"⚠️ Không tìm thấy file ZIP: {zip_file}")
        return False
    
    print(f"Tìm thấy file ZIP: {zip_file.name}")
    
    # Vào trang test_data
    test_data_url = f"https://oj.tica.edu.vn/problem/{problem_id}/test_data"
    print(f"Đang vào: {test_data_url}")
    page.goto(test_data_url)
    page.wait_for_load_state("networkidle")
    time.sleep(1)
    
    # Kiểm tra xem đã có testcase chưa
    print("\nKiểm tra dữ liệu testcase hiện tại...")
    try:
        delete_checkboxes = page.locator('input[name^="cases-"][name$="-DELETE"]').all()
        if len(delete_checkboxes) > 0:
            print(f"  ⚠️ Đã có {len(delete_checkboxes)} testcases trên server")
            print(f"  ℹ️ Bỏ qua upload (chỉ upload khi dữ liệu trống)")
            return False
        else:
            print(f"  ✅ Chưa có testcase nào, sẽ upload")
    except Exception as e:
        print(f"  ℹ️ Không tìm thấy testcase (có thể đang trống): {e}")
    
    # Upload ZIP file
    print("\nĐang upload ZIP file...")
    
    # Đợi input file element xuất hiện
    try:
        page.wait_for_selector('#id_problem-data-zipfile', timeout=10000)
        page.set_input_files('#id_problem-data-zipfile', str(zip_file))
        time.sleep(1)
        print("✅ Đã chọn file ZIP")
    except Exception as e:
        print(f"❌ Lỗi khi upload file: {e}")
        return False
    
    # Click nút submit để upload ZIP
    print("\nĐang click 'Please press this button if you have just updated the zip data'...")
    page.click('input[type="submit"][value="Please press this button if you have just updated the zip data"]')
    page.wait_for_load_state("networkidle")
    print("✅ Đã upload ZIP file!")
    
    # Đợi trang reload và testcases được tạo
    print("\nĐợi trang cập nhật...")
    time.sleep(3)
    
    # Xóa testcase 11
    print("Đang xóa testcase 11...")
    try:
        delete_checkboxes = page.locator('input[name^="cases-"][name$="-DELETE"]').all()
        print(f"  Tìm thấy {len(delete_checkboxes)} checkboxes DELETE")
        
        if len(delete_checkboxes) >= 11:
            # Checkbox thứ 11 (index 10)
            delete_checkboxes[10].check()
            print("  ✅ Đã tick DELETE cho testcase 11")
        else:
            print(f"⚠️ Chỉ có {len(delete_checkboxes)} testcases, không thể xóa testcase 11")
    except Exception as e:
        print(f"⚠️ Lỗi khi xóa testcase 11: {e}")
    
    # Click Apply!
    print("\nĐang click Apply!...")
    try:
        page.click('input[type="submit"][value="Apply!"]')
        page.wait_for_load_state("networkidle")
        print("✅ Đã click Apply!")
    except Exception as e:
        print(f"⚠️ Lỗi khi click Apply: {e}")
    
    print(f"✅ Hoàn thành xử lý bài {problem_id}")
    return True

def upload_all_problems():
    """Upload testcases cho tất cả các bài"""
    if not PROBLEMS_DIR.exists():
        print(f"❌ Không tìm thấy thư mục problems: {PROBLEMS_DIR}")
        return
    
    problem_ids = [d.name for d in PROBLEMS_DIR.iterdir() if d.is_dir()]
    
    print(f"Tìm thấy {len(problem_ids)} bài toán")
    print("Danh sách:", ", ".join(problem_ids[:10]), "..." if len(problem_ids) > 10 else "")
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        
        # Đăng nhập
        login_tica(page)
        
        # Upload từng bài
        success_count = 0
        skipped_count = 0
        failed_problems = []
        
        for problem_id in problem_ids:
            try:
                if upload_testcases(page, problem_id):
                    success_count += 1
                else:
                    skipped_count += 1
            except Exception as e:
                print(f"❌ Lỗi khi upload {problem_id}: {e}")
                failed_problems.append(problem_id)
            time.sleep(2)  # Delay giữa các bài
        
        print(f"\n{'='*60}")
        print(f"Hoàn thành!")
        print(f"  ✅ Upload thành công: {success_count}/{len(problem_ids)} bài")
        print(f"  ⏭️  Bỏ qua (đã có data): {skipped_count} bài")
        print(f"  ❌ Lỗi: {len(failed_problems)} bài")
        if failed_problems:
            print(f"\nBài lỗi: {', '.join(failed_problems)}")
        
        browser.close()

def upload_single_problem(problem_id):
    """Upload testcases cho một bài cụ thể"""
    print(f"Upload testcases cho bài: {problem_id}")
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        
        # Đăng nhập
        login_tica(page)
        
        # Upload bài
        upload_testcases(page, problem_id)
        
        time.sleep(3)  # Đợi xem kết quả
        browser.close()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Upload một bài cụ thể
        problem_id = sys.argv[1]
        upload_single_problem(problem_id)
    else:
        # Upload tất cả
        upload_all_problems()
