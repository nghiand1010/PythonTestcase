"""
SMART TESTCASE GENERATOR - Version 2.0
Tự động phát hiện format input từ editorial code và sinh testcase thông minh
"""

import os
import json
import random
import re
import sys
import io
import shutil
from typing import Dict, List, Tuple

def detect_input_lines(editorial_code: str) -> int:
    """Đếm số dòng input cần thiết từ editorial code"""
    # Đếm số lần gọi input()
    input_count = len(re.findall(r'input\(\)', editorial_code))
    
    # Đếm map(int, input().split())
    split_input_count = len(re.findall(r'input\(\)\.split\(\)', editorial_code))
    
    return max(input_count, split_input_count) if input_count > 0 else 1

def fix_file_io_editorial(editorial_code: str) -> str:
    """Sửa editorial code đọc từ file thành stdin"""
    
    # Thay thế open('FILE.INP') thành sys.stdin
    editorial_code = re.sub(
        r"open\(['\"][\w\.]+['\"],\s*['\"]r['\"].*?\)",
        "sys.stdin",
        editorial_code
    )
    
    # Xóa các dòng with open(...)
    editorial_code = re.sub(
        r"with\s+open\(['\"][^'\"]+['\"]\s*,\s*['\"]r['\"].*?\)\s+as\s+\w+:",
        "# Fixed: reading from stdin",
        editorial_code
    )
    
    # Thay f.readline() -> input()
    editorial_code = re.sub(r'\w+\.readline\(\)', 'input()', editorial_code)
    
    # Thay f.read() -> sys.stdin.read()
    editorial_code = re.sub(r'\w+\.read\(\)', 'sys.stdin.read()', editorial_code)
    
    return editorial_code

def parse_constraints(problem_body: str) -> List[Dict]:
    """Phân tích constraints từ đề bài - improved version"""
    constraints = []
    
    # Xử lý 10^5 -> 100000
    problem_body = re.sub(r'10\^(\d+)', lambda m: str(10**int(m.group(1))), problem_body)
    
    # Pattern: min ≤ var ≤ max
    matches = re.finditer(r'(\d+)\s*[≤<=]+\s*([a-zA-Z_]\w*)\s*[≤<=]+\s*(\d+)', problem_body)
    for match in matches:
        var_name = match.group(2).lower()
        constraints.append({
            'var': var_name,
            'min': int(match.group(1)),
            'max': int(match.group(3))
        })
    
    # Nếu không tìm thấy, thử pattern đơn giản hơn: var ≤ max
    if not constraints:
        matches = re.finditer(r'([a-zA-Z_]\w*)\s*[≤<=]+\s*(\d+)', problem_body)
        for match in matches:
            var_name = match.group(1).lower()
            if var_name in ['n', 'm', 'k', 'x', 'y', 'a', 'b', 'c', 't']:
                constraints.append({
                    'var': var_name,
                    'min': 1,
                    'max': int(match.group(2))
                })
    
    return constraints

def extract_python_code(editorial_content: str) -> str:
    """Trích xuất code Python từ editorial"""
    # Code block markdown
    code_block_pattern = r'```(?:python)?\s*\n(.*?)\n```'
    match = re.search(code_block_pattern, editorial_content, re.DOTALL | re.IGNORECASE)
    if match:
        return match.group(1).strip()
    
    return editorial_content.strip()

def run_editorial_code(editorial_code: str, input_data: str, timeout: int = 5) -> str:
    """Chạy code Python với input để lấy output"""
    input_io = io.StringIO(input_data)
    output_io = io.StringIO()
    
    stdin_backup = sys.stdin
    stdout_backup = sys.stdout
    
    try:
        sys.stdin = input_io
        sys.stdout = output_io
        
        # Fix file I/O
        editorial_code = fix_file_io_editorial(editorial_code)
        
        # Thực thi code
        exec_globals = {'sys': sys, '__name__': '__main__'}
        exec(editorial_code, exec_globals)
        
        # Gọi hàm solve() nếu có
        if 'solve' in exec_globals and callable(exec_globals['solve']):
            sys.stdin = io.StringIO(input_data)  # Reset input
            exec_globals['solve']()
        
    except EOFError:
        return "ERROR: EOF - Input không đủ dòng"
    except Exception as e:
        return f"ERROR: {type(e).__name__}: {e}"
    finally:
        sys.stdin = stdin_backup
        sys.stdout = stdout_backup
    
    return output_io.getvalue()

