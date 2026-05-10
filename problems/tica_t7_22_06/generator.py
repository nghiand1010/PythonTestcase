# -*- coding: utf-8 -*-
"""
Testcase Generator for tica_t7_22_06
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
    Generate testcases for tica_t7_22_06
    Input: a (number on line 1), n (on line 2), m (on line 3)
    String grows as: a + reverse(a), repeated n times. Find m-th char.
    Constraints: 1 <= a <= 10^9, 0 <= n <= 20, 1 <= m <= result_length
    """
    test_cases = []
    
    # Test 1-3: Edge cases
    test_cases.append("123\\n0\\n1\\n")  # n=0, first char
    test_cases.append("5\\n1\\n2\\n")    # n=1: "55"
    test_cases.append("7\\n2\\n5\\n")    # n=2: "7777", check valid m
    
    # Test 4-10: Progressive n values
    for n in [3, 4, 5, 6, 8, 10, 15]:
        a = random.randint(1, 100)
        max_len = len(str(a)) * (2 ** n)
        m = random.randint(1, min(max_len, 10**6))
        test_cases.append(f"{a}\\n{n}\\n{m}\\n")
    
    # Test 11: Large case
    test_cases.append("99\\n18\\n100000\\n")
    
    # Generate and save
    print(f"Generating testcases for tica_t7_22_06...")
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
    zip_path = os.path.join(SCRIPT_DIR, "tica_t7_22_06_testcases.zip")
    
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for i in range(1, 12):
            input_file = os.path.join(SCRIPT_DIR, f"input{i}.in")
            output_file = os.path.join(SCRIPT_DIR, f"output{i}.out")
            
            if os.path.exists(input_file):
                zipf.write(input_file, f"input{i}.in")
            if os.path.exists(output_file):
                zipf.write(output_file, f"output{i}.out")
    
    print(f"[ZIP] Created ZIP: tica_t7_22_06_testcases.zip")

if __name__ == "__main__":
    if generate_testcases():
        create_zip()
