# -*- coding: utf-8 -*-
"""
Testcase Generator for tica_git22
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
    Generate testcases for tica_git22
    Input: n (denominations count), s (target amount), then n denominations sorted desc
    Constraints: 1 <= n <= 100, 1 <= s, a[i] <= 10^6
    """
    test_cases = []
    
    # Test 1: Minimum case
    test_cases.append("1 10\n10\n")
    
    # Test 2: Small case
    test_cases.append("3 100\n50 20 10\n")
    
    # Test 3: Standard denominations
    test_cases.append("5 1000\n500 200 100 50 20\n")
    
    # Test 4-10: Scaled cases
    for scale in [10, 100, 1000, 10000, 100000, 500000, 1000000]:
        n = min(random.randint(10, 100), 100)
        s = scale
        denoms = sorted([random.randint(1, scale//5) for _ in range(n)], reverse=True)
        test_cases.append(f"{n} {s}\n" + " ".join(map(str, denoms)) + "\n")
    
    # Test 11: Random case
    n = 30
    s = 50000
    denoms = sorted([random.randint(10, 5000) for _ in range(n)], reverse=True)
    test_cases.append(f"{n} {s}\n" + " ".join(map(str, denoms)) + "\n")
    
    # Generate and save
    print(f"Generating testcases for tica_git22...")
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
    zip_path = os.path.join(SCRIPT_DIR, "tica_git22_testcases.zip")
    
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for i in range(1, 12):
            input_file = os.path.join(SCRIPT_DIR, f"input{i}.in")
            output_file = os.path.join(SCRIPT_DIR, f"output{i}.out")
            
            if os.path.exists(input_file):
                zipf.write(input_file, f"input{i}.in")
            if os.path.exists(output_file):
                zipf.write(output_file, f"output{i}.out")
    
    print(f"[ZIP] Created ZIP: tica_git22_testcases.zip")

if __name__ == "__main__":
    if generate_testcases():
        create_zip()
