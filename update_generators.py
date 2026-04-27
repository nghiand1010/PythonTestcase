# -*- coding: utf-8 -*-
"""
Update tat ca generator.py - exec truc tiep editorial.py
"""

import os

PROBLEMS = [
    '23kvatestthmatma', '24thtbbnqnhy4', 'bdsochia2', 'bdxau_namdinh',
    'bsodientu', 'cachnhiet', 'chong_gachcao', 'dayso_bimat',
    'doi_xung_hsg', 'exchange_money', 'file_name', 'khuyenmai_keo',
    'lehoiphim', 'muahang_qnam', 'nenso', 'nhomhocsinh',
    'nuocep_hoaqua', 'nuoica', 'rutthe2', 'sapxepcs',
    'sdbiet', 'so_lonnhat', 'sodacbiet5', 'sodep2',
    'somayman_qnam', 'soquediem', 'sothuvi', 'thttd_ds',
    'tica_dso2', 'toan_hoc', 'tongcs2022', 'vienda',
    'vitri_robot', 'vong_tay', 'write_remove', 'xau_adn',
    'xau_conlr', 'xcs_xau', 'xenke_vongtron'
]

NEW_GENERATOR_TEMPLATE = '''# -*- coding: utf-8 -*-
"""
Testcase Generator for {problem_id}
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
        
        exec(editorial_code, {{'__name__': '__main__'}})
        
    except Exception as e:
        return f"ERROR: {{e}}"
    finally:
        sys.stdin = stdin_backup
        sys.stdout = stdout_backup
    
    return output_io.getvalue()

def save_testcase(test_num, input_data, output_data):
    """Luu 1 testcase vao thu muc cua generator.py"""
    input_path = os.path.join(SCRIPT_DIR, f"input{{test_num}}.in")
    output_path = os.path.join(SCRIPT_DIR, f"output{{test_num}}.out")
    
    with open(input_path, 'w', encoding='utf-8') as f:
        f.write(input_data)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(output_data)

def generate_testcases():
    """
    Sinh 11 testcases
    TODO: Customize strategies cho tung bai cu the
    """
    print("Generating testcases for {problem_id}...")
    
    # TODO: CUSTOMIZE INPUT GENERATION HERE
    # Day la template - can sua cho phu hop voi tung bai
    
    test_inputs = []
    
    # Test 1: Min values
    test_inputs.append("1\\n")
    
    # Test 2-10: Various cases
    for i in range(2, 11):
        test_inputs.append(f"{{i}}\\n")
    
    # Test 11: Max values  
    test_inputs.append("1000\\n")
    
    # Generate and save
    success = 0
    for i, input_data in enumerate(test_inputs, 1):
        output_data = run_editorial(input_data)
        if not output_data.startswith("ERROR"):
            save_testcase(i, input_data, output_data)
            success += 1
        else:
            print(f"  WARNING: Test {{i}} failed: {{output_data}}")
    
    print(f"  SUCCESS: Generated {{success}}/11 testcases")
    return success

def create_zip():
    """Tao file ZIP chua tat ca testcases trong thu muc generator.py"""
    zip_name = "{problem_id}_testcases.zip"
    zip_path = os.path.join(SCRIPT_DIR, zip_name)
    
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for i in range(1, 12):
            inp = os.path.join(SCRIPT_DIR, f"input{{i}}.in")
            out = os.path.join(SCRIPT_DIR, f"output{{i}}.out")
            if os.path.exists(inp):
                zipf.write(inp, f"input{{i}}.in")
            if os.path.exists(out):
                zipf.write(out, f"output{{i}}.out")
    
    print(f"  Created {{zip_name}}")

if __name__ == "__main__":
    print("="*60)
    print(f"TESTCASE GENERATOR: {problem_id}")
    print("="*60)
    
    # Clean up old files trong thu muc generator.py
    for i in range(1, 12):
        for ext in ['.in', '.out']:
            fname = f"input{{i}}{{ext}}" if ext == '.in' else f"output{{i}}{{ext}}"
            fpath = os.path.join(SCRIPT_DIR, fname)
            if os.path.exists(fpath):
                os.remove(fpath)
    
    # Generate
    success = generate_testcases()
    
    if success >= 10:  # Chap nhan neu >= 10/11 thanh cong
        create_zip()
        print("\\nSUCCESS!")
    else:
        print(f"\\nWARNING: Only {{success}}/11 testcases generated")
'''

def update_generator(problem_id):
    """Cap nhat generator.py cho mot bai"""
    generator_path = f"problems/{problem_id}/generator.py"
    
    if not os.path.exists(generator_path):
        return False
    
    new_content = NEW_GENERATOR_TEMPLATE.format(problem_id=problem_id)
    
    with open(generator_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    return True

def main():
    print("="*60)
    print("UPDATE ALL GENERATOR.PY FILES")
    print("="*60)
    print()
    
    updated = 0
    for problem_id in PROBLEMS:
        if update_generator(problem_id):
            print(f"[{problem_id}] updated")
            updated += 1
        else:
            print(f"[{problem_id}] SKIP")
    
    print()
    print("="*60)
    print(f"Updated: {updated}/{len(PROBLEMS)}")
    print("="*60)

if __name__ == "__main__":
    main()
