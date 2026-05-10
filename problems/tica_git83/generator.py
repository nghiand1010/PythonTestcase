# -*- coding: utf-8 -*-
"""
Testcase Generator for tica_git83
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
    Generate testcases for tica_git83
    Input: n, then n pairs (height, price) - find max frequency cafe
    Constraints: 1 <= n <= 10^5, 1 <= h, p <= 10^6
    """
    test_cases = []
    
    # Test 1: Simple case
    test_cases.append("5\n5 10\n5 10\n5 10\n6 15\n6 15\n")
    
    # Test 2: All different
    test_cases.append("4\n1 100\n2 200\n3 300\n4 400\n")
    
    # Test 3: All same
    test_cases.append("10\n100 200\n100 200\n100 200\n100 200\n100 200\n100 200\n100 200\n100 200\n100 200\n100 200\n")
    
    # Test 4-10: Scaled cases
    for n in [100, 500, 1000, 5000, 10000, 50000, 100000]:
        cafes = []
        for _ in range(n):
            h = random.randint(1, 1000000)
            p = random.randint(1, 1000000)
            cafes.append(f"{h} {p}")
        test_cases.append(f"{n}\n" + "\n".join(cafes) + "\n")
    
    # Test 11: Random with duplicates
    cafes = [(random.choice([100, 200, 300]), random.choice([50, 100, 150])) for _ in range(1000)]
    test_cases.append(f"1000\n" + "\n".join(f"{h} {p}" for h, p in cafes) + "\n")
    
    # Generate and save
    print(f"Generating testcases for tica_git83...")
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
    zip_path = os.path.join(SCRIPT_DIR, "tica_git83_testcases.zip")
    
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for i in range(1, 12):
            input_file = os.path.join(SCRIPT_DIR, f"input{i}.in")
            output_file = os.path.join(SCRIPT_DIR, f"output{i}.out")
            
            if os.path.exists(input_file):
                zipf.write(input_file, f"input{i}.in")
            if os.path.exists(output_file):
                zipf.write(output_file, f"output{i}.out")
    
    print(f"[ZIP] Created ZIP: tica_git83_testcases.zip")

if __name__ == "__main__":
    if generate_testcases():
        create_zip()
