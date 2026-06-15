#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tìm tất cả bài có lỗi "file does not exist" trên TICA OJ
"""

from playwright.sync_api import sync_playwright
import time
import re

USERNAME = "thinhdt"
PASSWORD = "Th09051989@"

def get_all_problems(page):
    """Lấy danh sách tất cả problems"""
    print("📋 Lấy danh sách problems...")
    
    problems = set()
    page_num = 1
    
    while True:
        url = f"https://oj.tica.edu.vn/problems/?page={page_num}"
        print(f"   Đang đọc trang {page_num}...", end=" ", flush=True)
        
        try:
            page.goto(url, timeout=10000)
            time.sleep(1)
            
            # Tìm tất cả links có href="/problem/..."
            problem_links = page.locator('a[href^="/problem/"]').all()
            
            if len(problem_links) == 0:
                print("hết")
                break
            
            count = 0
            for link in problem_links:
                try:
                    href = link.get_attribute('href')
                    if href:
                        # Extract problem code: /problem/CODE hoặc /problem/CODE/
                        match = re.search(r'/problem/([^/]+)/?$', href)
                        if match:
                            problem_code = match.group(1)
                            # Bỏ qua các link không phải problem code
                            if problem_code not in ['add', 'edit'] and not problem_code.isdigit():
                                if problem_code not in problems:
                                    problems.add(problem_code)
                                    count += 1
                except:
                    pass
            
            print(f"{count} bài mới")
            
            # Nếu không có bài mới nào, có thể đã hết
            if count == 0:
                break
                
            page_num += 1
            
            # Safety limit
            if page_num > 30:
                print("   Đạt giới hạn 30 trang")
                break
            
        except:
            print("lỗi")
            break
    
    problems_list = sorted(list(problems))
    print(f"✅ Tổng cộng: {len(problems_list)} bài\n")
    return problems_list

def check_problem_error(page, problem_id):
    """Kiểm tra bài có lỗi testcase không"""
    url = f"https://oj.tica.edu.vn/problem/{problem_id}/test_data"
    
    try:
        page.goto(url, timeout=8000)
        time.sleep(0.3)
        
        html = page.content()
        
        # Kiểm tra lỗi "does not exist"
        errors = []
        
        # Input file errors
        input_errors = re.findall(r'Input file for case (\d+) does not exist: ([\w\.]+)', html)
        if input_errors:
            errors.append(f"Missing {len(input_errors)} input files")
        
        # Output file errors
        output_errors = re.findall(r'Output file for case (\d+) does not exist: ([\w\.]+)', html)
        if output_errors:
            errors.append(f"Missing {len(output_errors)} output files")
        
        return errors
        
    except Exception as e:
        return []

def main():
    print("="*70)
    print("🔍 TÌM TẤT CẢ BÀI CÓ LỖI TESTCASE")
    print("="*70)
    print()
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        # Login
        print("🔐 Đăng nhập...")
        page.goto("https://oj.tica.edu.vn/accounts/login/")
        page.fill('input[name="username"]', USERNAME)
        page.fill('input[name="password"]', PASSWORD)
        page.click('button[type="submit"]')
        page.wait_for_load_state("networkidle")
        print("✅ Đã đăng nhập\n")
        
        # Lấy danh sách problems
        problems = get_all_problems(page)
        
        # Check từng bài
        print("🔍 Kiểm tra từng bài...\n")
        error_problems = []
        
        for i, problem_id in enumerate(problems, 1):
            print(f"[{i}/{len(problems)}] {problem_id}...", end=" ", flush=True)
            
            errors = check_problem_error(page, problem_id)
            
            if errors:
                print(f"❌ {', '.join(errors)}")
                error_problems.append((problem_id, errors))
            else:
                print("✅")
            
            # Tránh quá tải server
            if i % 50 == 0:
                print("   ⏸️  Nghỉ 2s...")
                time.sleep(2)
        
        browser.close()
        
        # Summary
        print("\n" + "="*70)
        print("📊 KẾT QUẢ")
        print("="*70)
        print(f"✅ OK: {len(problems) - len(error_problems)}/{len(problems)}")
        print(f"❌ Có lỗi: {len(error_problems)}/{len(problems)}")
        
        if error_problems:
            print("\n❌ Danh sách bài có lỗi:\n")
            for problem_id, errors in error_problems:
                print(f"  • {problem_id}: {', '.join(errors)}")
                print(f"    https://oj.tica.edu.vn/problem/{problem_id}/test_data")
            
            # Lưu ra file
            with open("problems_with_testcase_errors.txt", "w", encoding="utf-8") as f:
                f.write("Bài có lỗi testcase (file does not exist)\n")
                f.write("="*70 + "\n\n")
                for problem_id, errors in error_problems:
                    f.write(f"{problem_id}: {', '.join(errors)}\n")
                    f.write(f"  https://oj.tica.edu.vn/problem/{problem_id}/test_data\n\n")
            
            print(f"\n💾 Đã lưu danh sách vào: problems_with_testcase_errors.txt")

if __name__ == "__main__":
    main()
