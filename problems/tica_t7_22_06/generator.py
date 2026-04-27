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
    String grows as: length * (2^n), find m-th character
    """
    test_cases = []
    
    # Test 1-3: Edge cases
    test_cases.append("123\n0\n1\n")  # n=0, first char
    test_cases.append("5\n1\n2\n")    # n=1: "55"
    test_cases.append("7\n2\n5\n")    # n=2: "7777", m > length (should return -1)
    
    # Test 4-10: Progressive n values
    test_cases.append("9\n3\n10\n")           # n=3, moderate position
    test_cases.append("12\n4\n20\n")          # n=4
    test_cases.append("123\n5\n500\n")        # n=5, larger
    test_cases.append("456\n6\n1000\n")       # n=6
    test_cases.append("789\n7\n5000\n")       # n=7
    test_cases.append("11\n8\n10000\n")       # n=8
    test_cases.append("99\n9\n50000\n")       # n=9, near max
    
    # Test 11: Random valid case
    test_cases.append("42\n5\n" + str(random.randint(1, 100)) + "\n")
    
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
