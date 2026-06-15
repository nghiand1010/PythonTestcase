# -*- coding: utf-8 -*-
"""
Check all 30 problems in our problems directory to see how many testcases are uploaded on TICA OJ.
"""
import os
import sys
import time
from pathlib import Path
from playwright.sync_api import sync_playwright

if sys.platform.startswith('win'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except AttributeError:
        import io
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
        sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

SCRIPT_DIR = Path(__file__).parent.absolute()
PROBLEMS_DIR = SCRIPT_DIR / "problems"
TICA_BASE = "https://oj.tica.edu.vn"
TICA_LOGIN = f"{TICA_BASE}/accounts/login/"
USERNAME = "thinhdt"
PASSWORD = "Th09051989@"

def count_testcases(page):
    """Count actual testcases (input checkboxes for deletion)"""
    all_checkboxes = page.locator('input[type="checkbox"][name*="-DELETE"]')
    count = 0
    for i in range(all_checkboxes.count()):
        name = all_checkboxes.nth(i).get_attribute('name')
        if '__prefix__' not in name and 'delete-all' not in name:
            count += 1
    return count

def main():
    problems = sorted([d.name for d in PROBLEMS_DIR.iterdir() if d.is_dir()])
    print(f"Checking {len(problems)} problems on TICA OJ...")
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        
        # Login
        print("Logging in...")
        page.goto(TICA_LOGIN)
        page.fill('input[name="username"]', USERNAME)
        page.fill('input[name="password"]', PASSWORD)
        page.click('button[type="submit"]')
        page.wait_for_load_state("networkidle")
        print("Logged in successfully.")
        
        results = []
        
        for i, problem_id in enumerate(problems, 1):
            url = f"{TICA_BASE}/problem/{problem_id}/test_data"
            page.goto(url)
            page.wait_for_load_state("networkidle")
            
            # Check permissions or 404
            content = page.content()
            if "You don't have permission" in content:
                status = "NO_PERMISSION"
                count = -1
            elif "404" in page.title() or "Not Found" in content:
                status = "NOT_FOUND"
                count = -1
            else:
                count = count_testcases(page)
                status = "OK" if count >= 10 else "INCOMPLETE"
                
            results.append((problem_id, count, status))
            print(f"[{i}/{len(problems)}] {problem_id}: {count} testcases ({status})")
            
        print("\n" + "="*60)
        print("SUMMARY OF TESTCASE UPLOADS ON TICA OJ")
        print("="*60)
        for problem_id, count, status in results:
            print(f"{problem_id:<25}: {count:>2} testcases [{status}]")
            
        browser.close()

if __name__ == "__main__":
    main()
