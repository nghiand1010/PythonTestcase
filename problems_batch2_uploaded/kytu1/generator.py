# -*- coding: utf-8 -*-
"""
Testcase Generator for kytu1
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
    Generate testcases for kytu1
    Input: x y (2 chuỗi trên 1 dòng), Q, sau đó Q dòng mỗi dòng u v
    Constraints: 1 ≤ L ≤ 10⁵, 1 ≤ Q ≤ 10⁵
    """
    test_cases = []
    
    def random_string(length):
        return ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(length))
    
    # Test 1-3: Edge cases
    test_cases.append("a a\n1\n1 1\n")  # L=1, Q=1
    test_cases.append("abc cba\n1\n1 2\n")  # ví dụ từ đề
    test_cases.append("icpc cici\n3\n1 2\n2 3\n2 4\n")  # ví dụ từ đề
    
    # Test 4-10: Phân bố thông minh
    # Test 4: L=10, Q=10
    x = random_string(10)
    y = random_string(10)
    queries = "\n".join(f"{random.randint(1, 2)} {random.randint(1, 10)}" for _ in range(10))
    test_cases.append(f"{x} {y}\n10\n{queries}\n")
    
    # Test 5: L=100, Q=50
    x = random_string(100)
    y = random_string(100)
    queries = "\n".join(f"{random.randint(1, 2)} {random.randint(1, 100)}" for _ in range(50))
    test_cases.append(f"{x} {y}\n50\n{queries}\n")
    
    # Test 6: L=1000, Q=1000
    x = random_string(1000)
    y = random_string(1000)
    queries = "\n".join(f"{random.randint(1, 2)} {random.randint(1, 1000)}" for _ in range(1000))
    test_cases.append(f"{x} {y}\n1000\n{queries}\n")
    
    # Test 7: L=10000, Q=10000
    x = random_string(10000)
    y = random_string(10000)
    queries = "\n".join(f"{random.randint(1, 2)} {random.randint(1, 10000)}" for _ in range(10000))
    test_cases.append(f"{x} {y}\n10000\n{queries}\n")
    
    # Test 8: L=100000 (max), Q=10000
    x = random_string(100000)
    y = random_string(100000)
    queries = "\n".join(f"{random.randint(1, 2)} {random.randint(1, 100000)}" for _ in range(10000))
    test_cases.append(f"{x} {y}\n10000\n{queries}\n")
    
    # Test 9: L=100000 (max), Q=100000 (max)
    x = random_string(100000)
    y = random_string(100000)
    queries = "\n".join(f"{random.randint(1, 2)} {random.randint(1, 100000)}" for _ in range(100000))
    test_cases.append(f"{x} {y}\n100000\n{queries}\n")
    
    # Test 10: chuỗi giống nhau
    L = 1000
    x = random_string(L)
    y = x  # giống nhau
    queries = "\n".join(f"{random.randint(1, 2)} {random.randint(1, L)}" for _ in range(100))
    test_cases.append(f"{x} {y}\n100\n{queries}\n")
    
    # Test 11: Random case
    L = random.randint(1000, 50000)
    Q = random.randint(1000, 50000)
    x = random_string(L)
    y = random_string(L)
    queries = "\n".join(f"{random.randint(1, 2)} {random.randint(1, L)}" for _ in range(Q))
    test_cases.append(f"{x} {y}\n{Q}\n{queries}\n")
    
    # Generate and save
    print(f"Generating testcases for kytu1...")
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
    zip_path = os.path.join(SCRIPT_DIR, "kytu1_testcases.zip")
    
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for i in range(1, 12):
            input_file = os.path.join(SCRIPT_DIR, f"input{i}.in")
            output_file = os.path.join(SCRIPT_DIR, f"output{i}.out")
            
            if os.path.exists(input_file):
                zipf.write(input_file, f"input{i}.in")
            if os.path.exists(output_file):
                zipf.write(output_file, f"output{i}.out")
    
    print(f"📦 Created ZIP: kytu1_testcases.zip")

if __name__ == "__main__":
    if generate_testcases():
        create_zip()
