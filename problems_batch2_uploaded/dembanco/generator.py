# -*- coding: utf-8 -*-
"""
Testcase Generator for dembanco
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
    Generate testcases for dembanco
    Input: N, x1, y1, x2, y2 (5 dòng riêng biệt)
    Constraints: 1 ≤ N ≤ 10⁹, 1 ≤ x1, y1, x2, y2 ≤ N, x1 ≤ x2, y1 ≤ y2
    """
    test_cases = []
    
    # Test 1-3: Edge cases
    test_cases.append("1\n1\n1\n1\n1\n")  # bàn cờ 1x1, 1 ô duy nhất
    test_cases.append("5\n1\n1\n5\n5\n")  # ví dụ từ đề: toàn bộ bàn cờ 5x5
    test_cases.append("7\n2\n3\n6\n5\n")  # ví dụ từ đề: hình chữ nhật
    
    # Test 4-10: Phân bố thông minh
    test_cases.append("10\n1\n1\n10\n10\n")  # bàn 10x10
    test_cases.append("100\n50\n50\n100\n100\n")  # N=100, hình chữ nhật lớn
    test_cases.append(f"{10**6}\n1\n1\n{10**6}\n{10**6}\n")  # 10⁶, toàn bộ
    test_cases.append(f"{10**9}\n1\n1\n1000\n1000\n")  # N lớn, hình vuông nhỏ
    test_cases.append(f"{10**9}\n{10**9-100}\n{10**9-100}\n{10**9}\n{10**9}\n")  # góc dưới phải
    test_cases.append(f"{10**9}\n1\n1\n{10**9}\n1\n")  # cột dài
    test_cases.append(f"{10**9}\n1\n1\n1\n{10**9}\n")  # hàng dài
    
    # Test 11: Random case
    N = random.randint(10**6, 10**9)
    x1 = random.randint(1, N//2)
    y1 = random.randint(1, N//2)
    x2 = random.randint(x1, N)
    y2 = random.randint(y1, N)
    test_cases.append(f"{N}\n{x1}\n{y1}\n{x2}\n{y2}\n")
    
    # Generate and save
    print(f"Generating testcases for dembanco...")
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
    zip_path = os.path.join(SCRIPT_DIR, "dembanco_testcases.zip")
    
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for i in range(1, 12):
            input_file = os.path.join(SCRIPT_DIR, f"input{i}.in")
            output_file = os.path.join(SCRIPT_DIR, f"output{i}.out")
            
            if os.path.exists(input_file):
                zipf.write(input_file, f"input{i}.in")
            if os.path.exists(output_file):
                zipf.write(output_file, f"output{i}.out")
    
    print(f"📦 Created ZIP: dembanco_testcases.zip")

if __name__ == "__main__":
    if generate_testcases():
        create_zip()