def generate_smart_input(constraints: List[Dict], num_inputs: int, test_num: int) -> str:
    """
    Sinh input thông minh dựa vào constraints và số dòng cần
    """
    
    if not constraints:
        # Không có constraints, sinh test đơn giản
        values = []
        for i in range(num_inputs):
            if test_num == 1:
                values.append("1")
            elif test_num == 2:
                values.append("10")
            elif test_num <= 5:
                values.append(str(test_num * 10))
            else:
                values.append(str(random.randint(1, 100)))
        return '\n'.join(values) + '\n'
    
    # Có constraints
    values = []
    for i in range(num_inputs):
        if i < len(constraints):
            constraint = constraints[i]
            min_val = constraint['min']
            max_val = min(constraint['max'], 10000)  # Giới hạn max
            
            # 11 chiến lược test
            strategies = [
                min_val,
                min_val + 1,
                (min_val + max_val) // 2,
                max_val - 1,
                max_val,
                random.randint(min_val, max_val),
                random.randint(min_val, (min_val + max_val) // 2),
                random.randint((min_val + max_val) // 2, max_val),
                min_val + random.randint(0, min(10, (max_val - min_val) // 2)),
                max_val - random.randint(0, min(10, (max_val - min_val) // 2)),
                random.choice([min_val, max_val, (min_val + max_val) // 2])
            ]
            
            value = strategies[test_num - 1] if test_num <= len(strategies) else random.randint(min_val, max_val)
            value = max(min_val, min(max_val, value))
            values.append(str(value))
        else:
            # Không đủ constraint, sinh random
            values.append(str(random.randint(1, 100)))
    
    return '\n'.join(values) + '\n'

def process_problem_smart(problem_id: str, problem_dir: str) -> bool:
    """Xử lý 1 bài toán với smart logic"""
    
    print(f"\n{'='*60}")
    print(f"🎯 {problem_id}")
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
        print(f"  ⚠️  Không có editorial - Bỏ qua")
        return False
    
    with open(editorial_file, 'r', encoding='utf-8') as f:
        editorial_content = f.read()
    
    if not editorial_content.strip():
        print(f"  ⚠️  Editorial rỗng - Bỏ qua")
        return False
    
    # Parse constraints
    constraints = parse_constraints(problem_body)
    print(f"  📊 Constraints: {len(constraints)}")
    
    # Extract Python code
    editorial_code = extract_python_code(editorial_content)
    if not editorial_code:
        print(f"  ❌ Không trích xuất được code")
        return False
    
    # Phát hiện số dòng input
    num_inputs = detect_input_lines(editorial_code)
    print(f"  📝 Số dòng input: {num_inputs}")
    print(f"  💻 Editorial: {len(editorial_code)} ký tự")
    
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
            input_data = generate_smart_input(constraints, num_inputs, test_num)
            
            # Chạy editorial để có output
            output_data = run_editorial_code(editorial_code, input_data)
            
            if output_data.startswith("ERROR:"):
                if test_num == 1:  # Chỉ in lỗi test đầu
                    print(f"  ⚠️  {output_data}")
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
            if test_num == 1:
                print(f"  ❌ Lỗi: {e}")
            continue
    
    print(f"  ✅ Tạo được {success_count}/11 testcase")
    
    if success_count == 0:
        print(f"  ❌ FAILED")
        return False
    
    # Tạo file zip
    zip_file = f"{output_dir}.zip"
    shutil.make_archive(output_dir, 'zip', output_dir)
    print(f"  📦 {zip_file}")
    
    return True

def main():
    """Main function - xử lý tất cả bài chưa có zip"""
    
    problems_dir = "problems"
    
    if not os.path.exists(problems_dir):
        print(f"❌ Không tìm thấy thư mục {problems_dir}/")
        return
    
    # Lấy danh sách problem folders
    problem_folders = [d for d in os.listdir(problems_dir) 
                      if os.path.isdir(os.path.join(problems_dir, d))]
    
    # Lọc các bài chưa có zip
    problems_to_process = []
    for problem_id in problem_folders:
        zip_file = f"daura_{problem_id}.zip"
        if not os.path.exists(zip_file):
            problems_to_process.append(problem_id)
    
    print(f"🚀 SMART TESTCASE GENERATOR v2.0")
    print(f"{'='*60}")
    print(f"📝 Tìm thấy {len(problems_to_process)} bài cần xử lý\n")
    
    if not problems_to_process:
        print("✅ Tất cả bài đã có testcase!")
        return
    
    success_count = 0
    failed_list = []
    
    for i, problem_id in enumerate(problems_to_process, 1):
        problem_dir = os.path.join(problems_dir, problem_id)
        
        print(f"[{i}/{len(problems_to_process)}] ", end="")
        
        try:
            result = process_problem_smart(problem_id, problem_dir)
            if result:
                success_count += 1
            else:
                failed_list.append(problem_id)
        except Exception as e:
            print(f"  ❌ Exception: {e}")
            failed_list.append(problem_id)
    
    # Tổng kết
    print(f"\n{'='*60}")
    print(f"✅ HOÀN THÀNH!")
    print(f"{'='*60}")
    print(f"✅ Thành công: {success_count}/{len(problems_to_process)} bài")
    
    if failed_list:
        print(f"\n⚠️  Các bài chưa xử lý được ({len(failed_list)}):")
        for problem_id in failed_list:
            print(f"   - {problem_id}")
    
    print(f"\n📁 Kết quả: daura_{{problem_id}}.zip")
    print(f"{'='*60}\n")

if __name__ == "__main__":
    main()
