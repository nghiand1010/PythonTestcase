# -*- coding: utf-8 -*-
"""
Testcase Generator for exchange_money
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
    Sinh 11 testcases cho bai EXCHANGE_MONEY - Doi tien
    Constraint: T <= 50, 1 <= N <= 100000
    Logic: Greedy coin change voi 10 menh gia: 1000,500,200,100,50,20,10,5,2,1
    """
    print("Generating testcases for exchange_money...")
    
    test_inputs = []
    
    # Test 1: Vi du de bai
    test_inputs.append("2\n70\n121\n")
    
    # Test 2: N=1 (min)
    test_inputs.append("1\n1\n")
    
    # Test 3: N=1000 (1 to 1000 dong)
    test_inputs.append("1\n1000\n")
    
    # Test 4: Cac menh gia khac nhau
    test_inputs.append("5\n5\n10\n50\n100\n500\n")
    
    # Test 5: So le phuc tap
    test_inputs.append("3\n123\n456\n789\n")
    
    # Test 6: Max N=100000
    test_inputs.append("1\n100000\n")
    
    # Test 7: Nhieu test (T=50)
    test_inputs.append("50\n" + "\n".join(str(i*100) for i in range(1, 51)) + "\n")
    
    # Test 8: So yeu cau nhieu to nho
    test_inputs.append("5\n1\n2\n3\n4\n6\n")
    
    # Test 9: So gan menh gia
    test_inputs.append("5\n199\n299\n499\n999\n1999\n")
    
    # Test 10: Range trung binh
    test_inputs.append("10\n" + "\n".join(str(i*1000) for i in range(1, 11)) + "\n")
    
    # Test 11: Random values
    test_inputs.append("10\n" + "\n".join(str((i*137)%100000+1) for i in range(10)) + "\n")
    
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
    zip_name = "exchange_money_testcases.zip"
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
    print(f"TESTCASE GENERATOR: exchange_money")
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
