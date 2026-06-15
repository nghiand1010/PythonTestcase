#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AUTO PIPELINE CHO 3 BÀI: bdsochia2, sodep2, stickers
Tự động: Tạo generator → Generate testcases → Upload → Submit
"""

import os
import sys
import subprocess
import time
import random
import zipfile
from pathlib import Path
from playwright.sync_api import sync_playwright

SCRIPT_DIR = Path(__file__).parent.absolute()
PROBLEMS_DIR = SCRIPT_DIR / "problems"
USERNAME = "thinhdt"
PASSWORD = "Th09051989@"

# 3 bài cần xử lý
PROBLEMS = ["bdsochia2", "sodep2", "stickers"]

# ==============================================================================
# GENERATORS CHO TỪNG BÀI
# ==============================================================================

def create_bdsochia2_generator():
    """bdsochia2: n = int(input()) - single integer"""
    generator_code = '''#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generator cho bdsochia2"""
from pathlib import Path
import subprocess
import zipfile
import random

SCRIPT_DIR = Path(__file__).parent.absolute()

def generate_testcases():
    """Sinh 11 testcases"""
    test_cases = []
    
    # Test 1-3: Small
    test_cases.append("1\\n")
    test_cases.append("2\\n")
    test_cases.append("10\\n")
    
    # Test 4-7: Medium
    test_cases.append("100\\n")
    test_cases.append("1000\\n")
    test_cases.append("10000\\n")
    test_cases.append("100000\\n")
    
    # Test 8-10: Large
    test_cases.append("1000000\\n")
    test_cases.append("10000000\\n")
    test_cases.append("100000000\\n")
    
    # Test 11: Stress
    test_cases.append("1000000000\\n")
    
    return test_cases

def run_editorial(input_data):
    """Chạy editorial để sinh output"""
    result = subprocess.run(
        ['python', SCRIPT_DIR / 'editorial.py'],
        input=input_data,
        capture_output=True,
        text=True,
        encoding='utf-8'
    )
    return result.stdout

def main():
    print("="*60)
    print("🔧 Generator: bdsochia2")
    print("="*60)
    
    test_cases = generate_testcases()
    print(f"📝 Đã tạo {len(test_cases)} testcases")
    
    # Create test files
    for i, input_data in enumerate(test_cases, 1):
        print(f"  Test {i}... ", end="", flush=True)
        
        # Save input
        input_file = SCRIPT_DIR / f"input{i}.txt"
        with open(input_file, 'w', encoding='utf-8') as f:
            f.write(input_data)
        
        # Generate output
        try:
            output_data = run_editorial(input_data)
            output_file = SCRIPT_DIR / f"output{i}.txt"
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(output_data)
            print("✅")
        except Exception as e:
            print(f"❌ {e}")
            return False
    
    # Create ZIP
    zip_path = SCRIPT_DIR / "bdsochia2_testcases.zip"
    print(f"\\n📦 Tạo ZIP: {zip_path.name}")
    
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for i in range(1, len(test_cases) + 1):
            zipf.write(SCRIPT_DIR / f"input{i}.txt", f"input{i}.txt")
            zipf.write(SCRIPT_DIR / f"output{i}.txt", f"output{i}.txt")
    
    print(f"✅ Đã tạo ZIP với {len(test_cases)} testcases")
    
    # Cleanup - delete test 11
    print(f"\\n🗑️  Xóa test 11...")
    (SCRIPT_DIR / "input11.txt").unlink(missing_ok=True)
    (SCRIPT_DIR / "output11.txt").unlink(missing_ok=True)
    print("✅ Đã xóa test 11")
    
    return True

if __name__ == "__main__":
    main()
'''
    return generator_code

def create_sodep2_generator():
    """sodep2: T test cases, each with a, b"""
    generator_code = '''#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generator cho sodep2"""
from pathlib import Path
import subprocess
import zipfile
import random

SCRIPT_DIR = Path(__file__).parent.absolute()

