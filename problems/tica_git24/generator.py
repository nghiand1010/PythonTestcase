# -*- coding: utf-8 -*-
"""
Testcase Generator for tica_git24
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
    Generate testcases for tica_git24
    Input: n, then n numbers - count changes between adjacent elements
    Constraints: 1 <= n <= 10^5, 1 <= a[i] <= 10^9
    """
    test_cases = []
    
    # Test 1: All same - 0 changes
    test_cases.append("3\n5 5 5\n")
    
    # Test 2: All different
    test_cases.append("5\n1 2 3 4 5\n")
    
    # Test 3: Alternating pattern
    test_cases.append("10\n1 2 1 2 1 2 1 2 1 2\n")
    
    # Test 4-10: Scaled cases
    for scale in [100, 1000, 5000, 10000, 30000, 60000, 100000]:
        nums = [random.randint(1, min(scale, 10**9)) for _ in range(scale)]
        test_cases.append(f"{scale}\n" + " ".join(map(str, nums)) + "\n")
    
    # Test 11: Random case
    nums = [random.randint(1, 10000) for _ in range(5000)]
    test_cases.append(f"5000\n" + " ".join(map(str, nums)) + "\n")
    
    # Generate and save
    print(f"Generating testcases for tica_git24...")
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
    zip_path = os.path.join(SCRIPT_DIR, "tica_git24_testcases.zip")
    
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for i in range(1, 12):
            input_file = os.path.join(SCRIPT_DIR, f"input{i}.in")
            output_file = os.path.join(SCRIPT_DIR, f"output{i}.out")
            
            if os.path.exists(input_file):
                zipf.write(input_file, f"input{i}.in")
            if os.path.exists(output_file):
                zipf.write(output_file, f"output{i}.out")
    
    print(f"[ZIP] Created ZIP: tica_git24_testcases.zip")

if __name__ == "__main__":
    if generate_testcases():
        create_zip()
