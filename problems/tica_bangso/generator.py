# -*- coding: utf-8 -*-
"""
Testcase Generator for tica_bangso
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
    Generate testcases for tica_bangso
    Input: N (size), M, K (row, col) - find value at position (M,K) in special table
    Constraints: 1 <= M, K <= N <= 10^9
    """
    test_cases = []
    
    # Test 1: Minimum case
    test_cases.append("5\n1 1\n")
    
    # Test 2: Small case
    test_cases.append("5\n3 3\n")
    
    # Test 3: Edge case - corners
    test_cases.append("10\n1 10\n")
    
    # Test 4: Medium N (100)
    test_cases.append("100\n50 50\n")
    
    # Test 5-7: Medium cases (10^4-10^6)
    test_cases.append("10000\n5000 3000\n")
    test_cases.append("100000\n50000 75000\n")
    test_cases.append("1000000\n500000 999999\n")
    
    # Test 8-10: Large cases (near 10^9)
    test_cases.append("10000000\n1000000 5000000\n")
    test_cases.append("100000000\n50000000 50000000\n")
    test_cases.append("1000000000\n999999999 999999999\n")
    
    # Test 11: Random medium case
    test_cases.append("12345\n6789 10111\n")
    
    # Generate and save
    print(f"Generating testcases for tica_bangso...")
    for i, input_data in enumerate(test_cases, 1):
        try:
            output_data = run_editorial(input_data)
            save_testcase(i, input_data, output_data)
            print(f"  [OK] Test {i}")
        except Exception as e:
            print(f"  [FAIL] Test {i}: {e}")
            return False
    
    print(f"[OK] Generated {len(test_cases)}/11 testcases")
    return True

def create_zip():
    """Tạo file ZIP chứa tất cả testcases"""
    zip_path = os.path.join(SCRIPT_DIR, "tica_bangso_testcases.zip")
    
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for i in range(1, 12):
            input_file = os.path.join(SCRIPT_DIR, f"input{i}.in")
            output_file = os.path.join(SCRIPT_DIR, f"output{i}.out")
            
            if os.path.exists(input_file):
                zipf.write(input_file, f"input{i}.in")
            if os.path.exists(output_file):
                zipf.write(output_file, f"output{i}.out")
    
    print(f"[ZIP] Created ZIP: tica_bangso_testcases.zip")

if __name__ == "__main__":
    if generate_testcases():
        create_zip()
