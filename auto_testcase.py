"""
Script tự động sinh testcase và chạy editorial để có output
Đọc từ tica_problems.json và tự động tạo input + output
"""

import json
import random
import re
import os
import sys
import io
import shutil
from typing import Dict, List

def tao_so_ngau_nhien(min_value, max_value):
    """Tạo số ngẫu nhiên trong khoảng"""
    return random.randint(min_value, max_value)

def tao_mang_ngau_nhien(n, min_val, max_val):
    """Tạo mảng n số ngẫu nhiên"""
    return [random.randint(min_val, max_val) for _ in range(n)]

def parse_constraint(constraint_text: str) -> Dict:
    """
    Phân tích constraint để lấy min, max
    VD: "1 ≤ N ≤ 15" -> {'var': 'N', 'min': 1, 'max': 15}
    """
    # Xử lý 10^5 -> 100000
    constraint_text = re.sub(r'10\^(\d+)', lambda m: str(10**int(m.group(1))), constraint_text)
    
    # Pattern: min ≤ var ≤ max
    match = re.search(r'(\d+)\s*[≤<=]+\s*([a-zA-Z_]\w*)\s*[≤<=]+\s*(\d+)', constraint_text)
    if match:
        return {
            'var': match.group(2),
            'min': int(match.group(1)),
            'max': int(match.group(3))
        }
    
    # Pattern: var ≤ max
    match = re.search(r'([a-zA-Z_]\w*)\s*[≤<=]+\s*(\d+)', constraint_text)
    if match:
        return {
            'var': match.group(1),
            'min': 1,
            'max': int(match.group(2))
        }
    
    return None

def run_editorial_code(editorial_code: str, input_data: str) -> str:
    """Chạy code từ editorial với input để lấy output"""
    
    # Tạo StringIO để capture input/output
    input_io = io.StringIO(input_data)
    output_io = io.StringIO()
    
    stdin_goc = sys.stdin
    stdout_goc = sys.stdout
    
    try:
        sys.stdin = input_io
        sys.stdout = output_io
        
        # Thực thi code
        exec_globals = {}
        exec(editorial_code, exec_globals)
        
    except Exception as e:
        return f"ERROR: {e}"
    finally:
        sys.stdin = stdin_goc
        sys.stdout = stdout_goc
    
    output_content = output_io.getvalue()
    output_io.close()
    
    return output_content

def detect_language(editorial_content: str) -> str:
    """Phát hiện ngôn ngữ của editorial"""
    if 'def ' in editorial_content or 'import ' in editorial_content or 'print(' in editorial_content:
        return 'python'
    elif '#include' in editorial_content or 'int main' in editorial_content:
        return 'cpp'
    elif 'public class' in editorial_content or 'public static void main' in editorial_content:
        return 'java'
    return 'unknown'

def extract_python_code(editorial_content: str) -> str:
    """Trích xuất code Python từ editorial"""
    
    # Tìm code block
    code_block_pattern = r'```python\s*\n(.*?)\n```'
    match = re.search(code_block_pattern, editorial_content, re.DOTALL)
    if match:
        return match.group(1)
    
    # Nếu không có markdown, giả sử toàn bộ là code
    return editorial_content

