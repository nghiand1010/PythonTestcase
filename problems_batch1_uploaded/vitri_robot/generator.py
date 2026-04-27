# -*- coding: utf-8 -*-
"""
Testcase Generator for vitri_robot
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
    Sinh 11 testcases cho bai VITRI_ROBOT
    Constraint: 1 <= a,b,k <= 10^9
    Logic: Vi tri sau k buoc = (k//2)*(a-b) + (k%2)*a
    """
    print("Generating testcases for vitri_robot...")
    
    test_inputs = []
    
    # Test 1: Vi du de bai
    test_inputs.append("5 2 3\n")
    
    # Test 2: k=1 (chi di a)
    test_inputs.append("10 5 1\n")
    
    # Test 3: k=2 (di a roi lui b)
    test_inputs.append("10 5 2\n")
    
    # Test 4: k chan lon
    test_inputs.append("100 50 1000\n")
    
    # Test 5: k le lon
    test_inputs.append("100 50 1001\n")
    
    # Test 6: a=b
    test_inputs.append("10 10 100\n")
    
    # Test 7: a<b (lui nhieu hon)
    test_inputs.append("5 10 10\n")
    
    # Test 8: k=10^6
    test_inputs.append("100 50 1000000\n")
    
    # Test 9: k=10^8
    test_inputs.append("1000 500 100000000\n")
    
    # Test 10: Max a,b,k=10^9
    test_inputs.append("1000000000 1 1000000000\n")
    
    # Test 11: Random
    test_inputs.append("123456789 987654321 555555555\n")
    
    # Test 10: Random
    test_inputs.append("12345 6789 98765\n")
    
    # Test 11: Edge
    test_inputs.append("1 1 1\n")
    
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
    zip_name = "vitri_robot_testcases.zip"
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
    print(f"TESTCASE GENERATOR: vitri_robot")
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
