# -*- coding: utf-8 -*-
"""
Testcase Generator for tica_py93
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
    Bài 93: Tạo số - Tạo 2 số có tổng nhỏ nhất từ n chữ số
    Input: T testcases, each: n, then n digits
    Constraints: 0 < T ≤ 100, 0 < n ≤ 50
    """
    test_cases = []
    
    # Test 1: n=1
    test_cases.append("1\n1\n5\n")
    
    # Test 2: n=2  
    test_cases.append("1\n2\n1 0\n")
    
    # Test 3: n=4 (example)
    test_cases.append("2\n4\n1 2 3 4\n3\n0 0 9\n")
    
    # Test 4-7: Small to medium
    test_cases.append("5\n5\n1 2 3 4 5\n6\n0 1 2 3 4 5\n7\n9 8 7 6 5 4 3\n10\n" + " ".join(str(random.randint(0, 9)) for _ in range(10)) + "\n15\n" + " ".join(str(random.randint(0, 9)) for _ in range(15)) + "\n")
    test_cases.append("3\n20\n" + " ".join(str(random.randint(0, 9)) for _ in range(20)) + "\n25\n" + " ".join(str(random.randint(0, 9)) for _ in range(25)) + "\n30\n" + " ".join(str(random.randint(0, 9)) for _ in range(30)) + "\n")
    test_cases.append("2\n35\n" + " ".join(str(random.randint(0, 9)) for _ in range(35)) + "\n40\n" + " ".join(str(random.randint(0, 9)) for _ in range(40)) + "\n")
    test_cases.append("2\n45\n" + " ".join(str(random.randint(0, 9)) for _ in range(45)) + "\n50\n" + " ".join(str(random.randint(0, 9)) for _ in range(50)) + "\n")
    
    # Test 8-10: Large
    test_cases.append("10\n" + "\n".join(f"{random.randint(10, 50)}\n" + " ".join(str(random.randint(0, 9)) for _ in range(random.randint(10, 50))) for _ in range(10)) + "\n")
    test_cases.append("20\n" + "\n".join(f"{random.randint(20, 50)}\n" + " ".join(str(random.randint(0, 9)) for _ in range(random.randint(20, 50))) for _ in range(20)) + "\n")
    test_cases.append("50\n" + "\n".join(f"{random.randint(1, 50)}\n" + " ".join(str(random.randint(0, 9)) for _ in range(random.randint(1, 50))) for _ in range(50)) + "\n")
    
    # Test 11: Stress
    test_cases.append("100\n" + "\n".join(f"{random.randint(1, 50)}\n" + " ".join(str(random.randint(0, 9)) for _ in range(random.randint(1, 50))) for _ in range(100)) + "\n")
    
    # Generate and save
    print(f"Generating testcases for tica_py93...")
    for i, input_data in enumerate(test_cases, 1):
        try:
            output_data = run_editorial(input_data)
            save_testcase(i, input_data, output_data)
            print(f"  [OK] Test {i}: OK")
        except Exception as e:
            print(f"  [FAIL] Test {i}: Error - {e}")
            return False
    
    print(f"[SUCCESS] Generated 11/11 testcases")
    return True

def create_zip():
    """Tạo file ZIP chứa tất cả testcases"""
    zip_path = os.path.join(SCRIPT_DIR, "tica_py93_testcases.zip")
    
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for i in range(1, 12):
            input_file = os.path.join(SCRIPT_DIR, f"input{i}.in")
            output_file = os.path.join(SCRIPT_DIR, f"output{i}.out")
            
            if os.path.exists(input_file):
                zipf.write(input_file, f"input{i}.in")
            if os.path.exists(output_file):
                zipf.write(output_file, f"output{i}.out")
    
    print(f"[ZIP] Created ZIP: tica_py93_testcases.zip")

if __name__ == "__main__":
    if generate_testcases():
        create_zip()
