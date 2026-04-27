# -*- coding: utf-8 -*-
"""
Testcase Generator for tica_git84
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
    Generate testcases for tica_git84
    Count rows in n×n matrix where row sum > 1
    """
    test_cases = []
    
    # Test 1-3: Edge cases
    test_cases.append("1\n1\n")  # Single element
    test_cases.append("2\n0 0\n1 1\n")  # One row with sum > 1
    test_cases.append("3\n1 0 0\n0 1 0\n0 0 1\n")  # Identity matrix
    
    # Test 4-10: Varied distributions
    test_cases.append("5\n" + "\n".join(" ".join(str(random.randint(0, 1)) for _ in range(5)) for _ in range(5)) + "\n")  # Small n
    test_cases.append("10\n" + "\n".join(" ".join(str(random.randint(0, 2)) for _ in range(10)) for _ in range(10)) + "\n")  # n=10
    test_cases.append("20\n" + "\n".join(" ".join(str(random.randint(0, 3)) for _ in range(20)) for _ in range(20)) + "\n")  # n=20
    test_cases.append("50\n" + "\n".join(" ".join(str(random.randint(0, 1)) for _ in range(50)) for _ in range(50)) + "\n")  # Medium
    test_cases.append("100\n" + "\n".join(" ".join(str(random.randint(0, 5)) for _ in range(100)) for _ in range(100)) + "\n")  # Large
    test_cases.append("30\n" + "\n".join(" ".join(str(0 if random.random() < 0.8 else 1) for _ in range(30)) for _ in range(30)) + "\n")  # Sparse
    test_cases.append("15\n" + "\n".join(" ".join(str(random.randint(0, 10)) for _ in range(15)) for _ in range(15)) + "\n")  # Larger values
    
    # Test 11: Random case
    test_cases.append("25\n" + "\n".join(" ".join(str(random.randint(0, 3)) for _ in range(25)) for _ in range(25)) + "\n")
    
    # Generate and save
    print(f"Generating testcases for tica_git84...")
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
    zip_path = os.path.join(SCRIPT_DIR, "tica_git84_testcases.zip")
    
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for i in range(1, 12):
            input_file = os.path.join(SCRIPT_DIR, f"input{i}.in")
            output_file = os.path.join(SCRIPT_DIR, f"output{i}.out")
            
            if os.path.exists(input_file):
                zipf.write(input_file, f"input{i}.in")
            if os.path.exists(output_file):
                zipf.write(output_file, f"output{i}.out")
    
    print(f"[ZIP] Created ZIP: tica_git84_testcases.zip")

if __name__ == "__main__":
    if generate_testcases():
        create_zip()
