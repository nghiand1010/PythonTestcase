# -*- coding: utf-8 -*-
"""
Testcase Generator for tica_py149
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
    Generate testcases for tica_py149
    Input: T testcases, each with "n k" on one line, then array of n integers
    Constraints: T≤100, N≤1000, K≤9, A[i]≤1000
    """
    test_cases = []
    
    # Test 1: Minimum case - k=0
    test_cases.append("1\n5 0\n10 20 30 40 50\n")
    
    # Test 2: k=1 - common digit
    test_cases.append("1\n5 1\n11 12 13 14 15\n")
    
    # Test 3: k=9 - less common
    test_cases.append("1\n5 9\n99 199 299 399 499\n")
    
    # Test 4-10: Scaled cases
    for t_num in range(4, 11):
        t = min(100, 5 + t_num * 5)
        cases = []
        for _ in range(t):
            n = random.randint(1, 1000)
            k = random.randint(0, 9)
            arr = [random.randint(0, 1000) for _ in range(n)]
            cases.append(f"{n} {k}\n" + " ".join(map(str, arr)))
        test_cases.append(f"{t}\n" + "\n".join(cases) + "\n")
    
    # Test 11: Stress test - max values
    t = 100
    cases = []
    for _ in range(t):
        n = random.randint(500, 1000)
        k = random.randint(0, 9)
        arr = [random.randint(0, 1000) for _ in range(n)]
        cases.append(f"{n} {k}\n" + " ".join(map(str, arr)))
    test_cases.append(f"{t}\n" + "\n".join(cases) + "\n")
    
    # Generate and save
    print(f"Generating testcases for tica_py149...")
    for i, input_data in enumerate(test_cases, 1):
        try:
            output_data = run_editorial(input_data)
            save_testcase(i, input_data, output_data)
            print(f"  [OK] Test {i}: OK")
        except Exception as e:
            print(f"  [FAIL] Test {i}: Error - {e}")
            return False
    
    print(f"[SUCCESS] Generated 11/11 testcases")
    return True

def create_zip():
    """Tạo file ZIP chứa tất cả testcases"""
    zip_path = os.path.join(SCRIPT_DIR, "tica_py149_testcases.zip")
    
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for i in range(1, 12):
            input_file = os.path.join(SCRIPT_DIR, f"input{i}.in")
            output_file = os.path.join(SCRIPT_DIR, f"output{i}.out")
            
            if os.path.exists(input_file):
                zipf.write(input_file, f"input{i}.in")
            if os.path.exists(output_file):
                zipf.write(output_file, f"output{i}.out")
    
    print(f"[ZIP] Created ZIP: tica_py149_testcases.zip")

if __name__ == "__main__":
    if generate_testcases():
        create_zip()
