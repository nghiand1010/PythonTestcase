# -*- coding: utf-8 -*-
"""
Script để tạo generator.py cơ bản cho tất cả các bài
"""

from pathlib import Path

SCRIPT_DIR = Path(__file__).parent.absolute()
PROBLEMS_DIR = SCRIPT_DIR / "problems"

GENERATOR_TEMPLATE = '''# -*- coding: utf-8 -*-
"""
Testcase Generator for {problem_id}
"""

import os
import sys
from io import StringIO
import random
import zipfile

# Absolute path
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

def run_editorial(input_data):
    """Chạy editorial.py với input và trả về output"""
    editorial_path = os.path.join(SCRIPT_DIR, "editorial.py")
    
    with open(editorial_path, 'r', encoding='utf-8') as f:
        editorial_code = f.read()
    
    # Redirect stdin/stdout
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    
    try:
        sys.stdin = StringIO(input_data)
        sys.stdout = StringIO()
        
        # Execute editorial code
        exec(editorial_code, {{'__name__': '__main__', 'sys': sys, 'StringIO': StringIO}})
        
        output = sys.stdout.getvalue()
        return output
    finally:
        sys.stdin = old_stdin
        sys.stdout = old_stdout

def save_testcase(test_num, input_data, output_data):
    """Lưu testcase vào file"""
    input_file = os.path.join(SCRIPT_DIR, f"input{{test_num}}.in")
    output_file = os.path.join(SCRIPT_DIR, f"output{{test_num}}.out")
    
    with open(input_file, 'w', encoding='utf-8') as f:
        f.write(input_data)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(output_data)

def generate_testcases():
    """
    Generate testcases for {problem_id}
    TODO: Customize this function based on problem constraints
    """
    test_cases = []
    
    # Test 1: Minimum case
    test_cases.append("1\\n1\\n")
    
    # Test 2-3: Small cases
    test_cases.append("2\\n1 2\\n")
    test_cases.append("3\\n1 2 3\\n")
    
    # Test 4-10: Varied cases (TODO: customize based on constraints)
    for i in range(4, 11):
        n = 10 ** (i - 2)  # Scale from 100 to 10^8
        test_cases.append(f"{{n}}\\n" + " ".join(str(random.randint(1, n)) for _ in range(min(n, 1000))) + "\\n")
    
    # Test 11: Random case
    test_cases.append("5\\n1 2 3 4 5\\n")
    
    # Generate and save
    print(f"Generating testcases for {problem_id}...")
    for i, input_data in enumerate(test_cases, 1):
        try:
            output_data = run_editorial(input_data)
            save_testcase(i, input_data, output_data)
            print(f"  ✅ Test {{i}}: OK")
        except Exception as e:
            print(f"  ❌ Test {{i}}: Error - {{e}}")
            return False
    
    print(f"✅ SUCCESS: Generated {{len(test_cases)}}/11 testcases")
    return True

def create_zip():
    """Tạo file ZIP chứa tất cả testcases"""
    zip_path = os.path.join(SCRIPT_DIR, "{problem_id}_testcases.zip")
    
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for i in range(1, 12):
            input_file = os.path.join(SCRIPT_DIR, f"input{{i}}.in")
            output_file = os.path.join(SCRIPT_DIR, f"output{{i}}.out")
            
            if os.path.exists(input_file):
                zipf.write(input_file, f"input{{i}}.in")
            if os.path.exists(output_file):
                zipf.write(output_file, f"output{{i}}.out")
    
    print(f"📦 Created ZIP: {problem_id}_testcases.zip")

if __name__ == "__main__":
    if generate_testcases():
        create_zip()
'''

def create_generator(problem_id):
    """Tạo generator.py cho một bài"""
    problem_dir = PROBLEMS_DIR / problem_id
    generator_py = problem_dir / "generator.py"
    editorial_py = problem_dir / "editorial.py"
    
    if not editorial_py.exists():
        return False, "Không có editorial.py"
    
    if generator_py.exists():
        return False, "generator.py đã tồn tại"
    
    # Tạo generator.py từ template
    content = GENERATOR_TEMPLATE.format(problem_id=problem_id)
    generator_py.write_text(content, encoding='utf-8')
    
    return True, "OK"

def main():
    """Xử lý tất cả các bài"""
    problem_dirs = sorted([d for d in PROBLEMS_DIR.iterdir() if d.is_dir()])
    
    print(f"Tìm thấy {len(problem_dirs)} bài toán")
    print("=" * 60)
    
    success = 0
    skipped = 0
    
    for problem_dir in problem_dirs:
        problem_id = problem_dir.name
        ok, msg = create_generator(problem_id)
        
        if ok:
            print(f"✅ {problem_id}")
            success += 1
        else:
            skipped += 1
    
    print("=" * 60)
    print(f"Hoàn thành!")
    print(f"  ✅ Tạo mới: {success}")
    print(f"  ⏭️  Bỏ qua: {skipped}")

if __name__ == "__main__":
    main()
