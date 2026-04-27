# -*- coding: utf-8 -*-
"""
Script để tự động test tất cả generators
Chỉ test các bài có editorial.py Python (skip C++ và NO_EDITORIAL)
"""

from pathlib import Path
import subprocess
import sys

SCRIPT_DIR = Path(__file__).parent.absolute()
PROBLEMS_DIR = SCRIPT_DIR / "problems"

def get_python_problems():
    """Get all problems with Python editorial (not C++)"""
    problems = []
    for problem_dir in sorted(PROBLEMS_DIR.iterdir()):
        if not problem_dir.is_dir():
            continue
        
        # Skip if no editorial
        if (problem_dir / "NO_EDITORIAL.txt").exists():
            continue
        
        editorial = problem_dir / "editorial.py"
        if not editorial.exists():
            continue
        
        # Check if it's C++
        content = editorial.read_text(encoding='utf-8')
        if '#include' in content or 'using namespace std' in content:
            continue
        
        problems.append(problem_dir.name)
    
    return problems

PROBLEMS_TO_CUSTOMIZE = get_python_problems()

def test_generator(problem_id):
    """Test generator và tạo testcases + ZIP"""
    problem_dir = PROBLEMS_DIR / problem_id
    generator_py = problem_dir / "generator.py"
    
    if not generator_py.exists():
        return False, "Không có generator.py"
    
    try:
        # Run generator
        result = subprocess.run(
            [sys.executable, str(generator_py)],
            cwd=str(problem_dir),
            capture_output=True,
            text=True,
            timeout=30,
            encoding='utf-8'
        )
        
        # Check if successful - support multiple formats
        success_patterns = [
            "SUCCESS: Generated 11/11",
            "[SUCCESS] Generated 11/11", 
            "[OK] Generated 11/11"
        ]
        is_success = any(pattern in result.stdout for pattern in success_patterns)
        
        if is_success:
            # Check if ZIP created
            zip_file = problem_dir / f"{problem_id}_testcases.zip"
            if zip_file.exists():
                return True, "OK"
            else:
                return False, "Thiếu ZIP file"
        else:
            # Return error
            if result.stderr:
                return False, result.stderr[:300]
            else:
                return False, result.stdout[:300]
    except subprocess.TimeoutExpired:
        return False, "Timeout"
    except Exception as e:
        return False, str(e)[:300]

def main():
    """Test tất cả generators và báo cáo kết quả"""
    print(f"Testing {len(PROBLEMS_TO_CUSTOMIZE)} generators...")
    print("=" * 60)
    
    success_list = []
    failed_list = []
    
    for i, problem_id in enumerate(PROBLEMS_TO_CUSTOMIZE, 1):
        print(f"[{i}/{len(PROBLEMS_TO_CUSTOMIZE)}] Testing {problem_id}...", end=" ", flush=True)
        ok, msg = test_generator(problem_id)
        
        if ok:
            print("✅")
            success_list.append(problem_id)
        else:
            print(f"❌")
            print(f"  Error: {msg}")
            failed_list.append(problem_id)
    
    print("=" * 60)
    print(f"Kết quả:")
    print(f"  ✅ Thành công: {len(success_list)}/{len(PROBLEMS_TO_CUSTOMIZE)}")
    print(f"  ❌ Thất bại: {len(failed_list)}/{len(PROBLEMS_TO_CUSTOMIZE)}")
    
    if success_list:
        print(f"\n✅ Đã hoàn thành:")
        for p in success_list:
            print(f"  - {p}")
    
    if failed_list:
        print(f"\n❌ Cần sửa:")
        for p in failed_list:
            print(f"  - {p}")
        
        # Save failed list
        with open(SCRIPT_DIR / "generators_failed.txt", "w", encoding="utf-8") as f:
            f.write("\n".join(failed_list))
        print(f"\n💾 Đã lưu danh sách thất bại vào: generators_failed.txt")

if __name__ == "__main__":
    main()
