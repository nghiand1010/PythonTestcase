#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AUTO UPLOAD TESTCASES CHO 3 BÀI
"""

from playwright.sync_api import sync_playwright
import time
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent.absolute()
PROBLEMS_DIR = SCRIPT_DIR / "problems"
USERNAME = "thinhdt"
PASSWORD = "Th09051989@"

PROBLEMS = ["bdsochia2", "sodep2", "stickers"]

def upload_testcases(page, problem_id):
    """Upload testcases cho 1 bài"""
    print(f"\\n{'='*60}")
    print(f"📤 {problem_id}")
    print(f"{'='*60}")
    
    # Mở test_data page
    url = f"https://oj.tica.edu.vn/problem/{problem_id}/test_data"
    print(f"🌐 Mở: {url}")
    page.goto(url)
    page.wait_for_load_state("networkidle")
    time.sleep(1)
    
    # Đếm testcases hiện tại
    all_checkboxes = page.locator('input[type="checkbox"][name*="cases-"]')
    test_count = 0
    for i in range(all_checkboxes.count()):
        name = all_checkboxes.nth(i).get_attribute('name')
        if '__prefix__' not in name and 'DELETION' not in name:
            test_count += 1
    
    print(f"📊 Testcases hiện tại: {test_count}")
    
    # Nếu đã có testcases, xóa đi
    if test_count > 0:
        print("🗑️  Xóa testcases cũ...")
        delete_all_checkbox = page.locator('input#delete-all')
        delete_all_checkbox.check()
        
        apply_button = page.locator('input[type="submit"][value="Apply!"]')
        apply_button.click()
        print("   ✓ Đã nhấn Apply, đợi xử lý...")
        time.sleep(3)
        page.wait_for_load_state("networkidle")
        
        # Reload và verify
        page.reload()
        time.sleep(1)
        
        all_checkboxes = page.locator('input[type="checkbox"][name*="cases-"]')
        test_count = 0
        for i in range(all_checkboxes.count()):
            name = all_checkboxes.nth(i).get_attribute('name')
            if '__prefix__' not in name and 'DELETION' not in name:
                test_count += 1
        
        if test_count == 0:
            print("   ✅ Đã xóa hết testcases cũ")
        else:
            print(f"   ⚠️  Còn {test_count} testcases")
            return False
    
    # Upload ZIP
    zip_file = PROBLEMS_DIR / problem_id / f"{problem_id}_testcases.zip"
    if not zip_file.exists():
        print(f"❌ Không tìm thấy ZIP: {zip_file}")
        return False
    
    print(f"📦 Upload ZIP: {zip_file.name}")
    file_input = page.locator('input#id_problem-data-zipfile')
    file_input.set_input_files(str(zip_file))
    print("   ✓ Đã chọn file ZIP")
    
    # Nhấn Apply để xử lý ZIP
    print("🔘 Nhấn Apply để xử lý ZIP...")
    apply_button = page.locator('input[type="submit"][value="Apply!"]')
    apply_button.click()
    print("   ✓ Đã nhấn Apply, đợi xử lý...")
    time.sleep(5)
    page.wait_for_load_state("networkidle")
    
    # Reload và kiểm tra
    print("🔍 Reload và kiểm tra testcases...")
    page.reload()
    time.sleep(2)
    page.wait_for_load_state("networkidle")
    
    all_checkboxes = page.locator('input[type="checkbox"][name*="cases-"]')
    test_count = 0
    for i in range(all_checkboxes.count()):
        name = all_checkboxes.nth(i).get_attribute('name')
        if '__prefix__' not in name and 'DELETION' not in name:
            test_count += 1
    
    print(f"   📊 Số testcases: {test_count}")
    
    # Kiểm tra lỗi
    html = page.content()
    if 'Input file for case' in html and 'does not exist' in html:
        print("   ❌ Có lỗi: Input file does not exist")
        return False
    
    if test_count > 0:
        print("✅ THÀNH CÔNG!")
        return True
    else:
        print("❌ THẤT BẠI - Chưa có testcases")
        return False

def main():
    print("="*60)
    print("📤 AUTO UPLOAD TESTCASES CHO 3 BÀI")
    print("="*60)
    print(f"\\n📋 Xử lý {len(PROBLEMS)} bài\\n")
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        # Login
        print("🔐 Đăng nhập TICA OJ...")
        page.goto("https://oj.tica.edu.vn/accounts/login/")
        page.fill('input[name="username"]', USERNAME)
        page.fill('input[name="password"]', PASSWORD)
        page.click('button[type="submit"]')
        page.wait_for_load_state('networkidle')
        print("✅ Đã đăng nhập\\n")
        
        success = []
        failed = []
        
        for i, problem_id in enumerate(PROBLEMS, 1):
            print(f"\\n[{i}/{len(PROBLEMS)}] Processing: {problem_id}")
            
            try:
                if upload_testcases(page, problem_id):
                    success.append(problem_id)
                else:
                    failed.append(problem_id)
            except Exception as e:
                print(f"❌ Lỗi: {e}")
                failed.append(problem_id)
            
            print("⏸️  Đợi 2s trước bài tiếp theo...")
            time.sleep(2)
        
        browser.close()
    
    # Summary
    print("\\n" + "="*60)
    print("📊 KẾT QUẢ")
    print("="*60)
    print(f"✅ Thành công: {len(success)}/{len(PROBLEMS)}")
    print(f"❌ Thất bại: {len(failed)}/{len(PROBLEMS)}")
    
    if success:
        print("\\n✅ Các bài thành công:")
        for p in success:
            print(f"  - {p}")
    
    if failed:
        print("\\n❌ Các bài thất bại:")
        for p in failed:
            print(f"  - {p}")
    
    if len(success) == len(PROBLEMS):
        print("\\n" + "="*60)
        print("🎉 HOÀN THÀNH! Tiếp theo chạy: py auto_submit_3_bai.py")
        print("="*60)

if __name__ == "__main__":
    main()
