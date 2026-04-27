# -*- coding: utf-8 -*-
"""
Organize problems into folders:
- problems_ready_to_upload: 67 bài có generator thành công
- problems_no_editorial: 193 bài không có editorial
"""

from pathlib import Path
import shutil

SCRIPT_DIR = Path(__file__).parent.absolute()
PROBLEMS_DIR = SCRIPT_DIR / "problems"

# 67 bài thành công từ auto_customize_generators.py
SUCCESSFUL_PROBLEMS = [
    'contest1_caudo', 'contest1_chuoidouble', 'dayso10', 'daysos', 'demso2',
    'hcmdep', 'lichbyteland', 'lucky1', 'muahoa2', 'ngaytieptheo2',
    'tcsbangnhau1', 'tica_2022ldoa3', 'tica_23ldoa3', 'tica_23thtmta3',
    'tica_23thtmta4', 'tica_412', 'tica_460', 'tica_461', 'tica_465',
    'tica_a21', 'tica_bangso', 'tica_buttongame', 'tica_cuago',
    'tica_git1', 'tica_git100', 'tica_git12', 'tica_git13', 'tica_git14',
    'tica_git17', 'tica_git18', 'tica_git19', 'tica_git2', 'tica_git21',
    'tica_git3', 'tica_git4', 'tica_git5', 'tica_git6', 'tica_git7',
    'tica_git8', 'tica_git84', 'tica_git9', 'tica_hno20b1', 'tica_hoanvi1',
    'tica_ks905b1', 'tica_ks905b4', 'tica_locha924b1', 'tica_locha924b3',
    'tica_snnine', 'tica_sodep', 'tica_t7_24_08', 'tica_t7_27_07',
    'tica_tbltkhdkbaib', 'tica_tha23hdkdstk1', 'tica_tholac2',
    'tica_tht22dna3', 'tica_tht22lda2', 'tica_tht22str2a2', 'tica_tht24tka4',
    'tica_thu7_thun', 'tica_tinhoctre3', 'tica_tinklon2', 'tichuoc',
    'tochucsukien', 'tomau4', 'tongcs2', 'trongcayantrai', 'zigzag'
]

def copy_ready_to_upload():
    """Copy 67 bài thành công vào problems_ready_to_upload"""
    target_dir = SCRIPT_DIR / "problems_ready_to_upload"
    
    # Xóa thư mục cũ nếu có
    if target_dir.exists():
        shutil.rmtree(target_dir)
    
    target_dir.mkdir()
    
    copied = 0
    for problem_id in SUCCESSFUL_PROBLEMS:
        src = PROBLEMS_DIR / problem_id
        if src.exists():
            dst = target_dir / problem_id
            shutil.copytree(src, dst)
            copied += 1
            print(f"✓ {problem_id}")
        else:
            print(f"✗ {problem_id} - không tồn tại")
    
    print(f"\n✅ Đã copy {copied}/{len(SUCCESSFUL_PROBLEMS)} bài vào {target_dir}")
    return copied

def copy_no_editorial():
    """Copy các bài không có editorial vào problems_no_editorial"""
    target_dir = SCRIPT_DIR / "problems_no_editorial"
    
    # Xóa thư mục cũ nếu có
    if target_dir.exists():
        shutil.rmtree(target_dir)
    
    target_dir.mkdir()
    
    copied = 0
    for problem_dir in sorted(PROBLEMS_DIR.iterdir()):
        if not problem_dir.is_dir():
            continue
        
        # Check if has NO_EDITORIAL.txt marker
        if (problem_dir / "NO_EDITORIAL.txt").exists():
            dst = target_dir / problem_dir.name
            shutil.copytree(problem_dir, dst)
            copied += 1
            print(f"✓ {problem_dir.name}")
    
    print(f"\n✅ Đã copy {copied} bài không có editorial vào {target_dir}")
    return copied

if __name__ == "__main__":
    print("="*60)
    print("COPY 67 BÀI THÀNH CÔNG")
    print("="*60)
    count1 = copy_ready_to_upload()
    
    print("\n" + "="*60)
    print("COPY CÁC BÀI KHÔNG CÓ EDITORIAL")
    print("="*60)
    count2 = copy_no_editorial()
    
    print("\n" + "="*60)
    print("TỔNG KẾT")
    print("="*60)
    print(f"✅ problems_ready_to_upload: {count1} bài")
    print(f"✅ problems_no_editorial: {count2} bài")
    print(f"\nBạn có thể kiểm tra thủ công trước khi upload!")
