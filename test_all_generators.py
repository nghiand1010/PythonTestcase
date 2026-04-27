# -*- coding: utf-8 -*-
"""
Script để customize generator.py cho tất cả các bài bằng AI
Sẽ tự động chạy và customize từng bài một
"""

from pathlib import Path
import subprocess
import sys

SCRIPT_DIR = Path(__file__).parent.absolute()
PROBLEMS_DIR = SCRIPT_DIR / "problems"

def get_problems_with_generator():
    """Lấy danh sách các bài có generator.py"""
    problems = []
    for problem_dir in sorted(PROBLEMS_DIR.iterdir()):
        if not problem_dir.is_dir():
            continue
        
        generator_py = problem_dir / "generator.py"
        editorial_py = problem_dir / "editorial.py"
        
        if generator_py.exists() and editorial_py.exists():
            problems.append(problem_dir.name)
    
    return problems

def test_generator(problem_id):
    """Test generator xem có work không"""
    problem_dir = PROBLEMS_DIR / problem_id
    generator_py = problem_dir / "generator.py"
    
    try:
        result = subprocess.run(
            [sys.executable, str(generator_py)],
            cwd=str(problem_dir),
            capture_output=True,
            text=True,
            timeout=30
        )
        
        # Check if successful
        if "SUCCESS: Generated 11/11" in result.stdout:
            return True, "OK"
        else:
            # Get error message
            if result.stderr:
                return False, result.stderr[:200]
            else:
                return False, result.stdout[:200]
    except subprocess.TimeoutExpired:
        return False, "Timeout"
    except Exception as e:
        return False, str(e)

def main():
    """Test tất cả các generator"""
    problems = get_problems_with_generator()
    
    print(f"Tìm thấy {len(problems)} bài có generator.py")
    print("=" * 60)
    print("Testing generators...")
    print("=" * 60)
    
    success_list = []
    failed_list = []
    
    for i, problem_id in enumerate(problems, 1):
        print(f"[{i}/{len(problems)}] Testing {problem_id}...", end=" ")
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
    print(f"  ✅ Thành công: {len(success_list)}/{len(problems)}")
    print(f"  ❌ Cần customize: {len(failed_list)}/{len(problems)}")
    
    if failed_list:
        print("\\nDanh sách cần customize:")
        for pid in failed_list:
            print(f"  - {pid}")
        
        # Save to file
        with open(SCRIPT_DIR / "problems_need_customize.txt", "w", encoding="utf-8") as f:
            f.write("\\n".join(failed_list))
        print("\\n💾 Đã lưu danh sách vào: problems_need_customize.txt")

if __name__ == "__main__":
    main()
