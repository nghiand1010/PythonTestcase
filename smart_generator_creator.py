#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SMART GENERATOR CREATOR
Phân tích editorial chi tiết và tạo generator đúng format
"""

import os
import re
import random
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent.absolute()
PROBLEMS_DIR = SCRIPT_DIR / "problems"

def analyze_editorial_deeply(editorial_code):
    """Phân tích editorial chi tiết để xác định input format"""
    lines = [l.strip() for l in editorial_code.split('\n') if l.strip() and not l.strip().startswith('#')]
    
    inputs = []
    for i, line in enumerate(lines):
        if 'input()' not in line or '=' not in line:
            continue
        
        # Single int
        if re.search(r'(\w+)\s*=\s*int\(input\(\)\)', line):
            match = re.search(r'(\w+)\s*=\s*int\(input\(\)\)', line)
            inputs.append(('int', match.group(1)))
        
        # Three ints from split (n, x, y = map(int, input().split()))
        elif re.search(r'(\w+),\s*(\w+),\s*(\w+)\s*=\s*map\(int,\s*input\(\)\.split\(\)\)', line):
            match = re.search(r'(\w+),\s*(\w+),\s*(\w+)\s*=\s*map\(int,\s*input\(\)\.split\(\)\)', line)
            inputs.append(('three_ints', (match.group(1), match.group(2), match.group(3))))
        
        # Two ints from split (T, S = map(int, input().split()))
        elif re.search(r'(\w+),\s*(\w+)\s*=\s*map\(int,\s*input\(\)\.split\(\)\)', line):
            match = re.search(r'(\w+),\s*(\w+)\s*=\s*map\(int,\s*input\(\)\.split\(\)\)', line)
            inputs.append(('two_ints', (match.group(1), match.group(2))))
        
        # Array from split (arr = list(map(int, input().split())))
        elif 'list(map(int' in line or 'map(int' in line:
            match = re.search(r'(\w+)\s*=', line)
            if match:
                inputs.append(('int_array', match.group(1)))
        
        # String input
        elif re.search(r'(\w+)\s*=\s*input\(\)', line):
            match = re.search(r'(\w+)\s*=\s*input\(\)', line)
            inputs.append(('string', match.group(1)))
    
    return inputs

def generate_testcases_for_pattern(inputs):
    """Tạo testcases dựa trên input pattern"""
    testcases = []
    
    # Pattern: n, string (như cuahang_sohoc)
    if len(inputs) == 2 and inputs[0][0] == 'int' and inputs[1][0] == 'string':
        # Test 1-3: Small strings
        testcases.append("3\n010\n")
        testcases.append("5\n11011\n")
        testcases.append("10\n" + ''.join(random.choice('01') for _ in range(10)) + "\n")
        
        # Test 4-7: Medium
        for n in [100, 1000, 5000, 10000]:
            testcases.append(f"{n}\n" + ''.join(random.choice('01') for _ in range(n)) + "\n")
        
        # Test 8-10: Large
        for n in [50000, 100000, 200000]:
            testcases.append(f"{n}\n" + ''.join(random.choice('01') for _ in range(n)) + "\n")
        
        # Test 11: Stress
        n = 500000
        testcases.append(f"{n}\n" + ''.join(random.choice('01') for _ in range(n)) + "\n")
    
    # Pattern: two ints (T, S)
    elif len(inputs) == 1 and inputs[0][0] == 'two_ints':
        # Test 1-3: Small
        testcases.extend(["1 1\n", "2 3\n", "10 20\n"])
        
        # Test 4-7: Medium
        testcases.extend([
            "100 200\n",
            "1000 2000\n",
            "5000 10000\n",
            "10000 20000\n"
        ])
        
        # Test 8-10: Large
        testcases.extend([
            "20000 40000\n",
            "30000 60000\n",
            "50000 100000\n"
        ])
        
        # Test 11: Stress (giảm xuống để tránh timeout)
        testcases.append("100000 200000\n")
    
    # Pattern: three ints (n, x, y)
    elif len(inputs) == 1 and inputs[0][0] == 'three_ints':
        # Test 1-3: Small
        testcases.extend(["3 1 1\n", "5 2 3\n", "10 5 5\n"])
        
        # Test 4-7: Medium
        testcases.extend([
            "100 50 50\n",
            "1000 500 500\n",
            "5000 2500 2500\n",
            "10000 5000 5000\n"
        ])
        
        # Test 8-10: Large
        testcases.extend([
            "50000 25000 25000\n",
            "100000 50000 50000\n",
            "200000 100000 100000\n"
        ])
        
        # Test 11: Stress
        testcases.append("500000 250000 250000\n")
    
    # Pattern: two ints + array (n, k + array)
    elif len(inputs) == 2 and inputs[0][0] == 'two_ints' and inputs[1][0] == 'int_array':
        # Test 1: n=1
        testcases.append("1 1\n1\n")
        
        # Test 2-3: Small arrays
        testcases.append("5 2\n1 2 3 4 5\n")
        testcases.append("10 5\n" + " ".join(str(random.randint(1, 100)) for _ in range(10)) + "\n")
        
        # Test 4-7: Medium
        for n in [100, 1000, 5000, 10000]:
            k = n // 2
            testcases.append(f"{n} {k}\n" + " ".join(str(random.randint(1, 1000000)) for _ in range(n)) + "\n")
        
        # Test 8-10: Large
        for n in [50000, 100000, 200000]:
            k = n // 2
            testcases.append(f"{n} {k}\n" + " ".join(str(random.randint(1, 1000000)) for _ in range(n)) + "\n")
        
        # Test 11: Stress
        n = 500000
        k = n // 2
        testcases.append(f"{n} {k}\n" + " ".join(str(random.randint(1, 1000000)) for _ in range(n)) + "\n")
    
    # Pattern: three ints + array (n, p, q + array)
    elif len(inputs) == 2 and inputs[0][0] == 'three_ints' and inputs[1][0] == 'int_array':
        # Test 1: n=1
        testcases.append("1 1 1\n1\n")
        
        # Test 2-3: Small arrays
        testcases.append("5 2 3\n1 2 3 4 5\n")
        testcases.append("10 5 5\n" + " ".join(str(random.randint(1, 100)) for _ in range(10)) + "\n")
        
        # Test 4-7: Medium
        for n in [100, 1000, 5000, 10000]:
            p = random.randint(1, n)
            q = random.randint(1, n)
            testcases.append(f"{n} {p} {q}\n" + " ".join(str(random.randint(1, 1000000)) for _ in range(n)) + "\n")
        
        # Test 8-10: Large
        for n in [50000, 100000, 200000]:
            p = random.randint(1, n)
            q = random.randint(1, n)
            testcases.append(f"{n} {p} {q}\n" + " ".join(str(random.randint(1, 1000000)) for _ in range(n)) + "\n")
        
        # Test 11: Stress
        n = 500000
        p = random.randint(1, n)
        q = random.randint(1, n)
        testcases.append(f"{n} {p} {q}\n" + " ".join(str(random.randint(1, 1000000)) for _ in range(n)) + "\n")
    
    # Pattern: n, array (standard)
    elif len(inputs) == 2 and inputs[0][0] == 'int' and inputs[1][0] == 'int_array':
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
    
    # Pattern: single int
    elif len(inputs) == 1 and inputs[0][0] == 'int':
        # Test 1-3: Small
        testcases.extend(["1\n", "2\n", "10\n"])
        
        # Test 4-7: Medium
        testcases.extend(["100\n", "1000\n", "10000\n", "50000\n"])
        
        # Test 8-10: Large
        testcases.extend(["100000\n", "500000\n", "1000000\n"])
        
        # Test 11: Stress
        testcases.append("1000000\n")
    
    # Default: single numbers
    else:
        testcases = [
            "1\n", "2\n", "10\n", "100\n", "1000\n",
            "10000\n", "50000\n", "100000\n", "500000\n", "1000000\n", "1000000\n"
        ]
    
    return testcases

def create_custom_generator(problem_id):
    """Tạo custom generator cho problem"""
    editorial_path = PROBLEMS_DIR / problem_id / "editorial.py"
    
    if not editorial_path.exists():
        return False, "No editorial"
    
    with open(editorial_path, 'r', encoding='utf-8') as f:
        editorial_code = f.read()
    
    # Analyze inputs
    inputs = analyze_editorial_deeply(editorial_code)
    
    if not inputs:
        return False, "Cannot detect input pattern"
    
    # Generate testcases
    testcases = generate_testcases_for_pattern(inputs)
    
    # Read current generator
    generator_path = PROBLEMS_DIR / problem_id / "generator.py"
    with open(generator_path, 'r', encoding='utf-8') as f:
        generator_code = f.read()
    
    # Replace testcase section
    test_lines = []
    for tc in testcases:
        tc_repr = repr(tc)  # Use repr() to properly escape
        test_lines.append(f"    test_cases.append({tc_repr})")
    
    testcases_code = '\n'.join(test_lines)
    
    # Find and replace
    start_marker = "def generate_testcases():"
    end_marker = "    # Generate and save"
    
    start_idx = generator_code.find(start_marker)
    end_idx = generator_code.find(end_marker)
    
    if start_idx != -1 and end_idx != -1:
        # Find docstring end
        docstring_start = generator_code.find('"""', start_idx + len(start_marker))
        docstring_end = generator_code.find('"""', docstring_start + 3)
        
        if docstring_end != -1:
            new_code = (
                generator_code[:docstring_end + 3] +
                "\n    test_cases = []\n\n" +
                testcases_code +
                "\n\n" +
                generator_code[end_idx:]
            )
            
            with open(generator_path, 'w', encoding='utf-8') as f:
                f.write(new_code)
            
            return True, "OK"
    
    return False, "Cannot modify generator"

