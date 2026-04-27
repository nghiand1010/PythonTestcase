"""
Script để đọc bài toán từ TICA OJ và tự động tạo testcase
Yêu cầu: pip install playwright beautifulsoup4
Sau đó chạy: playwright install chromium
"""

from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import json
import re
import time
import os
import random

# CẤU HÌNH - Thay đổi tại đây
TICA_USERNAME = "thinhdt"  # Thay bằng username của bạn
TICA_PASSWORD = "Th09051989@"  # Thay bằng password của bạn

# Filters
HIDE_SOLVED_PROBLEMS = True  # True = chỉ lấy bài chưa solved
MAX_PROBLEMS = None  # None = lấy tất cả

PROBLEM_URLS = [
    # "https://oj.tica.edu.vn/problems/PROBLEM_ID",
    # Thêm các URL bài toán vào đây nếu muốn lấy bài cụ thể
]

def login_tica(page):
    """Đăng nhập vào TICA OJ"""
    print("Đang đăng nhập...")
    page.goto("https://oj.tica.edu.vn/accounts/login/")
    page.wait_for_load_state("networkidle")
    
    # Điền thông tin đăng nhập
    page.fill('input[name="username"]', TICA_USERNAME)
    page.fill('input[name="password"]', TICA_PASSWORD)
    page.click('button[type="submit"]')
    
    # Đợi đăng nhập thành công
    page.wait_for_load_state("networkidle")
    time.sleep(2)
    print("✅ Đã đăng nhập thành công!")

def extract_constraints(text):
    """
    Phân tích text để tìm constraints
    VD: "1 ≤ N ≤ 15" hoặc "(2 ≤ n ≤ 10^5, S ≤ 10^6)"
    """
    constraints = []
    
    # Pattern để tìm constraints dạng: var ≤/< value hoặc value ≤/< var ≤/< value
    patterns = [
        r'(\d+)\s*[≤<=]+\s*([a-zA-Z_]\w*)\s*[≤<=]+\s*(\d+(?:\^\d+)?)',  # 1 ≤ n ≤ 100
        r'([a-zA-Z_]\w*)\s*[≤<=]+\s*(\d+(?:\^\d+)?)',  # n ≤ 100
        r'\(([^)]+)\)',  # Constraints trong ngoặc đơn
    ]
    
    for pattern in patterns:
        matches = re.finditer(pattern, text)
        for match in matches:
            constraints.append(match.group(0))
    
    return constraints

def parse_problem(page, problem_url):
    """Đọc thông tin bài toán từ trang edit"""
    print(f"\n{'='*60}")
    print(f"Đang đọc: {problem_url}")
    
    # Lấy ID từ URL
    problem_id = problem_url.rstrip('/').split('/')[-1]
    
    # Chuyển sang trang edit
    edit_url = f"https://oj.tica.edu.vn/problem/{problem_id}/edit"
    print(f"Vào trang edit: {edit_url}")
    
    try:
        page.goto(edit_url)
        page.wait_for_load_state("networkidle")
        time.sleep(2)
        
        # Lấy HTML content
        content = page.content()
        soup = BeautifulSoup(content, 'html.parser')
        
        # Kiểm tra xem có phải trang lỗi không
        if "403" in content or "Forbidden" in content or "không có quyền" in content.lower():
            print(f"  ⚠️  Không có quyền truy cập trang edit, bỏ qua bài này")
            return None
        
        # Lấy tên bài toán (từ input field)
        title = "Unknown"
        title_input = soup.find('input', {'name': 'title'}) or \
                     soup.find('input', {'id': 'id_title'}) or \
                     soup.find('input', {'id': 'title'})
        if title_input:
            title = title_input.get('value', 'Unknown')
        
        # Lấy Problem body (từ textarea)
        problem_body = ""
        body_selectors = [
            soup.find('textarea', {'name': 'description'}),
            soup.find('textarea', {'id': 'id_description'}),
            soup.find('textarea', {'name': 'problem_body'}),
            soup.find('textarea', {'id': 'problem_body'}),
        ]
        
        for elem in body_selectors:
            if elem:
                problem_body = elem.get_text()
                break
        
        # Lấy Editorial content (từ textarea)
        editorial_content = ""
        
        # TICA OJ lưu editorial trong solution-X-content
        # Tìm tất cả textarea có name bắt đầu bằng "solution-"
        solution_textareas = soup.find_all('textarea', {'name': lambda x: x and x.startswith('solution-') and x.endswith('-content')})
        
        for elem in solution_textareas:
            content = elem.get_text().strip()
            if content:
                editorial_content += content + "\n\n"
        
        editorial_content = editorial_content.strip()
        
        # Nếu không có editorial, ghi chú
        if not editorial_content:
            print(f"  ℹ️  Bài này không có Editorial content (sẽ bỏ qua khi auto-generate)")
        
        # Tìm phần INPUT trong problem body
        input_section = ""
        if problem_body:
            lines = problem_body.split('\n')
            capture = False
            for line in lines:
                if re.search(r'(input|đầu vào|dữ liệu vào)', line, re.IGNORECASE):
                    capture = True
                elif re.search(r'(output|đầu ra|dữ liệu ra|sample|example|ví dụ)', line, re.IGNORECASE):
                    if capture:
                        break
                if capture:
                    input_section += line + "\n"
        
        # Trích xuất constraints
        constraints = extract_constraints(problem_body) if problem_body else []
        
        problem_info = {
            'id': problem_id,
            'title': title,
            'url': problem_url,
            'edit_url': edit_url,
            'problem_body': problem_body,
            'editorial_content': editorial_content,
            'input_format': input_section.strip(),
            'constraints': constraints,
        }
        
        print(f"📌 Bài: {title}")
        print(f"🔗 ID: {problem_id}")
        print(f"\n📝 Problem Body: {len(problem_body)} ký tự")
        print(f"💡 Editorial: {len(editorial_content)} ký tự")
        print(f"⚙️  Constraints: {len(constraints)} found")
        
        return problem_info
        
    except Exception as e:
        print(f"❌ Lỗi khi parse {problem_id}: {e}")
        import traceback
        traceback.print_exc()
        return None

