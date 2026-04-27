# -*- coding: utf-8 -*-
"""
Testcase Generator for tichuoc
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
    Generate testcases for tichuoc
    1 < N < 250
    """
    test_cases = []
    
    # Test 1-3: Edge cases
    test_cases.append("16")  # Sample (has even divisors: 2,4,8)
    test_cases.append("3")   # Odd prime (no even divisors)
    test_cases.append("2")   # Min even (no divisors < 2)
    
    # Test 4-10: Various cases
    test_cases.append("4")   # Small even (divisor: 2)
    test_cases.append("12")  # Multiple even divisors (2,4,6)
    test_cases.append("24")  # More divisors
    test_cases.append("100") # Large even
    test_cases.append("128") # Power of 2
    test_cases.append("200") # Near max
    test_cases.append("249") # Max (odd, no even divisors)
    
    # Test 11: Random
    test_cases.append(str(random.randint(2, 249)))
    
    # Generate and save
    print(f"Generating testcases for tichuoc...")
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
    zip_path = os.path.join(SCRIPT_DIR, "tichuoc_testcases.zip")
    
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for i in range(1, 12):
            input_file = os.path.join(SCRIPT_DIR, f"input{i}.in")
            output_file = os.path.join(SCRIPT_DIR, f"output{i}.out")
            
            if os.path.exists(input_file):
                zipf.write(input_file, f"input{i}.in")
            if os.path.exists(output_file):
                zipf.write(output_file, f"output{i}.out")
    
    print(f"Created ZIP: tichuoc_testcases.zip")

if __name__ == "__main__":
    if generate_testcases():
        create_zip()
