# -*- coding: utf-8 -*-
"""
Testcase Generator for tica_py81
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
    Generate testcases for tica_py81 - Dragon Fighting Problem
    Constraints: T ≤ 100, n ≤ 10^5, x ≤ 10^9, d_i,h_i ≤ 10^9
    """
    test_cases = []
    
    # Test 1: Minimal case - one attack can one-shot
    input1 = "1\n1 1\n10 5\n"
    test_cases.append(input1)
    
    # Test 2: Impossible case - all attacks cause net regrowth
    input2 = "1\n3 10\n3 5\n2 10\n4 8\n"
    test_cases.append(input2)
    
    # Test 3: Small case with strategy - need multiple attacks (from example)
    input3 = "3\n3 10\n6 3\n8 2\n1 4\n4 10\n4 1\n3 2\n2 6\n2 15\n1 100\n2 15\n10 11\n14 100\n"
    test_cases.append(input3)
    
    # Test 4: Medium case (n=10, x=100)
    input4_lines = ["1", "10 100"]
    for i in range(10):
        d = random.randint(10, 50)
        h = random.randint(1, d-1) if random.random() > 0.3 else random.randint(d, d+20)
        input4_lines.append(f"{d} {h}")
    # Ensure at least one attack has positive net damage
    input4_lines[2] = "60 20"
    test_cases.append("\n".join(input4_lines) + "\n")
    
    # Test 5: Larger (n=100, x=1000)
    input5_lines = ["1", "100 1000"]
    for i in range(100):
        d = random.randint(50, 500)
        h = random.randint(1, 400)
        input5_lines.append(f"{d} {h}")
    # Ensure solvable
    input5_lines[2] = "800 100"
    test_cases.append("\n".join(input5_lines) + "\n")
    
    # Test 6: n=1000, x=10^5
    input6_lines = ["1", "1000 100000"]
    for i in range(1000):
        d = random.randint(1000, 50000)
        h = random.randint(500, 40000)
        input6_lines.append(f"{d} {h}")
    # Add one-shot possibility
    input6_lines[2] = "150000 1000"
    test_cases.append("\n".join(input6_lines) + "\n")
    
    # Test 7: n=10000, x=10^6
    input7_lines = ["1", "10000 1000000"]
    for i in range(10000):
        d = random.randint(10000, 500000)
        h = random.randint(5000, 400000)
        input7_lines.append(f"{d} {h}")
    # Ensure good net damage
    input7_lines[2] = "600000 50000"
    test_cases.append("\n".join(input7_lines) + "\n")
    
    # Test 8: n=50000, x=10^7
    input8_lines = ["1", "50000 10000000"]
    for i in range(50000):
        d = random.randint(100000, 5000000)
        h = random.randint(50000, 4000000)
        input8_lines.append(f"{d} {h}")
    input8_lines[2] = "6000000 500000"
    test_cases.append("\n".join(input8_lines) + "\n")
    
    # Test 9: n=100000, x=10^8
    input9_lines = ["1", "100000 100000000"]
    for i in range(100000):
        d = random.randint(1000000, 50000000)
        h = random.randint(500000, 40000000)
        input9_lines.append(f"{d} {h}")
    input9_lines[2] = "60000000 5000000"
    test_cases.append("\n".join(input9_lines) + "\n")
    
    # Test 10: Max constraints (n=10^5, x=10^9)
    input10_lines = ["1", "100000 1000000000"]
    for i in range(100000):
        d = random.randint(10000000, 500000000)
        h = random.randint(5000000, 400000000)
        input10_lines.append(f"{d} {h}")
    # Ensure solvable with good strategy
    input10_lines[2] = "600000000 50000000"
    test_cases.append("\n".join(input10_lines) + "\n")
    
    # Test 11: Random with multiple test cases (T=100)
    input11_lines = ["100"]
    for tc in range(100):
        n = random.randint(1, 1000)
        x = random.randint(1, 1000000)
        input11_lines.append(f"{n} {x}")
        for i in range(n):
            d = random.randint(1, 1000000)
            h = random.randint(1, 1000000)
            input11_lines.append(f"{d} {h}")
    test_cases.append("\n".join(input11_lines) + "\n")
    
    # Generate and save
    print(f"Generating testcases for tica_py81...")
    
    for test_num in range(1, 12):
        input_data = test_cases[test_num - 1]
        
        try:
            output_data = run_editorial(input_data)
            save_testcase(test_num, input_data, output_data)
            print(f"[OK] Test {test_num}: Generated successfully")
        except Exception as e:
            print(f"[FAIL] Test {test_num}: {str(e)}")
            return False
    
    return True

def create_zip():
    """Tạo file ZIP chứa tất cả testcases"""
    zip_path = os.path.join(SCRIPT_DIR, "tica_py81_testcases.zip")
    
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for i in range(1, 12):
            input_file = os.path.join(SCRIPT_DIR, f"input{i}.in")
            output_file = os.path.join(SCRIPT_DIR, f"output{i}.out")
            
            if os.path.exists(input_file):
                zipf.write(input_file, f"input{i}.in")
            if os.path.exists(output_file):
                zipf.write(output_file, f"output{i}.out")
    
    print(f"[ZIP] Created ZIP: tica_py81_testcases.zip")

if __name__ == "__main__":
    if generate_testcases():
        create_zip()
        print("[SUCCESS] Generated 11/11 testcases")
