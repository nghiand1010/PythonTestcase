# -*- coding: utf-8 -*-
"""
Testcase Generator for tica_py84
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
    Generate testcases for tica_py84: Sandwiches
    Problem: Maximize profit selling beef/chicken sandwiches (each needs 2 bread)
    Constraints: q ≤ 100, 1 ≤ b,p,f ≤ 100, 1 ≤ h,c ≤ 100
    Strategy: Make more expensive sandwich first (greedy)
    """
    test_cases = []
    
    # Test 1: Minimum values, beef more expensive
    test_cases.append("1\n2 1 1\n10 5\n")
    
    # Test 2: Not enough bread
    test_cases.append("1\n1 100 100\n100 100\n")
    
    # Test 3: Chicken more expensive (from example)
    test_cases.append("1\n15 2 3\n5 10\n")
    
    # Test 4: Various scenarios
    test_cases.append("5\n10 3 2\n20 15\n20 5 5\n10 10\n6 1 1\n50 50\n100 50 50\n5 10\n8 2 3\n15 15\n")
    
    # Test 5: Equal prices
    test_cases.append("3\n10 5 5\n20 20\n50 25 25\n10 10\n100 50 50\n15 15\n")
    
    # Test 6: Lots of bread, limited meat
    test_cases.append("1\n100 10 10\n50 40\n")
    
    # Test 7: Lots of meat, limited bread
    test_cases.append("1\n10 100 100\n100 99\n")
    
    # Test 8: One type of meat is 0 (edge case via small values)
    test_cases.append("3\n20 10 1\n100 1\n20 1 10\n1 100\n10 5 5\n1 100\n")
    
    # Test 9: Maximum constraint values
    test_cases.append("10\n100 100 100\n100 100\n100 100 100\n100 1\n100 100 100\n1 100\n100 50 50\n50 50\n100 1 99\n100 100\n100 99 1\n100 100\n100 100 1\n99 100\n100 1 100\n100 99\n50 25 25\n100 100\n60 30 30\n75 80\n")
    
    # Test 10: Multiple queries with random values
    testcase_10 = ["20"]
    for _ in range(20):
        b = random.randint(1, 100)
        p = random.randint(1, 100)
        f = random.randint(1, 100)
        h = random.randint(1, 100)
        c = random.randint(1, 100)
        testcase_10.append(f"{b} {p} {f}")
        testcase_10.append(f"{h} {c}")
    test_cases.append("\n".join(testcase_10) + "\n")
    
    # Test 11: Edge cases and random mix
    testcase_11 = ["15"]
    # Add some specific edge cases
    edges = [
        ("2 1 1", "100 99"),  # Close prices, min bread
        ("100 1 1", "1 100"),  # Lots of bread, chicken expensive
        ("100 1 1", "100 1"),  # Lots of bread, beef expensive
        ("4 2 2", "50 50"),   # Exact bread for both
        ("3 10 10", "1 1"),   # Odd bread (can only make 1 sandwich)
    ]
    for b_p_f, h_c in edges:
        testcase_11.append(b_p_f)
        testcase_11.append(h_c)
    # Fill rest with random
    for _ in range(10):
        b = random.randint(1, 100)
        p = random.randint(1, 100)
        f = random.randint(1, 100)
        h = random.randint(1, 100)
        c = random.randint(1, 100)
        testcase_11.append(f"{b} {p} {f}")
        testcase_11.append(f"{h} {c}")
    test_cases.append("\n".join(testcase_11) + "\n")
    
    # Generate and save
    print(f"Generating testcases for tica_py84...")
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
    zip_path = os.path.join(SCRIPT_DIR, "tica_py84_testcases.zip")
    
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for i in range(1, 12):
            input_file = os.path.join(SCRIPT_DIR, f"input{i}.in")
            output_file = os.path.join(SCRIPT_DIR, f"output{i}.out")
            
            if os.path.exists(input_file):
                zipf.write(input_file, f"input{i}.in")
            if os.path.exists(output_file):
                zipf.write(output_file, f"output{i}.out")
    
    print(f"[ZIP] Created ZIP: tica_py84_testcases.zip")

if __name__ == "__main__":
    if generate_testcases():
        create_zip()
