#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tìm tất cả bài có lỗi testcase trên TICA OJ
"""

from playwright.sync_api import sync_playwright
import time
import re

USERNAME = "thinhdt"
PASSWORD = "Th09051989@"

def check_problem_errors(page, problem_id):
    """Kiểm tra bài có lỗi testcase không"""
    url = f"https://oj.tica.edu.vn/problem/{problem_id}/test_data"
    
    try:
        page.goto(url, timeout=10000)
        time.sleep(1)
        
        html = page.content()
        
        # Kiểm tra các loại lỗi
        errors = []
        
        if 'Input file for case' in html and 'does not exist' in html:
            matches = re.findall(r'Input file for case \d+ does not exist: ([\w\.]+)', html)
            if matches:
                errors.append(f"Missing input files: {', '.join(matches)}")
        
        if 'Output file for case' in html and 'does not exist' in html:
            matches = re.findall(r'Output file for case \d+ does not exist: ([\w\.]+)', html)
            if matches:
                errors.append(f"Missing output files: {', '.join(matches)}")
        
        if 'Failed to open as ZIP file' in html:
            errors.append("Failed to open ZIP")
        
        return errors
    except Exception as e:
        return [f"Error checking: {str(e)}"]

def main():
    print("="*60)
    print("🔍 TÌM BÀI CÓ LỖI TESTCASE")
    print("="*60)
    
    # Danh sách bài cần check (23 bài mới + sodep2)
    problems = [
        "sodep2",  # Bài user báo lỗi
        "bupbe", "chon_2stong", "cuahang_sohoc", "dem_chia3", 
        "dongho_bthuc", "nhonhatchia36", "quacau", "tso_chia5", 
        "tuikeo_nguyenkhoa", "docsach_books", "docsach_marisa", 
        "matran_xoanoc", "table_tennis", "thangmay", "tuoinuoc", 
        "matran_xoanoc5",
        # 7 bài còn lại từ 23 bài (không upload được)
        "caudo", "hinhtron2", "lucgiacthoi", "nhat_soi", 
        "tongcsk", "bang_xoanvuong", "chiavo_oc"
    ]
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        # Login
        print("\n🔐 Đăng nhập...")
        page.goto("https://oj.tica.edu.vn/accounts/login/")
        page.fill('input[name="username"]', USERNAME)
        page.fill('input[name="password"]', PASSWORD)
        page.click('button[type="submit"]')
        page.wait_for_load_state("networkidle")
        print("✅ Đã đăng nhập\n")
        
        error_problems = []
        ok_problems = []
        
        for i, problem_id in enumerate(problems, 1):
            print(f"[{i}/{len(problems)}] Checking {problem_id}...", end=" ", flush=True)
            
            errors = check_problem_errors(page, problem_id)
            
            if errors:
                print(f"❌ {len(errors)} lỗi")
                for err in errors:
                    print(f"    - {err}")
                error_problems.append((problem_id, errors))
            else:
                print("✅ OK")
                ok_problems.append(problem_id)
            
            time.sleep(0.5)
        
        browser.close()
        
        # Summary
        print("\n" + "="*60)
        print("📊 KẾT QUẢ")
        print("="*60)
        print(f"✅ OK: {len(ok_problems)}/{len(problems)}")
        print(f"❌ Có lỗi: {len(error_problems)}/{len(problems)}")
        
        if error_problems:
            print("\n❌ Danh sách bài có lỗi:")
            for problem_id, errors in error_problems:
                print(f"\n  • {problem_id}:")
                for err in errors:
                    print(f"      - {err}")

if __name__ == "__main__":
    main()
