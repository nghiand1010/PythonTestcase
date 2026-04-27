# -*- coding: utf-8 -*-
"""
Testcase Generator for tica_hoanvi1
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
    Generate testcases for tica_hoanvi1
    Find k-th permutation of 1..n (n! permutations total)
    Constraint: n ≤ 12 (12! = 479 million, practical limit)
    """
    test_cases = []
    
    # Test 1-3: Edge cases
    test_cases.append("1 1\n")  # Trivial case
    test_cases.append("2 1\n")  # First permutation of 2
    test_cases.append("3 3\n")  # 3rd permutation of 3
    
    # Test 4-10: Varied distributions
    test_cases.append("4 3\n")  # Example from problem
    test_cases.append("5 10\n")  # n=5, mid position
    test_cases.append("6 100\n")  # n=6, larger k
    test_cases.append("7 1000\n")  # n=7, large k
    test_cases.append("8 10000\n")  # n=8, very large k
    test_cases.append("10 1000000\n")  # n=10, huge k
    test_cases.append("12 100000000\n")  # n=12, massive k
    
    # Test 11: Random case
    n = random.randint(8, 12)
    import math
    max_k = math.factorial(n)
    k = random.randint(1, max_k)
    test_cases.append(f"{n} {k}\n")
    
    # Generate and save
    print(f"Generating testcases for tica_hoanvi1...")
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
    zip_path = os.path.join(SCRIPT_DIR, "tica_hoanvi1_testcases.zip")
    
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for i in range(1, 12):
            input_file = os.path.join(SCRIPT_DIR, f"input{i}.in")
            output_file = os.path.join(SCRIPT_DIR, f"output{i}.out")
            
            if os.path.exists(input_file):
                zipf.write(input_file, f"input{i}.in")
            if os.path.exists(output_file):
                zipf.write(output_file, f"output{i}.out")
    
    print(f"[ZIP] Created ZIP: tica_hoanvi1_testcases.zip")

if __name__ == "__main__":
    if generate_testcases():
        create_zip()