def main():
    import subprocess
    import sys
    
    print("="*60)
    print("🧠 SMART GENERATOR CREATOR")
    print("="*60)
    
    problems = sorted([p.name for p in PROBLEMS_DIR.iterdir() if p.is_dir()])
    print(f"\n📋 Found {len(problems)} problems\n")
    
    success = []
    failed = []
    
    for i, problem_id in enumerate(problems, 1):
        print(f"[{i}/{len(problems)}] {problem_id}...")
        
        # Create custom generator
        ok, msg = create_custom_generator(problem_id)
        if not ok:
            print(f"  ❌ {msg}")
            failed.append((problem_id, msg))
            continue
        
        # Run generator
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
                print(f"  ✅ Generated testcases + ZIP")
                success.append(problem_id)
            else:
                error_msg = result.stderr[:200] if result.stderr else "Unknown error"
                print(f"  ❌ Generator failed: {error_msg}")
                failed.append((problem_id, error_msg))
        except Exception as e:
            print(f"  ❌ Exception: {e}")
            failed.append((problem_id, str(e)))
    
    print("\n" + "="*60)
    print("📊 KẾT QUẢ")
    print("="*60)
    print(f"✅ Thành công: {len(success)}/{len(problems)}")
    print(f"❌ Thất bại: {len(failed)}/{len(problems)}")
    
    if success:
        print(f"\n✅ Các bài thành công:")
        for p in success:
            print(f"  - {p}")
    
    if failed:
        print(f"\n❌ Các bài thất bại:")
        for p, msg in failed:
            print(f"  - {p}: {msg}")

if __name__ == "__main__":
    main()
