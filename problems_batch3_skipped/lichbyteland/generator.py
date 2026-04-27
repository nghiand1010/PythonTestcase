# -*- coding: utf-8 -*-
"""
Testcase Generator for lichbyteland
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
    Generate testcases for lichbyteland
    w: 1-7, d: 1-31, m: 1 ≤ m ≤ 10^9
    """
    test_cases = []
    
    # Test 1-3: Edge cases
    test_cases.append("3\n10 1")       # Sample
    test_cases.append("1\n1 1")        # Min (first day of year)
    test_cases.append("7\n31 1")       # Last day of month 1
    
    # Test 4-10: Scale m from 10² → 10^9
    test_cases.append("1\n1 2")        # Month 2
    test_cases.append("2\n15 100")
    test_cases.append("3\n20 1000")
    test_cases.append("4\n10 10000")
    test_cases.append("5\n25 1000000")
    test_cases.append("6\n5 100000000")
    test_cases.append("7\n30 1000000000")  # 10^9 (max)
    
    # Test 11: Random
    w = random.randint(1, 7)
    m = random.randint(500000000, 1000000000)
    # Check if month is odd (31 days) or even (30 days)
    max_d = 31 if m % 2 == 1 else 30
    d = random.randint(1, max_d)
    test_cases.append(f"{w}\n{d} {m}")
    
    # Generate and save
    print(f"Generating testcases for lichbyteland...")
    for i, case in enumerate(test_cases, 1):
        try:
            input_data = case + "\n"
            output_data = run_editorial(input_data)
            save_testcase(i, input_data, output_data)
            print(f"  [OK] Test {i}")
        except Exception as e:
            print(f"  [FAIL] Test {i}: Error - {e}")
            return False
    
    print(f"SUCCESS: Generated {len(test_cases)}/11 testcases")
    return True

def create_zip():
    """Tạo file ZIP chứa tất cả testcases"""
    zip_path = os.path.join(SCRIPT_DIR, "lichbyteland_testcases.zip")
    
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for i in range(1, 12):
            input_file = os.path.join(SCRIPT_DIR, f"input{i}.in")
            output_file = os.path.join(SCRIPT_DIR, f"output{i}.out")
            
            if os.path.exists(input_file):
                zipf.write(input_file, f"input{i}.in")
            if os.path.exists(output_file):
                zipf.write(output_file, f"output{i}.out")
    
    print(f"Created ZIP: lichbyteland_testcases.zip")

if __name__ == "__main__":
    if generate_testcases():
        create_zip()
