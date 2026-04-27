# -*- coding: utf-8 -*-
"""
Testcase Generator for sodacbiet4
"""

import os
import sys
from io import StringIO
import random
import zipfile

# Absolute path
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

def run_editorial(input_data):
    """Chạy editorial.py với input và trả về output"""
    editorial_path = os.path.join(SCRIPT_DIR, "editorial.py")
    
    with open(editorial_path, 'r', encoding='utf-8') as f:
        editorial_code = f.read()
    
    # Redirect stdin/stdout
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    
    try:
        sys.stdin = StringIO(input_data)
        sys.stdout = StringIO()
        
        # Execute editorial code
        exec(editorial_code, {'__name__': '__main__', 'sys': sys, 'StringIO': StringIO})
        
        output = sys.stdout.getvalue()
        return output
    finally:
        sys.stdin = old_stdin
        sys.stdout = old_stdout

def save_testcase(test_num, input_data, output_data):
    """Lưu testcase vào file"""
    input_file = os.path.join(SCRIPT_DIR, f"input{test_num}.in")
    output_file = os.path.join(SCRIPT_DIR, f"output{test_num}.out")
    
    with open(input_file, 'w', encoding='utf-8') as f:
        f.write(input_data)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(output_data)

def generate_testcases():
    """
    Generate testcases for sodacbiet4
    Input: n (1 số)
    Constraints: 10 ≤ n ≤ 10¹⁸
    Output: 1 hoặc -1 (dòng 1), tổng bình phương chữ số (dòng 2)
    """
    test_cases = []
    
    # Test 1-3: Edge cases
    test_cases.append("10\n")  # min, 1² + 0² = 1 (không nguyên tố)
    test_cases.append("21\n")  # ví dụ từ đề (số đặc biệt)
    test_cases.append("24\n")  # ví dụ từ đề (không đặc biệt)
    
    # Test 4-10: Phân bố thông minh
    test_cases.append("12\n")  # 1² + 2² = 5 (nguyên tố)
    test_cases.append("100\n")  # 1² + 0² + 0² = 1 (không nguyên tố)
    test_cases.append("1111\n")  # 1² + 1² + 1² + 1² = 4 (không nguyên tố)
    test_cases.append("123456\n")  # 1² + 2² + 3² + 4² + 5² + 6² = 91 (không nguyên tố)
    test_cases.append(f"{10**12}\n")  # 10¹², 1 + 0×12 = 1 (không nguyên tố)
    test_cases.append(f"{10**18}\n")  # 10¹⁸ (max), 1 + 0×18 = 1 (không nguyên tố)
    test_cases.append("9999999999999999\n")  # toàn chữ số 9
    
    # Test 11: Random case
    n = random.randint(10**12, 10**18)
    test_cases.append(f"{n}\n")
    
    # Generate and save
    print(f"Generating testcases for sodacbiet4...")
    for i, input_data in enumerate(test_cases, 1):
        try:
            output_data = run_editorial(input_data)
            save_testcase(i, input_data, output_data)
            print(f"  [OK] Test {i}: OK")
        except Exception as e:
            print(f"  [FAIL] Test {i}: Error - {e}")
            return False
    
    print(f"[OK] SUCCESS: Generated {len(test_cases)}/11 testcases")
    return True

def create_zip():
    """Tạo file ZIP chứa tất cả testcases"""
    zip_path = os.path.join(SCRIPT_DIR, "sodacbiet4_testcases.zip")
    
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for i in range(1, 12):
            input_file = os.path.join(SCRIPT_DIR, f"input{i}.in")
            output_file = os.path.join(SCRIPT_DIR, f"output{i}.out")
            
            if os.path.exists(input_file):
                zipf.write(input_file, f"input{i}.in")
            if os.path.exists(output_file):
                zipf.write(output_file, f"output{i}.out")
    
    print(f"📦 Created ZIP: sodacbiet4_testcases.zip")

if __name__ == "__main__":
    if generate_testcases():
        create_zip()
