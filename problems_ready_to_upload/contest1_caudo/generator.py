# -*- coding: utf-8 -*-
"""
Testcase Generator for contest1_caudo
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
    Generate testcases for contest1_caudo
    Constraint: 1 ≤ N ≤ 20, 1 ≤ a_i ≤ 50
    """
    test_cases = []
    
    # Test 1-3: Edge cases
    test_cases.append("1\n2\n")  # N=1
    test_cases.append("2\n3 4\n")  # N=2
    test_cases.append("3\n2 3 2\n")  # Example from problem
    
    # Test 4-10: Varied cases
    test_cases.append("5\n" + " ".join(str(random.randint(1, 10)) for _ in range(5)) + "\n")
    test_cases.append("8\n" + " ".join(str(random.randint(1, 20)) for _ in range(8)) + "\n")
    test_cases.append("10\n" + " ".join(str(random.randint(1, 30)) for _ in range(10)) + "\n")
    test_cases.append("15\n" + " ".join(str(random.randint(1, 40)) for _ in range(15)) + "\n")
    test_cases.append("18\n" + " ".join(str(random.randint(1, 50)) for _ in range(18)) + "\n")
    test_cases.append("20\n" + " ".join(str(random.randint(1, 50)) for _ in range(20)) + "\n")  # Max N
    test_cases.append("20\n" + " ".join(["50"] * 20) + "\n")  # Max N, max values
    
    # Test 11: Random
    n = random.randint(10, 20)
    test_cases.append(f"{n}\n" + " ".join(str(random.randint(1, 50)) for _ in range(n)) + "\n")
    
    # Generate and save
    print(f"Generating testcases for contest1_caudo...")
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
    zip_path = os.path.join(SCRIPT_DIR, "contest1_caudo_testcases.zip")
    
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for i in range(1, 12):
            input_file = os.path.join(SCRIPT_DIR, f"input{i}.in")
            output_file = os.path.join(SCRIPT_DIR, f"output{i}.out")
            
            if os.path.exists(input_file):
                zipf.write(input_file, f"input{i}.in")
            if os.path.exists(output_file):
                zipf.write(output_file, f"output{i}.out")
    
    print(f"[ZIP] Created ZIP: contest1_caudo_testcases.zip")

if __name__ == "__main__":
    if generate_testcases():
        create_zip()
