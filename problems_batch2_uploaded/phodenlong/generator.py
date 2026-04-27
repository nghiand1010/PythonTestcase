# -*- coding: utf-8 -*-
"""
Testcase Generator for phodenlong
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
    Generate testcases for phodenlong
    Input: n (1 số)
    Constraints: 1 ≤ n ≤ 10¹⁸
    Output: floor(sqrt(n))
    """
    test_cases = []
    
    # Test 1-3: Edge cases
    test_cases.append("1\n")  # min, sqrt(1) = 1
    test_cases.append("4\n")  # số chính phương, sqrt(4) = 2
    test_cases.append("5\n")  # ví dụ từ đề, sqrt(5) = 2
    
    # Test 4-10: Phân bố thông minh
    test_cases.append("100\n")  # 10², sqrt = 10
    test_cases.append("1000\n")  # 10³, sqrt = 31
    test_cases.append(f"{10**6}\n")  # 10⁶, sqrt = 1000
    test_cases.append(f"{10**9}\n")  # 10⁹, sqrt = 31622
    test_cases.append(f"{10**12}\n")  # 10¹², sqrt = 1000000
    test_cases.append(f"{10**15}\n")  # 10¹⁵, sqrt = 31622776
    test_cases.append(f"{10**18}\n")  # 10¹⁸ (max), sqrt = 1000000000
    
    # Test 11: Random case
    n = random.randint(10**12, 10**18)
    test_cases.append(f"{n}\n")
    
    # Generate and save
    print(f"Generating testcases for phodenlong...")
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
    zip_path = os.path.join(SCRIPT_DIR, "phodenlong_testcases.zip")
    
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for i in range(1, 12):
            input_file = os.path.join(SCRIPT_DIR, f"input{i}.in")
            output_file = os.path.join(SCRIPT_DIR, f"output{i}.out")
            
            if os.path.exists(input_file):
                zipf.write(input_file, f"input{i}.in")
            if os.path.exists(output_file):
                zipf.write(output_file, f"output{i}.out")
    
    print(f"📦 Created ZIP: phodenlong_testcases.zip")

if __name__ == "__main__":
    if generate_testcases():
        create_zip()
