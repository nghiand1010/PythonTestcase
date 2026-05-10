# -*- coding: utf-8 -*-
"""
Testcase Generator for nhat_soi
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
    Generate testcases for nhat_soi
    Input: n, p, q, then n numbers - determine Andy/Bob winners
    Constraints: 1 <= n <= 10^5, numbers in array, p and q are in array
    """
    test_cases = []
    
    # Test 1: Simple case
    arr = [1, 2, 3, 4, 5]
    test_cases.append(f"5 2 4\n" + " ".join(map(str, arr)) + "\n")
    
    # Test 2: Odd count
    arr = [10, 20, 30, 40, 50, 60, 70]
    test_cases.append(f"7 30 60\n" + " ".join(map(str, arr)) + "\n")
    
    # Test 3: Even count
    arr = [5, 10, 15, 20, 25, 30]
    test_cases.append(f"6 10 25\n" + " ".join(map(str, arr)) + "\n")
    
    # Test 4-10: Scaled cases
    for n in [10, 50, 100, 1000, 10000, 50000, 100000]:
        arr = sorted([random.randint(1, 1000000) for _ in range(n)])
        p = arr[random.randint(0, n-1)]
        q = arr[random.randint(0, n-1)]
        test_cases.append(f"{n} {p} {q}\n" + " ".join(map(str, arr)) + "\n")
    
    # Test 11: Random
    arr = sorted([random.randint(1, 100000) for _ in range(5000)])
    p = arr[1000]
    q = arr[3000]
    test_cases.append(f"5000 {p} {q}\n" + " ".join(map(str, arr)) + "\n")
    
    # Generate and save
    print(f"Generating testcases for nhat_soi...")
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
    zip_path = os.path.join(SCRIPT_DIR, "nhat_soi_testcases.zip")
    
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for i in range(1, 12):
            input_file = os.path.join(SCRIPT_DIR, f"input{i}.in")
            output_file = os.path.join(SCRIPT_DIR, f"output{i}.out")
            
            if os.path.exists(input_file):
                zipf.write(input_file, f"input{i}.in")
            if os.path.exists(output_file):
                zipf.write(output_file, f"output{i}.out")
    
    print(f"[ZIP] Created ZIP: nhat_soi_testcases.zip")

if __name__ == "__main__":
    if generate_testcases():
        create_zip()
