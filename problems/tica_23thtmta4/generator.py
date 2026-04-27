# -*- coding: utf-8 -*-
"""
Testcase Generator for tica_23thtmta4
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
    Generate testcases for tica_23thtmta4
    Input: a (string of digits), l, r (1-indexed positions)
    Creates s = a + reverse(a), sum digits from position l to r
    Constraints: 1 <= len(a) <= 10^5, 1 <= l <= r <= 2*len(a)
    """
    test_cases = []
    
    # Test 1: Minimum case - single digit
    test_cases.append("1\n1\n1\n")
    
    # Test 2: Small case from problem
    test_cases.append("123\n1\n3\n")
    
    # Test 3: Edge case - query full string
    test_cases.append("99\n1\n4\n")
    
    # Test 4: Small varied (100 digits)
    a = ''.join(str(random.randint(1, 9)) for _ in range(50))
    test_cases.append(f"{a}\n1\n{len(a)*2}\n")
    
    # Test 5-7: Medium cases (1000-10000 digits)
    for size in [500, 2000, 5000]:
        a = ''.join(str(random.randint(1, 9)) for _ in range(size))
        l = random.randint(1, size)
        r = random.randint(l, size * 2)
        test_cases.append(f"{a}\n{l}\n{r}\n")
    
    # Test 8-10: Large cases (near 10^5)
    for size in [30000, 60000, 100000]:
        a = ''.join(str(random.randint(1, 9)) for _ in range(size))
        l = random.randint(1, size * 2 // 2)
        r = random.randint(size, size * 2)
        test_cases.append(f"{a}\n{l}\n{r}\n")
    
    # Test 11: Random medium case
    a = ''.join(str(random.randint(1, 9)) for _ in range(1000))
    test_cases.append(f"{a}\n100\n1500\n")
    
    # Generate and save
    print(f"Generating testcases for tica_23thtmta4...")
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
    zip_path = os.path.join(SCRIPT_DIR, "tica_23thtmta4_testcases.zip")
    
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for i in range(1, 12):
            input_file = os.path.join(SCRIPT_DIR, f"input{i}.in")
            output_file = os.path.join(SCRIPT_DIR, f"output{i}.out")
            
            if os.path.exists(input_file):
                zipf.write(input_file, f"input{i}.in")
            if os.path.exists(output_file):
                zipf.write(output_file, f"output{i}.out")
    
    print(f"[ZIP] Created ZIP: tica_23thtmta4_testcases.zip")

if __name__ == "__main__":
    if generate_testcases():
        create_zip()
