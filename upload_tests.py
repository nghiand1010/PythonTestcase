# -*- coding: utf-8 -*-
"""
Script để upload testcases lên TICA OJ
Yêu cầu: pip install playwright
"""

from playwright.sync_api import sync_playwright
import os
import time
import glob

# CẤU HÌNH
TICA_USERNAME = "thinhdt"
TICA_PASSWORD = "Th09051989@"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROBLEMS_DIR = os.path.join(BASE_DIR, "problems")

def login_tica(page):
    """Đăng nhập vào TICA OJ"""
    print("Đang đăng nhập...")
    page.goto("https://oj.tica.edu.vn/accounts/login/")
    page.wait_for_load_state("networkidle")
    
    # Điền thông tin đăng nhập
    page.fill('input[name="username"]', TICA_USERNAME)
    page.fill('input[name="password"]', TICA_PASSWORD)
    page.click('button[type="submit"]')
    
    # Đợi đăng nhập thành công
    page.wait_for_load_state("networkidle")
    time.sleep(2)
    print("✅ Đã đăng nhập thành công!")

def upload_testcases(page, problem_id):
    """
    Upload testcases cho một bài toán và xóa testcase 11
    """
    print(f"\n{'='*60}")
    print(f"Đang xử lý bài: {problem_id}")
    
    # Đường dẫn đến thư mục testcases
    problem_dir = os.path.join(PROBLEMS_DIR, problem_id)
    if not os.path.exists(problem_dir):
        print(f"❌ Không tìm thấy thư mục: {problem_dir}")
        return False
    
    # Kiểm tra file testcases
    input_files = sorted(glob.glob(os.path.join(problem_dir, "input*.in")))
    output_files = sorted(glob.glob(os.path.join(problem_dir, "output*.out")))
    
    if not input_files or not output_files:
        print(f"❌ Không tìm thấy testcases trong {problem_dir}")
        return False
    
    print(f"Tìm thấy {len(input_files)} input files và {len(output_files)} output files")
    
    # Vào trang test_data
    test_data_url = f"https://oj.tica.edu.vn/problem/{problem_id}/test_data"
    print(f"Đang vào: {test_data_url}")
    
    try:
        page.goto(test_data_url)
        page.wait_for_load_state("networkidle")
        time.sleep(2)
        
        # Click nút "Add test case" để mở form upload
        print("\nClick Add test case để mở form upload...")
        try:
            add_case_button = page.locator('a#add-case-row').first
            if add_case_button.is_visible():
                add_case_button.click()
                time.sleep(1)
                print("✅ Đã mở form upload")
        except Exception as e:
            print(f"⚠️ Không tìm thấy nút Add test case: {e}")
        
        # Upload từng cặp input/output
        for i in range(len(input_files)):
            if i < len(output_files):
                input_file = input_files[i]
                output_file = output_files[i]
                
                print(f"  Đang upload test {i+1}...")
                
                try:
                    # Tìm các input file trong row cuối cùng
                    # Pattern: input[id$="input_file"] và input[id$="output_file"]
                    
                    # Tìm row cuối cùng trong tbody
                    last_row = page.locator('#case-table tbody tr').last
                    
                    # Upload input file
                    input_file_input = last_row.locator('input[id$="input_file"]').first
                    if input_file_input.is_visible():
                        input_file_input.set_input_files(input_file)
                        time.sleep(0.5)
                    
                    # Upload output file
                    output_file_input = last_row.locator('input[id$="output_file"]').first
                    if output_file_input.is_visible():
                        output_file_input.set_input_files(output_file)
                        time.sleep(0.5)
                    
                    print(f"  ✅ Đã upload test {i+1}")
                    
                    # Nếu không phải test cuối, click Add để thêm row mới
                    if i < len(input_files) - 1:
                        add_case_button = page.locator('a#add-case-row').first
                        if add_case_button.is_visible():
                            add_case_button.click()
                            time.sleep(1)
                        
                except Exception as e:
                    print(f"  ❌ Lỗi khi upload test {i+1}: {e}")
                    continue
        
        # Sau khi upload xong, đợi trang update
        print("\nĐợi trang cập nhật...")
        time.sleep(3)
        
        # Tick delete vào testcase 11
        print("Đang xóa testcase 11...")
        try:
            # Tìm tất cả checkboxes có name pattern "cases-*-DELETE"
            all_delete_checkboxes = page.locator('input[name$="-DELETE"]').all()
            print(f"  Tìm thấy {len(all_delete_checkboxes)} checkboxes DELETE")
            
            # Testcase 11 có index 10 (bắt đầu từ 0)
            if len(all_delete_checkboxes) >= 11:
                # Check checkbox thứ 11 (index 10)
                all_delete_checkboxes[10].check()
                print("✅ Đã tick delete cho testcase 11")
            else:
                print(f"⚠️ Chỉ có {len(all_delete_checkboxes)} testcases, không thể xóa testcase 11")
        
        except Exception as e:
            print(f"⚠️ Không thể xóa testcase 11: {e}")
        
        # Click nút Apply!
        print("\nĐang click Apply!...")
        try:
            # Nút Apply có text "Apply!" (có dấu chấm than)
            apply_button = page.locator('input[type="submit"][value="Apply!"]').first
            
            if apply_button.is_visible():
                apply_button.click()
                time.sleep(2)
                print("✅ Đã click Apply!")
            else:
                print("⚠️ Không tìm thấy nút Apply!")
        
        except Exception as e:
            print(f"❌ Lỗi khi click Apply: {e}")
        
        print(f"✅ Hoàn thành xử lý bài {problem_id}")
        return True
        
    except Exception as e:
        print(f"❌ Lỗi khi xử lý bài {problem_id}: {e}")
        return False

def upload_all_problems():
    """Upload testcases cho tất cả các bài"""
    # Lấy danh sách các thư mục trong problems/
    if not os.path.exists(PROBLEMS_DIR):
        print(f"❌ Không tìm thấy thư mục problems: {PROBLEMS_DIR}")
        return
    
    problem_ids = [d for d in os.listdir(PROBLEMS_DIR) 
                   if os.path.isdir(os.path.join(PROBLEMS_DIR, d))]
    
    print(f"Tìm thấy {len(problem_ids)} bài toán")
    print("Danh sách:", ", ".join(problem_ids[:10]), "..." if len(problem_ids) > 10 else "")
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # headless=False để xem quá trình
        context = browser.new_context()
        page = context.new_page()
        
        # Đăng nhập
        login_tica(page)
        
        # Upload từng bài
        success_count = 0
        for problem_id in problem_ids:
            if upload_testcases(page, problem_id):
                success_count += 1
            time.sleep(2)  # Delay giữa các bài
        
        print(f"\n{'='*60}")
        print(f"Hoàn thành! Upload thành công {success_count}/{len(problem_ids)} bài")
        
        browser.close()

def upload_single_problem(problem_id):
    """Upload testcases cho một bài cụ thể"""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        
        login_tica(page)
        upload_testcases(page, problem_id)
        
        browser.close()

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        # Upload bài cụ thể: python upload_tests.py muahang_qnam
        problem_id = sys.argv[1]
        print(f"Upload testcases cho bài: {problem_id}")
        upload_single_problem(problem_id)
    else:
        # Upload tất cả
        print("Upload testcases cho TẤT CẢ các bài")
        print("Để upload 1 bài cụ thể: python upload_tests.py <problem_id>")
        print()
        
        confirm = input("Bạn có chắc muốn upload tất cả? (yes/no): ")
        if confirm.lower() == "yes":
            upload_all_problems()
        else:
            print("Đã hủy.")
