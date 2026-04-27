# -*- coding: utf-8 -*-
"""
Script để tạo editorial.py từ editorial.txt
"""

from pathlib import Path
import re

SCRIPT_DIR = Path(__file__).parent.absolute()
PROBLEMS_DIR = SCRIPT_DIR / "problems"

def clean_editorial_code(content):
    """Clean editorial code - remove markdown fences"""
    # Remove markdown code fences
    content = re.sub(r'^```(?:python)?\s*\n', '', content, flags=re.MULTILINE)
    content = re.sub(r'\n```\s*$', '', content, flags=re.MULTILINE)
    content = content.strip()
    return content

def create_editorial_py(problem_id):
    """Tạo editorial.py từ editorial.txt"""
    problem_dir = PROBLEMS_DIR / problem_id
    editorial_txt = problem_dir / "editorial.txt"
    editorial_py = problem_dir / "editorial.py"
    
    if not editorial_txt.exists():
        return False, "Không có editorial.txt"
    
    if editorial_py.exists():
        return False, "editorial.py đã tồn tại"
    
    # Đọc editorial.txt
    content = editorial_txt.read_text(encoding='utf-8')
    
    # Clean code
    code = clean_editorial_code(content)
    
    if not code or len(code) < 10:
        return False, "Editorial rỗng hoặc quá ngắn"
    
    # Tạo editorial.py
    py_content = f'''# -*- coding: utf-8 -*-
"""
Editorial Solution for {problem_id}
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


{code}
'''
    
    editorial_py.write_text(py_content, encoding='utf-8')
    return True, "OK"

def main():
    """Xử lý tất cả các bài"""
    problem_dirs = sorted([d for d in PROBLEMS_DIR.iterdir() if d.is_dir()])
    
    print(f"Tìm thấy {len(problem_dirs)} bài toán")
    print("=" * 60)
    
    success = 0
    skipped = 0
    failed = 0
    
    for problem_dir in problem_dirs:
        problem_id = problem_dir.name
        ok, msg = create_editorial_py(problem_id)
        
        if ok:
            print(f"✅ {problem_id}")
            success += 1
        elif "đã tồn tại" in msg or "Không có editorial" in msg:
            skipped += 1
        else:
            print(f"⚠️ {problem_id}: {msg}")
            failed += 1
    
    print("=" * 60)
    print(f"Hoàn thành!")
    print(f"  ✅ Tạo mới: {success}")
    print(f"  ⏭️  Bỏ qua: {skipped}")
    print(f"  ❌ Lỗi: {failed}")

if __name__ == "__main__":
    main()