def check_for_solved_problems(page):
    """Kiểm tra xem có bài solved nào không"""
    try:
        # Tìm các bài đã solved: <td class="solved" solved="1"> với icon <i class="solved-problem-color fa fa-lock">
        solved_elements = page.query_selector_all('td.solved[solved="1"]')
        if solved_elements:
            count = len(solved_elements)
            print(f"  ⚠️  Tìm thấy {count} bài đã solved (cần ẩn đi)")
            return True
        else:
            print(f"  ✅ Không có bài solved nào")
            return False
    except Exception as e:
        print(f"  ⚠️  Lỗi khi check solved: {e}")
        return False

def apply_filters(page):
    """Áp dụng các filter trên trang problems"""
    
    if not HIDE_SOLVED_PROBLEMS:
        print("  ℹ️  Không áp dụng filter (HIDE_SOLVED_PROBLEMS = False)")
        return False
    
    print("\nĐang áp dụng filters...")
    
    # Tìm và click "Hide solved problems"
    try:
        # Thử các selector phổ biến
        selectors = [
            'input[type="checkbox"]:has-text("Hide solved")',
            'input[type="checkbox"][name*="solved"]',
            'input[type="checkbox"][id*="solved"]',
            'label:has-text("Hide solved") input',
            'text=/hide.*solved/i >> xpath=.. >> input',
            '.filter-checkbox:has-text("solved")',
        ]
        
        for selector in selectors:
            try:
                checkbox = page.query_selector(selector)
                if checkbox:
                    is_checked = checkbox.is_checked()
                    if not is_checked:
                        checkbox.check()
                        print("  ✅ Đã bật filter 'Hide solved problems'")
                        time.sleep(1)
                        page.wait_for_load_state("networkidle")
                    else:
                        print("  ℹ️  Filter 'Hide solved problems' đã được bật sẵn")
                    return True
            except:
                continue
        
        print("  ⚠️  Không tìm thấy filter 'Hide solved problems'")
        print("     Có thể filter này không tồn tại hoặc cần selector khác")
        print("     Chạy explore_tica_page.py để xem cấu trúc trang")
        
    except Exception as e:
        print(f"  ⚠️  Lỗi khi apply filter: {e}")
    
    return False

def verify_and_apply_filter(page, max_retries=3):
    """Verify và apply filter nhiều lần cho đến khi không còn solved problems"""
    for attempt in range(1, max_retries + 1):
        print(f"\n🔍 Kiểm tra lần {attempt}...")
        has_solved = check_for_solved_problems(page)
        
        if not has_solved:
            print("  ✅ Filter đã hoạt động đúng!")
            return True
        
        # Có solved problems, cần apply filter
        print(f"  🔄 Cần apply filter (lần thử {attempt}/{max_retries})")
        apply_filters(page)
        time.sleep(2)
        page.wait_for_load_state("networkidle")
    
    # Sau max_retries lần vẫn còn solved
    print(f"  ⚠️  Sau {max_retries} lần thử vẫn còn bài solved, có thể filter bị lỗi")
    has_solved = check_for_solved_problems(page)
    return not has_solved

