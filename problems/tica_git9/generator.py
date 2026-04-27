# -*- coding: utf-8 -*-
"""
Testcase Generator for tica_git9
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
    Generate testcases for tica_git9
    Team formation: m (boys), n (girls), k (reserve needed)
    Maximize teams (2 boys + 1 girl) while keeping k reserve
    """
    test_cases = []
    
    # Test 1-3: Edge cases
    test_cases.append("2 1 0\n")  # Exactly 1 team, no reserve
    test_cases.append("0 1 1\n")  # No boys, need reserve
    test_cases.append("10 5 3\n")  # Simple case
    
    # Test 4-10: Varied distributions
    test_cases.append("100 50 10\n")  # Small values
    test_cases.append("1000 500 100\n")  # Medium values
    test_cases.append("10000 5000 500\n")  # Larger values
    test_cases.append("100000 50000 5000\n")  # Large values
    test_cases.append("1000000 500000 10000\n")  # Very large
    test_cases.append(f"{random.randint(1000, 100000)} {random.randint(500, 50000)} {random.randint(100, 10000)}\n")  # Random medium
    test_cases.append(f"{random.randint(100000, 1000000)} {random.randint(50000, 500000)} {random.randint(10000, 100000)}\n")  # Random large
    
    # Test 11: Random case
    test_cases.append(f"{random.randint(10, 1000000)} {random.randint(5, 500000)} {random.randint(1, 100000)}\n")
    
    # Generate and save
    print(f"Generating testcases for tica_git9...")
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
    zip_path = os.path.join(SCRIPT_DIR, "tica_git9_testcases.zip")
    
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for i in range(1, 12):
            input_file = os.path.join(SCRIPT_DIR, f"input{i}.in")
            output_file = os.path.join(SCRIPT_DIR, f"output{i}.out")
            
            if os.path.exists(input_file):
                zipf.write(input_file, f"input{i}.in")
            if os.path.exists(output_file):
                zipf.write(output_file, f"output{i}.out")
    
    print(f"[ZIP] Created ZIP: tica_git9_testcases.zip")

if __name__ == "__main__":
    if generate_testcases():
        create_zip()
