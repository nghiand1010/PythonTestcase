#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PIPELINE HOÀN CHỈNH CHO 3 BÀI: bdsochia2, sodep2, stickers
Bước 1: Tạo generator.py
Bước 2: Chạy generator tạo testcases + ZIP
Bước 3: Upload ZIP lên TICA OJ
Bước 4: Auto-submit editorial.py
"""

import os
import sys
import subprocess
import time
from pathlib import Path
from playwright.sync_api import sync_playwright

SCRIPT_DIR = Path(__file__).parent.absolute()
PROBLEMS_DIR = SCRIPT_DIR / "problems"
USERNAME = "thinhdt"
PASSWORD = "Th09051989@"

# 3 bài cần xử lý
PROBLEMS = ["bdsochia2", "sodep2", "stickers"]

print("=" * 70)
print("🚀 PIPELINE HOÀN CHỈNH CHO 3 BÀI")
print("=" * 70)
print(f"\n📋 Danh sách: {', '.join(PROBLEMS)}\n")

# ==============================================================================
# BƯỚC 1: TẠO GENERATOR
# ==============================================================================
print("=" * 70)
print("📝 BƯỚC 1: TẠO GENERATOR")
print("=" * 70)

for problem_id in PROBLEMS:
    print(f"\n🔧 {problem_id}...")
    
    # Đọc editorial
    editorial_path = PROBLEMS_DIR / problem_id / "editorial.py"
    if not editorial_path.exists():
        print(f"  ❌ Không tìm thấy editorial.py")
        sys.exit(1)
    
    with open(editorial_path, 'r', encoding='utf-8') as f:
        editorial_code = f.read()
    
    # Tạo generator.py template
    generator_template = f'''#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generator cho {problem_id}
"""
from pathlib import Path
import zipfile
import shutil

SCRIPT_DIR = Path(__file__).parent.absolute()

def generate_testcases():
    """Sinh testcases"""
    test_cases = []
    
    # TODO: Phân tích editorial và thêm testcases phù hợp
    # Ví dụ pattern:
    # Test 1-3: Small (n = 1, 2, 10)
    # Test 4-7: Medium (100, 1K, 5K, 10K)
    # Test 8-10: Large (50K, 100K, 200K)
    # Test 11: Stress (500K hoặc max)
    
    # THAY ĐỔI PHẦN NÀY DỰA TRÊN EDITORIAL
    test_cases = [
        "1\\n",
        "2\\n",
        "10\\n",
        "100\\n",
        "1000\\n",
        "10000\\n",
        "50000\\n",
        "100000\\n",
        "200000\\n",
        "500000\\n",
        "1000000\\n",
    ]
    
    return test_cases

def run_editorial(input_data):
    """Chạy editorial để sinh output"""
    import subprocess
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
    print(f"🔧 Generator: {problem_id}")
    print("="*60)
    
    # Generate testcases
    test_cases = generate_testcases()
    print(f"📝 Đã tạo {{len(test_cases)}} testcases")
    
    # Create test files
    for i, input_data in enumerate(test_cases, 1):
        print(f"  Test {{i}}... ", end="", flush=True)
        
        # Save input
        input_file = SCRIPT_DIR / f"input{{i}}.txt"
        with open(input_file, 'w', encoding='utf-8') as f:
            f.write(input_data)
        
        # Generate output
        try:
            output_data = run_editorial(input_data)
            output_file = SCRIPT_DIR / f"output{{i}}.txt"
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(output_data)
            print("✅")
        except Exception as e:
            print(f"❌ {{e}}")
            return False
    
    # Create ZIP
    zip_path = SCRIPT_DIR / f"{problem_id}_testcases.zip"
    print(f"\\n📦 Tạo ZIP: {{zip_path.name}}")
    
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for i in range(1, len(test_cases) + 1):
            zipf.write(SCRIPT_DIR / f"input{{i}}.txt", f"input{{i}}.txt")
            zipf.write(SCRIPT_DIR / f"output{{i}}.txt", f"output{{i}}.txt")
    
    print(f"✅ Đã tạo ZIP với {{len(test_cases)}} testcases")
    
    # Cleanup - delete test 11
    print(f"\\n🗑️  Xóa test 11...")
    (SCRIPT_DIR / "input11.txt").unlink(missing_ok=True)
    (SCRIPT_DIR / "output11.txt").unlink(missing_ok=True)
    print("✅ Đã xóa test 11")
    
    return True

if __name__ == "__main__":
    main()
'''
    
    # Lưu generator
    generator_path = PROBLEMS_DIR / problem_id / "generator.py"
    with open(generator_path, 'w', encoding='utf-8') as f:
        f.write(generator_template)
    
    print(f"  ✅ Đã tạo generator.py (cần customize thủ công)")

print("\n" + "=" * 70)
print("⚠️  LƯU Ý: Bạn cần customize generator.py cho từng bài!")
print("=" * 70)
print("\nMở từng file generator.py và:")
print("1. Phân tích editorial để hiểu input format")
print("2. Thay đổi phần generate_testcases() cho đúng")
print("3. Đảm bảo có 11 testcases (1-3 small, 4-7 medium, 8-10 large, 11 stress)")
print("\nSau khi customize xong, chạy tiếp:")
print("  py pipeline_3_bai.py --continue")
