# -*- coding: utf-8 -*-
"""
Testcase Generator for tica_locha924b3
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
    Generate testcases for tica_locha924b3
    Max difference a[j]-a[i] where i < j
    """
    test_cases = []
    
    # Test 1-3: Edge cases
    test_cases.append("2\n5 10\n")  # Simple case: 10-5=5
    test_cases.append("3\n10 5 15\n")  # Max at end
    test_cases.append("5\n-4 2 8 -6 5\n")  # Example from problem (answer: 12)
    
    # Test 4-10: Varied distributions
    test_cases.append("10\n" + " ".join(str(random.randint(-100, 100)) for _ in range(10)) + "\n")  # Small n
    test_cases.append("100\n" + " ".join(str(random.randint(-1000, 1000)) for _ in range(100)) + "\n")  # Medium n
    test_cases.append("1000\n" + " ".join(str(random.randint(-10000, 10000)) for _ in range(1000)) + "\n")  # Large n
    test_cases.append("10000\n" + " ".join(str(random.randint(-100000, 100000)) for _ in range(10000)) + "\n")  # Very large n
    test_cases.append("50000\n" + " ".join(str(random.randint(-1000000, 1000000)) for _ in range(50000)) + "\n")  # Huge n
    test_cases.append("5000\n" + " ".join(str(random.randint(-10**9, 10**9)) for _ in range(5000)) + "\n")  # Max value range
    test_cases.append("20000\n" + " ".join(str(random.randint(-10**8, 10**8)) for _ in range(20000)) + "\n")  # Large mixed
    
    # Test 11: Random case
    n = random.randint(1000, 10000)
    test_cases.append(f"{n}\n" + " ".join(str(random.randint(-10**6, 10**6)) for _ in range(n)) + "\n")
    
    # Generate and save
    print(f"Generating testcases for tica_locha924b3...")
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
    zip_path = os.path.join(SCRIPT_DIR, "tica_locha924b3_testcases.zip")
    
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for i in range(1, 12):
            input_file = os.path.join(SCRIPT_DIR, f"input{i}.in")
            output_file = os.path.join(SCRIPT_DIR, f"output{i}.out")
            
            if os.path.exists(input_file):
                zipf.write(input_file, f"input{i}.in")
            if os.path.exists(output_file):
                zipf.write(output_file, f"output{i}.out")
    
    print(f"[ZIP] Created ZIP: tica_locha924b3_testcases.zip")

if __name__ == "__main__":
    if generate_testcases():
        create_zip()
