# -*- coding: utf-8 -*-
"""
Testcase Generator for tica_locha924b1
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
    Generate testcases for tica_locha924b1
    Count unique integers in two ranges [a,b] and [c,d]
    -10^18 ≤ a,b,c,d ≤ 10^18
    """
    test_cases = []
    
    # Test 1-3: Edge cases
    test_cases.append("3 5 7 9\n")  # Example 1: no overlap
    test_cases.append("4 9 3 5\n")  # Example 2: with overlap
    test_cases.append("1 10 5 15\n")  # Partial overlap
    
    # Test 4-10: Varied distributions
    test_cases.append("1 100 50 150\n")  # Small ranges with overlap
    test_cases.append("-100 100 -50 50\n")  # Negative and positive
    test_cases.append(f"{random.randint(-1000, 0)} {random.randint(0, 1000)} {random.randint(-1000, 0)} {random.randint(0, 1000)}\n")  # Mixed signs
    test_cases.append(f"{random.randint(1, 1000000)} {random.randint(1000001, 10000000)} {random.randint(5000000, 15000000)} {random.randint(15000001, 50000000)}\n")  # Large ranges
    test_cases.append(f"{random.randint(-1000000000, -1000)} {random.randint(-999, 1000000000)} {random.randint(-500000000, 500000000)} {random.randint(500000001, 1000000000)}\n")  # Very large
    test_cases.append(f"-{10**18} {10**18} -{10**18//2} {10**18//2}\n")  # Max range
    test_cases.append(f"{random.randint(-10**17, 0)} {random.randint(1, 10**17)} {random.randint(-10**17, 0)} {random.randint(1, 10**17)}\n")  # Near max
    
    # Test 11: Random case
    a, b = sorted([random.randint(-10**12, 10**12), random.randint(-10**12, 10**12)])
    c, d = sorted([random.randint(-10**12, 10**12), random.randint(-10**12, 10**12)])
    test_cases.append(f"{a} {b} {c} {d}\n")
    
    # Generate and save
    print(f"Generating testcases for tica_locha924b1...")
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
    zip_path = os.path.join(SCRIPT_DIR, "tica_locha924b1_testcases.zip")
    
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for i in range(1, 12):
            input_file = os.path.join(SCRIPT_DIR, f"input{i}.in")
            output_file = os.path.join(SCRIPT_DIR, f"output{i}.out")
            
            if os.path.exists(input_file):
                zipf.write(input_file, f"input{i}.in")
            if os.path.exists(output_file):
                zipf.write(output_file, f"output{i}.out")
    
    print(f"[ZIP] Created ZIP: tica_locha924b1_testcases.zip")

if __name__ == "__main__":
    if generate_testcases():
        create_zip()
