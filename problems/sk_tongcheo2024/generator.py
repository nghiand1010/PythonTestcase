# -*- coding: utf-8 -*-
"""
Testcase Generator for sk_tongcheo2024
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
    Generate testcases for sk_tongcheo2024
    Input: N, Q, then Q pairs (x, y) - compute diagonal sums formula
    Constraints: 1 <= N, Q <= 10^6, 1 <= x, y <= N
    """
    test_cases = []
    
    # Test 1: Simple case
    test_cases.append("3 2\n1 1\n2 2\n")
    
    # Test 2: Small matrix
    test_cases.append("5 3\n1 1\n3 3\n5 5\n")
    
    # Test 3: Larger matrix
    test_cases.append("10 5\n2 3\n5 5\n7 8\n1 10\n10 1\n")
    
    # Test 4-10: Scaled cases
    for scale in [100, 1000, 10000, 100000, 200000, 500000, 1000000]:
        N = scale
        Q = min(scale, 1000000)
        queries = []
        for _ in range(min(Q, 10000)):
            x = random.randint(1, N)
            y = random.randint(1, N)
            queries.append(f"{x} {y}")
        test_cases.append(f"{N} {len(queries)}\n" + "\n".join(queries) + "\n")
    
    # Test 11: Random
    N = 50000
    Q = 1000
    queries = [f"{random.randint(1, N)} {random.randint(1, N)}" for _ in range(Q)]
    test_cases.append(f"{N} {Q}\n" + "\n".join(queries) + "\n")
    
    # Generate and save
    print(f"Generating testcases for sk_tongcheo2024...")
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
    zip_path = os.path.join(SCRIPT_DIR, "sk_tongcheo2024_testcases.zip")
    
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for i in range(1, 12):
            input_file = os.path.join(SCRIPT_DIR, f"input{i}.in")
            output_file = os.path.join(SCRIPT_DIR, f"output{i}.out")
            
            if os.path.exists(input_file):
                zipf.write(input_file, f"input{i}.in")
            if os.path.exists(output_file):
                zipf.write(output_file, f"output{i}.out")
    
    print(f"[ZIP] Created ZIP: sk_tongcheo2024_testcases.zip")

if __name__ == "__main__":
    if generate_testcases():
        create_zip()
