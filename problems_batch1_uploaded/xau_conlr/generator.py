# -*- coding: utf-8 -*-
"""
Testcase Generator for xau_conlr
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
    Sinh 11 testcases cho bai XAU_CONLR
    Constraint: |y| <= 10^6, N <= 100, 0 <= L <= R < len(y)
    Logic: Substring query y[L:R+1] (inclusive)
    """
    print("Generating testcases for xau_conlr...")
    
    test_inputs = []
    
    # Test 1: Vi du de bai
    test_inputs.append("0123456\n3\n2 5\n2 3\n0 6\n")
    
    # Test 2: Single query
    test_inputs.append("abcdef\n1\n0 5\n")
    
    # Test 3: Multiple queries
    test_inputs.append("hello world\n5\n0 4\n6 10\n0 0\n1 1\n4 6\n")
    
    # Test 4: String ngan
    test_inputs.append("abc\n3\n0 0\n1 1\n2 2\n")
    
    # Test 5: Full string
    test_inputs.append("test\n1\n0 3\n")
    
    # Test 6: Overlapping queries
    test_inputs.append("abcdefgh\n5\n0 3\n2 5\n4 7\n1 6\n0 7\n")
    
    # Test 7: N=100 queries, |s|=10^3
    test_inputs.append("a"*1000 + "\n100\n" + "\n".join(f"{i*10} {i*10+9}" for i in range(100)) + "\n")
    
    # Test 8: |s|=10^4
    test_inputs.append("x"*10000 + "\n10\n" + "\n".join(f"{i*1000} {i*1000+999}" for i in range(10)) + "\n")
    
    # Test 9: |s|=10^5
    test_inputs.append("y"*100000 + "\n20\n" + "\n".join(f"{i*5000} {i*5000+4999}" for i in range(20)) + "\n")
    
    # Test 10: |s|=5*10^5
    test_inputs.append("z"*500000 + "\n10\n" + "\n".join(f"{i*50000} {i*50000+49999}" for i in range(10)) + "\n")
    
    # Test 11: Max |s|=10^6
    test_inputs.append("abc"*333333 + "a" + "\n50\n" + "\n".join(f"{i*20000} {i*20000+19999}" for i in range(50)) + "\n")
    
    # Test 10: Random
    test_inputs.append("quickbrownfox\n7\n0 5\n6 10\n11 12\n0 2\n5 8\n9 12\n0 12\n")
    
    # Test 11: Edge cases
    test_inputs.append("test string\n5\n0 0\n10 10\n0 10\n4 4\n5 9\n")
    
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
    zip_name = "xau_conlr_testcases.zip"
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
    print(f"TESTCASE GENERATOR: xau_conlr")
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
