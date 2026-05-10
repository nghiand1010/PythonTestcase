# -*- coding: utf-8 -*-
"""
Testcase Generator for tica_py91
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
    Generate testcases for tica_py91 - Tìm số
    Input: T test cases, each has two integers A B
    Find smallest C such that A + B + C is prime
    Constraints: 0 < T ≤ 60, 0 < A,B ≤ 10000
    """
    test_cases = []
    
    # Test 1: Example case from problem
    test_cases.append("2\n1 3\n4 3\n")
    
    # Test 2: Small values - edge cases
    test_cases.append("3\n1 1\n1 2\n2 2\n")
    
    # Test 3: When A+B is already prime (C should be 2)
    test_cases.append("4\n1 4\n2 3\n3 8\n7 12\n")
    
    # Test 4: When A+B is even (C should be 1 or 3)
    test_cases.append("5\n2 4\n5 7\n10 20\n100 200\n1000 2000\n")
    
    # Test 5: When A+B is odd (C should be even)
    test_cases.append("5\n1 6\n3 8\n15 26\n99 100\n1001 2002\n")
    
    # Test 6: Medium values (100-1000)
    test_cases.append("10\n" + "\n".join(f"{random.randint(100, 500)} {random.randint(100, 500)}" for _ in range(10)) + "\n")
    
    # Test 7: Large values (1000-5000)
    test_cases.append("15\n" + "\n".join(f"{random.randint(1000, 2500)} {random.randint(1000, 2500)}" for _ in range(15)) + "\n")
    
    # Test 8: Very large values (5000-10000)
    test_cases.append("20\n" + "\n".join(f"{random.randint(5000, 8000)} {random.randint(5000, 8000)}" for _ in range(20)) + "\n")
    
    # Test 9: Maximum values (near 10000)
    test_cases.append("25\n" + "\n".join(f"{random.randint(9000, 10000)} {random.randint(9000, 10000)}" for _ in range(25)) + "\n")
    
    # Test 10: Maximum T=60 with mixed values
    t = 60
    queries = []
    for i in range(t):
        if i < 10:
            a, b = random.randint(1, 10), random.randint(1, 10)
        elif i < 30:
            a, b = random.randint(10, 1000), random.randint(10, 1000)
        else:
            a, b = random.randint(1000, 10000), random.randint(1000, 10000)
        queries.append(f"{a} {b}")
    test_cases.append(f"{t}\n" + "\n".join(queries) + "\n")
    
    # Test 11: Random case (will be deleted after upload)
    t = random.randint(5, 20)
    queries = [f"{random.randint(1, 5000)} {random.randint(1, 5000)}" for _ in range(t)]
    test_cases.append(f"{t}\n" + "\n".join(queries) + "\n")
    
    # Generate and save
    print(f"Generating testcases for tica_py91...")
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
    zip_path = os.path.join(SCRIPT_DIR, "tica_py91_testcases.zip")
    
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for i in range(1, 12):
            input_file = os.path.join(SCRIPT_DIR, f"input{i}.in")
            output_file = os.path.join(SCRIPT_DIR, f"output{i}.out")
            
            if os.path.exists(input_file):
                zipf.write(input_file, f"input{i}.in")
            if os.path.exists(output_file):
                zipf.write(output_file, f"output{i}.out")
    
    print(f"[ZIP] Created ZIP: tica_py91_testcases.zip")

if __name__ == "__main__":
    if generate_testcases():
        create_zip()
