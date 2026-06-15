#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SIMPLE: CHỈ XÓA VÀ UPLOAD - KHÔNG LÀM GÌ THÊM
"""

from playwright.sync_api import sync_playwright
import time
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent.absolute()
PROBLEMS_DIR = SCRIPT_DIR / "problems"
USERNAME = "thinhdt"
PASSWORD = "Th09051989@"

# Test với 1 bài trước
PROBLEMS = ["bupbe"]

def simple_delete_and_upload(page, problem_id):
    """CHỈ xóa và upload - KHÔNG làm gì thêm"""
    print(f"\n{'='*60}")
    print(f"🔄 {problem_id}")
    print(f"{'='*60}")
    
    # Mở trang
    url = f"https://oj.tica.edu.vn/problem/{problem_id}/test_data"
    print(f"🌐 Mở: {url}")
    page.goto(url)
    page.wait_for_load_state("networkidle")
    
    # Bước 1: Delete all
    print("🗑️  BƯỚC 1: Click delete all checkbox")
    delete_all_checkbox = page.locator('input#id_cases-DELETION_DELETE_ALL')
    if delete_all_checkbox.count() > 0:
        delete_all_checkbox.check()
        print("   ✓ Đã check")
        
        # Apply
        print("   Nhấn Apply...")
        apply_button = page.locator('input[type="submit"][value="Apply!"]')
        apply_button.click()
        print("   ✓ Đã Apply, đợi 5s...")
        time.sleep(5)
        page.wait_for_load_state("networkidle")
        print("   ✓ Xong xóa")
    
    # Bước 2: Upload ZIP
    zip_file = PROBLEMS_DIR / problem_id / f"{problem_id}_testcases.zip"
    print(f"\n📦 BƯỚC 2: Upload ZIP: {zip_file.name}")
    file_input = page.locator('input#id_problem-data-zipfile')
    file_input.set_input_files(str(zip_file))
    print("   ✓ Đã chọn file ZIP")
    
    print("\n✅ XONG! Vui lòng kiểm tra trang web bằng mắt")
    print(f"   URL: {url}")
    
    # Đợi 30s để user xem
    print("\n⏸️  Đợi 30s để bạn kiểm tra...")
    time.sleep(30)

def main():
    print("="*60)
    print("SIMPLE TEST: CHỈ XÓA VÀ UPLOAD")
    print("="*60)
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        # Login
        print("\n🔐 Đăng nhập...")
        page.goto("https://oj.tica.edu.vn/accounts/login/")
        page.fill('input[name="username"]', USERNAME)
        page.fill('input[name="password"]', PASSWORD)
        page.click('button[type="submit"]')
        page.wait_for_load_state('networkidle')
        print("✅ Đã đăng nhập")
        
        for problem_id in PROBLEMS:
            simple_delete_and_upload(page, problem_id)
        
        browser.close()

if __name__ == "__main__":
    main()
