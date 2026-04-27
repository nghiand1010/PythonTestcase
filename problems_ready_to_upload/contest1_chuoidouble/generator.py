# -*- coding: utf-8 -*-
"""
Testcase Generator for contest1_chuoidouble
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
    Generate testcases for contest1_chuoidouble
    Constraint: 1 ≤ len(s) ≤ 255 (string of lowercase letters)
    """
    test_cases = []
    
    # Test 1-3: Edge cases
    test_cases.append("a\n")  # Length 1
    test_cases.append("ab\n")  # Length 2
    test_cases.append("dcab\n")  # Example from problem
    
    # Test 4-10: Varied lengths
    test_cases.append("eraslketc\n")  # Example from problem
    test_cases.append(''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(10)) + "\n")
    test_cases.append(''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(50)) + "\n")
    test_cases.append(''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(100)) + "\n")
    test_cases.append(''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(150)) + "\n")
    test_cases.append(''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(200)) + "\n")
    test_cases.append(''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(255)) + "\n")  # Max
    
    # Test 11: Random
    test_cases.append(''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(random.randint(100, 200))) + "\n")
    
    # Generate and save
    print(f"Generating testcases for contest1_chuoidouble...")
    for i, input_data in enumerate(test_cases, 1):
        try:
            output_data = run_editorial(input_data)
            save_testcase(i, input_data, output_data)
            print(f"  [OK] Test {i}")
        except Exception as e:
            print(f"  [FAIL] Test {i}: Error - {e}")
            return False
    
    print(f"[OK] SUCCESS: Generated {len(test_cases)}/11 testcases")
    return True

def create_zip():
    """Tạo file ZIP chứa tất cả testcases"""
    zip_path = os.path.join(SCRIPT_DIR, "contest1_chuoidouble_testcases.zip")
    
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for i in range(1, 12):
            input_file = os.path.join(SCRIPT_DIR, f"input{i}.in")
            output_file = os.path.join(SCRIPT_DIR, f"output{i}.out")
            
            if os.path.exists(input_file):
                zipf.write(input_file, f"input{i}.in")
            if os.path.exists(output_file):
                zipf.write(output_file, f"output{i}.out")
    
    print(f"[ZIP] Created ZIP: contest1_chuoidouble_testcases.zip")

if __name__ == "__main__":
    if generate_testcases():
        create_zip()
