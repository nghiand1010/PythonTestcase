# -*- coding: utf-8 -*-
"""
Auto-submit editorial.py vào TICA OJ cho 91 bài đã upload testcases
"""

from playwright.sync_api import sync_playwright
import time
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent.absolute()
PROBLEMS_DIR = SCRIPT_DIR / "problems"

TICA_USERNAME = "thinhdt"
TICA_PASSWORD = "Th09051989@"

# 91 bài đã upload thành công
ALL_PROBLEMS = [
    # Batch 1: tica_py81-91 (10 bài)
    "tica_py81", "tica_py82", "tica_py83", "tica_py84", "tica_py85",
    "tica_py86", "tica_py87", "tica_py88", "tica_py89", "tica_py90", "tica_py91",
    
    # Batch 2: tica_py92-101 (10 bài)
    "tica_py92", "tica_py93", "tica_py94", "tica_py95", "tica_py96",
    "tica_py97", "tica_py98", "tica_py99", "tica_py100", "tica_py101",
    
    # Batch 3: tica_py142-151 (10 bài)
    "tica_py142", "tica_py143", "tica_py144", "tica_py145", "tica_py146",
    "tica_py147", "tica_py148", "tica_py149", "tica_py150", "tica_py151",
    
    # Batch 4: tica_py152-161 (10 bài)
    "tica_py152", "tica_py153", "tica_py154", "tica_py155", "tica_py156",
    "tica_py157", "tica_py158", "tica_py159", "tica_py160", "tica_py161",
    
    # Batch 5: tica_py162-171 (10 bài)
    "tica_py162", "tica_py163", "tica_py164", "tica_py165", "tica_py166",
    "tica_py167", "tica_py168", "tica_py169", "tica_py170", "tica_py171",
    
    # Batch 6: tica_py172-181 (10 bài)
    "tica_py172", "tica_py173", "tica_py174", "tica_py175", "tica_py176",
    "tica_py177", "tica_py178", "tica_py179", "tica_py180", "tica_py181",
    
    # Batch 7: tica_py182-191 (10 bài)
    "tica_py182", "tica_py183", "tica_py184", "tica_py185", "tica_py186",
    "tica_py187", "tica_py188", "tica_py189", "tica_py190", "tica_py191",
    
    # Batch 8: tica_py192-200 (9 bài)
    "tica_py192", "tica_py193", "tica_py194", "tica_py195", "tica_py196",
    "tica_py197", "tica_py198", "tica_py199", "tica_py200",
    
    # Batch 9: Remaining (12 bài)
    "min_taudien", "nguocdong_tg", "qua_noel", "sk_tongcheo2024",
    "thietbi_daynui", "thu6_ngay13", "tich_2so", "tomau_nangcap",
    "tongchux", "tongx_dbiet", "vienda", "xoayvong"
]

def read_editorial_code(problem_id):
    """Đọc editorial.py của bài"""
    editorial_file = PROBLEMS_DIR / problem_id / "editorial.py"
    if not editorial_file.exists():
        return None
    return editorial_file.read_text(encoding='utf-8')

def submit_code(page, problem_id, code, idx, total):
    """Submit code vào TICA OJ"""
    print(f"[{idx}/{total}] {problem_id}...", end=" ", flush=True)
    
    try:
        # Navigate to submit page
        page.goto(f"https://oj.tica.edu.vn/problem/{problem_id}/submit")
        page.wait_for_load_state("networkidle")
        time.sleep(1)
        
        # Fill code into Ace editor AND sync to textarea
        page.evaluate('''(code) => {
            var editor = ace.edit("ace_source");
            editor.setValue(code, -1);
            editor.clearSelection();
            // Sync to textarea for form submit
            var textarea = document.getElementById('id_source');
            if (textarea) {
                textarea.value = code;
            }
        }''', code)
        time.sleep(1)
        
        # Select Python 3 (value=9)
        page.select_option('select#id_language', '9')
        time.sleep(0.5)
        
        # Click Submit button (input not button!)
        page.locator('input[type="submit"][value="Submit!"]').click()
        page.wait_for_load_state("networkidle")
        time.sleep(2)
        
        # Check if submission successful
        current_url = page.url
        if '/submission/' in current_url:
            submission_id = current_url.split('/submission/')[-1].strip('/')
            print(f"✅ ID:{submission_id}")
            return True, submission_id
        else:
            print("❌ No submission ID")
            return False, None
            
    except Exception as e:
        print(f"❌ {str(e)[:50]}")
        return False, None

def main():
    print("="*70)
    print("AUTO-SUBMIT 91 BÀI EDITORIAL LÊN TICA OJ")
    print("="*70)
    print(f"Total: {len(ALL_PROBLEMS)} bài\n")
    
    # Check editorial files
    print("Checking editorial files...")
    missing = []
    for problem_id in ALL_PROBLEMS:
        code = read_editorial_code(problem_id)
        if code is None:
            missing.append(problem_id)
    
    if missing:
        print(f"⚠️  Missing {len(missing)} editorial files:")
        for p in missing[:10]:
            print(f"  - {p}")
        if len(missing) > 10:
            print(f"  ... and {len(missing)-10} more")
        print()
    
    valid_problems = [p for p in ALL_PROBLEMS if p not in missing]
    print(f"✅ Found {len(valid_problems)} valid editorial files\n")
    
    if not valid_problems:
        print("❌ No problems to submit!")
        return
    
    # Ask user confirmation
    response = input(f"Submit {len(valid_problems)} bài lên TICA OJ? (y/n): ")
    if response.lower() != 'y':
        print("Cancelled.")
        return
    
    print("\n" + "="*70)
    print("SUBMITTING...")
    print("="*70 + "\n")
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        try:
            # Login
            print("Logging in...")
            page.goto("https://oj.tica.edu.vn/accounts/login/")
            page.wait_for_load_state("networkidle")
            page.fill('input[name="username"]', TICA_USERNAME)
            page.fill('input[name="password"]', TICA_PASSWORD)
            page.click('button[type="submit"]')
            page.wait_for_load_state("networkidle")
            time.sleep(2)
            print("✅ Logged in\n")
            
            # Submit all
            success = []
            failed = []
            
            for idx, problem_id in enumerate(valid_problems, 1):
                code = read_editorial_code(problem_id)
                ok, sub_id = submit_code(page, problem_id, code, idx, len(valid_problems))
                
                if ok:
                    success.append((problem_id, sub_id))
                else:
                    failed.append(problem_id)
                
                # Small delay between submissions
                time.sleep(1)
            
            # Summary
            print(f"\n{'='*70}")
            print("KẾT QUẢ SUBMIT")
            print("="*70)
            print(f"✅ Success: {len(success)} bài")
            print(f"❌ Failed: {len(failed)} bài")
            
            if failed:
                print(f"\n⚠️  Failed problems:")
                for p in failed[:10]:
                    print(f"  - {p}")
                if len(failed) > 10:
                    print(f"  ... and {len(failed)-10} more")
            
            if success:
                print(f"\n✅ Submission IDs:")
                for p, sid in success[:10]:
                    print(f"  - {p}: https://oj.tica.edu.vn/submission/{sid}")
                if len(success) > 10:
                    print(f"  ... and {len(success)-10} more")
            
        finally:
            input("\nPress Enter to close browser...")
            browser.close()

if __name__ == "__main__":
    main()
