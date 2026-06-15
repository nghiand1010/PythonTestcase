"""
Kiểm tra các bài đã upload có testcase không
"""
from playwright.sync_api import sync_playwright
import time

PROBLEMS = [
    "bupbe",
    "chon_2stong",
    "cuahang_sohoc",
    "dem_chia3",
    "dongho_bthuc",
    "nhonhatchia36",
    "quacau",
    "tso_chia5",
    "tuikeo_nguyenkhoa",
    "docsach_books",
    "docsach_marisa",
    "matran_xoanoc",
    "table_tennis",
    "thangmay",
    "tuoinuoc",
    "matran_xoanoc5",
]

def count_testcases(page):
    """Đếm số testcases"""
    all_checkboxes = page.locator('input[type="checkbox"][name*="cases-"]')
    count = 0
    for i in range(all_checkboxes.count()):
        name = all_checkboxes.nth(i).get_attribute('name')
        if '__prefix__' not in name and 'DELETION' not in name and 'delete-all' not in name:
            count += 1
    return count

def main():
    print("="*60)
    print("🔍 KIỂM TRA TESTCASES ĐÃ UPLOAD")
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
        print("✅ Đã đăng nhập\n")
        
        results = []
        
        for problem_id in PROBLEMS:
            url = f"https://oj.tica.edu.vn/problem/{problem_id}/test_data"
            print(f"🔍 {problem_id}...")
            page.goto(url)
            page.wait_for_load_state("networkidle")
            
            count = count_testcases(page)
            results.append((problem_id, count))
            
            if count > 0:
                print(f"   ✅ {count} testcases")
            else:
                print(f"   ❌ KHÔNG CÓ testcase!")
            
            time.sleep(1)
        
        print(f"\n{'='*60}")
        print("📊 TỔNG KẾT")
        print(f"{'='*60}")
        
        ok_count = sum(1 for _, c in results if c > 0)
        fail_count = sum(1 for _, c in results if c == 0)
        
        print(f"✅ Có testcase: {ok_count}/{len(PROBLEMS)}")
        print(f"❌ Không có: {fail_count}/{len(PROBLEMS)}")
        
        if fail_count > 0:
            print("\n❌ Các bài KHÔNG CÓ testcase:")
            for prob, count in results:
                if count == 0:
                    print(f"  - {prob}")
        
        browser.close()

if __name__ == "__main__":
    main()