def generate_testcases():
    """Sinh 11 testcases"""
    test_cases = []
    
    # Test 1-3: Small
    test_cases.append("1\\n1 10\\n")
    test_cases.append("2\\n1 100\\n50 150\\n")
    test_cases.append("3\\n1 10\\n20 30\\n100 200\\n")
    
    # Test 4-7: Medium
    test_cases.append("5\\n" + "\\n".join(f"{random.randint(1, 1000)} {random.randint(1001, 10000)}" for _ in range(5)) + "\\n")
    test_cases.append("10\\n" + "\\n".join(f"{random.randint(1, 10000)} {random.randint(10001, 100000)}" for _ in range(10)) + "\\n")
    test_cases.append("20\\n" + "\\n".join(f"{random.randint(1, 100000)} {random.randint(100001, 1000000)}" for _ in range(20)) + "\\n")
    test_cases.append("50\\n" + "\\n".join(f"{random.randint(1, 1000000)} {random.randint(1000001, 10000000)}" for _ in range(50)) + "\\n")
    
    # Test 8-10: Large
    test_cases.append("100\\n" + "\\n".join(f"{random.randint(1, 10000000)} {random.randint(10000001, 100000000)}" for _ in range(100)) + "\\n")
    test_cases.append("100\\n" + "\\n".join(f"{random.randint(1, 100000000)} {random.randint(100000001, 1000000000)}" for _ in range(100)) + "\\n")
    test_cases.append("100\\n" + "\\n".join(f"{random.randint(1, 1000000000)} {random.randint(1, 1000000000)}" for _ in range(100)) + "\\n")
    
    # Test 11: Stress
    test_cases.append("100\\n" + "\\n".join(f"{random.randint(1, 10**18)} {random.randint(1, 10**18)}" for _ in range(100)) + "\\n")
    
    return test_cases

def run_editorial(input_data):
    """Chạy editorial để sinh output"""
    result = subprocess.run(
        ['python', SCRIPT_DIR / 'editorial.py'],
        input=input_data,
        capture_output=True,
        text=True,
        encoding='utf-8'
    )
    return result.stdout

def main():
    print("="*60)
    print("🔧 Generator: sodep2")
    print("="*60)
    
    test_cases = generate_testcases()
    print(f"📝 Đã tạo {len(test_cases)} testcases")
    
    # Create test files
    for i, input_data in enumerate(test_cases, 1):
        print(f"  Test {i}... ", end="", flush=True)
        
        # Save input
        input_file = SCRIPT_DIR / f"input{i}.txt"
        with open(input_file, 'w', encoding='utf-8') as f:
            f.write(input_data)
        
        # Generate output
        try:
            output_data = run_editorial(input_data)
            output_file = SCRIPT_DIR / f"output{i}.txt"
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(output_data)
            print("✅")
        except Exception as e:
            print(f"❌ {e}")
            return False
    
    # Create ZIP
    zip_path = SCRIPT_DIR / "sodep2_testcases.zip"
    print(f"\\n📦 Tạo ZIP: {zip_path.name}")
    
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for i in range(1, len(test_cases) + 1):
            zipf.write(SCRIPT_DIR / f"input{i}.txt", f"input{i}.txt")
            zipf.write(SCRIPT_DIR / f"output{i}.txt", f"output{i}.txt")
    
    print(f"✅ Đã tạo ZIP với {len(test_cases)} testcases")
    
    # Cleanup - delete test 11
    print(f"\\n🗑️  Xóa test 11...")
    (SCRIPT_DIR / "input11.txt").unlink(missing_ok=True)
    (SCRIPT_DIR / "output11.txt").unlink(missing_ok=True)
    print("✅ Đã xóa test 11")
    
    return True

if __name__ == "__main__":
    main()
'''
    return generator_code

def create_stickers_generator():
    """stickers: 2 strings T and S"""
    generator_code = '''#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generator cho stickers"""
from pathlib import Path
import subprocess
import zipfile
import random

SCRIPT_DIR = Path(__file__).parent.absolute()

def random_digit_string(length):
    """Tạo string gồm các chữ số 0-9"""
    return ''.join(random.choice('0123456789') for _ in range(length))

def generate_testcases():
    """Sinh 11 testcases"""
    test_cases = []
    
    # Test 1-3: Small
    test_cases.append("12345\\n123\\n")
    test_cases.append("2525252525\\n25\\n")
    test_cases.append("6969696969\\n69\\n")
    
    # Test 4-7: Medium
    test_cases.append(f"{random_digit_string(100)}\\n{random_digit_string(10)}\\n")
    test_cases.append(f"{random_digit_string(1000)}\\n{random_digit_string(50)}\\n")
    test_cases.append(f"{random_digit_string(10000)}\\n{random_digit_string(100)}\\n")
    test_cases.append(f"{random_digit_string(50000)}\\n{random_digit_string(500)}\\n")
    
    # Test 8-10: Large
    test_cases.append(f"{random_digit_string(100000)}\\n{random_digit_string(1000)}\\n")
    test_cases.append(f"{random_digit_string(100000)}\\n{random_digit_string(5000)}\\n")
    test_cases.append(f"{random_digit_string(100000)}\\n{random_digit_string(10000)}\\n")
    
    # Test 11: Stress
    test_cases.append(f"{random_digit_string(100000)}\\n{random_digit_string(50000)}\\n")
    
    return test_cases

