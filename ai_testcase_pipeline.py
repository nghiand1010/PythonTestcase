#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AI Testcase Pipeline for 7 New Problems:
1. Cleans the editorial text into editorial.py.
2. Writes custom generator.py scripts with tailored inputs (strings vs numbers, small vs large cases).
3. Executes generator.py to produce inputs, outputs, and ZIP files.
"""

import os
import sys
import re
import shutil
import subprocess
from pathlib import Path

# Reconfigure stdout/stderr to use UTF-8 on Windows
if sys.platform.startswith('win'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except AttributeError:
        import io
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
        sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

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

# Reconfigure stdout/stderr to use UTF-8 on Windows
if sys.platform.startswith('win'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except AttributeError:
        import io
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
        sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

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
    test_cases = []
{testcases_code}
    
    # Generate and save
    print(f"Generating testcases for {problem_id}...")
    for i, input_data in enumerate(test_cases, 1):
        try:
            output_data = run_editorial(input_data)
            save_testcase(i, input_data, output_data)
            print(f"  [OK] Test {{i}}")
        except Exception as e:
            print(f"  [Error] Test {{i}}: {{e}}")
            return False
    
    print(f"SUCCESS: Generated {{len(test_cases)}}/11 testcases")
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
    
    print(f"Created ZIP: {problem_id}_testcases.zip")

if __name__ == "__main__":
    if generate_testcases():
        create_zip()
        # Delete local test files to keep directory clean (except ZIP)
        for i in range(1, 12):
            input_file = os.path.join(SCRIPT_DIR, f"input{{i}}.in")
            output_file = os.path.join(SCRIPT_DIR, f"output{{i}}.out")
            if os.path.exists(input_file):
                os.remove(input_file)
            if os.path.exists(output_file):
                os.remove(output_file)
        print("Local test files cleaned up.")
'''

GENERATOR_CODES = {
    'dsconlai': '''
    test_cases.append("20\\n4\\n7\\n")
    test_cases.append("30\\n5\\n0\\n")
    test_cases.append("50\\n7\\n3\\n")
    for _ in range(4):
        m = random.randint(100, 100000)
        k = random.randint(2, 500)
        d = random.randint(0, 9)
        test_cases.append(f"{m}\\n{k}\\n{d}\\n")
    for _ in range(3):
        m = random.randint(10**10, 10**12)
        k = random.randint(10**7, 10**9)
        d = random.randint(0, 9)
        test_cases.append(f"{m}\\n{k}\\n{d}\\n")
    test_cases.append("1000000000000\\n1000000000\\n7\\n")
''',
    'hk_smayman': '''
    test_cases.append("7\\n")
    test_cases.append("465\\n")
    test_cases.append("88448\\n")
    for _ in range(4):
        val = "".join(random.choice("0123456789") for _ in range(random.randint(3, 6)))
        val = val.lstrip('0') or "4"
        test_cases.append(f"{val}\\n")
    for _ in range(3):
        val = "".join(random.choice("0123456789") for _ in range(random.randint(10, 12)))
        val = val.lstrip('0') or "8"
        test_cases.append(f"{val}\\n")
    test_cases.append("1000000000000\\n")
''',
    'thetminh': '''
    test_cases.append("10 2\\n")
    test_cases.append("6 3\\n")
    test_cases.append("0 1\\n")
    test_cases.append("5 1\\n")
    test_cases.append("9 1\\n")
    test_cases.append("18 2\\n")
    test_cases.append("27 3\\n")
    test_cases.append("18 4\\n")
    test_cases.append("25 4\\n")
    test_cases.append("35 4\\n")
    test_cases.append("36 4\\n")
''',
    'xoakcs_lonnhat': '''
    test_cases.append("92744\\n3\\n")
    test_cases.append("28491\\n3\\n")
    test_cases.append("100000\\n2\\n")
    for _ in range(4):
        length = random.randint(10, 30)
        n_str = "".join(random.choice("0123456789") for _ in range(length))
        n_str = n_str.replace("0", "1")
        if n_str[0] == "0":
            n_str = "9" + n_str[1:]
        k = random.randint(1, length - 1)
        test_cases.append(f"{n_str}\\n{k}\\n")
    for _ in range(3):
        length = random.randint(80, 100)
        n_str = "".join(random.choice("0123456789") for _ in range(length))
        if n_str[0] == "0":
            n_str = "9" + n_str[1:]
        k = random.randint(1, length - 1)
        test_cases.append(f"{n_str}\\n{k}\\n")
    n_str = "9" * 100
    test_cases.append(f"{n_str}\\n50\\n")
''',
    'xoakcso_nhonhat': '''
    test_cases.append("28491\\n3\\n")
    test_cases.append("92744\\n3\\n")
    test_cases.append("910710\\n3\\n")
    for _ in range(4):
        length = random.randint(10, 30)
        n_str = "".join(random.choice("0123456789") for _ in range(length))
        if n_str[0] == "0":
            n_str = "1" + n_str[1:]
        k = random.randint(1, length - 1)
        test_cases.append(f"{n_str}\\n{k}\\n")
    for _ in range(3):
        length = random.randint(80, 100)
        n_str = "".join(random.choice("0123456789") for _ in range(length))
        if n_str[0] == "0":
            n_str = "1" + n_str[1:]
        k = random.randint(1, length - 1)
        test_cases.append(f"{n_str}\\n{k}\\n")
    n_str = "910710" * 16 + "5"
    test_cases.append(f"{n_str}\\n45\\n")
''',
    'xoacs_chia5': '''
    test_cases.append("345902\\n")
    test_cases.append("123\\n")
    test_cases.append("0\\n")
    for _ in range(4):
        length = random.randint(10, 100)
        n_str = "".join(random.choice("0123456789") for _ in range(length))
        if n_str[0] == "0":
            n_str = "3" + n_str[1:]
        test_cases.append(f"{n_str}\\n")
    for _ in range(3):
        length = random.randint(10000, 100000)
        n_str = "".join(random.choice("0123456789") for _ in range(length))
        if n_str[0] == "0":
            n_str = "7" + n_str[1:]
        test_cases.append(f"{n_str}\\n")
    n_str = "12346789" * 12500
    test_cases.append(f"{n_str}\\n")
''',
    'timkhobau': '''
    def make_valid(n, ch):
        import random
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        alphabet_without_ch = alphabet.replace(ch, "")
        s_chars = []
        for _ in range(n):
            if random.random() < 0.2:
                s_chars.append(ch)
            else:
                s_chars.append(random.choice(alphabet_without_ch))
        S = "".join(s_chars)
        K = S.replace(ch, "")
        return f"{S}{K}\\n{ch}\\n"

    test_cases.append(make_valid(8, "a"))
    test_cases.append(make_valid(15, "x"))
    test_cases.append("abcde\\nz\\n")
    for _ in range(4):
        test_cases.append(make_valid(random.randint(500, 1000), random.choice("abcdefg")))
    for _ in range(3):
        test_cases.append(make_valid(random.randint(300000, 450000), random.choice("xyz")))
    test_cases.append("a" * 500000 + "b" * 500000 + "\\nx\\n")
''',
    'chuvi_cn': '''
    test_cases.append("6\\n")
    test_cases.append("1\\n")
    test_cases.append("100\\n")
    for _ in range(4):
        test_cases.append(f"{random.randint(100, 1000000)}\\n")
    for _ in range(3):
        test_cases.append(f"{random.randint(10**10, 10**12)}\\n")
    test_cases.append("1000000000000\\n")
''',
    'tica_xephang_sontra': '''
    test_cases.append("10 4\\n")
    test_cases.append("10 1\\n")
    test_cases.append("10 10\\n")
    for _ in range(4):
        n = random.randint(100, 1000000)
        k = random.randint(1, n)
        test_cases.append(f"{n} {k}\\n")
    for _ in range(3):
        n = random.randint(10**10, 10**12)
        k = random.randint(1, n)
        test_cases.append(f"{n} {k}\\n")
    test_cases.append("1000000000000 1000000000000\\n")
''',
    'avab': '''
    test_cases.append("3\\n1 3\\n11 11\\n30 20\\n")
    test_cases.append("5\\n10 10\\n1 2\\n5 10\\n20 30\\n100 100\\n")
    test_cases.append("1\\n1000000000 1000000000\\n")
    for _ in range(4):
        lines = ["50"]
        for _ in range(50):
            a = random.randint(1, 10000)
            b = random.randint(1, 10000)
            lines.append(f"{a} {b}")
        test_cases.append("\\n".join(lines) + "\\n")
    for _ in range(3):
        lines = ["100"]
        for _ in range(100):
            a = random.randint(1, 10**9)
            b = random.randint(1, 10**9)
            lines.append(f"{a} {b}")
        test_cases.append("\\n".join(lines) + "\\n")
    lines = ["100"]
    for _ in range(100):
        lines.append(f"1000000000 1")
    test_cases.append("\\n".join(lines) + "\\n")
''',
    'tica_dxchan': '''
    test_cases.append("1\\n")
    test_cases.append("6\\n")
    test_cases.append("10\\n")
    for _ in range(4):
        test_cases.append(f"{random.randint(11, 1000000)}\\n")
    for _ in range(3):
        test_cases.append(f"{random.randint(10**10, 10**15)}\\n")
    test_cases.append("10000000000000000\\n")
'''
}

def clean_editorial_code(content):
    content = content.strip()
    blocks = re.findall(r'```(?:python)?\s*\n(.*?)\n```', content, re.DOTALL)
    if not blocks:
        blocks = re.findall(r'```(?:python)?(.*?)```', content, re.DOTALL)
    if blocks:
        for b in blocks:
            if len(b.strip()) > 10:
                return b.strip()
    return content

def main():
    print("=" * 60)
    print("🚀 STARTING AI TESTCASE GENERATION PIPELINE")
    print("=" * 60)
    
    problems = sorted([d.name for d in PROBLEMS_DIR.iterdir() if d.is_dir()])
    print(f"\n📋 Processing {len(problems)} problems...")
    
    success_count = 0
    failed_problems = []
    
    for i, problem_id in enumerate(problems, 1):
        print(f"\n[{i}/{len(problems)}] Problem: {problem_id}")
        problem_dir = PROBLEMS_DIR / problem_id
        editorial_txt = problem_dir / "editorial.txt"
        
        if not editorial_txt.exists():
            print("  ❌ Skip: editorial.txt not found")
            failed_problems.append((problem_id, "editorial.txt not found"))
            continue
            
        # Clean editorial code
        content = editorial_txt.read_text(encoding='utf-8')
        code = clean_editorial_code(content)
        
        # Write editorial.py
        editorial_py = problem_dir / "editorial.py"
        py_content = f'# -*- coding: utf-8 -*-\n"""\nEditorial for {problem_id}\n"""\n\nimport sys\nfrom io import StringIO\nimport random\n\n{code}\n'
        editorial_py.write_text(py_content, encoding='utf-8')
        print("  ✅ Created editorial.py")
        
        # Write generator.py
        generator_py = problem_dir / "generator.py"
        testcases_code = GENERATOR_CODES.get(problem_id, "")
        if not testcases_code:
            print(f"  ❌ Skip: No custom generator defined for {problem_id}")
            failed_problems.append((problem_id, "No custom generator defined"))
            continue
            
        generator_content = GENERATOR_TEMPLATE.format(
            problem_id=problem_id,
            testcases_code=testcases_code
        )
        generator_py.write_text(generator_content, encoding='utf-8')
        print("  ✅ Created generator.py")
        
        # Run generator.py
        try:
            print("  ⚙️ Running generator.py...", end="", flush=True)
            result = subprocess.run(
                [sys.executable, str(generator_py)],
                capture_output=True,
                text=True,
                timeout=60,
                cwd=str(problem_dir)
            )
            if result.returncode == 0:
                print(" ✅ OK (Generated ZIP)")
                success_count += 1
            else:
                err_msg = result.stderr[:300] if result.stderr else "Unknown error"
                print(f" ❌ Failed: {err_msg}")
                failed_problems.append((problem_id, f"Execution failed: {err_msg}"))
        except Exception as e:
            print(f" ❌ Exception: {e}")
            failed_problems.append((problem_id, f"Exception: {e}"))
            
    print("\n" + "=" * 60)
    print("🏁 PIPELINE COMPLETED")
    print("=" * 60)
    print(f"✅ Success: {success_count}/{len(problems)}")
    if failed_problems:
        print(f"❌ Failed: {len(failed_problems)}")
        for p, err in failed_problems:
            print(f"  - {p}: {err}")

if __name__ == "__main__":
    main()
