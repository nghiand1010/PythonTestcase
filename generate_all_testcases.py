"""
Script tự động tạo testcase cho TẤT CẢ bài trong thư mục problems/
- Đọc đề bài từ problem.md
- Đọc editorial từ editorial.txt
- Sinh testcase thông minh (11 test/bài)
- Chạy editorial Python để có output
- Tạo thư mục daura_{id}/ và zip
"""

import os
import json
import random
import re
import sys
import io
import shutil
from typing import Dict, List, Tuple

def parse_constraints(problem_body: str) -> List[Dict]:
    """Phân tích constraints từ đề bài"""
    constraints = []
    
    # Xử lý 10^5 -> 100000
    problem_body = re.sub(r'10\^(\d+)', lambda m: str(10**int(m.group(1))), problem_body)
    
    # Pattern: min ≤ var ≤ max
    matches = re.finditer(r'(\d+)\s*[≤<=]+\s*([a-zA-Z_]\w*)\s*[≤<=]+\s*(\d+)', problem_body)
    for match in matches:
        constraints.append({
            'var': match.group(2).lower(),
            'min': int(match.group(1)),
            'max': int(match.group(3))
        })
    
    # Pattern: var ≤ max
    if not constraints:
        matches = re.finditer(r'([a-zA-Z_]\w*)\s*[≤<=]+\s*(\d+)', problem_body)
        for match in matches:
            var_name = match.group(1).lower()
            if var_name in ['n', 'm', 'k', 'x', 'y', 'a', 'b', 'c']:
                constraints.append({
                    'var': var_name,
                    'min': 1,
                    'max': int(match.group(2))
                })
    
    return constraints

def extract_python_code(editorial_content: str) -> str:
    """Trích xuất code Python từ editorial"""
    # Nếu có code block markdown
    code_block_pattern = r'```(?:python)?\s*\n(.*?)\n```'
    match = re.search(code_block_pattern, editorial_content, re.DOTALL | re.IGNORECASE)
    if match:
        return match.group(1).strip()
    
    # Nếu không, giả sử toàn bộ là code
    return editorial_content.strip()

def run_editorial_code(editorial_code: str, input_data: str) -> str:
    """Chạy code Python với input để lấy output"""
    input_io = io.StringIO(input_data)
    output_io = io.StringIO()
    
    stdin_backup = sys.stdin
    stdout_backup = sys.stdout
    
    try:
        sys.stdin = input_io
        sys.stdout = output_io
        
        # Thực thi code
        exec_globals = {}
        exec(editorial_code, exec_globals)
        
        # Gọi hàm solve() nếu có
        if 'solve' in exec_globals and callable(exec_globals['solve']):
            sys.stdin = io.StringIO(input_data)  # Reset input
            exec_globals['solve']()
        
    except Exception as e:
        return f"ERROR: {e}"
    finally:
        sys.stdin = stdin_backup
        sys.stdout = stdout_backup
    
    return output_io.getvalue()

