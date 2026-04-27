# -*- coding: utf-8 -*-
"""
Testcase Generator for bdxau_namdinh
Follow template tu taotestcase.py
"""

import os
import sys
import io
import random
import zipfile

# Xac dinh thu muc cua generator.py (de luu file vao dung cho)
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

def run_editorial(input_data):
    """Chay editorial voi input va tra ve output"""
    input_io = io.StringIO(input_data)
    output_io = io.StringIO()
    
    stdin_backup = sys.stdin
    stdout_backup = sys.stdout
    
    try:
        sys.stdin = input_io
        sys.stdout = output_io
        
        # Tim editorial.py trong cung thu muc voi generator.py
        editorial_path = os.path.join(SCRIPT_DIR, 'editorial.py')
        
        with open(editorial_path, 'r', encoding='utf-8') as f:
            editorial_code = f.read()
        
        exec(editorial_code, {'__name__': '__main__'})
        
    except Exception as e:
        return f"ERROR: {e}"
    finally:
        sys.stdin = stdin_backup
        sys.stdout = stdout_backup
    
    return output_io.getvalue()

def save_testcase(test_num, input_data, output_data):
    """Luu 1 testcase vao thu muc cua generator.py"""
    input_path = os.path.join(SCRIPT_DIR, f"input{test_num}.in")
    output_path = os.path.join(SCRIPT_DIR, f"output{test_num}.out")
    
    with open(input_path, 'w', encoding='utf-8') as f:
        f.write(input_data)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(output_data)

def generate_testcases():
    """
    Sinh 11 testcases cho bai BDXAU_NAMDINH
    Constraint: |S| <= 100, 1 <= n, i <= 10^6
    Strategy: Phan bo n deu den 10^6
    """
    print("Generating testcases for bdxau_namdinh...")
    
    test_inputs = []
    
    # Test 1: Min - S="1", n=1, i=1
    test_inputs.append("1\n1 1\n")
    
    # Test 2: S="2", n=1, i=2
    test_inputs.append("2\n1 2\n")
    
    # Test 3: Vi du - S="123", n=1, i=5
    test_inputs.append("123\n1 5\n")
    
    # Test 4: n=10
    test_inputs.append("23\n10 5\n")
    
    # Test 5: n=100
    test_inputs.append("234\n100 10\n")
    
    # Test 6: n=1000
    test_inputs.append("345\n1000 50\n")
    
    # Test 7: n=10^4
    test_inputs.append("456\n10000 100\n")
    
    # Test 8: n=10^5
    test_inputs.append("567\n100000 500\n")
    
    # Test 9: n=10^6
    test_inputs.append("2\n1000000 1\n")
    
    # Test 10: S dai, n vua
    test_inputs.append("123456789\n1000 100\n")
    
    # Test 11: Random
    test_inputs.append("789\n5000 250\n")
    
    # Test 10: S dai (100 ky tu)
    test_inputs.append("123456789" * 11 + "1\n1 50\n")
    
    # Test 11: Multiple digits, moderate n
    test_inputs.append("321\n5 1000\n")
    
    # Generate and save
    success = 0
    for i, input_data in enumerate(test_inputs, 1):
        output_data = run_editorial(input_data)
        if not output_data.startswith("ERROR"):
            save_testcase(i, input_data, output_data)
            success += 1
        else:
            print(f"  WARNING: Test {i} failed: {output_data}")
    
    print(f"  SUCCESS: Generated {success}/11 testcases")
    return success

def create_zip():
    """Tao file ZIP chua tat ca testcases trong thu muc generator.py"""
    zip_name = "bdxau_namdinh_testcases.zip"
    zip_path = os.path.join(SCRIPT_DIR, zip_name)
    
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for i in range(1, 12):
            inp = os.path.join(SCRIPT_DIR, f"input{i}.in")
            out = os.path.join(SCRIPT_DIR, f"output{i}.out")
            if os.path.exists(inp):
                zipf.write(inp, f"input{i}.in")
            if os.path.exists(out):
                zipf.write(out, f"output{i}.out")
    
    print(f"  Created {zip_name}")

if __name__ == "__main__":
    print("="*60)
    print(f"TESTCASE GENERATOR: bdxau_namdinh")
    print("="*60)
    
    # Clean up old files trong thu muc generator.py
    for i in range(1, 12):
        for ext in ['.in', '.out']:
            fname = f"input{i}{ext}" if ext == '.in' else f"output{i}{ext}"
            fpath = os.path.join(SCRIPT_DIR, fname)
            if os.path.exists(fpath):
                os.remove(fpath)
    
    # Generate
    success = generate_testcases()
    
    if success >= 10:  # Chap nhan neu >= 10/11 thanh cong
        create_zip()
        print("\nSUCCESS!")
    else:
        print(f"\nWARNING: Only {success}/11 testcases generated")
