# -*- coding: utf-8 -*-
"""
Testcase Generator for hsgioi
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
    Generate testcases for hsgioi
    Input: N C K (1 dòng), sau đó N dòng mỗi dòng a_i b_i
    Constraints: 1 ≤ N ≤ 10³, 1 ≤ C, K ≤ 10⁹, 0 ≤ a_i, b_i ≤ 10⁹
    """
    test_cases = []
    
    # Test 1-3: Edge cases
    test_cases.append("1 1 1\n0 1\n")  # N=1, đơn giản nhất
    test_cases.append("1 1 10\n10 1\n")  # học sinh đã đạt giải
    test_cases.append("3 5 6\n1 1\n2 1\n4 2\n")  # ví dụ từ đề
    
    # Test 4-10: Phân bố thông minh
    # Test 4: N nhỏ, C nhỏ
    test_cases.append("5 10 100\n10 5\n20 10\n50 20\n80 5\n90 10\n")
    
    # Test 5: N=100, C=1000
    lines = ["100 1000 1000\n"]
    for _ in range(100):
        a = random.randint(0, 500)
        b = random.randint(1, 50)
        lines.append(f"{a} {b}\n")
    test_cases.append("".join(lines))
    
    # Test 6: N=1000, C=10^6
    lines = [f"1000 {10**6} {10**6}\n"]
    for _ in range(1000):
        a = random.randint(0, 10**6)
        b = random.randint(1, 1000)
        lines.append(f"{a} {b}\n")
    test_cases.append("".join(lines))
    
    # Test 7: N lớn, K lớn, C vừa
    lines = [f"1000 {10**6} {10**9}\n"]
    for _ in range(1000):
        a = random.randint(0, 10**9)
        b = random.randint(1, 10**6)
        lines.append(f"{a} {b}\n")
    test_cases.append("".join(lines))
    
    # Test 8: N max, C max, K max
    lines = [f"1000 {10**9} {10**9}\n"]
    for _ in range(1000):
        a = random.randint(0, 10**9)
        b = random.randint(1, 10**9)
        lines.append(f"{a} {b}\n")
    test_cases.append("".join(lines))
    
    # Test 9: tất cả học sinh đã đạt giải
    lines = [f"500 1000 100\n"]
    for _ in range(500):
        a = random.randint(100, 10**9)
        b = random.randint(1, 1000)
        lines.append(f"{a} {b}\n")
    test_cases.append("".join(lines))
    
    # Test 10: b_i = 0 (không thể cải thiện)
    lines = [f"100 {10**6} 1000\n"]
    for _ in range(100):
        a = random.randint(0, 500)
        b = random.choice([0, random.randint(1, 100)])
        lines.append(f"{a} {b}\n")
    test_cases.append("".join(lines))
    
    # Test 11: Random case
    N = random.randint(100, 1000)
    C = random.randint(10**3, 10**9)
    K = random.randint(10**3, 10**9)
    lines = [f"{N} {C} {K}\n"]
    for _ in range(N):
        a = random.randint(0, K)
        b = random.randint(0, 10**6)
        lines.append(f"{a} {b}\n")
    test_cases.append("".join(lines))
    
    # Generate and save
    print(f"Generating testcases for hsgioi...")
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
    zip_path = os.path.join(SCRIPT_DIR, "hsgioi_testcases.zip")
    
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for i in range(1, 12):
            input_file = os.path.join(SCRIPT_DIR, f"input{i}.in")
            output_file = os.path.join(SCRIPT_DIR, f"output{i}.out")
            
            if os.path.exists(input_file):
                zipf.write(input_file, f"input{i}.in")
            if os.path.exists(output_file):
                zipf.write(output_file, f"output{i}.out")
    
    print(f"📦 Created ZIP: hsgioi_testcases.zip")

if __name__ == "__main__":
    if generate_testcases():
        create_zip()
