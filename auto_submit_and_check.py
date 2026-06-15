# -*- coding: utf-8 -*-
"""
Auto-submit editorial.py for all 30 problems to TICA OJ, poll grading status, and verify testcase correctness.
"""
import os
import sys
import time
import re
from pathlib import Path
from playwright.sync_api import sync_playwright

# Reconfigure stdout/stderr to use UTF-8 on Windows
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

def read_editorial_code(problem_id):
    """Read editorial.py content for a problem"""
    editorial_file = PROBLEMS_DIR / problem_id / "editorial.py"
    if not editorial_file.exists():
        return None
    return editorial_file.read_text(encoding='utf-8')

def parse_grading_status(html):
    """Parse DMOJ grading results from HTML page"""
    # Extract all testcase statuses using a robust regex that handles both attribute orderings
    testcase_statuses = []
    for m in re.finditer(r'<span[^>]+case-([A-Z]+)[^>]*title="[^"]*"|<span[^>]+title="[^"]*"[^>]*case-([A-Z]+)', html):
        status = m.group(1) or m.group(2)
        testcase_statuses.append(status)
        
    is_grading = any(q in html for q in ["Queued", "Grading", "Running", "Đang chấm", "Đang đợi"])
    
    if not testcase_statuses:
        if is_grading:
            return "GRADING", 0
        if "Compile Error" in html or "Lỗi biên dịch" in html or "case-CE" in html:
            return "CE", 0
        return "UNKNOWN", 0
        
    unique_statuses = set(testcase_statuses)
    total_cases = len(testcase_statuses)

    if is_grading:
        return "GRADING", total_cases

    if unique_statuses == {"AC"}:
        return "AC", total_cases
        
    # Return worst status found
    for status in ["WA", "TLE", "MLE", "RTE", "CE"]:
        if status in unique_statuses:
            return status, total_cases
            
    return "/".join(unique_statuses), total_cases

def main():
    if len(sys.argv) > 1:
        problems = sys.argv[1:]
    else:
        problems = sorted([d.name for d in PROBLEMS_DIR.iterdir() if d.is_dir()])
        
    print("="*70)
    print(f"🚀 AUTO-SUBMIT AND VERIFY TESTCASES FOR {len(problems)} PROBLEMS")
    print("="*70)
    
    results = {}
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        
        # Login
        print("🔐 Logging into TICA OJ...")
        page.goto(TICA_LOGIN)
        page.fill('input[name="username"]', USERNAME)
        page.fill('input[name="password"]', PASSWORD)
        page.click('button[type="submit"]')
        page.wait_for_load_state("networkidle")
        print("✅ Logged in successfully.\n")
        
        for idx, problem_id in enumerate(problems, 1):
            print(f"[{idx}/{len(problems)}] Processing: {problem_id}")
            code = read_editorial_code(problem_id)
            
            if not code:
                print(f"  ❌ Skip: editorial.py not found")
                results[problem_id] = ("MISSING_EDITORIAL", 0, "N/A")
                continue
                
            # Submit code
            try:
                submit_url = f"{TICA_BASE}/problem/{problem_id}/submit"
                page.goto(submit_url)
                page.wait_for_load_state("networkidle")
                time.sleep(1)
                
                # Check permissions
                if "You don't have permission" in page.content():
                    print("  ❌ No permission to submit this problem")
                    results[problem_id] = ("NO_PERMISSION", 0, "N/A")
                    continue
                
                # Fill Ace editor and sync textarea
                page.evaluate('''(code) => {
                    var editor = ace.edit("ace_source");
                    editor.setValue(code, -1);
                    editor.clearSelection();
                    var textarea = document.getElementById('id_source');
                    if (textarea) {
                        textarea.value = code;
                    }
                }''', code)
                time.sleep(1)
                
                # Select Python 3 (value=9)
                page.select_option('select#id_language', '9')
                time.sleep(0.5)
                
                # Click localized submit button
                submit_btn = page.locator('input[type="submit"][value*="Nộp"], input[type="submit"][value*="Submit"], input[type="submit"]').first
                submit_btn.click()
                page.wait_for_load_state("networkidle")
                time.sleep(2)
                
                current_url = page.url
                if '/submission/' not in current_url:
                    print("  ❌ Submit failed (did not redirect to submission page)")
                    results[problem_id] = ("SUBMIT_FAILED", 0, "N/A")
                    continue
                    
                submission_id = current_url.split('/submission/')[1].split('/')[0].split('?')[0]
                print(f"  📤 Submitted. Submission ID: #{submission_id}")
                
                # Poll grading status
                status = "GRADING"
                test_count = 0
                max_attempts = 15
                
                for attempt in range(1, max_attempts + 1):
                    time.sleep(3)
                    page.goto(f"{TICA_BASE}/submission/{submission_id}")
                    page.wait_for_load_state("networkidle")
                    
                    status, test_count = parse_grading_status(page.content())
                    print(f"    - Attempt {attempt}/{max_attempts}: Status = {status}")
                    
                    if status != "GRADING":
                        break
                        
                if status == "GRADING":
                    status = "TIMEOUT"
                    
                print(f"  📊 Final result: {status} ({test_count} tests)")
                results[problem_id] = (status, test_count, submission_id)
                
            except Exception as e:
                print(f"  ❌ Exception during submission: {e}")
                results[problem_id] = (f"ERROR: {str(e)[:40]}", 0, "N/A")
                
            # Wait 2 seconds between problems to be polite to the server
            time.sleep(2)
            
        browser.close()
        
    # Print summary table
    print("\n" + "="*80)
    print("🏁 SUBMISSION VERIFICATION SUMMARY")
    print("="*80)
    print(f"{'Problem ID':<25} | {'Status':<10} | {'Tests':<5} | {'Submission URL'}")
    print("-"*80)
    
    ac_count = 0
    fail_count = 0
    
    for problem_id in sorted(results.keys()):
        status, test_count, sub_id = results[problem_id]
        url = f"{TICA_BASE}/submission/{sub_id}" if sub_id != "N/A" else "N/A"
        
        status_display = f"✅ {status}" if status == "AC" else f"❌ {status}"
        print(f"{problem_id:<25} | {status_display:<10} | {test_count:<5} | {url}")
        
        if status == "AC":
            ac_count += 1
        else:
            fail_count += 1
            
    print("="*80)
    print(f"🏆 Total Verified: {ac_count}/{len(results)} Accepted")
    print(f"⚠️  Failed/Incomplete: {fail_count}/{len(results)}")
    print("="*80)

if __name__ == "__main__":
    main()
