#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script to scrape all problems on TICA OJ that:
1. Do not have testcases on the server
2. Already have an editorial (solution) code

Saves them to the 'problems' directory.
Moves any existing 'problems' directory to a backup location beforehand.
Uses Playwright only for login, and requests for ultra-fast scraping.
"""

import sys
import time
import shutil
from datetime import datetime
from pathlib import Path
import requests
from bs4 import BeautifulSoup
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

TICA_BASE = "https://oj.tica.edu.vn"
TICA_LOGIN = f"{TICA_BASE}/accounts/login/"
USERNAME = "thinhdt"
PASSWORD = "Th09051989@"

SCRIPT_DIR = Path(__file__).parent.absolute()
PROBLEMS_DIR = SCRIPT_DIR / "problems"

def move_old_problems():
    """Moves existing problems directory to a backup folder with timestamp"""
    if PROBLEMS_DIR.exists():
        # Only backup if it has files inside, to avoid empty backups
        has_files = any(PROBLEMS_DIR.iterdir())
        if not has_files:
            print("ℹ️ Existing problems directory is empty, skipping backup.")
            return

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_dir = SCRIPT_DIR / f"problems_old_{timestamp}"
        print(f"📦 Moving existing problems folder to {backup_dir.name}...")
        try:
            shutil.move(str(PROBLEMS_DIR), str(backup_dir))
            print("✅ Successfully moved the old problems directory.")
        except Exception as e:
            print(f"⚠️ Warning: Could not move directory: {e}")
            print("Trying to rename directly...")
            try:
                PROBLEMS_DIR.rename(backup_dir)
                print("✅ Successfully renamed the old problems directory.")
            except Exception as e2:
                print(f"❌ Error moving directory: {e2}")
                print("Will proceed by writing to the directory as-is.")
    
    # Create fresh empty directory
    PROBLEMS_DIR.mkdir(parents=True, exist_ok=True)

def login_tica(page):
    """Logs in to TICA OJ"""
    print("🔐 Logging in to TICA OJ via Playwright...")
    page.goto(TICA_LOGIN)
    page.wait_for_load_state("networkidle")
    
    page.fill('input[name="username"]', USERNAME)
    page.fill('input[name="password"]', PASSWORD)
    page.click('button[type="submit"]')
    page.wait_for_load_state("networkidle")
    time.sleep(2)
    print("✅ Logged in successfully.\n")

def get_all_problems(session):
    """Pagers through problems page to collect all problem IDs using requests"""
    print("📋 Retrieving all problem IDs from problems list...")
    problem_ids = []
    page_num = 1
    
    while page_num == 1:
        url = f"{TICA_BASE}/problems/?page={page_num}"
        print(f"  📄 Scanning page {page_num}...", end="", flush=True)
        
        try:
            response = session.get(url, timeout=15)
            if response.status_code != 200:
                print(f" ❌ Failed: status {response.status_code}")
                break
            soup = BeautifulSoup(response.text, 'lxml')
        except Exception as e:
            print(f" ❌ Failed: {e}")
            break
            
        # Get all links
        links = soup.find_all('a', href=True)
        page_problems = []
        
        for link in links:
            href = link['href']
            if href.startswith('/problem/'):
                clean_href = href.strip('/')
                parts = clean_href.split('/')
                # Only match format: problem/{id} (length 2, no extra subpaths)
                if len(parts) == 2 and parts[0] == 'problem':
                    pid = parts[1]
                    if pid and pid not in page_problems:
                        page_problems.append(pid)
                        
        if not page_problems:
            print(f" ℹ️ No problems found. Ending pagination.")
            break
            
        for pid in page_problems:
            if pid not in problem_ids:
                problem_ids.append(pid)
                
        print(f" ✅ Found {len(page_problems)} problems.")
        page_num += 1
        
    print(f"\n📊 Total problems discovered on TICA OJ: {len(problem_ids)}\n")
    return problem_ids

def check_has_testcases(session, problem_id):
    """Checks if the problem already has testcases uploaded on the server using requests"""
    url = f"{TICA_BASE}/problem/{problem_id}/test_data"
    try:
        response = session.get(url, timeout=15)
        if response.status_code != 200:
            return f"HTTP_{response.status_code}"
            
        content = response.text
        if "You don't have permission" in content:
            return "NO_PERMISSION"
        if "Could not find a problem" in content:
            return "NOT_FOUND"
            
        soup = BeautifulSoup(content, 'lxml')
        
        # Check for DELETE checkboxes for real testcases
        all_delete_checkboxes = soup.find_all('input', {'type': 'checkbox'})
        real_test_checkboxes = [
            cb for cb in all_delete_checkboxes
            if cb.get('name', '').startswith('cases-') and 
               cb.get('name', '').endswith('-DELETE') and 
               '__prefix__' not in cb.get('name', '')
        ]
        
        return len(real_test_checkboxes) > 0
    except Exception as e:
        print(f"Error checking testcases for {problem_id}: {e}")
        return "ERROR"

def scrape_problem_data(session, problem_id):
    """
    Scrapes problem description and editorial code from the edit page using requests.
    Returns (problem_text, editorial_code, status)
    """
    edit_url = f"{TICA_BASE}/problem/{problem_id}/edit"
    try:
        response = session.get(edit_url, timeout=15)
        if response.status_code != 200:
            return None, None, f"HTTP_{response.status_code}"
            
        soup = BeautifulSoup(response.text, 'lxml')
        
        # Get description
        desc_textarea = soup.find('textarea', {'name': 'description'})
        problem_text = desc_textarea.get_text() if desc_textarea else ""
        
        # Get editorial
        editorial_textarea = soup.find('textarea', {'name': 'solution-0-content'})
        editorial_code = ""
        if editorial_textarea:
            editorial_code = editorial_textarea.get_text().strip()
            
        if not editorial_code:
            return None, None, "NO_EDITORIAL"
            
        return problem_text, editorial_code, "SUCCESS"
    except Exception as e:
        return None, None, f"ERROR: {e}"

def save_problem(problem_id, problem_text, editorial_code):
    """Saves the problem description and editorial code to disk"""
    folder = PROBLEMS_DIR / problem_id
    folder.mkdir(parents=True, exist_ok=True)
    
    # Save problem description
    with open(folder / "problem.txt", "w", encoding="utf-8") as f:
        f.write(problem_text)
        
    # Save editorial solution
    with open(folder / "editorial.txt", "w", encoding="utf-8") as f:
        f.write(editorial_code)

def main():
    print("=" * 60)
    print("🚀 TICA OJ SCRAPER: PROBLEMS WITHOUT TESTS (FAST MODE)")
    print("=" * 60)
    
    # 1. Back up and recreate the problems folder
    move_old_problems()
    
    # 2. Scrape with Playwright to login and transfer session to requests
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        
        try:
            # Login
            login_tica(page)
            
            # Get cookies and setup requests Session
            playwright_cookies = context.cookies()
            session = requests.Session()
            for cookie in playwright_cookies:
                session.cookies.set(cookie['name'], cookie['value'], domain=cookie['domain'])
                
            session.headers.update({
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                'Referer': TICA_BASE
            })
            print("✅ Playwright session cookies transferred to requests.Session.")
            
        finally:
            browser.close()
            
    # 3. Perform scraping using requests Session
    try:
        # Get all problem IDs
        all_problem_ids = get_all_problems(session)
        
        scraped_problems = []
        skipped_has_tests = 0
        skipped_no_editorial = 0
        errors = []
        
        print("=" * 60)
        print("🔍 Processing each problem...")
        print("=" * 60)
        
        for i, problem_id in enumerate(all_problem_ids, 1):
            print(f"[{i}/{len(all_problem_ids)}] {problem_id} -> ", end="", flush=True)
            
            # Check if it has testcases
            has_tests = check_has_testcases(session, problem_id)
            
            if has_tests == "NO_PERMISSION":
                print("🔒 Skip (No permission)")
                errors.append((problem_id, "No permission"))
                continue
            elif has_tests == "NOT_FOUND":
                print("❓ Skip (Not found)")
                errors.append((problem_id, "Not found"))
                continue
            elif has_tests == "ERROR":
                print("❌ Skip (Error checking)")
                errors.append((problem_id, "Error checking"))
                continue
            elif isinstance(has_tests, str) and has_tests.startswith("HTTP_"):
                print(f"❌ Skip ({has_tests})")
                errors.append((problem_id, has_tests))
                continue
            elif has_tests is True:
                print("✅ Skip (Has tests)")
                skipped_has_tests += 1
                continue
            
            # Problem has no testcases, check edit page for editorial
            problem_text, editorial_code, status = scrape_problem_data(session, problem_id)
            
            if status == "SUCCESS":
                save_problem(problem_id, problem_text, editorial_code)
                scraped_problems.append(problem_id)
                print("📥 SAVED (No tests, editorial found!)")
            elif status == "NO_EDITORIAL":
                print("⏭️ Skip (No editorial)")
                skipped_no_editorial += 1
            else:
                print(f"❌ Skip ({status})")
                errors.append((problem_id, status))
            
            # Tiny sleep to avoid server overload but keep it extremely fast
            time.sleep(0.05)
            
        # Summary
        print("\n" + "=" * 60)
        print("🏁 SCRAPING COMPLETED")
        print("=" * 60)
        print(f"✅ Saved to problems/:   {len(scraped_problems)} problems")
        print(f"⏭️ Skipped (has tests):   {skipped_has_tests} problems")
        print(f"⏭️ Skipped (no editorial): {skipped_no_editorial} problems")
        print(f"❌ Errors/Warnings:      {len(errors)} problems")
        
        if scraped_problems:
            print("\nProblems Scraped:")
            for p_id in scraped_problems:
                print(f"  - {p_id}")
                
        if errors:
            print("\nErrors/Warnings Details:")
            for p_id, err in errors:
                print(f"  - {p_id}: {err}")
                
    except Exception as e:
        print(f"\n❌ Global scraper exception: {e}")

if __name__ == "__main__":
    main()
