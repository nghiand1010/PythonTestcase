# -*- coding: utf-8 -*-
"""
Fix tất cả editorial.py - loại bỏ markdown code fence ```
"""

import os
import re

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

def clean_editorial_file(problem_id):
    """Loại bỏ markdown code fence từ editorial.py"""
    editorial_py = f"problems/{problem_id}/editorial.py"
    
    if not os.path.exists(editorial_py):
        return False
    
    with open(editorial_py, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Tách phần header và phần code
    lines = content.split('\n')
    
    # Tìm dòng "import sys" hoặc dòng đầu tiên sau header
    header_end = 0
    for i, line in enumerate(lines):
        if 'import sys' in line or 'from io import' in line:
            header_end = i
            break
    
    # Lấy header (từ đầu đến trước import sys)
    header_lines = lines[:header_end]
    
    # Lấy phần code (sau import sys)
    code_lines = lines[header_end:]
    
    # Join lại và loại bỏ các dấu ```
    code_content = '\n'.join(code_lines)
    
    # Loại bỏ các markdown code fence
    code_content = code_content.replace('```python', '')
    code_content = code_content.replace('```py', '')
    code_content = code_content.replace('```', '')
    
    # Loại bỏ các dòng trống thừa ở đầu
    code_lines = code_content.split('\n')
    while code_lines and not code_lines[0].strip():
        code_lines.pop(0)
    
    # Rebuild file
    new_content = '\n'.join(header_lines) + '\n' + '\n'.join(code_lines)
    
    # Ghi lại file
    with open(editorial_py, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    return True

def verify_editorial_runnable(problem_id):
    """Kiểm tra xem editorial.py có chạy được không"""
    editorial_py = f"problems/{problem_id}/editorial.py"
    
    if not os.path.exists(editorial_py):
        return False, "File not found"
    
    try:
        with open(editorial_py, 'r', encoding='utf-8') as f:
            code = f.read()
        
        # Thử compile
        compile(code, editorial_py, 'exec')
        return True, "OK"
    except SyntaxError as e:
        return False, f"SyntaxError: {e}"
    except Exception as e:
        return False, f"Error: {e}"

def main():
    print("="*60)
    print("FIX EDITORIAL.PY FILES - Loai bo markdown code fence")
    print("="*60)
    print()
    
    fixed_count = 0
    verified_count = 0
    errors = []
    
    for problem_id in PROBLEMS:
        print(f"[{problem_id}]", end=" ")
        
        # Clean file
        if clean_editorial_file(problem_id):
            print("cleaned", end=" ")
            fixed_count += 1
            
            # Verify
            ok, msg = verify_editorial_runnable(problem_id)
            if ok:
                print("-> OK")
                verified_count += 1
            else:
                print(f"-> ERROR: {msg}")
                errors.append((problem_id, msg))
        else:
            print("-> SKIP (no file)")
    
    print()
    print("="*60)
    print(f"TONG KET:")
    print(f"  Cleaned: {fixed_count}/{len(PROBLEMS)}")
    print(f"  Verified OK: {verified_count}/{len(PROBLEMS)}")
    
    if errors:
        print(f"\nLoi ({len(errors)} bai):")
        for pid, msg in errors:
            print(f"  - {pid}: {msg}")
    else:
        print("\nTat ca file deu OK!")
    
    print()
    print("Done!")

if __name__ == "__main__":
    main()