def get_existing_problem_ids():
    """Lấy danh sách problem IDs đã có trong batch 1 và 2"""
    existing_ids = set()
    
    for batch_dir in ["problems_batch1_uploaded", "problems_batch2_uploaded"]:
        if os.path.exists(batch_dir):
            for item in os.listdir(batch_dir):
                item_path = os.path.join(batch_dir, item)
                if os.path.isdir(item_path):
                    existing_ids.add(item)
    
    return existing_ids

def scrape_all_problems():
    """Đọc tất cả các bài toán và lưu vào thư mục riêng"""
    all_problems = []
    
    # Lấy danh sách bài đã có
    existing_ids = get_existing_problem_ids()
    print(f"\n📋 Đã có {len(existing_ids)} bài từ batch trước (sẽ bỏ qua)")
    if len(existing_ids) > 0:
        print(f"   VD: {', '.join(list(existing_ids)[:5])}, ...")
    
    # Tạo thư mục chính để chứa tất cả bài
    problems_dir = "problems"
    if not os.path.exists(problems_dir):
        os.makedirs(problems_dir)
        print(f"📁 Đã tạo thư mục: {problems_dir}/\n")
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # headless=True để chạy nền
        context = browser.new_context()
        page = context.new_page()
        
        try:
            # Đăng nhập
            login_tica(page)
            
            # Nếu không có URL cụ thể, lấy danh sách từ trang problems
            if not PROBLEM_URLS:
                print("\nĐang lấy danh sách bài toán...")
                
                # Scrape TẤT CẢ các trang có thể
                urls = []
                page_num = 1
                max_pages = 50  # Giới hạn an toàn để tránh loop vô hạn
                
                while page_num <= max_pages:
                    print(f"\n{'='*60}")
                    print(f"Đang scrape trang {page_num}...")
                    
                    if page_num == 1:
                        # Trang 1: vào bình thường rồi apply filter
                        page_url = "https://oj.tica.edu.vn/problems/"
                        page.goto(page_url)
                        page.wait_for_load_state("networkidle")
                        time.sleep(1)
                        
                        # Áp dụng filters và verify
                        verify_and_apply_filter(page, max_retries=3)
                        time.sleep(1)
                    else:
                        # Trang 2+: dùng URL có sẵn filter
                        page_url = f"https://oj.tica.edu.vn/problems/?hide_solved=1&page={page_num}"
                        print(f"  Dùng URL với filter sẵn: {page_url}")
                        page.goto(page_url)
                        page.wait_for_load_state("networkidle")
                        time.sleep(2)
                        
                        # Chỉ verify, không click filter nữa
                        print("\n🔍 Verify trang...")
                        check_for_solved_problems(page)
                    
                    # Check URL hiện tại
                    current_url = page.url
                    print(f"  URL hiện tại: {current_url}")
                    if f"page={page_num}" not in current_url and page_num > 1:
                        print(f"  ⚠️ CẢNH BÁO: Không đúng trang {page_num}!")
                    
                    # Lấy tất cả link bài toán
                    urls_before = len(urls)
                    problem_links = page.query_selector_all('a[href*="/problem/"]')
                    
                    if len(problem_links) == 0:
                        print(f"  ⚠️ Không tìm thấy bài toán nào, dừng scraping")
                        break
                    
                    for link in problem_links:
                        href = link.get_attribute('href')
                        if href and '/problem/' in href:
                            # Lọc bỏ các link không phải bài toán (như /edit, /submit, v.v.)
                            if any(x in href for x in ['/edit', '/submit', '/submissions', '/stats', '/data']):
                                continue
                            
                            # Lấy problem_id từ href
                            # VD: /problem/ABC123 hoặc /problem/ABC123/
                            match = re.search(r'/problem/([a-zA-Z0-9_-]+)/?$', href)
                            if match:
                                problem_id = match.group(1)
                                full_url = f"https://oj.tica.edu.vn/problem/{problem_id}"
                                if full_url not in urls:
                                    urls.append(full_url)
                    
                    urls_after = len(urls)
                    new_count = urls_after - urls_before
                    print(f"  ✅ Lấy được {new_count} bài MỚI từ trang {page_num} (tổng: {urls_after} bài)")
                    
                    # Nếu không có bài mới, dừng lại
                    if new_count == 0:
                        print(f"  ℹ️ Không có bài mới, đã hết trang")
                        break
                    
                    page_num += 1
                
                print(f"Tìm thấy {len(urls)} bài toán")
                
                # Lọc bỏ các bài đã có trong batch trước
                filtered_urls = []
                for url in urls:
                    problem_id = url.rstrip('/').split('/')[-1]
                    if problem_id not in existing_ids:
                        filtered_urls.append(url)
                    else:
                        print(f"  ⏭️  Bỏ qua bài đã có: {problem_id}")
                
                print(f"Sau khi lọc: {len(filtered_urls)} bài MỚI (bỏ qua {len(urls) - len(filtered_urls)} bài cũ)")
                
                # Giới hạn số lượng nếu có
                if MAX_PROBLEMS:
                    target_urls = filtered_urls[:MAX_PROBLEMS]
                    print(f"Sẽ đọc {len(target_urls)} bài (giới hạn bởi MAX_PROBLEMS)")
                else:
                    target_urls = filtered_urls
                    print(f"Sẽ đọc tất cả {len(target_urls)} bài")
            else:
                target_urls = PROBLEM_URLS
            
            # Đọc từng bài và lưu vào thư mục riêng
            success_count = 0
            count_with_editorial = 0
            count_no_editorial = 0
            for i, url in enumerate(target_urls, 1):
                try:
                    print(f"\n[{i}/{len(target_urls)}] ", end="")
                    problem_info = parse_problem(page, url)
                    
                    if problem_info:
                        all_problems.append(problem_info)
                        
                        # Tạo thư mục cho bài này
                        problem_folder = os.path.join(problems_dir, problem_info['id'])
                        os.makedirs(problem_folder, exist_ok=True)
                        
                        # Lưu Problem Body
                        if problem_info['problem_body']:
                            problem_file = os.path.join(problem_folder, 'problem.md')
                            with open(problem_file, 'w', encoding='utf-8') as f:
                                f.write(f"# {problem_info['title']}\n\n")
                                f.write(f"**URL:** {problem_info['url']}\n\n")
                                f.write(f"---\n\n")
                                f.write(problem_info['problem_body'])
                            print(f"  💾 Lưu đề bài: problem.md")
                        
                        # Lưu Editorial Content hoặc đánh dấu không có editorial
                        if problem_info['editorial_content']:
                            editorial_file = os.path.join(problem_folder, 'editorial.txt')
                            with open(editorial_file, 'w', encoding='utf-8') as f:
                                f.write(problem_info['editorial_content'])
                            print(f"  💾 Lưu editorial: editorial.txt")
                            count_with_editorial += 1
                        else:
                            # Tạo file marker để đánh dấu không có editorial
                            marker_file = os.path.join(problem_folder, 'NO_EDITORIAL.txt')
                            with open(marker_file, 'w', encoding='utf-8') as f:
                                f.write('This problem does not have an editorial solution.\n')
                            print(f"  ⚠️  Không có editorial (đã tạo NO_EDITORIAL.txt)")
                            count_no_editorial += 1
                        
                        # Lưu metadata
                        metadata_file = os.path.join(problem_folder, 'info.json')
                        with open(metadata_file, 'w', encoding='utf-8') as f:
                            json.dump({
                                'id': problem_info['id'],
                                'title': problem_info['title'],
                                'url': problem_info['url'],
                                'edit_url': problem_info.get('edit_url', ''),
                                'constraints': problem_info['constraints'],
                                'has_editorial': len(problem_info['editorial_content']) > 0
                            }, f, ensure_ascii=False, indent=2)
                        
                        print(f"  📁 Thư mục: {problem_folder}/")
                        success_count += 1
                    
                    # Delay tránh spam
                    time.sleep(random.uniform(1, 2))
                    
                except Exception as e:
                    print(f"❌ Lỗi khi đọc {url}: {e}")
                    continue
            
        finally:
            browser.close()
    
    # Lưu kết quả tổng hợp (backup)
    output_file = "tica_problems.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(all_problems, f, ensure_ascii=False, indent=2)
    
    print(f"\n{'='*60}")
    print(f"✅ HOÀN THÀNH!")
    print(f"📁 Đã lưu {success_count} bài vào thư mục: {problems_dir}/")
    print(f"   ├─ {count_with_editorial} bài CÓ EDITORIAL")
    print(f"   └─ {count_no_editorial} bài KHÔNG CÓ EDITORIAL (có file NO_EDITORIAL.txt)")
    print(f"📄 File backup JSON: {output_file}")
    print(f"\n💡 Mỗi bài có:")
    print(f"   - problem.md    (đề bài)")
    print(f"   - editorial.txt (code đáp án, nếu có)")
    print(f"   - NO_EDITORIAL.txt (marker nếu không có editorial)")
    print(f"   - info.json     (metadata)")
    print(f"{'='*60}\n")
    
    return all_problems

if __name__ == "__main__":
    print("🚀 TICA OJ Problem Scraper")
    print("="*60)
    
    # Kiểm tra cấu hình
    if TICA_USERNAME == "your_username":
        print("⚠️  Vui lòng cập nhật TICA_USERNAME và TICA_PASSWORD trong file!")
        print("   Mở file scrape_tica.py và thay đổi dòng 13-14")
        exit(1)
    
    # Bắt đầu scrape
    scrape_all_problems()
