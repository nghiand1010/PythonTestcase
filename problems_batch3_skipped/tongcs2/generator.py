# -*- coding: utf-8 -*-
"""
Testcase Generator for tongcs2
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
    Generate testcases for tongcs2
    1 ≤ n ≤ 45
    """
    test_cases = []
    
    # Test 1-3: Edge cases
    test_cases.append("1")   # Min (output: 1)
    test_cases.append("18")  # Sample (output: 189)
    test_cases.append("45")  # Max (output: 123456789)
    
    # Test 4-10: Various values
    test_cases.append("2")   # Small
    test_cases.append("10")  # Mid-small
    test_cases.append("15")  # Mid
    test_cases.append("20")  # Mid-high
    test_cases.append("30")  # High
    test_cases.append("36")  # 1+2+3+4+5+6+7+8+9=45, so 36 is close
    test_cases.append("44")  # Near max
    
    # Test 11: Random
    test_cases.append(str(random.randint(1, 45)))
    
    # Generate and save
    print(f"Generating testcases for tongcs2...")
    for i, n_str in enumerate(test_cases, 1):
        try:
            input_data = n_str + "\n"
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
    zip_path = os.path.join(SCRIPT_DIR, "tongcs2_testcases.zip")
    
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for i in range(1, 12):
            input_file = os.path.join(SCRIPT_DIR, f"input{i}.in")
            output_file = os.path.join(SCRIPT_DIR, f"output{i}.out")
            
            if os.path.exists(input_file):
                zipf.write(input_file, f"input{i}.in")
            if os.path.exists(output_file):
                zipf.write(output_file, f"output{i}.out")
    
    print(f"Created ZIP: tongcs2_testcases.zip")

if __name__ == "__main__":
    if generate_testcases():
        create_zip()
