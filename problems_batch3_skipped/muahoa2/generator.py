# -*- coding: utf-8 -*-
"""
Testcase Generator for muahoa2
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
    Generate testcases for muahoa2
    1 ≤ a < b ≤ 1000, 0 ≤ c ≤ 100000
    """
    test_cases = []
    
    # Test 1-3: Edge cases
    test_cases.append("2 3 11")      # Sample
    test_cases.append("1 2 0")       # c=0 (no money)
    test_cases.append("1 1000 100000")  # Max b, max c
    
    # Test 4-10: Scale c from small to 100000
    test_cases.append("1 2 10")
    test_cases.append("5 10 100")
    test_cases.append("10 50 1000")
    test_cases.append("50 100 5000")
    test_cases.append("100 500 10000")
    test_cases.append("200 800 50000")
    test_cases.append("500 999 100000")  # Near max
    
    # Test 11: Random
    a = random.randint(1, 500)
    b = random.randint(a + 1, 1000)
    c = random.randint(0, 100000)
    test_cases.append(f"{a} {b} {c}")
    
    # Generate and save
    print(f"Generating testcases for muahoa2...")
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
    zip_path = os.path.join(SCRIPT_DIR, "muahoa2_testcases.zip")
    
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for i in range(1, 12):
            input_file = os.path.join(SCRIPT_DIR, f"input{i}.in")
            output_file = os.path.join(SCRIPT_DIR, f"output{i}.out")
            
            if os.path.exists(input_file):
                zipf.write(input_file, f"input{i}.in")
            if os.path.exists(output_file):
                zipf.write(output_file, f"output{i}.out")
    
    print(f"Created ZIP: muahoa2_testcases.zip")

if __name__ == "__main__":
    if generate_testcases():
        create_zip()
