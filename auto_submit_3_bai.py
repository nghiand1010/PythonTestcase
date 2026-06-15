#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AUTO SUBMIT EDITORIAL CHO 3 BÀI
"""

from playwright.sync_api import sync_playwright
import time
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent.absolute()
PROBLEMS_DIR = SCRIPT_DIR / "problems"
USERNAME = "thinhdt"
PASSWORD = "Th09051989@"

PROBLEMS = ["bdsochia2", "sodep2", "stickers"]

def submit_code(page, problem_id):
    """Submit editorial.py cho 1 bài"""
    print(f"\\n[{problem_id}]", end=" ", flush=True)
    
    # Đọc editorial
    editorial_path = PROBLEMS_DIR / problem_id / "editorial.py"
    if not editorial_path.exists():
        print("❌ Không tìm thấy editorial.py")
        return False
    
    with open(editorial_path, 'r', encoding='utf-8') as f:
        code = f.read()
    
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
        
        # Submit (input not button!)
        page.locator('input[type="submit"][value="Submit!"]').click()
        page.wait_for_load_state("networkidle")
        time.sleep(2)
        
        # Get submission ID
        current_url = page.url
        if '/submission/' in current_url:
            submission_id = current_url.split('/submission/')[1].split('/')[0].split('?')[0]
            print(f"✅ Submission #{submission_id}")
            return True
        else:
            print("❌ Không thấy submission ID")
            return False
            
    except Exception as e:
        print(f"❌ Lỗi: {e}")
        return False

def main():
    print("="*60)
    print("🚀 AUTO SUBMIT EDITORIAL CHO 3 BÀI")
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
            print(f"[{i}/{len(PROBLEMS)}] ", end="", flush=True)
            
            try:
                if submit_code(page, problem_id):
                    success.append(problem_id)
                else:
                    failed.append(problem_id)
            except Exception as e:
                print(f"❌ Lỗi: {e}")
                failed.append(problem_id)
            
            time.sleep(1)
        
        browser.close()
    
    # Summary
    print("\\n" + "="*60)
    print("📊 KẾT QUẢ")
    print("="*60)
    print(f"✅ Thành công: {len(success)}/{len(PROBLEMS)}")
    print(f"❌ Thất bại: {len(failed)}/{len(PROBLEMS)}")
    
    if success:
        print("\\n✅ Các bài đã submit:")
        for p in success:
            print(f"  - {p}")
    
    if failed:
        print("\\n❌ Các bài thất bại:")
        for p in failed:
            print(f"  - {p}")
    
    if len(success) == len(PROBLEMS):
        print("\\n" + "="*60)
        print("🎉 HOÀN THÀNH! Đã submit 3 bài")
        print("="*60)

if __name__ == "__main__":
    main()
