"""
Organize batch 4 - 4 bài mới
"""
from pathlib import Path
import shutil

SCRIPT_DIR = Path(__file__).parent.absolute()
PROBLEMS_DIR = SCRIPT_DIR / "problems"

# 4 bài mới từ scrape_missing_testcases.py
# Trong đó: caudo, hinhtron2, lucgiacthoi, vienda cần customize
NEW_PROBLEMS = [
    "caudo",
    "hinhtron2", 
    "lucgiacthoi",
    "vienda"
]

def copy_to_batch4():
    """Copy 4 bài mới sang problems_batch4/"""
    batch4_dir = SCRIPT_DIR / "problems_batch4"
    batch4_dir.mkdir(exist_ok=True)
    
    copied = 0
    for problem_id in NEW_PROBLEMS:
        src = PROBLEMS_DIR / problem_id
        dst = batch4_dir / problem_id
        
        if src.exists():
            if dst.exists():
                shutil.rmtree(dst)
            shutil.copytree(src, dst)
            copied += 1
            print(f"✅ Copied {problem_id}")
        else:
            print(f"❌ Not found: {problem_id}")
    
    print(f"\n📊 Tổng: {copied}/4 bài")
    print(f"💾 Đã copy vào: {batch4_dir}")

if __name__ == "__main__":
    copy_to_batch4()
