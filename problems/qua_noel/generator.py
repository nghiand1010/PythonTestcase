# -*- coding: utf-8 -*-
"""
Testcase Generator for qua_noel
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
    Generate testcases for qua_noel
    Input: n, k, d, then n numbers - group gifts within range k with min d per group
    Constraints: 1 <= n, d <= 10^5, 1 <= k <= 10^9, 1 <= a[i] <= 10^9
    """
    test_cases = []
    
    # Test 1: Simple case
    test_cases.append("5 10 2\n1 5 7 9 11\n")
    
    # Test 2: All in one group
    test_cases.append("4 100 3\n1 2 3 4\n")
    
    # Test 3: Each separate
    test_cases.append("5 5 1\n1 10 20 30 40\n")
    
    # Test 4-10: Scaled cases
    for n in [10, 100, 1000, 10000, 30000, 60000, 100000]:
        k = random.randint(1, 1000000)
        d = random.randint(1, min(n, 1000))
        nums = sorted([random.randint(1, 1000000000) for _ in range(n)])
        test_cases.append(f"{n} {k} {d}\n" + " ".join(map(str, nums)) + "\n")
    
    # Test 11: Random
    n = 5000
    k = 100000
    d = 50
    nums = sorted([random.randint(1, 10000000) for _ in range(n)])
    test_cases.append(f"{n} {k} {d}\n" + " ".join(map(str, nums)) + "\n")
    
    # Generate and save
    print(f"Generating testcases for qua_noel...")
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
    zip_path = os.path.join(SCRIPT_DIR, "qua_noel_testcases.zip")
    
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for i in range(1, 12):
            input_file = os.path.join(SCRIPT_DIR, f"input{i}.in")
            output_file = os.path.join(SCRIPT_DIR, f"output{i}.out")
            
            if os.path.exists(input_file):
                zipf.write(input_file, f"input{i}.in")
            if os.path.exists(output_file):
                zipf.write(output_file, f"output{i}.out")
    
    print(f"[ZIP] Created ZIP: qua_noel_testcases.zip")

if __name__ == "__main__":
    if generate_testcases():
        create_zip()
