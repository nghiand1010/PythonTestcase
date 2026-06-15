#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AUTO CUSTOMIZE GENERATORS & CREATE TESTCASES
- Đọc editorial để hiểu logic
- Tạo testcase phù hợp với constraints
- Chạy generator và tạo ZIP
"""

import os
import sys
import json
import subprocess
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent.absolute()
PROBLEMS_DIR = SCRIPT_DIR / "problems"

def read_editorial(problem_id):
    """Đọc editorial.py để hiểu bài toán"""
    editorial_path = PROBLEMS_DIR / problem_id / "editorial.py"
    if editorial_path.exists():
        with open(editorial_path, 'r', encoding='utf-8') as f:
            return f.read()
    return None

def read_info(problem_id):
    """Đọc info.json để lấy constraints"""
    info_path = PROBLEMS_DIR / problem_id / "info.json"
    if info_path.exists():
        with open(info_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return None

def analyze_editorial_inputs(editorial_code):
    """Phân tích editorial để xác định input format"""
    lines = editorial_code.split('\n')
    input_pattern = []
    
    for line in lines:
        line = line.strip()
        if 'input()' in line and '=' in line:
            # Single input
            if 'int(input())' in line:
                input_pattern.append('int')
            elif 'float(input())' in line:
                input_pattern.append('float')
            elif 'map(int' in line or 'list(map' in line:
                input_pattern.append('list_int')
            else:
                input_pattern.append('str')
    
    return input_pattern

def generate_smart_testcases(problem_id, input_pattern):
    """Generate testcase thông minh dựa vào input pattern"""
    import random
    
    testcases = []
    
    # Analyze pattern
    if len(input_pattern) == 1:
        # Single value problems
        if input_pattern[0] == 'int':
            # Test 1-3: Small
            testcases.extend(["1\n", "2\n", "10\n"])
            # Test 4-7: Medium
            testcases.extend(["100\n", "1000\n", "10000\n", "50000\n"])
            # Test 8-10: Large
            testcases.extend(["100000\n", "500000\n", "1000000\n"])
            # Test 11: Stress
            testcases.append("1000000\n")
    
    elif len(input_pattern) == 2:
        # Two inputs (n, then array/list)
        if input_pattern[0] == 'int' and input_pattern[1] == 'list_int':
            # Array problems
            # Test 1: n=1
            testcases.append("1\n1\n")
            # Test 2-3: Small arrays
            testcases.append("5\n1 2 3 4 5\n")
            testcases.append("10\n" + " ".join(str(random.randint(1, 100)) for _ in range(10)) + "\n")
            # Test 4-7: Medium
            for n in [100, 1000, 5000, 10000]:
                testcases.append(f"{n}\n" + " ".join(str(random.randint(1, 1000000)) for _ in range(n)) + "\n")
            # Test 8-10: Large
            for n in [50000, 100000, 200000]:
                testcases.append(f"{n}\n" + " ".join(str(random.randint(1, 1000000)) for _ in range(n)) + "\n")
            # Test 11: Stress
            n = 500000
            testcases.append(f"{n}\n" + " ".join(str(random.randint(1, 1000000)) for _ in range(n)) + "\n")
    
    else:
        # Complex patterns - use generic approach
        testcases = [
            "1\n", "2\n", "10\n", "100\n", "1000\n",
            "10000\n", "50000\n", "100000\n", "500000\n", "1000000\n", "1000000\n"
        ]
    
    return testcases

def create_simple_testcases(problem_id):
    """Tạo testcase thông minh cho bài toán"""
    editorial = read_editorial(problem_id)
    if not editorial:
        print(f"  ❌ Không có editorial")
        return False
    
    generator_path = PROBLEMS_DIR / problem_id / "generator.py"
    
    # Analyze editorial to understand input pattern
    input_pattern = analyze_editorial_inputs(editorial)
    
    # Generate smart testcases
    testcases = generate_smart_testcases(problem_id, input_pattern)
    
    # Convert to code format
    testcases_code_lines = []
    for i, tc in enumerate(testcases, 1):
        tc_escaped = tc.replace('\n', '\\n').replace('"', '\\"')
        testcases_code_lines.append(f'    test_cases.append("{tc_escaped}")')
    
    testcases_code = '\n'.join(testcases_code_lines)
    
    # Read current generator
    with open(generator_path, 'r', encoding='utf-8') as f:
        generator_code = f.read()
    
    # Find and replace the testcase generation section
    start_marker = "def generate_testcases():"
    end_marker = "    # Generate and save"
    
    start_idx = generator_code.find(start_marker)
    end_idx = generator_code.find(end_marker)
    
    if start_idx != -1 and end_idx != -1:
        # Find the docstring end
        docstring_end = generator_code.find('"""', start_idx + len(start_marker) + 3)
        if docstring_end != -1:
            new_code = generator_code[:docstring_end + 3] + "\n    test_cases = []\n\n" + testcases_code + "\n\n" + generator_code[end_idx:]
            
            with open(generator_path, 'w', encoding='utf-8') as f:
                f.write(new_code)
            
            return True
    
    print(f"  ⚠️  Không thể customize generator")
    return False

def run_generator(problem_id):
    """Chạy generator.py để tạo testcase"""
    generator_path = PROBLEMS_DIR / problem_id / "generator.py"
    
    try:
        result = subprocess.run(
            [sys.executable, str(generator_path)],
            capture_output=True,
            text=True,
            timeout=60,
            cwd=str(PROBLEMS_DIR / problem_id)
        )
        
        if result.returncode == 0:
            print(f"  ✅ Generated testcases")
            return True
        else:
            print(f"  ❌ Error: {result.stderr[:200]}")
            return False
    except Exception as e:
        print(f"  ❌ Exception: {e}")
        return False

def main():
    print("="*60)
    print("🤖 AUTO CUSTOMIZE & GENERATE TESTCASES")
    print("="*60)
    
    # Get all problems
    problems = sorted([p.name for p in PROBLEMS_DIR.iterdir() if p.is_dir()])
    
    print(f"\n📋 Found {len(problems)} problems")
    
    success = []
    failed = []
    
    for i, problem_id in enumerate(problems, 1):
        print(f"\n[{i}/{len(problems)}] {problem_id}...")
        
        # Step 1: Customize generator (simple approach)
        if not create_simple_testcases(problem_id):
            failed.append(problem_id)
            continue
        
        # Step 2: Run generator
        if run_generator(problem_id):
            success.append(problem_id)
        else:
            failed.append(problem_id)
    
    print("\n" + "="*60)
    print("📊 KẾT QUẢ")
    print("="*60)
    print(f"✅ Thành công: {len(success)}/{len(problems)}")
    print(f"❌ Thất bại: {len(failed)}/{len(problems)}")
    
    if failed:
        print(f"\n❌ Các bài lỗi:")
        for p in failed:
            print(f"  - {p}")

if __name__ == "__main__":
    main()
