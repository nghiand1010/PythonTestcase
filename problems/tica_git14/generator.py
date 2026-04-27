# -*- coding: utf-8 -*-
"""
Testcase Generator for tica_git14
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
    Generate testcases for tica_git14
    Input: n, k, then n integers - find k-th smallest after sorting
    Constraints: 1 <= n <= 10^5, 0 <= k < n, values <= 10^9
    """
    test_cases = []
    
    # Test 1: Minimum case
    test_cases.append("3 0\n5 3 1\n")
    
    # Test 2: Small case
    test_cases.append("5 2\n10 20 5 15 25\n")
    
    # Test 3: Edge case - k is last
    test_cases.append("10 9\n" + " ".join(str(random.randint(1, 100)) for _ in range(10)) + "\n")
    
    # Test 4: Medium (n=100)
    arr = [random.randint(1, 1000) for _ in range(100)]
    test_cases.append(f"100 50\n" + " ".join(map(str, arr)) + "\n")
    
    # Test 5-7: Medium cases (1000-10000)
    for n in [1000, 5000, 10000]:
        k = n // 2
        arr = [random.randint(1, 1000000) for _ in range(n)]
        test_cases.append(f"{n} {k}\n" + " ".join(map(str, arr)) + "\n")
    
    # Test 8-10: Large cases (near 10^5)
    for n in [30000, 60000, 100000]:
        k = n // 3
        arr = [random.randint(1, 1000000000) for _ in range(n)]
        test_cases.append(f"{n} {k}\n" + " ".join(map(str, arr)) + "\n")
    
    # Test 11: Random medium case
    arr = [random.randint(1, 10000) for _ in range(500)]
    test_cases.append(f"500 250\n" + " ".join(map(str, arr)) + "\n")
    
    # Generate and save
    print(f"Generating testcases for tica_git14...")
    for i, input_data in enumerate(test_cases, 1):
        try:
            output_data = run_editorial(input_data)
            save_testcase(i, input_data, output_data)
            print(f"  [OK] Test {i}")
        except Exception as e:
            print(f"  [FAIL] Test {i}: {e}")
            return False
    
    print(f"[OK] Generated {len(test_cases)}/11 testcases")
    return True

def create_zip():
    """Tạo file ZIP chứa tất cả testcases"""
    zip_path = os.path.join(SCRIPT_DIR, "tica_git14_testcases.zip")
    
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for i in range(1, 12):
            input_file = os.path.join(SCRIPT_DIR, f"input{i}.in")
            output_file = os.path.join(SCRIPT_DIR, f"output{i}.out")
            
            if os.path.exists(input_file):
                zipf.write(input_file, f"input{i}.in")
            if os.path.exists(output_file):
                zipf.write(output_file, f"output{i}.out")
    
    print(f"[ZIP] Created ZIP: tica_git14_testcases.zip")

if __name__ == "__main__":
    if generate_testcases():
        create_zip()