def generate_smart_testcase(problem: Dict, test_num: int) -> str:
    """Tự động sinh testcase thông minh dựa trên constraints"""
    
    constraints = problem.get('constraints', [])
    parsed_constraints = {}
    
    for c in constraints:
        parsed = parse_constraint(c)
        if parsed:
            parsed_constraints[parsed['var'].lower()] = parsed
    
    # Phát hiện cấu trúc input
    input_format = problem.get('input_format', '').lower()
    problem_body = problem.get('problem_body', '').lower()
    
    # Tìm các biến chính
    vars_list = list(parsed_constraints.keys())
    
    if not vars_list:
        return "# Không tìm thấy constraints"
    
    # Sinh test case
    if test_num == 1:
        # Min values
        values = {var: parsed_constraints[var]['min'] for var in vars_list}
    elif test_num == 2:
        # Max values (giới hạn để tránh timeout)
        values = {var: min(parsed_constraints[var]['max'], 10000) for var in vars_list}
    else:
        # Random
        values = {var: tao_so_ngau_nhien(
            parsed_constraints[var]['min'], 
            min(parsed_constraints[var]['max'], 10000)
        ) for var in vars_list}
    
    # Xây dựng input string (cần custom theo từng bài)
    # Đây là template đơn giản
    input_lines = []
    
    # Thử phát hiện cấu trúc
    if 'hai số' in problem_body or 'two numbers' in problem_body.lower():
        # Dòng đầu có 2 số
        if len(vars_list) >= 2:
            input_lines.append(f"{values[vars_list[0]]} {values[vars_list[1]]}")
    elif len(vars_list) >= 1:
        # Mặc định: mỗi biến một dòng
        for var in vars_list[:2]:  # Lấy 2 biến đầu
            input_lines.append(str(values[var]))
    
    # Kiểm tra nếu cần mảng
    if 'mảng' in problem_body or 'array' in problem_body.lower():
        if 'n' in values:
            n = values['n']
            # Tạo mảng n phần tử
            arr = tao_mang_ngau_nhien(n, 1, 1000)
            input_lines.append(' '.join(map(str, arr)))
    
    return '\n'.join(input_lines) + '\n'

def auto_generate_testcases(json_file: str = "tica_problems.json", output_dir: str = "daura"):
    """Tự động tạo testcase và output cho tất cả bài"""
    
    # Đọc problems
    with open(json_file, 'r', encoding='utf-8') as f:
        problems = json.load(f)
    
    print(f"Đọc được {len(problems)} bài toán\n")
    
    for problem in problems:
        problem_id = problem['id']
        print(f"\n{'='*60}")
        print(f"Đang xử lý: {problem_id} - {problem['title']}")
        
        # Tạo thư mục
        problem_dir = f"{output_dir}_{problem_id}"
        if os.path.exists(problem_dir):
            shutil.rmtree(problem_dir)
        os.mkdir(problem_dir)
        
        # Phát hiện ngôn ngữ editorial
        editorial = problem.get('editorial_content', '')
        if not editorial:
            print(f"  ⚠️  Không có editorial, bỏ qua")
            continue
        
        lang = detect_language(editorial)
        print(f"  📝 Editorial language: {lang}")
        
        if lang != 'python':
            print(f"  ⚠️  Chỉ hỗ trợ Python, bỏ qua")
            # Lưu editorial để xem thủ công
            with open(f"{problem_dir}/editorial.txt", 'w', encoding='utf-8') as f:
                f.write(editorial)
            continue
        
        # Trích xuất Python code
        python_code = extract_python_code(editorial)
        
        # Tạo 11 test cases
        success_count = 0
        for i in range(1, 12):
            try:
                # Sinh input
                input_data = generate_smart_testcase(problem, i)
                
                # Ghi input
                with open(f"{problem_dir}/input{i}.in", 'w', encoding='utf-8') as f:
                    f.write(input_data)
                
                # Chạy editorial để lấy output
                output_data = run_editorial_code(python_code, input_data)
                
                # Ghi output
                with open(f"{problem_dir}/output{i}.out", 'w', encoding='utf-8') as f:
                    f.write(output_data.rstrip('\n'))
                
                success_count += 1
                
            except Exception as e:
                print(f"  ❌ Lỗi test {i}: {e}")
        
        print(f"  ✅ Đã tạo {success_count}/11 test cases")
        
        # Tạo zip
        try:
            shutil.make_archive(problem_dir, 'zip', problem_dir)
            print(f"  📦 Đã tạo {problem_dir}.zip")
        except:
            pass
    
    print(f"\n{'='*60}")
    print(f"✅ Hoàn thành!")

if __name__ == "__main__":
    print("🤖 AUTO TESTCASE GENERATOR")
    print("="*60)
    
    try:
        auto_generate_testcases()
    except FileNotFoundError:
        print("❌ Không tìm thấy file tica_problems.json")
        print("   Vui lòng chạy scrape_tica.py trước!")
    except Exception as e:
        print(f"❌ Lỗi: {e}")
        import traceback
        traceback.print_exc()
