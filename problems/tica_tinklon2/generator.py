# -*- coding: utf-8 -*-
"""
Testcase Generator for tica_tinklon2
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
    Generate testcases for tica_tinklon2
    Binary search: find largest element < k in sorted array
    """
    test_cases = []
    
    # Test 1-3: Edge cases
    test_cases.append("3\n1 2 3\n1\n")          # k smaller than all (output: KHONG CO)
    test_cases.append("3\n1 2 3\n2\n")          # k=2, output 1
    test_cases.append("5\n10 20 30 40 50\n35\n") # k between elements
    
    # Test 4-10: Various sizes
    test_cases.append("10\n" + " ".join(str(i*10) for i in range(1, 11)) + "\n55\n")  # n=10
    test_cases.append("20\n" + " ".join(str(i*5) for i in range(1, 21)) + "\n88\n")   # n=20
    test_cases.append("50\n" + " ".join(str(i*2) for i in range(1, 51)) + "\n75\n")   # n=50
    test_cases.append("100\n" + " ".join(str(i) for i in range(1, 101)) + "\n77\n")   # n=100
    test_cases.append("500\n" + " ".join(str(i*10) for i in range(1, 501)) + "\n3333\n") # n=500
    test_cases.append("1000\n" + " ".join(str(i*100) for i in range(1, 1001)) + "\n55555\n") # n=1000
    test_cases.append("5000\n" + " ".join(str(i*1000) for i in range(1, 5001)) + "\n3333333\n") # n=5000
    
    # Test 11: Random
    n = random.randint(100, 1000)
    arr = sorted([random.randint(1, 10000) for _ in range(n)])
    k = random.randint(arr[0], arr[-1] + 100)
    test_cases.append(f"{n}\n" + " ".join(map(str, arr)) + f"\n{k}\n")
    
    # Generate and save
    print(f"Generating testcases for tica_tinklon2...")
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
    zip_path = os.path.join(SCRIPT_DIR, "tica_tinklon2_testcases.zip")
    
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for i in range(1, 12):
            input_file = os.path.join(SCRIPT_DIR, f"input{i}.in")
            output_file = os.path.join(SCRIPT_DIR, f"output{i}.out")
            
            if os.path.exists(input_file):
                zipf.write(input_file, f"input{i}.in")
            if os.path.exists(output_file):
                zipf.write(output_file, f"output{i}.out")
    
    print(f"[ZIP] Created ZIP: tica_tinklon2_testcases.zip")

if __name__ == "__main__":
    if generate_testcases():
        create_zip()
