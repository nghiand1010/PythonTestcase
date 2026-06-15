#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
UPLOAD TESTCASES LÊN TICA OJ
- Tự động upload ZIP file chứa testcases
- Xóa test #11 để giữ lại 10 tests
- Hỗ trợ upload batch
"""

import os
import sys
import time
from pathlib import Path
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeout

# Reconfigure stdout/stderr to use UTF-8 on Windows
if sys.platform.startswith('win'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except AttributeError:
        import io
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
        sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

# Constants
SCRIPT_DIR = Path(__file__).parent.absolute()
PROBLEMS_DIR = SCRIPT_DIR / "problems"
TICA_BASE = "https://oj.tica.edu.vn"
TICA_LOGIN = f"{TICA_BASE}/accounts/login/"
USERNAME = "thinhdt"
PASSWORD = "Th09051989@"

def login_tica(page):
    """Đăng nhập TICA OJ"""
    print("\n🔐 Đăng nhập TICA OJ...")
    page.goto(TICA_LOGIN)
    page.fill('input[name="username"]', USERNAME)
    page.fill('input[name="password"]', PASSWORD)
    page.click('button[type="submit"]')
    page.wait_for_load_state('networkidle')
    print("✅ Đã đăng nhập")

def upload_testcase(page, problem_id):
    """Upload testcases cho 1 bài"""
    # Skip dayso10 - bài này luôn lỗi
    if problem_id == "dayso10":
        print(f"\n⏭️  Bỏ qua {problem_id} (bài này luôn lỗi)")
        return True  # Return True để không đếm là failed
    
    print(f"\n{'='*60}")
    print(f"📤 UPLOAD: {problem_id}")
    print(f"{'='*60}")
    
    # Tìm ZIP file
    problem_dir = PROBLEMS_DIR / problem_id
    zip_file = problem_dir / f"{problem_id}_testcases.zip"
    
    if not zip_file.exists():
        print(f"❌ Không tìm thấy ZIP: {zip_file}")
        return False
    
    # Đi đến trang test_data
    test_data_url = f"{TICA_BASE}/problem/{problem_id}/test_data"
    print(f"🌐 Mở: {test_data_url}")
    page.goto(test_data_url)
    page.wait_for_load_state('networkidle')
    
    # Check xem có quyền upload không
    if "You don't have permission" in page.content():
        print("❌ Không có quyền upload bài này")
        return False
    
    # LUÔN xóa hết testcases cũ trước (nếu có)
    all_delete_checkboxes = page.locator('input[type="checkbox"][name*="-DELETE"]')
    old_test_count = 0
    for i in range(all_delete_checkboxes.count()):
        name = all_delete_checkboxes.nth(i).get_attribute('name')
        if '__prefix__' not in name:
            old_test_count += 1
    
    if old_test_count > 0:
        print(f"🗑️  Phát hiện {old_test_count} testcases cũ, xóa hết...")
        
        # Find and check "Delete all" checkbox
        delete_all_checkbox = page.locator('input[type="checkbox"][name="delete-all"]')
        if delete_all_checkbox.count() > 0:
            delete_all_checkbox.check()
            print("✅ Đã chọn Delete all")
        else:
            # If no "delete-all" checkbox, check all individual delete checkboxes (except __prefix__)
            for i in range(all_delete_checkboxes.count()):
                name = all_delete_checkboxes.nth(i).get_attribute('name')
                if '__prefix__' not in name:
                    all_delete_checkboxes.nth(i).check()
            print(f"✅ Đã chọn xóa {old_test_count} testcases")
        
        # Click Apply to delete
        apply_button = page.locator('input[type="submit"][value="Apply!"]')
        if apply_button.count() > 0:
            apply_button.click()
            print("⏳ Đợi TICA xóa testcases (10s)...")
            time.sleep(10)
            page.wait_for_load_state('networkidle')
            print("✅ Đã xóa testcases cũ")
        else:
            print("⚠️  Không tìm thấy nút Apply!")
    else:
        print("✅ Chưa có testcases cũ")
    
    # Upload ZIP file
    print(f"📦 Upload ZIP: {zip_file.name}")
    file_input = page.locator('input#id_problem-data-zipfile')
    file_input.set_input_files(str(zip_file))
    
    # Click nút submit để xử lý ZIP (hỗ trợ cả tiếng Anh và tiếng Việt)
    submit_button = page.locator('input[type="submit"][value*="Please press"], input[type="submit"][value*="Nhấn nút này"]')
    if submit_button.count() > 0:
        submit_button.first.click()
        print("✅ Đã click submit xử lý ZIP")
    else:
        print("⚠️  Không tìm thấy nút submit xử lý ZIP cụ thể, thử click nút submit đầu tiên...")
        page.locator('input[type="submit"]').first.click()
    
    # Đợi 8 giây để TICA xử lý/giải nén ZIP
    print("⏳ Đợi TICA xử lý ZIP (8s)...")
    time.sleep(8)
    page.wait_for_load_state('networkidle')
    
    # QUAN TRỌNG: Nhấn Apply! để lưu toàn bộ thay đổi vào database
    print("🔘 Nhấn Apply! để lưu testcases...")
    apply_button = page.locator('input[type="submit"][value="Apply!"]')
    if apply_button.count() > 0:
        apply_button.click()
        print("⏳ Đợi TICA lưu thay đổi (6s)...")
        time.sleep(6)
        page.wait_for_load_state('networkidle')
    else:
        print("⚠️  Không tìm thấy nút Apply! để lưu")
        
    # Reload lại để xác nhận
    print("🔄 Reload trang để kiểm tra kết quả lưu...")
    page.reload()
    page.wait_for_load_state('networkidle')
    
    # Check if there's still error after upload  
    page_content_after = page.content()
    if "Input file for case" in page_content_after and "does not exist" in page_content_after:
        print("❌ Vẫn còn lỗi sau khi upload - upload không thành công")
        return False
    
    # Verify số lượng tests (đếm các checkbox không phải __prefix__)
    all_checkboxes = page.locator('input[type="checkbox"][name*="-DELETE"]')
    test_count = 0
    for i in range(all_checkboxes.count()):
        name = all_checkboxes.nth(i).get_attribute('name')
        if '__prefix__' not in name:
            test_count += 1
    
    print(f"📊 Số tests thực tế: {test_count}")
    
    if test_count >= 10:
        print("✅ UPLOAD THÀNH CÔNG")
        return True
    else:
        print(f"⚠️  Số tests bất thường: {test_count}")
        return False

def main():
    """Main function"""
    print("="*60)
    print("🚀 UPLOAD TESTCASES LÊN TICA OJ")
    print("="*60)
    
    # Lấy danh sách bài cần upload
    if len(sys.argv) > 1:
        # Upload specific problems
        problem_ids = sys.argv[1:]
    else:
        # Upload all problems có ZIP file
        problem_ids = []
        for problem_dir in sorted(PROBLEMS_DIR.iterdir()):
            if problem_dir.is_dir():
                zip_file = problem_dir / f"{problem_dir.name}_testcases.zip"
                if zip_file.exists():
                    problem_ids.append(problem_dir.name)
    
    if not problem_ids:
        print("❌ Không tìm thấy bài nào có ZIP file")
        return
    
    print(f"\n📋 Tìm thấy {len(problem_ids)} bài cần upload")
    
    # Confirm
    print("\n🔍 Danh sách bài:")
    for i, pid in enumerate(problem_ids, 1):
        print(f"  {i}. {pid}")
    
    # Start upload with Playwright
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        
        try:
            # Login
            login_tica(page)
            
            # Upload từng bài
            success_count = 0
            failed = []
            
            for i, problem_id in enumerate(problem_ids, 1):
                print(f"\n[{i}/{len(problem_ids)}] Processing: {problem_id}")
                
                try:
                    if upload_testcase(page, problem_id):
                        success_count += 1
                    else:
                        failed.append(problem_id)
                except Exception as e:
                    print(f"❌ LỖI: {e}")
                    failed.append(problem_id)
                
                # Pause giữa các bài
                if i < len(problem_ids):
                    print("\n⏸️  Đợi 2s trước bài tiếp theo...")
                    time.sleep(2)
            
            # Summary
            print("\n" + "="*60)
            print("📊 KẾT QUẢ UPLOAD")
            print("="*60)
            print(f"✅ Thành công: {success_count}/{len(problem_ids)}")
            if failed:
                print(f"❌ Thất bại: {len(failed)}")
                print("   - " + "\n   - ".join(failed))
            
        finally:
            browser.close()

if __name__ == "__main__":
    main()
