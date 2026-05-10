# -*- coding: utf-8 -*-
"""
Testcase Generator for tica_git90
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
    Generate testcases for tica_git90
    Input: n, then n lines (name + 3 scores) - find best and worst student
    Constraints: 1 <= n <= 1000, names are strings, scores are ints
    """
    test_cases = []
    
    # Test 1: Simple case
    test_cases.append("3\nAlice 10 20 30\nBob 15 25 35\nCharlie 5 10 15\n")
    
    # Test 2: Same total scores
    test_cases.append("2\nAlex 10 10 10\nBen 5 15 10\n")
    
    # Test 3: Edge case
    test_cases.append("5\nA 100 100 100\nB 50 50 50\nC 75 75 75\nD 25 25 25\nE 90 90 90\n")
    
    # Test 4-10: Scaled cases
    names = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Henry', 'Ivy', 'Jack']
    for n in [10, 50, 100, 200, 500, 800, 1000]:
        students = []
        for i in range(n):
            name = f"Student{i}" if i >= len(names) else names[i % len(names)]
            s1 = random.randint(0, 100)
            s2 = random.randint(0, 100)
            s3 = random.randint(0, 100)
            students.append(f"{name} {s1} {s2} {s3}")
        test_cases.append(f"{n}\n" + "\n".join(students) + "\n")
    
    # Test 11: Random
    students = [f"S{i} {random.randint(0,100)} {random.randint(0,100)} {random.randint(0,100)}" for i in range(100)]
    test_cases.append(f"100\n" + "\n".join(students) + "\n")
    
    # Generate and save
    print(f"Generating testcases for tica_git90...")
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
    zip_path = os.path.join(SCRIPT_DIR, "tica_git90_testcases.zip")
    
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for i in range(1, 12):
            input_file = os.path.join(SCRIPT_DIR, f"input{i}.in")
            output_file = os.path.join(SCRIPT_DIR, f"output{i}.out")
            
            if os.path.exists(input_file):
                zipf.write(input_file, f"input{i}.in")
            if os.path.exists(output_file):
                zipf.write(output_file, f"output{i}.out")
    
    print(f"[ZIP] Created ZIP: tica_git90_testcases.zip")

if __name__ == "__main__":
    if generate_testcases():
        create_zip()
