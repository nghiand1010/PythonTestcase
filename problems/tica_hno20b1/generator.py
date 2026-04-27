# -*- coding: utf-8 -*-
"""
Testcase Generator for tica_hno20b1
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
    Generate testcases for tica_hno20b1
    Find M to minimize |sum(L..M) - sum(M+1..R)|, L < R ≤ 10^9
    """
    test_cases = []
    
    # Test 1-3: Edge cases
    test_cases.append("2 7\n")  # Example from problem
    test_cases.append("1 2\n")  # Minimum range
    test_cases.append("1 10\n")  # Small range
    
    # Test 4-10: Varied distributions (60% ≤ 10^3, 40% ≤ 10^9)
    test_cases.append(f"{random.randint(1, 100)} {random.randint(101, 1000)}\n")  # Small
    test_cases.append(f"{random.randint(1, 500)} {random.randint(501, 1000)}\n")  # Subtask 1
    test_cases.append(f"{random.randint(1, 1000)} {random.randint(10000, 100000)}\n")  # Medium jump
    test_cases.append(f"{random.randint(1, 1000000)} {random.randint(10000000, 100000000)}\n")  # Large
    test_cases.append(f"{random.randint(1, 100000000)} {random.randint(500000000, 1000000000)}\n")  # Very large
    test_cases.append(f"{random.randint(1, 10000)} {random.randint(100000, 10000000)}\n")  # Mixed
    test_cases.append(f"1 {random.randint(100000000, 1000000000)}\n")  # Max range from 1
    
    # Test 11: Random case
    test_cases.append(f"{random.randint(1, 1000000)} {random.randint(10000000, 1000000000)}\n")
    
    # Generate and save
    print(f"Generating testcases for tica_hno20b1...")
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
    zip_path = os.path.join(SCRIPT_DIR, "tica_hno20b1_testcases.zip")
    
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for i in range(1, 12):
            input_file = os.path.join(SCRIPT_DIR, f"input{i}.in")
            output_file = os.path.join(SCRIPT_DIR, f"output{i}.out")
            
            if os.path.exists(input_file):
                zipf.write(input_file, f"input{i}.in")
            if os.path.exists(output_file):
                zipf.write(output_file, f"output{i}.out")
    
    print(f"[ZIP] Created ZIP: tica_hno20b1_testcases.zip")

if __name__ == "__main__":
    if generate_testcases():
        create_zip()
