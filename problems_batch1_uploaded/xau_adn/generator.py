# -*- coding: utf-8 -*-
"""
Testcase Generator for xau_adn
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
    Sinh 11 testcases cho bai XAU_ADN
    Constraint: 1 <= n <= 10^6
    Strategy: Phan bo do dai string deu den 10^6
    """
    print("Generating testcases for xau_adn...")
    
    test_inputs = []
    
    # Test 1: n=1
    test_inputs.append("A\n")
    
    # Test 2: n=4
    test_inputs.append("ATGC\n")
    
    # Test 3: Consecutive dau
    test_inputs.append("AAATGC\n")
    
    # Test 4: n=10^2
    test_inputs.append("ATGC"*25 + "\n")
    
    # Test 5: n=10^3
    test_inputs.append("ATGC"*250 + "\n")
    
    # Test 6: n=10^4 - co consecutive dai
    test_inputs.append("A"*1000 + "TGCA"*2250 + "\n")
    
    # Test 7: n=10^5
    test_inputs.append("ATGC"*25000 + "\n")
    
    # Test 8: n=5*10^5
    test_inputs.append("A"*100000 + "TGCA"*100000 + "\n")
    
    # Test 9: n=10^6
    test_inputs.append("ATGC"*250000 + "\n")
    
    # Test 10: Tat ca giong nhau
    test_inputs.append("G"*10000 + "\n")
    
    # Test 11: Random pattern
    test_inputs.append("".join(["ATGC"[i%4] for i in range(5000)]) + "\n")
    
    # Test 10: Large n=10000
    test_inputs.append("A"*5000 + "TGCA"*1250 + "\n")
    
    # Test 11: Mix with longest in middle
    test_inputs.append("ATGC" + "A"*1000 + "TGCA"*100 + "\n")
    
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
    zip_name = "xau_adn_testcases.zip"
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
    print(f"TESTCASE GENERATOR: xau_adn")
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
