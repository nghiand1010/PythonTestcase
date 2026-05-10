# -*- coding: utf-8 -*-
"""
Testcase Generator for tica_py83
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
    Generate testcases for tica_py83: Buy ice cream get gifts
    Problem: Find minimum ice creams to buy to guarantee 1 sticker AND 1 toy
    Constraints: T ≤ 100, 1 ≤ n ≤ 10^9, 1 ≤ s,t ≤ n, s+t ≥ n
    Answer: max(n-s, n-t) + 1
    """
    test_cases = []
    
    # Test 1: All boxes have both (answer = 1)
    test_cases.append("1\n10 10 10\n")
    
    # Test 2: Minimum values (n=1)
    test_cases.append("1\n1 1 1\n")
    
    # Test 3: Example from problem + edge cases
    test_cases.append("3\n10 5 7\n10 10 10\n2 1 1\n")
    
    # Test 4: Small diverse cases
    test_cases.append("5\n100 50 60\n100 99 1\n100 1 99\n50 25 25\n7 3 5\n")
    
    # Test 5: Medium scale (10^6)
    test_cases.append("1\n1000000 600000 500000\n")
    
    # Test 6: Large scale (10^9) - extreme sticker heavy
    test_cases.append("1\n999999999 999999998 1\n")
    
    # Test 7: Large scale (10^9) - extreme toy heavy
    test_cases.append("1\n1000000000 1 999999999\n")
    
    # Test 8: Edge case s+t = n (no boxes with both items)
    test_cases.append("3\n100 60 40\n1000 700 300\n50 30 20\n")
    
    # Test 9: Multiple medium cases
    testcase_9 = ["20"]
    for _ in range(20):
        n = random.randint(100, 10000)
        s = random.randint(1, n)
        # Ensure s+t >= n
        t = random.randint(max(1, n - s), n)
        testcase_9.append(f"{n} {s} {t}")
    test_cases.append("\n".join(testcase_9) + "\n")
    
    # Test 10: Maximum constraint stress test
    test_cases.append("10\n1000000000 999999999 999999999\n1000000000 1 1000000000\n1000000000 1000000000 1\n1000000000 500000000 500000000\n1000000000 500000001 500000000\n1000000000 500000000 500000001\n999999999 1 999999999\n999999999 999999999 1\n1000000000 600000000 400000000\n1000000000 333333333 666666667\n")
    
    # Test 11: Random diverse cases
    num_tests = random.randint(10, 20)
    testcase_11 = [str(num_tests)]
    for _ in range(num_tests):
        n = random.randint(1, 10**9)
        s = random.randint(1, n)
        # Ensure s+t >= n
        t = random.randint(max(1, n - s), n)
        testcase_11.append(f"{n} {s} {t}")
    test_cases.append("\n".join(testcase_11) + "\n")
    
    # Generate and save
    print(f"Generating testcases for tica_py83...")
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
    zip_path = os.path.join(SCRIPT_DIR, "tica_py83_testcases.zip")
    
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for i in range(1, 12):
            input_file = os.path.join(SCRIPT_DIR, f"input{i}.in")
            output_file = os.path.join(SCRIPT_DIR, f"output{i}.out")
            
            if os.path.exists(input_file):
                zipf.write(input_file, f"input{i}.in")
            if os.path.exists(output_file):
                zipf.write(output_file, f"output{i}.out")
    
    print(f"[ZIP] Created ZIP: tica_py83_testcases.zip")

if __name__ == "__main__":
    if generate_testcases():
        create_zip()
