#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Check testcase errors trên TICA OJ
Lấy HTML và phân tích lỗi
"""

from playwright.sync_api import sync_playwright
import time
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent.absolute()
USERNAME = "thinhdt"
PASSWORD = "Th09051989@"

# Danh sách các bài đã upload
UPLOADED_PROBLEMS = [
    "bupbe", "chon_2stong", "cuahang_sohoc", "dem_chia3", "dongho_bthuc",
    "nhonhatchia36", "quacau", "tso_chia5", "tuikeo_nguyenkhoa",
    "docsach_books", "docsach_marisa", "matran_xoanoc", "table_tennis",
    "thangmay", "tuoinuoc", "matran_xoanoc5"
]

def check_problem_testcases(page, problem_id):
    """Kiểm tra testcases của một bài"""
    print(f"\n{'='*60}")
    print(f"🔍 CHECKING: {problem_id}")
    print(f"{'='*60}")
    
    url = f"https://oj.tica.edu.vn/problem/{problem_id}/test_data"
    page.goto(url)
    page.wait_for_load_state("networkidle")
    time.sleep(2)
    
    # Lấy HTML
    html = page.content()
    
    # Save HTML để debug
    html_file = SCRIPT_DIR / f"debug_html_{problem_id}.html"
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"📄 Saved HTML to: {html_file.name}")
    
    # Kiểm tra errors trong HTML
    if 'error' in html.lower() or 'does not exist' in html.lower():
        print("⚠️  Có lỗi trong HTML!")
        
        # Tìm các dòng chứa error
        lines = html.split('\n')
        error_lines = [line for line in lines if 'error' in line.lower() or 'does not exist' in line.lower()]
        
        if error_lines:
            print("\n🔴 Error messages found:")
            for line in error_lines[:5]:  # Show first 5 errors
                clean_line = line.strip()[:200]  # First 200 chars
                print(f"  {clean_line}")
        
        return False
    
    # Đếm số testcases
    test_count = html.count('cases-') - html.count('__prefix__')
    print(f"📊 Số testcases: {test_count}")
    
    # Kiểm tra input/output files
    input_count = html.count('.in')
    output_count = html.count('.out')
    print(f"📁 Files: {input_count} inputs, {output_count} outputs")
    
    return True

def main():
    print("="*60)
    print("🔍 KIỂM TRA LỖI TESTCASES TRÊN TICA OJ")
    print("="*60)
    print(f"\n📋 Kiểm tra {len(UPLOADED_PROBLEMS)} bài\n")
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        # Login
        print("🔐 Đăng nhập...")
        page.goto("https://oj.tica.edu.vn/accounts/login/")
        page.fill('input[name="username"]', USERNAME)
        page.fill('input[name="password"]', PASSWORD)
        page.click('button[type="submit"]')
        page.wait_for_load_state('networkidle')
        print("✅ Đã đăng nhập\n")
        
        # Check từng bài
        problems_with_errors = []
        problems_ok = []
        
        for i, problem_id in enumerate(UPLOADED_PROBLEMS, 1):
            print(f"\n[{i}/{len(UPLOADED_PROBLEMS)}] {problem_id}")
            
            try:
                if check_problem_testcases(page, problem_id):
                    problems_ok.append(problem_id)
                else:
                    problems_with_errors.append(problem_id)
            except Exception as e:
                print(f"❌ Exception: {e}")
                problems_with_errors.append(problem_id)
            
            time.sleep(1)
        
        browser.close()
    
    # Summary
    print("\n" + "="*60)
    print("📊 KẾT QUẢ KIỂM TRA")
    print("="*60)
    print(f"✅ OK: {len(problems_ok)}/{len(UPLOADED_PROBLEMS)}")
    print(f"❌ Có lỗi: {len(problems_with_errors)}/{len(UPLOADED_PROBLEMS)}")
    
    if problems_with_errors:
        print("\n❌ Các bài có lỗi:")
        for p in problems_with_errors:
            print(f"  - {p}")
            print(f"    → HTML: debug_html_{p}.html")
    
    if problems_ok:
        print("\n✅ Các bài OK:")
        for p in problems_ok:
            print(f"  - {p}")

if __name__ == "__main__":
    main()
