# -*- coding: utf-8 -*-
"""
Testcase Generator for nuoica
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
    Sinh 11 testcases cho bai NUOICA - Nuoi ca
    Constraint: 1 <= n <= 10^6, 1 <= ai <= 10^9
    Logic: Moi ngay an 3 goi, greedy mua voi gia min tu dau
    """
    print("Generating testcases for nuoica...")
    
    test_inputs = []
    
    # Test 1: n=1, gia co dinh
    test_inputs.append("1\n10\n")
    
    # Test 2: n=2, gia giam
    test_inputs.append("2\n20 10\n")
    
    # Test 3: n=2, gia tang
    test_inputs.append("2\n10 20\n")
    
    # Test 4: n=5, gia giam dan
    test_inputs.append("5\n50 40 30 20 10\n")
    
    # Test 5: n=5, gia tang dan
    test_inputs.append("5\n10 20 30 40 50\n")
    
    # Test 6: Tat ca gia bang nhau
    test_inputs.append("10\n" + " ".join(["15"]*10) + "\n")
    
    # Test 7: Gia co min o giua
    test_inputs.append("7\n100 90 80 10 80 90 100\n")
    
    # Test 8: n=100
    test_inputs.append("100\n" + " ".join(str((i*13)%100+1) for i in range(100)) + "\n")
    
    # Test 9: n=10^3
    test_inputs.append("1000\n" + " ".join(str((i*17)%1000+1) for i in range(1000)) + "\n")
    
    # Test 10: n=10^5
    test_inputs.append("100000\n" + " ".join(str((i*23)%10000+1) for i in range(100000)) + "\n")
    
    # Test 11: Max n=10^6 (se cham)
    test_inputs.append("1000000\n" + " ".join(str((i*29)%100000+1) for i in range(1000000)) + "\n")
    
    # Test 10: n=1000
    test_inputs.append("1000\n" + " ".join(str((i*17)%1000+1) for i in range(1000)) + "\n")
    
    # Test 11: n=10000 (large but fast)
    test_inputs.append("10000\n" + " ".join(str((i%100)+1) for i in range(10000)) + "\n")
    
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
    zip_name = "nuoica_testcases.zip"
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
    print(f"TESTCASE GENERATOR: nuoica")
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
