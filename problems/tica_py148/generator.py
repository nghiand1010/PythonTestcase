# -*- coding: utf-8 -*-
"""
Testcase Generator for tica_py148
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
    Generate testcases for tica_py148
    Input: q queries, each with n, then array of n integers (permutation)
    Constraints: q≤200, N≤200
    """
    test_cases = []
    
    # Test 1: Minimum case - YES (clockwise)
    test_cases.append("1\n3\n1 2 3\n")
    
    # Test 2: YES (counter-clockwise)
    test_cases.append("1\n3\n1 3 2\n")
    
    # Test 3: NO case
    test_cases.append("1\n4\n1 3 2 4\n")
    
    # Test 4-10: Scaled cases
    for q_num in range(4, 11):
        q = min(200, 10 + q_num * 10)
        cases = []
        for _ in range(q):
            n = random.randint(1, 200)
            perm = list(range(1, n + 1))
            # 50% chance YES, 50% chance NO
            if random.random() < 0.5:
                # Create valid circular permutation
                start_pos = random.randint(0, n - 1)
                if random.random() < 0.5:
                    # Clockwise
                    result = [perm[(start_pos + i) % n] for i in range(n)]
                else:
                    # Counter-clockwise
                    result = [perm[(start_pos - i) % n] for i in range(n)]
            else:
                # Random invalid permutation
                random.shuffle(perm)
                result = perm
            cases.append(f"{n}\n" + " ".join(map(str, result)))
        test_cases.append(f"{q}\n" + "\n".join(cases) + "\n")
    
    # Test 11: Stress test - max N
    q = 200
    cases = []
    for _ in range(q):
        n = random.randint(100, 200)
        perm = list(range(1, n + 1))
        if random.random() < 0.5:
            start_pos = random.randint(0, n - 1)
            result = [perm[(start_pos + i) % n] for i in range(n)]
        else:
            random.shuffle(perm)
            result = perm
        cases.append(f"{n}\n" + " ".join(map(str, result)))
    test_cases.append(f"{q}\n" + "\n".join(cases) + "\n")
    
    # Generate and save
    print(f"Generating testcases for tica_py148...")
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
    zip_path = os.path.join(SCRIPT_DIR, "tica_py148_testcases.zip")
    
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for i in range(1, 12):
            input_file = os.path.join(SCRIPT_DIR, f"input{i}.in")
            output_file = os.path.join(SCRIPT_DIR, f"output{i}.out")
            
            if os.path.exists(input_file):
                zipf.write(input_file, f"input{i}.in")
            if os.path.exists(output_file):
                zipf.write(output_file, f"output{i}.out")
    
    print(f"[ZIP] Created ZIP: tica_py148_testcases.zip")

if __name__ == "__main__":
    if generate_testcases():
        create_zip()
