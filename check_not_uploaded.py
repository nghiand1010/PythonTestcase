#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kiểm tra bài nào có testcases nhưng chưa upload
"""

from pathlib import Path

SCRIPT_DIR = Path(__file__).parent.absolute()
PROBLEMS_DIR = SCRIPT_DIR / "problems"

# 91 bài đã upload lần trước
UPLOADED_OLD = [
    "tica_py81", "tica_py82", "tica_py83", "tica_py84", "tica_py85",
    "tica_py87", "tica_py88", "tica_py89", "tica_py90", "tica_py91",
    "tica_py92", "tica_py93", "tica_py94", "tica_py95", "tica_py96",
    "tica_py97", "tica_py98", "tica_py99", "tica_py100", "tica_py101",
    "tica_py142", "tica_py143", "tica_py144", "tica_py145", "tica_py146",
    "tica_py147", "tica_py148", "tica_py149", "tica_py150", "tica_py151",
    "tica_py152", "tica_py153", "tica_py154", "tica_py155", "tica_py156",
    "tica_py157", "tica_py158", "tica_py159", "tica_py160", "tica_py161",
    "tica_py162", "tica_py163", "tica_py164", "tica_py165", "tica_py166",
    "tica_py167", "tica_py168", "tica_py169", "tica_py170", "tica_py171",
    "tica_py172", "tica_py173", "tica_py174", "tica_py175", "tica_py176",
    "tica_py177", "tica_py178", "tica_py179", "tica_py180", "tica_py181",
    "tica_py182", "tica_py183", "tica_py184", "tica_py185", "tica_py186",
    "tica_py187", "tica_py188", "tica_py189", "tica_py190", "tica_py191",
    "tica_py192", "tica_py193", "tica_py194", "tica_py195", "tica_py196",
    "tica_py197", "tica_py198", "tica_py199", "tica_py200",
    "min_taudien", "nguocdong_tg", "qua_noel", "sk_tongcheo2024",
    "thietbi_daynui", "thu6_ngay13", "tich_2so", "tomau_nangcap",
    "tongchux", "tongx_dbiet", "vienda", "xoayvong"
]

# 17 bài mới vừa upload
UPLOADED_NEW = [
    "bang_xoanvuong", "chanlek", "ckmn25_chiahet6", "ckmn25_dongho",
    "ckmn25_dsconlac", "ckmn_xaudep", "cktq25_dso", "dso2cso",
    "loinhuan_cophieu", "ngaystem", "sk26_bddayso", "sk26_bong3mau",
    "sk26_dongho", "sk26_hvdacbiet", "sk26_hvxoanoc", "sk26_quanhau", "thoxemphim"
]

UPLOADED_ALL = set(UPLOADED_OLD + UPLOADED_NEW)

def main():
    print("="*60)
    print("KIỂM TRA BÀI CHƯA UPLOAD")
    print("="*60)
    
    # Tìm bài có editorial.py và ZIP
    ready_problems = []
    for problem_dir in sorted(PROBLEMS_DIR.iterdir()):
        if not problem_dir.is_dir():
            continue
        
        editorial_file = problem_dir / "editorial.py"
        zip_files = list(problem_dir.glob("*_testcases.zip"))
        
        if editorial_file.exists() and zip_files:
            ready_problems.append(problem_dir.name)
    
    print(f"\n📊 Total bài có editorial + ZIP: {len(ready_problems)}")
    print(f"📊 Đã upload (old): {len(UPLOADED_OLD)}")
    print(f"📊 Đã upload (new): {len(UPLOADED_NEW)}")
    
    # Tìm bài chưa upload
    not_uploaded = [p for p in ready_problems if p not in UPLOADED_ALL]
    
    print(f"\n{'='*60}")
    print(f"❌ BÀI CHƯA UPLOAD: {len(not_uploaded)}")
    print(f"{'='*60}")
    
    if not_uploaded:
        for i, problem_id in enumerate(not_uploaded, 1):
            print(f"  {i}. {problem_id}")
    else:
        print("✅ Tất cả bài đã upload!")

if __name__ == "__main__":
    main()
