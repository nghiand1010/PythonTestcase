# -*- coding: utf-8 -*-
"""
Testcase Generator for 24thtbbnqnhy4
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
    Sinh 11 testcases cho bai 24THTBBNQNHY4
    Constraint: 1 <= |s| <= 10^5
    Strategy: Phan bo do dai string deu
    """
    print("Generating testcases for 24thtbbnqnhy4...")
    
    test_inputs = []
    
    # Test 1: Min (Alice thang)
    test_inputs.append("abc\n")
    
    # Test 2: Vi du (Alice thang)
    test_inputs.append("abacaba\n")
    
    # Test 3: Co 1 cap (Bob)
    test_inputs.append("aa\n")
    
    # Test 4: |s|=10^2
    test_inputs.append(("ab"*50) + "\n")
    
    # Test 5: |s|=10^3
    test_inputs.append(("abc"*333 + "a") + "\n")
    
    # Test 6: |s|=10^4 - nhieu cap
    test_inputs.append(("aabbcc"*1666 + "aa") + "\n")
    
    # Test 7: |s|=5*10^4
    test_inputs.append(("a"*50000) + "\n")
    
    # Test 8: |s|=10^5
    test_inputs.append(("abcdefgh"*12500) + "\n")
    
    # Test 9: Pattern xen ke
    test_inputs.append(("abba"*5000) + "\n")
    
    # Test 10: Toan giong nhau
    test_inputs.append(("z"*20000) + "\n")
    
    # Test 11: Random
    test_inputs.append(("xyz"*3000) + "\n")
    
    # Test 9: Khong co cap trong string dai
    test_inputs.append("abcdefghij" * 100 + "\n")  # 0 cap -> Alice
    
    # Test 10: String dai voi so cap le
    test_inputs.append("aa" + "b" * 1000 + "cc" + "\n")  # 1+500+1=502 cap -> Alice
    
    # Test 11: Max length (10^5) voi pattern
    test_inputs.append("ab" * 50000 + "\n")  # 0 cap -> Alice
    
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
    zip_name = "24thtbbnqnhy4_testcases.zip"
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
    print(f"TESTCASE GENERATOR: 24thtbbnqnhy4")
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
