# -*- coding: utf-8 -*-
"""
Testcase Generator for tica_git4
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
    Generate testcases for tica_git4
    Input: X, Y, H (3 dòng riêng biệt)
    Output: ceil(H / (X - Y))
    """
    test_cases = []
    
    # Test 1: Minimum case (X=2, Y=1, H=1)
    test_cases.append("2\n1\n1\n")
    
    # Test 2: Small case (X=10, Y=5, H=10)
    test_cases.append("10\n5\n10\n")
    
    # Test 3: Edge case (X=100, Y=99, H=100)
    test_cases.append("100\n99\n100\n")
    
    # Test 4: Medium case
    test_cases.append("100\n50\n1000\n")
    
    # Test 5: Larger values
    test_cases.append("1000\n500\n10000\n")
    
    # Test 6: Even larger
    test_cases.append("10000\n5000\n100000\n")
    
    # Test 7: Very large H
    test_cases.append("100\n10\n1000000\n")
    
    # Test 8: Large X, Y, H
    test_cases.append("1000000\n100000\n10000000\n")
    
    # Test 9: X much larger than Y
    test_cases.append("1000000\n1\n100000000\n")
    
    # Test 10: Maximum reasonable values
    test_cases.append("1000000\n999999\n1000000000\n")
    
    # Test 11: Random mix
    test_cases.append("12345\n2345\n123456789\n")
    
    # Generate and save
    print(f"Generating testcases for tica_git4...")
    for i, input_data in enumerate(test_cases, 1):
        try:
            output_data = run_editorial(input_data)
            save_testcase(i, input_data, output_data)
            print(f"  [OK] Test {i}")
        except Exception as e:
            print(f"  [FAIL] Test {i}: Error - {e}")
            return False
    
    print(f"[SUCCESS] Generated {len(test_cases)}/11 testcases")
    return True

def create_zip():
    """Tạo file ZIP chứa tất cả testcases"""
    zip_path = os.path.join(SCRIPT_DIR, "tica_git4_testcases.zip")
    
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for i in range(1, 12):
            input_file = os.path.join(SCRIPT_DIR, f"input{i}.in")
            output_file = os.path.join(SCRIPT_DIR, f"output{i}.out")
            
            if os.path.exists(input_file):
                zipf.write(input_file, f"input{i}.in")
            if os.path.exists(output_file):
                zipf.write(output_file, f"output{i}.out")
    
    print(f"[ZIP] Created: tica_git4_testcases.zip")

if __name__ == "__main__":
    if generate_testcases():
        create_zip()
