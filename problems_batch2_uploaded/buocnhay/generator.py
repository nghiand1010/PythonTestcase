# -*- coding: utf-8 -*-
"""
Testcase Generator for buocnhay
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
    Generate testcases for buocnhay
    Input: x1, x2, a (3 dòng riêng biệt)
    Constraints: 1 ≤ x1 ≤ x2 ≤ 10¹², a ≤ 10³
    """
    test_cases = []
    
    # Test 1-3: Edge cases
    test_cases.append("1\n1\n1\n")  # min: x1=x2=1, a=1, khoảng cách 0
    test_cases.append("1\n2\n1\n")  # x1=1, x2=2, a=1, khoảng cách 1
    test_cases.append("1\n10\n3\n")  # khoảng cách 9, a=3 → 3 bước
    
    # Test 4-10: Phân bố thông minh
    test_cases.append("1\n100\n10\n")  # khoảng cách 99, 10²
    test_cases.append("1\n1000\n50\n")  # khoảng cách 999, 10³
    test_cases.append(f"1\n{10**6}\n100\n")  # 10⁶
    test_cases.append(f"1\n{10**9}\n500\n")  # 10⁹
    test_cases.append(f"{10**11}\n{10**12}\n999\n")  # 10¹²
    test_cases.append(f"500000000000\n{10**12}\n1000\n")  # gần max
    test_cases.append(f"1\n{10**12}\n1\n")  # max x2, min a
    
    # Test 11: Random case
    x1 = random.randint(1, 10**9)
    x2 = random.randint(x1, 10**12)
    a = random.randint(1, 1000)
    test_cases.append(f"{x1}\n{x2}\n{a}\n")
    
    # Generate and save
    print(f"Generating testcases for buocnhay...")
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
    zip_path = os.path.join(SCRIPT_DIR, "buocnhay_testcases.zip")
    
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for i in range(1, 12):
            input_file = os.path.join(SCRIPT_DIR, f"input{i}.in")
            output_file = os.path.join(SCRIPT_DIR, f"output{i}.out")
            
            if os.path.exists(input_file):
                zipf.write(input_file, f"input{i}.in")
            if os.path.exists(output_file):
                zipf.write(output_file, f"output{i}.out")
    
    print(f"📦 Created ZIP: buocnhay_testcases.zip")

if __name__ == "__main__":
    if generate_testcases():
        create_zip()
