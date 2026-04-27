# -*- coding: utf-8 -*-
"""
Testcase Generator for stickers
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
    Generate testcases for stickers
    Input: T (dòng 1), S (dòng 2) - dãy số (chuỗi các chữ số 0-9)
    Constraints: độ dài không quá 10⁵
    Output: số lượng dãy S tạo được từ T
    """
    test_cases = []
    
    def random_digits(length):
        return ''.join(str(random.randint(0, 9)) for _ in range(length))
    
    # Test 1-3: Edge cases
    test_cases.append("4444223\n445\n")  # ví dụ từ đề
    test_cases.append("668888\n899\n")  # ví dụ từ đề (có thể lật 6↔9)
    test_cases.append("0\n0\n")  # edge case: chỉ có chữ số 0
    
    # Test 4-10: Phân bố thông minh
    # Test 4: nhỏ, có 2 và 5 (có thể thay thế)
    test_cases.append("2255\n25\n")  # 2 có thể thay cho 5
    
    # Test 5: có 6 và 9 (có thể thay thế)
    test_cases.append("66999\n69\n")  # 6 có thể thay cho 9
    
    # Test 6: length = 100
    T = random_digits(100)
    S = random_digits(10)
    test_cases.append(f"{T}\n{S}\n")
    
    # Test 7: length = 1000
    T = random_digits(1000)
    S = random_digits(50)
    test_cases.append(f"{T}\n{S}\n")
    
    # Test 8: length = 10000
    T = random_digits(10000)
    S = random_digits(100)
    test_cases.append(f"{T}\n{S}\n")
    
    # Test 9: length = 100000 (max)
    T = random_digits(100000)
    S = random_digits(1000)
    test_cases.append(f"{T}\n{S}\n")
    
    # Test 10: T dài, S ngắn, không tạo được
    T = "111111"
    S = "222222"
    test_cases.append(f"{T}\n{S}\n")
    
    # Test 11: Random case
    T_len = random.randint(1000, 50000)
    S_len = random.randint(10, 1000)
    T = random_digits(T_len)
    S = random_digits(S_len)
    test_cases.append(f"{T}\n{S}\n")
    
    # Generate and save
    print(f"Generating testcases for stickers...")
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
    zip_path = os.path.join(SCRIPT_DIR, "stickers_testcases.zip")
    
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for i in range(1, 12):
            input_file = os.path.join(SCRIPT_DIR, f"input{i}.in")
            output_file = os.path.join(SCRIPT_DIR, f"output{i}.out")
            
            if os.path.exists(input_file):
                zipf.write(input_file, f"input{i}.in")
            if os.path.exists(output_file):
                zipf.write(output_file, f"output{i}.out")
    
    print(f"📦 Created ZIP: stickers_testcases.zip")

if __name__ == "__main__":
    if generate_testcases():
        create_zip()
