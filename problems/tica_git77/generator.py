# -*- coding: utf-8 -*-
"""
Testcase Generator for tica_git77
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
    Generate testcases for tica_git77
    Input: Multiple test cases: n (0 to end), then n numeric strings
    Constraints: 1 <= n <= 100, strings are numbers
    """
    test_cases = []
    
    # Test 1: Simple case
    test_cases.append("3\n100\n200\n300\n0\n")
    
    # Test 2: Leading zeros
    test_cases.append("3\n001\n010\n100\n0\n")
    
    # Test 3: Same numbers
    test_cases.append("4\n0050\n50\n050\n00050\n0\n")
    
    # Test 4-10: Scaled cases
    all_tests = []
    for case_count in [5, 10, 20, 30, 50, 80, 100]:
        n = random.randint(5, case_count)
        nums = [str(random.randint(0, 10**random.randint(1, 10))) for _ in range(n)]
        all_tests.append(f"{n}\n" + "\n".join(nums))
    test_cases.append("\n".join(all_tests) + "\n0\n")
    
    # Test 11: Random case
    n = 10
    nums = [str(random.randint(0, 10**20)) for _ in range(n)]
    test_cases.append(f"{n}\n" + "\n".join(nums) + "\n0\n")
    
    # Generate and save
    print(f"Generating testcases for tica_git77...")
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
    zip_path = os.path.join(SCRIPT_DIR, "tica_git77_testcases.zip")
    
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for i in range(1, 12):
            input_file = os.path.join(SCRIPT_DIR, f"input{i}.in")
            output_file = os.path.join(SCRIPT_DIR, f"output{i}.out")
            
            if os.path.exists(input_file):
                zipf.write(input_file, f"input{i}.in")
            if os.path.exists(output_file):
                zipf.write(output_file, f"output{i}.out")
    
    print(f"[ZIP] Created ZIP: tica_git77_testcases.zip")

if __name__ == "__main__":
    if generate_testcases():
        create_zip()
