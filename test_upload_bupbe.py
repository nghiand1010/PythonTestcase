from playwright.sync_api import sync_playwright
import time
from pathlib import Path

PROBLEMS_DIR = Path(__file__).parent / "problems"
problem_id = "bupbe"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    
    # Login
    print("🔐 Đăng nhập...")
    page.goto("https://oj.tica.edu.vn/accounts/login/")
    page.fill('input[name="username"]', 'thinhdt')
    page.fill('input[name="password"]', 'Th09051989@')
    page.click('button[type="submit"]')
    time.sleep(2)
    print("✅ Đã đăng nhập\n")
    
    # Go to test_data page
    url = f"https://oj.tica.edu.vn/problem/{problem_id}/test_data"
    print(f"🌐 Mở: {url}")
    page.goto(url)
    time.sleep(2)
    
    # Check if there are old testcases
    all_delete_checkboxes = page.locator('input[type="checkbox"][name*="-DELETE"]')
    old_test_count = 0
    for i in range(all_delete_checkboxes.count()):
        name = all_delete_checkboxes.nth(i).get_attribute('name')
        if '__prefix__' not in name:
            old_test_count += 1
    
    print(f"📊 Số testcases cũ: {old_test_count}")
    
    if old_test_count > 0:
        print("🗑️  Xóa testcases cũ...")
        delete_all_checkbox = page.locator('input#id_cases-DELETION_DELETE_ALL')
        delete_all_checkbox.check()
        print("✅ Đã chọn Delete all")
        
        # Click Apply
        try:
            apply_button = page.locator('input[type="submit"][value="Apply!"]')
            apply_button.click()
        except:
            try:
                apply_button = page.locator('button:has-text("Apply")')
                apply_button.click()
            except:
                apply_button = page.locator('input[type="submit"]').first
                apply_button.click()
        print("⏳ Đợi TICA xóa testcases (10s)...")
        time.sleep(10)
        page.wait_for_load_state("networkidle")
        print("✅ Đã xóa testcases cũ\n")
    else:
        print("✅ Không có testcases cũ\n")
    
    # Upload ZIP
    zip_file = PROBLEMS_DIR / problem_id / f"{problem_id}_testcases.zip"
    print(f"📦 Upload ZIP: {zip_file.name}")
    
    # Upload file
    file_input = page.locator('input#id_problem-data-zipfile')
    file_input.set_input_files(str(zip_file))
    print("✅ Đã chọn file ZIP")
    
    # Debug: List all buttons
    print("\n🔍 DEBUG: Tìm tất cả buttons:")
    all_buttons = page.locator('button, input[type="submit"]').all()
    for i, btn in enumerate(all_buttons):
        btn_type = btn.get_attribute('type') or 'N/A'
        btn_text = btn.text_content() or btn.get_attribute('value') or 'N/A'
        btn_name = btn.get_attribute('name') or 'N/A'
        print(f"  [{i}] type={btn_type}, text='{btn_text}', name={btn_name}")
    
    print("\n⏸️  Đợi 30s để bạn xem trang web...")
    time.sleep(30)
    
    browser.close()