def generate_smart_testcase(problem_id: str, constraints: List[Dict], test_num: int) -> str:
    """
    Sinh testcase thông minh dựa vào constraints
    test_num: 1-11 (11 testcase khác nhau)
    """
    
    if not constraints:
        # Không có constraints, tạo test đơn giản
        if test_num == 1:
            return "1\n"
        elif test_num == 2:
            return "10\n"
        else:
            return f"{random.randint(1, 100)}\n"
    
    # Lấy constraint chính (thường là biến đầu tiên: n)
    main_constraint = constraints[0]
    var_name = main_constraint['var']
    min_val = main_constraint['min']
    max_val = main_constraint['max']
    
    # Giới hạn max để tránh testcase quá lớn
    max_val = min(max_val, 10000)
    
    # 11 chiến lược test khác nhau
    test_strategies = [
        min_val,                                    # 1: Min value
        min_val + 1,                               # 2: Min + 1
        (min_val + max_val) // 2,                  # 3: Middle value
        max_val - 1,                               # 4: Max - 1
        max_val,                                   # 5: Max value
        random.randint(min_val, max_val),          # 6: Random
        random.randint(min_val, (min_val + max_val) // 2),  # 7: Random small
        random.randint((min_val + max_val) // 2, max_val),  # 8: Random large
        min_val + random.randint(0, 10),           # 9: Near min
        max_val - random.randint(0, 10),           # 10: Near max
        random.choice([min_val, max_val, (min_val + max_val) // 2])  # 11: Critical values
    ]
    
    # Lấy giá trị cho test này
    value = test_strategies[test_num - 1] if test_num <= len(test_strategies) else random.randint(min_val, max_val)
    value = max(min_val, min(max_val, value))  # Clamp
    
    # Sinh input (format đơn giản: n trên 1 dòng)
    # Với các bài phức tạp hơn, cần thêm logic
    input_lines = [str(value)]
    
    # Nếu có nhiều constraint, thêm các giá trị khác
    for i, constraint in enumerate(constraints[1:], 1):
        if i < 5:  # Giới hạn 5 dòng input
            c_min = constraint['min']
            c_max = min(constraint['max'], 10000)
            c_val = random.randint(c_min, c_max)
            input_lines.append(str(c_val))
    
    return '\n'.join(input_lines) + '\n'

def process_problem(problem_id: str, problem_dir: str):
    """Xử lý 1 bài toán: sinh testcase + zip"""
    
    print(f"\n{'='*60}")
    print(f"Đang xử lý: {problem_id}")
    print(f"{'='*60}")
    
    # Đọc problem.md
    problem_file = os.path.join(problem_dir, 'problem.md')
    if not os.path.exists(problem_file):
        print(f"  ❌ Không tìm thấy problem.md")
        return False
    
    with open(problem_file, 'r', encoding='utf-8') as f:
        problem_body = f.read()
    
    # Đọc editorial.txt
    editorial_file = os.path.join(problem_dir, 'editorial.txt')
    if not os.path.exists(editorial_file):
        print(f"  ⚠️  Không có editorial.txt - Bỏ qua")
        return False
    
    with open(editorial_file, 'r', encoding='utf-8') as f:
        editorial_content = f.read()
    
    if not editorial_content.strip():
        print(f"  ⚠️  Editorial rỗng - Bỏ qua")
        return False
    
    # Parse constraints
    constraints = parse_constraints(problem_body)
    print(f"  📊 Tìm thấy {len(constraints)} constraints")
    
    # Extract Python code
    editorial_code = extract_python_code(editorial_content)
    if not editorial_code:
        print(f"  ❌ Không trích xuất được Python code")
        return False
    
    print(f"  💻 Editorial code: {len(editorial_code)} ký tự")
    
    # Tạo thư mục output
    output_dir = f"daura_{problem_id}"
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
    os.makedirs(output_dir)
    
    # Sinh 11 testcase
    success_count = 0
    for test_num in range(1, 12):
        try:
            # Sinh input
            input_data = generate_smart_testcase(problem_id, constraints, test_num)
            
            # Chạy editorial để có output
            output_data = run_editorial_code(editorial_code, input_data)
            
            if output_data.startswith("ERROR:"):
                print(f"  ⚠️  Test {test_num}: {output_data}")
                continue
            
            # Lưu input và output
            input_file = os.path.join(output_dir, f"input{test_num}.in")
            output_file = os.path.join(output_dir, f"output{test_num}.out")
            
            with open(input_file, 'w', encoding='utf-8') as f:
                f.write(input_data)
            
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(output_data)
            
            success_count += 1
            
        except Exception as e:
            print(f"  ❌ Test {test_num} lỗi: {e}")
            continue
    
    print(f"  ✅ Đã tạo {success_count}/11 testcase")
    
    if success_count == 0:
        print(f"  ❌ Không tạo được testcase nào")
        return False
    
    # Tạo file zip
    zip_file = f"{output_dir}.zip"
    shutil.make_archive(output_dir, 'zip', output_dir)
    print(f"  📦 Đã tạo {zip_file}")
    
    return True

def main():
    """Xử lý tất cả bài trong problems/"""
    
    problems_dir = "problems"
    
    if not os.path.exists(problems_dir):
        print(f"❌ Không tìm thấy thư mục {problems_dir}/")
        return
    
    # Lấy danh sách tất cả problem folders
    problem_folders = [d for d in os.listdir(problems_dir) 
                      if os.path.isdir(os.path.join(problems_dir, d))]
    
    print(f"🚀 Tìm thấy {len(problem_folders)} bài toán")
    print(f"📝 Đang xử lý...\n")
    
    success_count = 0
    skip_count = 0
    error_count = 0
    
    for i, problem_id in enumerate(problem_folders, 1):
        problem_dir = os.path.join(problems_dir, problem_id)
        
        print(f"[{i}/{len(problem_folders)}] ", end="")
        
        try:
            result = process_problem(problem_id, problem_dir)
            if result:
                success_count += 1
            else:
                skip_count += 1
        except Exception as e:
            print(f"  ❌ Lỗi không xử lý được: {e}")
            error_count += 1
    
    # Tổng kết
    print(f"\n{'='*60}")
    print(f"✅ HOÀN THÀNH!")
    print(f"{'='*60}")
    print(f"✅ Thành công: {success_count} bài")
    print(f"⚠️  Bỏ qua: {skip_count} bài (không có editorial)")
    print(f"❌ Lỗi: {error_count} bài")
    print(f"\n📁 Kết quả:")
    print(f"   - Thư mục: daura_{{problem_id}}/")
    print(f"   - File zip: daura_{{problem_id}}.zip")
    print(f"{'='*60}\n")

if __name__ == "__main__":
    main()