def run_editorial(input_data):
    """Chạy editorial để sinh output"""
    result = subprocess.run(
        ['python', SCRIPT_DIR / 'editorial.py'],
        input=input_data,
        capture_output=True,
        text=True,
        encoding='utf-8'
    )
    return result.stdout

def main():
    print("="*60)
    print("🔧 Generator: stickers")
    print("="*60)
    
    test_cases = generate_testcases()
    print(f"📝 Đã tạo {len(test_cases)} testcases")
    
    # Create test files
    for i, input_data in enumerate(test_cases, 1):
        print(f"  Test {i}... ", end="", flush=True)
        
        # Save input
        input_file = SCRIPT_DIR / f"input{i}.txt"
        with open(input_file, 'w', encoding='utf-8') as f:
            f.write(input_data)
        
        # Generate output
        try:
            output_data = run_editorial(input_data)
            output_file = SCRIPT_DIR / f"output{i}.txt"
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(output_data)
            print("✅")
        except Exception as e:
            print(f"❌ {e}")
            return False
    
    # Create ZIP
    zip_path = SCRIPT_DIR / "stickers_testcases.zip"
    print(f"\\n📦 Tạo ZIP: {zip_path.name}")
    
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for i in range(1, len(test_cases) + 1):
            zipf.write(SCRIPT_DIR / f"input{i}.txt", f"input{i}.txt")
            zipf.write(SCRIPT_DIR / f"output{i}.txt", f"output{i}.txt")
    
    print(f"✅ Đã tạo ZIP với {len(test_cases)} testcases")
    
    # Cleanup - delete test 11
    print(f"\\n🗑️  Xóa test 11...")
    (SCRIPT_DIR / "input11.txt").unlink(missing_ok=True)
    (SCRIPT_DIR / "output11.txt").unlink(missing_ok=True)
    print("✅ Đã xóa test 11")
    
    return True

if __name__ == "__main__":
    main()
'''
    return generator_code

# ==============================================================================
# MAIN PIPELINE
# ==============================================================================

def main():
    print("=" * 70)
    print("🚀 AUTO PIPELINE CHO 3 BÀI")
    print("=" * 70)
    print(f"\\n📋 Danh sách: {', '.join(PROBLEMS)}\\n")
    
    # Step 1: Create generators
    print("=" * 70)
    print("📝 BƯỚC 1: TẠO GENERATORS")
    print("=" * 70)
    
    generators = {
        'bdsochia2': create_bdsochia2_generator(),
        'sodep2': create_sodep2_generator(),
        'stickers': create_stickers_generator()
    }
    
    for problem_id in PROBLEMS:
        print(f"\\n✅ {problem_id}")
        generator_path = PROBLEMS_DIR / problem_id / "generator.py"
        with open(generator_path, 'w', encoding='utf-8') as f:
            f.write(generators[problem_id])
    
    # Step 2: Run generators
    print("\\n" + "=" * 70)
    print("🔧 BƯỚC 2: CHẠY GENERATORS")
    print("=" * 70)
    
    for problem_id in PROBLEMS:
        print(f"\\n🔧 {problem_id}...")
        generator_path = PROBLEMS_DIR / problem_id / "generator.py"
        result = subprocess.run(['python', generator_path], cwd=PROBLEMS_DIR / problem_id)
        if result.returncode != 0:
            print(f"❌ Lỗi khi chạy generator cho {problem_id}")
            return
    
    print("\\n" + "=" * 70)
    print("✅ HOÀN THÀNH: Đã tạo testcases cho 3 bài")
    print("=" * 70)
    print("\\nTiếp theo:")
    print("1. Kiểm tra các file ZIP trong thư mục problems/*/")
    print("2. Chạy upload: py auto_upload_3_bai.py")
    print("3. Chạy submit: py auto_submit_3_bai.py")

if __name__ == "__main__":
    main()
