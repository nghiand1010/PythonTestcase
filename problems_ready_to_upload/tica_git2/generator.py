# -*- coding: utf-8 -*-
"""
Testcase Generator for tica_git2
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
    Generate testcases for tica_git2
    Constraints: 1 <= t <= 10, 1 <= n <= 50
    """
    test_cases = []
    
    # Test 1: Minimum case (n=1)
    test_cases.append("1\n1\n")
    
    # Test 2: Small case (n=2)
    test_cases.append("1\n2\n")
    
    # Test 3: Edge case (n=3, n=4)
    test_cases.append("2\n3\n4\n")
    
    # Test 4: Small values
    test_cases.append("3\n5\n6\n7\n")
    
    # Test 5: Medium values
    test_cases.append("4\n10\n15\n20\n25\n")
    
    # Test 6: Large values approaching max
    test_cases.append("5\n30\n35\n40\n45\n50\n")
    
    # Test 7: Maximum n only
    test_cases.append("1\n50\n")
    
    # Test 8: Mix of small and large
    test_cases.append("6\n1\n10\n20\n30\n40\n50\n")
    
    # Test 9: Maximum t with varied n
    test_cases.append("10\n5\n10\n15\n20\n25\n30\n35\n40\n45\n50\n")
    
    # Test 10: Maximum t with large n
    test_cases.append("10\n50\n49\n48\n47\n46\n45\n44\n43\n42\n41\n")
    
    # Test 11: Random mix
    test_cases.append("7\n12\n23\n34\n7\n18\n29\n50\n")
    
    # Generate and save
    print(f"Generating testcases for tica_git2...")
    for i, input_data in enumerate(test_cases, 1):
        try:
            output_data = run_editorial(input_data)
            save_testcase(i, input_data, output_data)
            print(f"  [OK] Test {i}")
        except Exception as e:
            print(f"  [FAIL] Test {i}: Error - {e}")
            return False
    
    print(f"[SUCCESS] Generated {len(test_cases)}/11 testcases")
    return True

def create_zip():
    """Tạo file ZIP chứa tất cả testcases"""
    zip_path = os.path.join(SCRIPT_DIR, "tica_git2_testcases.zip")
    
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for i in range(1, 12):
            input_file = os.path.join(SCRIPT_DIR, f"input{i}.in")
            output_file = os.path.join(SCRIPT_DIR, f"output{i}.out")
            
            if os.path.exists(input_file):
                zipf.write(input_file, f"input{i}.in")
            if os.path.exists(output_file):
                zipf.write(output_file, f"output{i}.out")
    
    print(f"[ZIP] Created: tica_git2_testcases.zip")

if __name__ == "__main__":
    if generate_testcases():
        create_zip()
