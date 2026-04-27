"""
RESTRUCTURE PROJECT - Chuyển editorial sang Python và tạo generator
Tất cả files (editorial.py, generator.py, input/output, ZIP) nằm CÙNG thư mục với problem.md
"""

import os
import shutil
import json
import zipfile

# Danh sách 38 bài đã có testcases ZIP (lấy từ daura_*.zip)
SUCCESSFUL_PROBLEMS = [
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

def create_generator_py_inline(problem_id):
    """Tạo generator.py inline"""
    template = f'''"""
Testcase Generator for {problem_id}
Follow template từ taotestcase.py
"""

import os
import sys
import io
import random
import zipfile
import shutil

def run_editorial(input_data):
    """Chạy editorial với input và trả về output"""
    input_io = io.StringIO(input_data)
    output_io = io.StringIO()
    
    stdin_backup = sys.stdin
    stdout_backup = sys.stdout
    
    try:
        sys.stdin = input_io
        sys.stdout = output_io
        
        # Execute editorial code
        with open('editorial.py', 'r', encoding='utf-8') as f:
            code = f.read()
            # Remove header comments
            lines = code.split('\\n')
            start_idx = 0
            for i, line in enumerate(lines):
                if 'import' in line or (line.strip() and not line.strip().startswith('#') and not line.strip().startswith('"""') and '"""' not in line):
                    start_idx = i
                    break
            code = '\\n'.join(lines[start_idx:])
            
        exec_globals = {{'sys': sys}}
        exec(code, exec_globals)
        
    except Exception as e:
        return f"ERROR: {{e}}"
    finally:
        sys.stdin = stdin_backup
        sys.stdout = stdout_backup
    
    return output_io.getvalue()

def save_testcase(test_num, input_data, output_data):
    """Lưu 1 testcase"""
    with open(f"input{{test_num}}.in", 'w', encoding='utf-8') as f:
        f.write(input_data)
    with open(f"output{{test_num}}.out", 'w', encoding='utf-8') as f:
        f.write(output_data)

def generate_testcases():
    """
    Sinh 11 testcases
    TODO: Customize strategies cho từng bài cụ thể
    """
    print("🔧 Generating testcases for {problem_id}...")
    
    # TODO: CUSTOMIZE INPUT GENERATION HERE
    # Đây là template - cần sửa cho phù hợp với từng bài
    
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
            print(f"  ⚠️  Test {{i}} failed: {{output_data}}")
    
    print(f"  ✅ Generated {{success}}/11 testcases")
    return success

def create_zip():
    """Tạo file ZIP chứa tất cả testcases"""
    zip_name = "{problem_id}_testcases.zip"
    
    with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for i in range(1, 12):
            inp = f"input{{i}}.in"
            out = f"output{{i}}.out"
            if os.path.exists(inp):
                zipf.write(inp)
            if os.path.exists(out):
                zipf.write(out)
    
    print(f"  📦 Created {{zip_name}}")

if __name__ == "__main__":
    print("="*60)
    print(f"TESTCASE GENERATOR: {problem_id}")
    print("="*60)
    
    # Clean up old files
    for i in range(1, 12):
        for ext in ['.in', '.out']:
            f = f"input{{i}}{{ext}}" if ext == '.in' else f"output{{i}}{{ext}}"
            if os.path.exists(f):
                os.remove(f)
    
    # Generate
    success = generate_testcases()
    
    if success >= 10:  # Chấp nhận nếu >= 10/11 thành công
        create_zip()
        print("\\n✅ SUCCESS!")
    else:
        print(f"\\n⚠️  Only {{success}}/11 testcases generated")
'''
    
    with open('generator.py', 'w', encoding='utf-8') as f:
        f.write(template)
    
    print(f"  ✅ Tạo generator.py (template)")

def copy_existing_testcases(problem_id):
    """Copy testcases từ daura_* folders nếu có"""
    source_dir = f"daura_{problem_id}"
    target_dir = f"problems/{problem_id}"
    
    if not os.path.exists(source_dir):
        return False
    
    # Copy input/output files
    copied = 0
    for i in range(1, 12):
        inp = f"{source_dir}/input{i}.in"
        out = f"{source_dir}/output{i}.out"
        
        if os.path.exists(inp):
            shutil.copy(inp, f"{target_dir}/input{i}.in")
            copied += 1
        if os.path.exists(out):
            shutil.copy(out, f"{target_dir}/output{i}.out")
    
    # Create ZIP
    if copied > 0:
        zip_path = f"{target_dir}/{problem_id}_testcases.zip"
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for i in range(1, 12):
                inp = f"{target_dir}/input{i}.in"
                out = f"{target_dir}/output{i}.out"
                if os.path.exists(inp):
                    zipf.write(inp, f"input{i}.in")
                if os.path.exists(out):
                    zipf.write(out, f"output{i}.out")
        
        print(f"  📦 Copy {copied} testcases + tạo ZIP")
        return True
    
    return False

def process_problem(problem_id):
    """Xử lý một bài toán"""
    print(f"\n{'='*60}")
    print(f"🎯 {problem_id}")
    print(f"{'='*60}")
    
    problem_dir = f"problems/{problem_id}"
    if not os.path.exists(problem_dir):
        print(f"  ⚠️  Thư mục không tồn tại")
        return False
    
    # Chuyển sang thư mục bài toán
    os.chdir(problem_dir)
    
    try:
        # 1. Tạo editorial.py
        editorial_txt = "editorial.txt"
        if not os.path.exists(editorial_txt):
            print(f"  ❌ Không có editorial.txt")
            os.chdir("../..")
            return False
        
        # Tạo editorial.py
        with open(editorial_txt, 'r', encoding='utf-8') as f:
            code = f.read()
        
        header = f'''"""
Editorial Solution for {problem_id}
Auto-generated from editorial.txt
"""

import sys
from io import StringIO

'''
        
        with open('editorial.py', 'w', encoding='utf-8') as f:
            f.write(header + code)
        
        print(f"  ✅ Tạo editorial.py")
        
        # 2. Tạo generator.py
        create_generator_py_inline(problem_id)
        
        # 3. Copy testcases đã có từ daura_* folders
        os.chdir("../..")  # về root
        success = copy_existing_testcases(problem_id)
        
        if success:
            print(f"  ✅ HOÀN THÀNH!")
            return True
        else:
            print(f"  ⚠️  Cần chạy generator.py để sinh testcases")
            return False
            
    except Exception as e:
        print(f"  ❌ Lỗi: {e}")
        os.chdir("../..")
        return False

def create_generator_py_inline(problem_id):
    """Tạo generator.py inline"""

def main():
    print("="*60)
    print("🚀 RESTRUCTURE PROJECT - Editorial → Python + Generator")
    print("="*60)
    print(f"\\n📋 Tổng số bài: {len(SUCCESSFUL_PROBLEMS)}")
    print("\\n🎯 Mục tiêu:")
    print("  1. editorial.txt → editorial.py")
    print("  2. Tạo generator.py (template)")
    print("  3. Copy testcases đã có")
    print("  4. Tạo ZIP trong problems/{problem_id}/")
    print("\\n" + "="*60 + "\\n")
    
    success_count = 0
    failed = []
    
    for problem_id in SUCCESSFUL_PROBLEMS:
        if process_problem(problem_id):
            success_count += 1
        else:
            failed.append(problem_id)
    
    print("\\n" + "="*60)
    print(f"✅ HOÀN THÀNH: {success_count}/{len(SUCCESSFUL_PROBLEMS)} bài")
    print("="*60)
    
    if failed:
        print(f"\\n⚠️  Cần kiểm tra lại: {len(failed)} bài")
        for p in failed:
            print(f"  - {p}")
    
    print("\\n📁 Cấu trúc mới:")
    print("  problems/")
    print("    {problem_id}/")
    print("      problem.md")
    print("      editorial.txt")
    print("      editorial.py          ← MỚI")
    print("      generator.py          ← MỚI")
    print("      input1.in             ← MỚI")
    print("      output1.out           ← MỚI")
    print("      ...")
    print("      {problem_id}_testcases.zip  ← MỚI")
    print("\\n🎉 Done!")

if __name__ == "__main__":
    main()
