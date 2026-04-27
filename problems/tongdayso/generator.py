# -*- coding: utf-8 -*-
"""
Testcase Generator for tongdayso
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
    Generate testcases for tongdayso
    Two inputs n and m
    """
    test_cases = []
    
    # Test 1-3: Edge cases
    test_cases.append("6\n6\n")     # Sample 1 (output: 21)
    test_cases.append("6\n3\n")     # Sample 2 (output: 9)
    test_cases.append("1\n1\n")     # Minimal
    
    # Test 4-10: Various combinations
    test_cases.append("10\n5\n")           # n=10, m=5
    test_cases.append("100\n50\n")         # n=100, m=50
    test_cases.append("1000\n500\n")       # n=1000, m=500
    test_cases.append("10000\n7777\n")     # n=10^4
    test_cases.append("100000\n55555\n")   # n=10^5
    test_cases.append("1000000\n333333\n") # n=10^6
    test_cases.append("10000000\n5555555\n") # n=10^7
    
    # Test 11: Random
    n = random.randint(10**4, 10**7)
    m = random.randint(1, n)
    test_cases.append(f"{n}\n{m}\n")
    
    # Generate and save
    print(f"Generating testcases for tongdayso...")
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
    zip_path = os.path.join(SCRIPT_DIR, "tongdayso_testcases.zip")
    
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for i in range(1, 12):
            input_file = os.path.join(SCRIPT_DIR, f"input{i}.in")
            output_file = os.path.join(SCRIPT_DIR, f"output{i}.out")
            
            if os.path.exists(input_file):
                zipf.write(input_file, f"input{i}.in")
            if os.path.exists(output_file):
                zipf.write(output_file, f"output{i}.out")
    
    print(f"[ZIP] Created ZIP: tongdayso_testcases.zip")

if __name__ == "__main__":
    if generate_testcases():
        create_zip()
