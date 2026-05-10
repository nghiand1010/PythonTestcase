# -*- coding: utf-8 -*-
"""
Testcase Generator for tich_2so
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
    Generate testcases for tich_2so
    Input: n, then n numbers - find max product of two numbers
    Constraints: 2 <= n <= 10^5, -10^9 <= a[i] <= 10^9
    """
    test_cases = []
    
    # Test 1: Simple positive
    test_cases.append("3\n1 2 3\n")
    
    # Test 2: With negatives
    test_cases.append("4\n-5 -3 2 4\n")
    
    # Test 3: All negative
    test_cases.append("5\n-10 -8 -6 -4 -2\n")
    
    # Test 4-10: Scaled cases
    for n in [10, 100, 1000, 10000, 30000, 60000, 100000]:
        nums = [random.randint(-1000000000, 1000000000) for _ in range(n)]
        test_cases.append(f"{n}\n" + " ".join(map(str, nums)) + "\n")
    
    # Test 11: Random
    nums = [random.randint(-100000000, 100000000) for _ in range(5000)]
    test_cases.append(f"5000\n" + " ".join(map(str, nums)) + "\n")
    
    # Generate and save
    print(f"Generating testcases for tich_2so...")
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
    zip_path = os.path.join(SCRIPT_DIR, "tich_2so_testcases.zip")
    
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for i in range(1, 12):
            input_file = os.path.join(SCRIPT_DIR, f"input{i}.in")
            output_file = os.path.join(SCRIPT_DIR, f"output{i}.out")
            
            if os.path.exists(input_file):
                zipf.write(input_file, f"input{i}.in")
            if os.path.exists(output_file):
                zipf.write(output_file, f"output{i}.out")
    
    print(f"[ZIP] Created ZIP: tich_2so_testcases.zip")

if __name__ == "__main__":
    if generate_testcases():
        create_zip()
