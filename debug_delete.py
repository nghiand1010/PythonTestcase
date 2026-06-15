"""
Debug script: Kiểm tra HTML trước và sau khi delete
"""
import time
from pathlib import Path
from playwright.sync_api import sync_playwright

PROBLEM_ID = "dem_chia3"
URL = f"https://oj.tica.edu.vn/problem/{PROBLEM_ID}/test_data"

def count_testcases(html):
    """Đếm số testcases từ HTML"""
    # Tìm các input checkbox testcase
    import re
    pattern = r'name="cases-\d+-'
    matches = re.findall(pattern, html)
    # Loại trùng
    unique = set(matches)
    return len(unique)

def main():
    print("="*60)
    print("🔍 DEBUG: KIỂM TRA DELETE")
    print(f"Problem: {PROBLEM_ID}")
    print("="*60)
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        
        # Login
        print("\n🔐 Đăng nhập...")
        page.goto("https://oj.tica.edu.vn/accounts/login/")
        page.fill('input[name="username"]', 'thinhdt')
        page.fill('input[name="password"]', 'Th09051989@')
        page.click('button[type="submit"]')
        page.wait_for_load_state("networkidle")
        print("✅ Đã đăng nhập")
        
        # Mở test_data page
        print(f"\n🌐 Mở: {URL}")
        page.goto(URL)
        page.wait_for_load_state("networkidle")
        
        # Lấy HTML TRƯỚC khi delete
        html_before = page.content()
        count_before = count_testcases(html_before)
        print(f"\n📊 TRƯỚC DELETE:")
        print(f"   Số testcases: {count_before}")
        
        # Save HTML
        Path("debug_before.html").write_text(html_before, encoding='utf-8')
        print("   Đã lưu: debug_before.html")
        
        # Click Delete All checkbox
        print("\n🗑️  Click Delete All checkbox...")
        delete_all_checkbox = page.locator('input#delete-all')
        if delete_all_checkbox.count() == 0:
            print("   ❌ KHÔNG TÌM THẤY DELETE ALL CHECKBOX!")
            browser.close()
            return
        
        delete_all_checkbox.check()
        print("   ✓ Đã check checkbox")
        
        # Click Apply button
        print("\n✅ Click Apply button...")
        apply_button = page.locator('input[type="submit"][value="Apply!"]')
        if apply_button.count() == 0:
            print("   ❌ KHÔNG TÌM THẤY APPLY BUTTON!")
            browser.close()
            return
        
        apply_button.click()
        print("   ✓ Đã click Apply")
        print("   ⏳ Đợi 5s để xử lý...")
        time.sleep(5)
        page.wait_for_load_state("networkidle")
        
        # Lấy HTML SAU khi delete
        html_after = page.content()
        count_after = count_testcases(html_after)
        print(f"\n📊 SAU DELETE:")
        print(f"   Số testcases: {count_after}")
        
        # Save HTML
        Path("debug_after.html").write_text(html_after, encoding='utf-8')
        print("   Đã lưu: debug_after.html")
        
        # So sánh
        print(f"\n{'='*60}")
        print("📈 KẾT QUẢ:")
        print(f"{'='*60}")
        print(f"Trước: {count_before} testcases")
        print(f"Sau:   {count_after} testcases")
        print(f"Đã xóa: {count_before - count_after} testcases")
        
        if count_after == 0:
            print("\n✅ DELETE THÀNH CÔNG!")
        elif count_after < count_before:
            print(f"\n⚠️  Chỉ xóa được {count_before - count_after}/{count_before}")
        else:
            print("\n❌ DELETE THẤT BẠI!")
        
        print("\n⏸️  Đợi 10s để bạn xem web...")
        time.sleep(10)
        
        browser.close()

if __name__ == "__main__":
    main()
