#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Check xem bài nào đã có testcases trên TICA OJ
"""

from playwright.sync_api import sync_playwright
import time

TICA_BASE = "https://oj.tica.edu.vn"
TICA_LOGIN = f"{TICA_BASE}/accounts/login/"
USERNAME = "thinhdt"
PASSWORD = "Th09051989@"

PROBLEMS_TO_CHECK = [
    "chiavo_oc", "chuky_theky", "contest1_muatao", "dayso10", 
    "duan", "hk_matma", "lich_saohoa", 
    "skhn_chianhom", "skhn_dsoantoan", "skhn_tongk"
]

def login_tica(page):
    """Đăng nhập TICA OJ"""
    print("🔐 Đăng nhập TICA OJ...")
    page.goto(TICA_LOGIN)
    page.fill('input[name="username"]', USERNAME)
    page.fill('input[name="password"]', PASSWORD)
    page.click('button[type="submit"]')
    page.wait_for_load_state('networkidle')
    print("✅ Đã đăng nhập\n")

def check_has_testcase(page, problem_id):
    """Check xem bài có testcases chưa"""
    try:
        url = f"{TICA_BASE}/problem/{problem_id}/test_data"
        page.goto(url, timeout=15000)
        page.wait_for_load_state('networkidle')
        
        # Check permission
        if "You don't have permission" in page.content():
            return "NO_PERMISSION"
        
        if "Could not find a problem" in page.content():
            return "NOT_FOUND"
        
        # Check có checkbox tests không (loại trừ "delete-all" và template "__prefix__")
        # Checkbox của test cases có pattern: cases-0-DELETE, cases-1-DELETE...
        all_delete_checkboxes = page.locator('input[type="checkbox"][name^="cases-"][name$="-DELETE"]').all()
        
        # Loại bỏ template checkboxes (chứa __prefix__)
        real_test_checkboxes = [cb for cb in all_delete_checkboxes 
                                if '__prefix__' not in (cb.get_attribute('name') or '')]
        count = len(real_test_checkboxes)
        
        if count > 0:
            return f"HAS_{count}_TESTS"
        else:
            return "NO_TESTS"
            
    except Exception as e:
        return f"ERROR: {str(e)[:30]}"

def main():
    print("="*60)
    print("CHECK TESTCASES TRÊN TICA OJ")
    print("="*60)
    print(f"Kiểm tra {len(PROBLEMS_TO_CHECK)} bài...\n")
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        
        try:
            login_tica(page)
            
            results = {
                'has_tests': [],
                'no_tests': [],
                'not_found': [],
                'no_permission': [],
                'error': []
            }
            
            for i, problem_id in enumerate(PROBLEMS_TO_CHECK, 1):
                print(f"[{i}/{len(PROBLEMS_TO_CHECK)}] {problem_id}...", end=" ")
                status = check_has_testcase(page, problem_id)
                print(status)
                
                if status.startswith("HAS_"):
                    results['has_tests'].append((problem_id, status))
                elif status == "NO_TESTS":
                    results['no_tests'].append(problem_id)
                elif status == "NOT_FOUND":
                    results['not_found'].append(problem_id)
                elif status == "NO_PERMISSION":
                    results['no_permission'].append(problem_id)
                else:
                    results['error'].append((problem_id, status))
                
                time.sleep(1)
            
            # Summary
            print("\n" + "="*60)
            print("KẾT QUẢ")
            print("="*60)
            
            if results['has_tests']:
                print(f"\n✅ ĐÃ CÓ TESTCASES ({len(results['has_tests'])}):")
                for p, status in results['has_tests']:
                    print(f"  - {p}: {status}")
            
            if results['no_tests']:
                print(f"\n❌ CHƯA CÓ TESTCASES ({len(results['no_tests'])}):")
                for p in results['no_tests']:
                    print(f"  - {p}")
            
            if results['not_found']:
                print(f"\n⚠️  KHÔNG TỒN TẠI ({len(results['not_found'])}):")
                for p in results['not_found']:
                    print(f"  - {p}")
            
            if results['no_permission']:
                print(f"\n🔒 KHÔNG CÓ QUYỀN ({len(results['no_permission'])}):")
                for p in results['no_permission']:
                    print(f"  - {p}")
            
            if results['error']:
                print(f"\n❌ LỖI ({len(results['error'])}):")
                for p, err in results['error']:
                    print(f"  - {p}: {err}")
            
            # Danh sách cần upload
            need_upload = results['no_tests']
            if need_upload:
                print(f"\n{'='*60}")
                print(f"📤 CẦN UPLOAD ({len(need_upload)} BÀI):")
                print("="*60)
                for p in need_upload:
                    print(f"  - {p}")
            
        finally:
            browser.close()

if __name__ == "__main__":
    main()
