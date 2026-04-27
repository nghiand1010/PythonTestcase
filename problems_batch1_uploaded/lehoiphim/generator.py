# -*- coding: utf-8 -*-
"""
Testcase Generator for lehoiphim
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
    Sinh 11 testcases cho bai LEHOIPHIM - Activity selection
    Constraint: 1 <= n <= 2*10^5, 1 <= a < b <= 10^9
    Logic: Greedy - sort by end time, chon phim ket thuc som nhat
    """
    print("Generating testcases for lehoiphim...")
    
    test_inputs = []
    
    # Test 1: Vi du de bai
    test_inputs.append("3\n3 5\n4 9\n5 8\n")
    
    # Test 2: n=1
    test_inputs.append("1\n1 100\n")
    
    # Test 3: Khong overlap
    test_inputs.append("4\n1 2\n3 4\n5 6\n7 8\n")
    
    # Test 4: Tat ca overlap
    test_inputs.append("5\n1 10\n2 9\n3 8\n4 7\n5 6\n")
    
    # Test 5: Nested intervals
    test_inputs.append("3\n1 100\n10 20\n30 40\n")
    
    # Test 6: n=10
    test_inputs.append("10\n" + "\n".join(f"{i*10} {i*10+5}" for i in range(1, 11)) + "\n")
    
    # Test 7: Large time values (10^9)
    test_inputs.append("5\n1 1000000000\n500000000 999999999\n1 500000000\n1 2\n999999998 999999999\n")
    
    # Test 8: n=100
    test_inputs.append("100\n" + "\n".join(f"{i} {i+10}" for i in range(1, 101)) + "\n")
    
    # Test 9: n=10^3
    test_inputs.append("1000\n" + "\n".join(f"{i} {i+5}" for i in range(1, 1001)) + "\n")
    
    # Test 10: n=10^5
    test_inputs.append("100000\n" + "\n".join(f"{i} {i+3}" for i in range(1, 100001)) + "\n")
    
    # Test 11: Max n=2*10^5
    test_inputs.append("200000\n" + "\n".join(f"{i} {i+2}" for i in range(1, 200001)) + "\n")
    
    # Test 10: n=1000
    test_inputs.append("1000\n" + "\n".join(f"{i} {i + (i%10+1)}" for i in range(1, 1001)) + "\n")
    
    # Test 11: Edge case - very close times
    test_inputs.append("10\n" + "\n".join(f"{i} {i+1}" for i in range(1, 11)) + "\n")
    
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
    zip_name = "lehoiphim_testcases.zip"
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
    print(f"TESTCASE GENERATOR: lehoiphim")
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
