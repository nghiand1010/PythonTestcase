# -*- coding: utf-8 -*-
"""
Testcase Generator for tica_py196
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
    Generate testcases for tica_py196
    Input: q, then q times (n, array) - count inversions from right
    """
    test_cases = []
    
    # Test 1: Edge - increasing
    test_cases.append("1\n5\n1 2 3 4 5\n")
    
    # Test 2: Edge - decreasing
    test_cases.append("1\n5\n5 4 3 2 1\n")
    
    # Test 3: Edge - mixed
    test_cases.append("2\n6\n3 1 4 1 5 9\n4\n2 3 1 4\n")
    
    # Test 4-10: Scaled tests
    scales = [10, 50, 100, 500, 1000, 5000, 10000]
    for scale in scales:
        q = min(10, scale // 10 + 1)
        lines = [str(q)]
        for _ in range(q):
            n = random.randint(max(1, scale // 10), scale)
            lines.append(str(n))
            lines.append(" ".join(str(random.randint(1, 10**6)) for _ in range(n)))
        test_cases.append("\n".join(lines) + "\n")
    
    # Test 11: Stress test
    q = 100
    lines = [str(q)]
    for _ in range(q):
        n = random.randint(1, 100)
        lines.append(str(n))
        lines.append(" ".join(str(random.randint(1, 10**18)) for _ in range(n)))
    test_cases.append("\n".join(lines) + "\n")
    
    # Generate and save
    print(f"Generating testcases for tica_py196...")
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
    zip_path = os.path.join(SCRIPT_DIR, "tica_py196_testcases.zip")
    
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for i in range(1, 12):
            input_file = os.path.join(SCRIPT_DIR, f"input{i}.in")
            output_file = os.path.join(SCRIPT_DIR, f"output{i}.out")
            
            if os.path.exists(input_file):
                zipf.write(input_file, f"input{i}.in")
            if os.path.exists(output_file):
                zipf.write(output_file, f"output{i}.out")
    
    print(f"[ZIP] Created ZIP: tica_py196_testcases.zip")

if __name__ == "__main__":
    if generate_testcases():
        create_zip()
