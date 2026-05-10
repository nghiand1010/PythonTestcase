# -*- coding: utf-8 -*-
"""
Testcase Generator for tica_py90
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
    Generate testcases for tica_py90 - Chia
    Input: q queries, each query has one integer n
    Constraints: 1 ≤ q ≤ 1000, 1 ≤ n ≤ 10^18
    Can divide by 2 (n/2), 3 (2n/3), 5 (4n/5) to reach 1
    """
    test_cases = []
    
    # Test 1: Example case from problem
    test_cases.append("7\n1\n10\n25\n30\n14\n27\n1000000000000000000\n")
    
    # Test 2: Small values with all valid operations
    test_cases.append("5\n1\n2\n3\n5\n6\n")
    
    # Test 3: Powers of 2, 3, 5
    test_cases.append("6\n8\n16\n9\n27\n25\n125\n")
    
    # Test 4: Numbers that cannot reach 1 (contain primes > 5)
    test_cases.append("5\n7\n11\n13\n77\n143\n")
    
    # Test 5: Mixed valid and invalid
    test_cases.append("8\n60\n100\n1024\n243\n3125\n49\n121\n1000\n")
    
    # Test 6: Large powers (10^6 range)
    queries = []
    queries.append(str(2**20))  # 1048576
    queries.append(str(3**12))  # 531441
    queries.append(str(5**8))   # 390625
    queries.append(str(2**15 * 3**7))
    test_cases.append(f"{len(queries)}\n" + "\n".join(queries) + "\n")
    
    # Test 7: Large powers (10^9 range)
    queries = []
    queries.append(str(2**30))  # ~10^9
    queries.append(str(3**19))  # ~10^9
    queries.append(str(5**13))  # ~10^9
    queries.append(str(2**20 * 3**10))
    test_cases.append(f"{len(queries)}\n" + "\n".join(queries) + "\n")
    
    # Test 8: Very large powers (10^15 range)
    queries = []
    queries.append(str(2**50))
    queries.append(str(3**32))
    queries.append(str(5**21))
    queries.append(str(2**30 * 3**20))
    test_cases.append(f"{len(queries)}\n" + "\n".join(queries) + "\n")
    
    # Test 9: Maximum range (10^18)
    queries = []
    queries.append(str(2**60))
    queries.append(str(3**38))
    queries.append(str(5**25))
    queries.append(str(2**40 * 3**25 * 5**10))
    test_cases.append(f"{len(queries)}\n" + "\n".join(queries) + "\n")
    
    # Test 10: Maximum q with mixed values
    q = 1000
    queries = []
    for _ in range(q):
        # Generate numbers with only factors 2, 3, 5
        p2 = random.randint(0, 60)
        p3 = random.randint(0, 38)
        p5 = random.randint(0, 25)
        n = (2**p2) * (3**p3) * (5**p5)
        if n <= 10**18:
            queries.append(str(n))
        else:
            queries.append(str(random.randint(1, 1000)))
    test_cases.append(f"{q}\n" + "\n".join(queries) + "\n")
    
    # Test 11: Random case (will be deleted after upload)
    q = random.randint(10, 50)
    queries = [str(random.randint(1, 10**6)) for _ in range(q)]
    test_cases.append(f"{q}\n" + "\n".join(queries) + "\n")
    
    # Generate and save
    print(f"Generating testcases for tica_py90...")
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
    zip_path = os.path.join(SCRIPT_DIR, "tica_py90_testcases.zip")
    
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for i in range(1, 12):
            input_file = os.path.join(SCRIPT_DIR, f"input{i}.in")
            output_file = os.path.join(SCRIPT_DIR, f"output{i}.out")
            
            if os.path.exists(input_file):
                zipf.write(input_file, f"input{i}.in")
            if os.path.exists(output_file):
                zipf.write(output_file, f"output{i}.out")
    
    print(f"[ZIP] Created ZIP: tica_py90_testcases.zip")

if __name__ == "__main__":
    if generate_testcases():
        create_zip()
