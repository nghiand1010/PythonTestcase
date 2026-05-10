# -*- coding: utf-8 -*-
"""
Testcase Generator for tica_py82
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
    Generate testcases for tica_py82: Count common divisors
    Problem: Find count of common divisors of all numbers in array
    Constraints: T ≤ 50, n ≤ 10^5, ai ≤ 10^12, sum(n) ≤ 10^5
    """
    test_cases = []
    
    # Test 1: Single number (all divisors count)
    test_cases.append("1\n1\n1\n")
    
    # Test 2: Two identical numbers (GCD = number itself)
    test_cases.append("1\n2\n12 12\n")
    
    # Test 3: Numbers with GCD = 1 (only 1 divisor)
    test_cases.append("1\n3\n13 17 19\n")
    
    # Test 4: Multiple testcases, small numbers
    test_cases.append("3\n2\n6 9\n3\n10 15 20\n4\n2 4 6 8\n")
    
    # Test 5: Large GCD with many divisors
    test_cases.append("1\n3\n360 720 1080\n")
    
    # Test 6: Powers of 2 (many divisors)
    test_cases.append("1\n5\n64 128 256 512 1024\n")
    
    # Test 7: Large numbers with small GCD
    test_cases.append("2\n3\n1000000000000 999999999999 999999999998\n2\n123456789012 987654321098\n")
    
    # Test 8: Mix of small and large numbers
    test_cases.append("1\n4\n100 1000 10000 100000\n")
    
    # Test 9: Maximum n with diverse numbers
    nums = [str(i * 6) for i in range(1, 101)]  # 100 numbers (multiples of 6)
    test_cases.append("1\n100\n" + " ".join(nums) + "\n")
    
    # Test 10: Multiple testcases at constraint boundary
    testcase_10 = ["10"]
    for _ in range(10):
        n = random.randint(50, 100)
        base = random.randint(2, 100)
        nums = [str(base * random.randint(1, 1000)) for _ in range(n)]
        testcase_10.append(str(n))
        testcase_10.append(" ".join(nums))
    test_cases.append("\n".join(testcase_10) + "\n")
    
    # Test 11: Random diverse testcases
    testcase_11 = ["5"]
    for _ in range(5):
        n = random.randint(1, 20)
        nums = [str(random.randint(1, 10**12)) for _ in range(n)]
        testcase_11.append(str(n))
        testcase_11.append(" ".join(nums))
    test_cases.append("\n".join(testcase_11) + "\n")
    
    # Generate and save
    print(f"Generating testcases for tica_py82...")
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
    zip_path = os.path.join(SCRIPT_DIR, "tica_py82_testcases.zip")
    
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for i in range(1, 12):
            input_file = os.path.join(SCRIPT_DIR, f"input{i}.in")
            output_file = os.path.join(SCRIPT_DIR, f"output{i}.out")
            
            if os.path.exists(input_file):
                zipf.write(input_file, f"input{i}.in")
            if os.path.exists(output_file):
                zipf.write(output_file, f"output{i}.out")
    
    print(f"[ZIP] Created ZIP: tica_py82_testcases.zip")

if __name__ == "__main__":
    if generate_testcases():
        create_zip()
