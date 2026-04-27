# -*- coding: utf-8 -*-
"""
Testcase Generator for dschinhphuong
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
    Generate testcases for dschinhphuong
    Input: n, rồi n số nguyên (trên 1 dòng)
    Constraints: 1 ≤ n ≤ 10⁵, 0 ≤ aᵢ ≤ 10⁹
    """
    test_cases = []
    
    # Test 1-3: Edge cases
    test_cases.append("1\n0\n")  # n=1, số 0 (số chính phương)
    test_cases.append("1\n1\n")  # n=1, số 1 (số chính phương)
    test_cases.append("5\n49 6 9 5 2\n")  # ví dụ từ đề
    
    # Test 4-10: Phân bố thông minh
    # Test 4: n=10, mix số chính phương và không
    test_cases.append("10\n1 4 9 16 25 36 49 64 81 100\n")  # toàn số chính phương
    
    # Test 5: n=100, không có số chính phương
    nums = [random.randint(2, 100) for _ in range(100)]
    nums = [x if int(x**0.5)**2 != x else x+1 for x in nums]  # loại bỏ số chính phương
    test_cases.append(f"100\n{' '.join(map(str, nums))}\n")
    
    # Test 6: n=1000
    nums = [random.randint(0, 10**6) for _ in range(1000)]
    test_cases.append(f"1000\n{' '.join(map(str, nums))}\n")
    
    # Test 7: n=10000
    nums = [random.randint(0, 10**9) for _ in range(10000)]
    test_cases.append(f"10000\n{' '.join(map(str, nums))}\n")
    
    # Test 8: n=50000
    nums = [random.randint(0, 10**9) for _ in range(50000)]
    test_cases.append(f"50000\n{' '.join(map(str, nums))}\n")
    
    # Test 9: n=100000, max n
    nums = [random.randint(0, 10**9) for _ in range(100000)]
    test_cases.append(f"100000\n{' '.join(map(str, nums))}\n")
    
    # Test 10: n lớn với nhiều số chính phương
    nums = []
    for _ in range(10000):
        if random.random() < 0.3:  # 30% là số chính phương
            k = random.randint(0, 31622)  # sqrt(10^9) ≈ 31622
            nums.append(k * k)
        else:
            nums.append(random.randint(0, 10**9))
    test_cases.append(f"10000\n{' '.join(map(str, nums))}\n")
    
    # Test 11: Random case
    n = random.randint(1000, 10000)
    nums = [random.randint(0, 10**9) for _ in range(n)]
    test_cases.append(f"{n}\n{' '.join(map(str, nums))}\n")
    
    # Generate and save
    print(f"Generating testcases for dschinhphuong...")
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
    zip_path = os.path.join(SCRIPT_DIR, "dschinhphuong_testcases.zip")
    
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for i in range(1, 12):
            input_file = os.path.join(SCRIPT_DIR, f"input{i}.in")
            output_file = os.path.join(SCRIPT_DIR, f"output{i}.out")
            
            if os.path.exists(input_file):
                zipf.write(input_file, f"input{i}.in")
            if os.path.exists(output_file):
                zipf.write(output_file, f"output{i}.out")
    
    print(f"📦 Created ZIP: dschinhphuong_testcases.zip")

if __name__ == "__main__":
    if generate_testcases():
        create_zip()
