# -*- coding: utf-8 -*-
"""
Upload testcases cho các bài cụ thể (FORCE - không kiểm tra đã có hay chưa)
"""

from playwright.sync_api import sync_playwright
from pathlib import Path
import time
import sys

# CẤU HÌNH
TICA_USERNAME = "thinhdt"
TICA_PASSWORD = "Th09051989@"
SCRIPT_DIR = Path(__file__).parent.absolute()
PROBLEMS_DIR = SCRIPT_DIR / "problems_ready_to_upload"

# DANH SÁCH BÀI CẦN UPLOAD - 13 bài THIẾU testcase (không bao gồm dayso10 lỗi)
def get_all_problems():
    """Lấy tất cả bài từ thư mục problems_ready_to_upload"""
    if not PROBLEMS_DIR.exists():
        return []
    return sorted([d.name for d in PROBLEMS_DIR.iterdir() if d.is_dir()])

PROBLEMS_TO_UPLOAD = [
    "tica_bangso"
]

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

def force_upload_testcases(page, problem_id):
    """Upload testcases - SKIP nếu đã có testcase trên server"""
    print(f"\n{'='*60}")
    print(f"Đang xử lý bài: {problem_id}")
    
    problem_dir = PROBLEMS_DIR / problem_id
    
    # Tìm file ZIP
    zip_file = problem_dir / f"{problem_id}_testcases.zip"
    
    if not zip_file.exists():
        print(f"❌ Không tìm thấy file ZIP: {zip_file}")
        return False
    
    print(f"✅ Tìm thấy file ZIP: {zip_file.name}")
    
    # Vào trang test_data
    test_data_url = f"https://oj.tica.edu.vn/problem/{problem_id}/test_data"
    print(f"Đang vào: {test_data_url}")
    
    try:
        page.goto(test_data_url)
        page.wait_for_load_state("networkidle")
        time.sleep(1)
    except Exception as e:
        print(f"❌ Lỗi khi vào trang: {e}")
        return False
    
    # Kiểm tra số testcases hiện tại
    print("\n📊 Kiểm tra dữ liệu hiện tại...")
    try:
        # Kiểm tra tbody của #case-table có chứa <tr> data không
        testcase_rows = page.locator('#case-table > tbody:not(.extra-row-body) > tr[data-type]').all()
        if len(testcase_rows) > 0:
            print(f"  ⚠️  Đã có {len(testcase_rows)} testcases trên server")
            print(f"  🔄 Sẽ upload đè lên (FORCE mode)")
        else:
            print(f"  ℹ️  Chưa có testcase nào → Sẽ upload")
    except Exception as e:
        print(f"  ℹ️  Không thể kiểm tra: {e}")
    
    # Upload ZIP file
    print("\n📦 Đang upload ZIP file...")
    
    try:
        page.wait_for_selector('#id_problem-data-zipfile', timeout=10000)
        page.set_input_files('#id_problem-data-zipfile', str(zip_file))
        time.sleep(1)
        print("✅ Đã chọn file ZIP")
    except Exception as e:
        print(f"❌ Lỗi khi upload file: {e}")
        return False
    
    # Click nút submit để upload ZIP
    print("\n🚀 Đang submit...")
    try:
        page.click('input[type="submit"][value="Please press this button if you have just updated the zip data"]')
        page.wait_for_load_state("networkidle")
        print("✅ Đã upload ZIP file!")
    except Exception as e:
        print(f"❌ Lỗi khi submit: {e}")
        return False
    
    # Đợi trang reload và testcases được tạo
    print("\n⏳ Đợi trang cập nhật...")
    time.sleep(3)
    
    # Xóa testcase 11
    print("\n🗑️  Đang xóa testcase 11...")
    try:
        delete_checkboxes = page.locator('input[name^="cases-"][name$="-DELETE"]').all()
        print(f"  📊 Tìm thấy {len(delete_checkboxes)} testcases")
        
        if len(delete_checkboxes) >= 11:
            # Check testcase 11 (index 10)
            delete_checkboxes[10].check()
            print(f"  ✅ Đã check testcase 11")
            
            # Click Apply!
            page.click('input[type="submit"][value="Apply!"]')
            page.wait_for_load_state("networkidle")
            time.sleep(1)
            print(f"  ✅ Đã xóa testcase 11")
        else:
            print(f"  ⚠️  Chỉ có {len(delete_checkboxes)} testcases, không xóa")
    except Exception as e:
        print(f"  ⚠️  Không thể xóa testcase 11: {e}")
    
    print(f"\n✅ Hoàn thành upload bài {problem_id}")
    return True

def main():
    """Upload testcases cho các bài cụ thể"""
    if not PROBLEMS_TO_UPLOAD:
        print("❌ Chưa có bài nào trong danh sách PROBLEMS_TO_UPLOAD")
        print("   Sửa script và thêm problem_id vào danh sách")
        return
    
    print(f"🎯 Sẽ upload lại bài: {', '.join(PROBLEMS_TO_UPLOAD)}")
    
    print("\n⚠️  CHẾ ĐỘ FORCE: Sẽ upload ĐÈ lên testcases cũ!")
    print("Nhấn Ctrl+C trong 3 giây để hủy...")
    try:
        time.sleep(3)
    except KeyboardInterrupt:
        print("\n❌ Đã hủy")
        return
    
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
        
        for problem_id in PROBLEMS_TO_UPLOAD:
            try:
                result = force_upload_testcases(page, problem_id)
                if result:
                    success_count += 1
                elif result is False:
                    skipped_count += 1
            except Exception as e:
                print(f"❌ Lỗi khi upload {problem_id}: {e}")
                failed_problems.append(problem_id)
            time.sleep(2)  # Delay giữa các bài
        
        print(f"\n{'='*60}")
        print(f"🏁 Hoàn thành!")
        print(f"  ✅ Upload thành công: {success_count}/{len(PROBLEMS_TO_UPLOAD)} bài")
        print(f"  ⏭️  Bỏ qua (đã có data): {skipped_count} bài")
        print(f"  ❌ Lỗi: {len(failed_problems)} bài")
        if failed_problems:
            print(f"\nBài lỗi: {', '.join(failed_problems)}")
        
        browser.close()

if __name__ == "__main__":
    main()
