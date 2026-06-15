#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SIMPLE TESTCASE GENERATOR
Tạo testcase đơn giản cho tất cả bài
"""

import os
import sys
import subprocess
import random
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
    """Run editorial.py with input and return output"""
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
    """Save testcase to files"""
    input_file = os.path.join(SCRIPT_DIR, f"input{{test_num}}.in")
    output_file = os.path.join(SCRIPT_DIR, f"output{{test_num}}.out")
    
    with open(input_file, 'w', encoding='utf-8') as f:
        f.write(input_data)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(output_data)

def generate_testcases():
    """Generate testcases for {problem_id}"""
    test_cases = []
    
{testcases_code}
    
    # Generate and save
    print(f"Generating testcases for {problem_id}...")
    for i, input_data in enumerate(test_cases, 1):
        try:
            output_data = run_editorial(input_data)
            save_testcase(i, input_data, output_data)
            print(f"  [OK] Test {{i}}: OK")
        except Exception as e:
            print(f"  [FAIL] Test {{i}}: Error - {{e}}")
            return False
    
    print(f"[SUCCESS] Generated {{len(test_cases)}}/{{len(test_cases)}} testcases")
    return True

def create_zip():
    """Create ZIP file containing all testcases"""
    zip_path = os.path.join(SCRIPT_DIR, "{problem_id}_testcases.zip")
    
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for i in range(1, 12):
            input_file = os.path.join(SCRIPT_DIR, f"input{{i}}.in")
            output_file = os.path.join(SCRIPT_DIR, f"output{{i}}.out")
            
            if os.path.exists(input_file):
                zipf.write(input_file, f"input{{i}}.in")
            if os.path.exists(output_file):
                zipf.write(output_file, f"output{{i}}.out")
    
    print(f"[ZIP] Created ZIP: {problem_id}_testcases.zip")

if __name__ == "__main__":
    if generate_testcases():
        create_zip()
'''

def analyze_editorial(editorial_path):
    """Phân tích editorial để xác định số inputs"""
    with open(editorial_path, 'r', encoding='utf-8') as f:
        code = f.read()
    
    # Count input() calls
    input_count = code.count('input()')
    
    # Check if has n and array
    has_n = 'n = int(input())' in code or 'N = int(input())' in code
    has_list = 'list(map' in code or 'split()' in code
    
    return {
        'input_count': input_count,
        'has_n': has_n,
        'has_list': has_list
    }

def generate_testcase_code(problem_id, analysis):
    """Generate testcase code based on analysis"""
    lines = []
    
    if analysis['has_n'] and analysis['has_list']:
        # Array problem: n, then array
        lines.append('    # Test 1: n=1')
        lines.append(r'    test_cases.append("1\n1\n")')
        lines.append('')
        lines.append('    # Test 2-3: Small')  
        lines.append(r'    test_cases.append("5\n1 2 3 4 5\n")')
        lines.append(r'    test_cases.append("10\n" + " ".join(str(random.randint(1, 100)) for _ in range(10)) + "\n")')
        lines.append('')
        lines.append('    # Test 4-7: Medium')
        lines.append('    for n in [100, 1000, 5000, 10000]:')
        lines.append(r'        test_cases.append(f"{n}\n" + " ".join(str(random.randint(1, 1000000)) for _ in range(n)) + "\n")')
        lines.append('')
        lines.append('    # Test 8-10: Large')
        lines.append('    for n in [50000, 100000, 200000]:')
        lines.append(r'        test_cases.append(f"{n}\n" + " ".join(str(random.randint(1, 1000000)) for _ in range(n)) + "\n")')
        lines.append('')
        lines.append('    # Test 11: Stress')
        lines.append('    n = 500000')
        lines.append(r'    test_cases.append(f"{n}\n" + " ".join(str(random.randint(1, 1000000)) for _ in range(n)) + "\n")')
    else:
        # Single number problems or simple cases
        lines.append('    # Test 1-3: Small')
        lines.append(r'    test_cases.extend(["1\n", "2\n", "10\n"])')
        lines.append('')
        lines.append('    # Test 4-7: Medium')
        lines.append(r'    test_cases.extend(["100\n", "1000\n", "10000\n", "50000\n"])')
        lines.append('')
        lines.append('    # Test 8-10: Large')
        lines.append(r'    test_cases.extend(["100000\n", "500000\n", "1000000\n"])')
        lines.append('')
        lines.append('    # Test 11: Stress')
        lines.append(r'    test_cases.append("1000000\n")')
    
    return '\n'.join(lines)

def create_generator(problem_id):
    """Tạo generator hoàn chỉnh cho một bài"""
    editorial_path = PROBLEMS_DIR / problem_id / "editorial.py"
    if not editorial_path.exists():
        return False
    
    # Analyze editorial
    analysis = analyze_editorial(editorial_path)
    
    # Generate testcase code
    testcases_code = generate_testcase_code(problem_id, analysis)
    
    # Create generator from template
    generator_code = GENERATOR_TEMPLATE.format(
        problem_id=problem_id,
        testcases_code=testcases_code
    )
    
    # Save generator
    generator_path = PROBLEMS_DIR / problem_id / "generator.py"
    with open(generator_path, 'w', encoding='utf-8') as f:
        f.write(generator_code)
    
    return True

def run_generator(problem_id):
    """Chạy generator để tạo testcase"""
    generator_path = PROBLEMS_DIR / problem_id / "generator.py"
    
    try:
        result = subprocess.run(
            [sys.executable, str(generator_path)],
            capture_output=True,
            text=True,
            timeout=120,
            cwd=str(PROBLEMS_DIR / problem_id)
        )
        
        if result.returncode == 0:
            return True, "OK"
        else:
            return False, result.stderr[:200]
    except subprocess.TimeoutExpired:
        return False, "Timeout"
    except Exception as e:
        return False, str(e)

def main():
    print("="*60)
    print("🤖 SIMPLE TESTCASE GENERATOR")
    print("="*60)
    
    problems = sorted([p.name for p in PROBLEMS_DIR.iterdir() if p.is_dir()])
    print(f"\n📋 Found {len(problems)} problems\\n")
    
    success = []
    failed = []
    
    for i, problem_id in enumerate(problems, 1):
        print(f"[{i}/{len(problems)}] {problem_id}...")
        
        # Create generator
        if not create_generator(problem_id):
            print(f"  ❌ No editorial")
            failed.append(problem_id)
            continue
        
        # Run generator
        ok, msg = run_generator(problem_id)
        if ok:
            print(f"  ✅ Generated testcases + ZIP")
            success.append(problem_id)
        else:
            print(f"  ❌ Error: {msg}")
            failed.append(problem_id)
    
    print("\\n" + "="*60)
    print("📊 KẾT QUẢ")
    print("="*60)
    print(f"✅ Thành công: {len(success)}/{len(problems)}")
    print(f"❌ Thất bại: {len(failed)}/{len(problems)}")
    
    if success:
        print(f"\\n✅ Các bài thành công:")
        for p in success:
            print(f"  - {p}")
    
    if failed:
        print(f"\\n❌ Các bài lỗi:")
        for p in failed:
            print(f"  - {p}")

if __name__ == "__main__":
    main()
