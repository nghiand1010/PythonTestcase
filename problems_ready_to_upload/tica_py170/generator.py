# -*- coding: utf-8 -*-
"""
Testcase Generator for tica_py170
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
    Generate testcases for tica_py170
    Input: t, then t times (n, array of times in HHMM, array of times in HHMM)
    """
    test_cases = []
    
    # Test 1: Edge - simple
    test_cases.append("1\n3\n900 1000 1100\n930 1030 1130\n")
    
    # Test 2: Edge - overlaps
    test_cases.append("1\n4\n800 900 1000 1100\n1000 1100 1200 1300\n")
    
    # Test 3: Edge - mixed
    test_cases.append("2\n2\n830 1400\n900 1500\n3\n1000 1200 1400\n1100 1300 1500\n")
    
    # Test 4-10: Scaled tests
    scales = [10, 50, 100, 500, 1000, 2000, 3000]
    for scale in scales:
        t = min(5, scale // 50 + 1)
        lines = [str(t)]
        for _ in range(t):
            n = random.randint(max(1, scale // 10), min(scale, 3000))
            lines.append(str(n))
            arr_in = []
            arr_out = []
            for _ in range(n):
                h_in = random.randint(0, 23)
                m_in = random.randint(0, 59)
                h_out = random.randint(h_in, 23)
                m_out = random.randint(0, 59) if h_out > h_in else random.randint(m_in, 59)
                arr_in.append(h_in * 100 + m_in)
                arr_out.append(h_out * 100 + m_out)
            lines.append(" ".join(str(x) for x in arr_in))
            lines.append(" ".join(str(x) for x in arr_out))
        test_cases.append("\n".join(lines) + "\n")
    
    # Test 11: Stress test
    t = 10
    lines = [str(t)]
    for _ in range(t):
        n = random.randint(1, 1000)
        lines.append(str(n))
        arr_in = [random.randint(0, 2359) for _ in range(n)]
        arr_out = [random.randint(0, 2359) for _ in range(n)]
        lines.append(" ".join(str(x) for x in arr_in))
        lines.append(" ".join(str(x) for x in arr_out))
    test_cases.append("\n".join(lines) + "\n")
    
    # Generate and save
    print(f"Generating testcases for tica_py170...")
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
    zip_path = os.path.join(SCRIPT_DIR, "tica_py170_testcases.zip")
    
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for i in range(1, 12):
            input_file = os.path.join(SCRIPT_DIR, f"input{i}.in")
            output_file = os.path.join(SCRIPT_DIR, f"output{i}.out")
            
            if os.path.exists(input_file):
                zipf.write(input_file, f"input{i}.in")
            if os.path.exists(output_file):
                zipf.write(output_file, f"output{i}.out")
    
    print(f"[ZIP] Created ZIP: tica_py170_testcases.zip")

if __name__ == "__main__":
    if generate_testcases():
        create_zip()
