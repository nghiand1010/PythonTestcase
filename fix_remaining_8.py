"""
Fix 8 bài còn lại - Custom generator cho từng bài
Focus: Sinh INPUT đúng format → Editorial sinh OUTPUT
"""

import os
import shutil
import random
import sys
import io

def run_editorial(code, input_data):
    """Chạy editorial với input"""
    input_io = io.StringIO(input_data)
    output_io = io.StringIO()
    
    stdin_backup = sys.stdin
    stdout_backup = sys.stdout
    
    try:
        sys.stdin = input_io
        sys.stdout = output_io
        exec_globals = {'sys': sys}
        exec(code, exec_globals)
    except Exception as e:
        return f"ERROR: {e}"
    finally:
        sys.stdin = stdin_backup
        sys.stdout = stdout_backup
    
    return output_io.getvalue()

def save_testcase(output_dir, test_num, input_data, output_data):
    """Lưu 1 testcase"""
    with open(f"{output_dir}/input{test_num}.in", 'w') as f:
        f.write(input_data)
    with open(f"{output_dir}/output{test_num}.out", 'w') as f:
        f.write(output_data)

# ========== 1. SODEP2 ==========
def fix_sodep2():
    print("\n🎯 SODEP2")
    output_dir = "daura_sodep2"
    os.makedirs(output_dir, exist_ok=True)
    
    editorial_code = """
def dem_uoc(a, b, p):
    tong = 0
    i = p
    while i <= b:
        tong += b // i - (a - 1) // i
        i *= p
    return tong

T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    so2 = dem_uoc(a, b, 2)
    so5 = dem_uoc(a, b, 5)
    print(min(so2, so5))
"""
    
    test_cases = [
        (1, [(1, 5)]),
        (1, [(1, 10)]),
        (2, [(1, 25), (10, 50)]),
        (3, [(1, 100), (50, 150), (100, 200)]),
        (1, [(1, 1000)]),
    ]
    
    success = 0
    for i, (T, pairs) in enumerate(test_cases, 1):
        input_lines = [str(T)]
        for a, b in pairs:
            input_lines.append(f"{a} {b}")
        input_data = '\n'.join(input_lines) + '\n'
        
        output_data = run_editorial(editorial_code, input_data)
        if not output_data.startswith("ERROR"):
            save_testcase(output_dir, i, input_data, output_data)
            success += 1
    
    # Thêm random tests
    for i in range(6, 12):
        T = random.randint(1, 3)
        input_lines = [str(T)]
        for _ in range(T):
            a = random.randint(1, 1000)
            b = random.randint(a, 10000)
            input_lines.append(f"{a} {b}")
        input_data = '\n'.join(input_lines) + '\n'
        
        output_data = run_editorial(editorial_code, input_data)
        if not output_data.startswith("ERROR"):
            save_testcase(output_dir, i, input_data, output_data)
            success += 1
    
    shutil.make_archive(output_dir, 'zip', output_dir)
    print(f"  ✅ {success}/11 testcase")
    return success > 0

# ========== 2. SOQUEDIEM ==========
def fix_soquediem():
    print("\n🎯 SOQUEDIEM")
    output_dir = "daura_soquediem"
    os.makedirs(output_dir, exist_ok=True)
    
    editorial_code = """
sticks = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
M, P = map(int, input().split())
cnt = 0
for x in range(100, 1000):
    if x % M != 0:
        continue
    a = x // 100
    b = (x // 10) % 10
    c = x % 10
    if a == b or b == c or a == c:
        continue
    total = sticks[a] + sticks[b] + sticks[c]
    if total % 2 == P:
        cnt += 1
print(cnt)
"""
    
    test_cases = [
        (1, 0), (1, 1), (2, 0), (2, 1),
        (5, 0), (5, 1), (10, 0), (10, 1),
        (7, 0), (3, 1), (11, 0)
    ]
    
    success = 0
    for i, (M, P) in enumerate(test_cases, 1):
        input_data = f"{M} {P}\n"
        output_data = run_editorial(editorial_code, input_data)
        if not output_data.startswith("ERROR"):
            save_testcase(output_dir, i, input_data, output_data)
            success += 1
    
    shutil.make_archive(output_dir, 'zip', output_dir)
    print(f"  ✅ {success}/11 testcase")
    return success > 0

# ========== 3. BDXAU_NAMDINH ==========
def fix_bdxau_namdinh():
    print("\n🎯 BDXAU_NAMDINH")
    output_dir = "daura_bdxau_namdinh"
    os.makedirs(output_dir, exist_ok=True)
    
    editorial_code = """
S = input().strip()
n, i = map(int, input().split())

def block_len(k, n, limit):
    length = 1
    for _ in range(n):
        length *= k
        if length >= limit:
            return limit
    return length

pos = 0
for ch in S:
    k = ord(ch) - ord('0')
    L = block_len(k, n, i)
    if pos + L >= i:
        print(ch)
        break
    pos += L
"""
    
    test_cases = [
        ("123", 1, 1), ("123", 1, 2), ("123", 1, 3),
        ("111", 2, 5), ("222", 2, 10),
        ("321", 3, 20), ("456", 2, 15),
        ("789", 1, 7), ("135", 2, 8),
        ("246", 3, 50), ("159", 2, 12)
    ]
    
    success = 0
    for idx, (S, n, i) in enumerate(test_cases, 1):
        input_data = f"{S}\n{n} {i}\n"
        output_data = run_editorial(editorial_code, input_data)
        if not output_data.startswith("ERROR"):
            save_testcase(output_dir, idx, input_data, output_data)
            success += 1
    
    shutil.make_archive(output_dir, 'zip', output_dir)
    print(f"  ✅ {success}/11 testcase")
    return success > 0

# ========== 4. VITRI_ROBOT ==========
def fix_vitri_robot():
    print("\n🎯 VITRI_ROBOT")
    output_dir = "daura_vitri_robot"
    os.makedirs(output_dir, exist_ok=True)
    
    editorial_code = """
x, y, d = map(int, input().split())
print((x + y * d) % 4 + 1)
"""
    
    test_cases = [
        (0, 0, 1), (1, 0, 1), (0, 1, 1),
        (1, 1, 1), (2, 2, 1), (5, 3, 2),
        (10, 5, 3), (0, 0, 0), (100, 50, 4),
        (7, 9, 2), (15, 20, 1)
    ]
    
    success = 0
    for i, (x, y, d) in enumerate(test_cases, 1):
        input_data = f"{x} {y} {d}\n"
        output_data = run_editorial(editorial_code, input_data)
        if not output_data.startswith("ERROR"):
            save_testcase(output_dir, i, input_data, output_data)
            success += 1
    
    shutil.make_archive(output_dir, 'zip', output_dir)
    print(f"  ✅ {success}/11 testcase")
    return success > 0

# ========== 5. XAU_CONLR ==========
def fix_xau_conlr():
    print("\n🎯 XAU_CONLR")
    output_dir = "daura_xau_conlr"
    os.makedirs(output_dir, exist_ok=True)
    
    editorial_code = """
S = input().strip()
L, R = map(int, input().split())
print(S[L-1:R])
"""
    
    test_cases = [
        ("abcdef", 1, 3), ("hello", 1, 5), ("world", 2, 4),
        ("python", 1, 1), ("test", 2, 3), ("programming", 3, 7),
        ("algorithm", 1, 4), ("data", 2, 4), ("code", 1, 2),
        ("string", 3, 5), ("example", 4, 7)
    ]
    
    success = 0
    for i, (S, L, R) in enumerate(test_cases, 1):
        input_data = f"{S}\n{L} {R}\n"
        output_data = run_editorial(editorial_code, input_data)
        if not output_data.startswith("ERROR"):
            save_testcase(output_dir, i, input_data, output_data)
            success += 1
    
    shutil.make_archive(output_dir, 'zip', output_dir)
    print(f"  ✅ {success}/11 testcase")
    return success > 0

# ========== 6. LEHOIPHIM (có lỗi indent - fix trước) ==========
def fix_lehoiphim():
    print("\n🎯 LEHOIPHIM")
    output_dir = "daura_lehoiphim"
    os.makedirs(output_dir, exist_ok=True)
    
    editorial_code = """
n = int(input())
a = list(map(int, input().split()))
a.sort()
count = 0
for i in range(n):
    for j in range(i+1, n):
        if a[j] % a[i] == 0:
            count += 1
print(count)
"""
    
    test_cases = [
        (3, [2, 4, 8]),
        (4, [1, 2, 3, 6]),
        (5, [1, 1, 1, 1, 1]),
        (2, [10, 20]),
        (4, [5, 10, 15, 30]),
        (3, [7, 14, 21]),
        (5, [2, 4, 6, 8, 10]),
        (1, [100]),
        (6, [1, 2, 3, 4, 5, 6]),
        (4, [3, 9, 27, 81]),
        (5, [5, 15, 25, 50, 75])
    ]
    
    success = 0
    for i, (n, arr) in enumerate(test_cases, 1):
        input_data = f"{n}\n{' '.join(map(str, arr))}\n"
        output_data = run_editorial(editorial_code, input_data)
        if not output_data.startswith("ERROR"):
            save_testcase(output_dir, i, input_data, output_data)
            success += 1
    
    shutil.make_archive(output_dir, 'zip', output_dir)
    print(f"  ✅ {success}/11 testcase")
    return success > 0

# ========== 7. MUAHANG_QNAM ==========
def fix_muahang_qnam():
    print("\n🎯 MUAHANG_QNAM")
    output_dir = "daura_muahang_qnam"
    os.makedirs(output_dir, exist_ok=True)
    
    # Editorial có lỗi sys.input → sửa thành input()
    editorial_code = """
n, p = map(int, input().split())
res = 0
for i in range(n-1, 0, -1):
    res += (p + i) // (i + 1)
print(res)
"""
    
    test_cases = [
        (1, 100), (2, 100), (3, 150),
        (5, 200), (10, 500), (1, 1000),
        (7, 350), (4, 180), (8, 400),
        (6, 270), (9, 450)
    ]
    
    success = 0
    for i, (n, p) in enumerate(test_cases, 1):
        input_data = f"{n} {p}\n"
        output_data = run_editorial(editorial_code, input_data)
        if not output_data.startswith("ERROR"):
            save_testcase(output_dir, i, input_data, output_data)
            success += 1
    
    shutil.make_archive(output_dir, 'zip', output_dir)
    print(f"  ✅ {success}/11 testcase")
    return success > 0

# ========== 8. STICKERS ==========
def fix_stickers():
    print("\n🎯 STICKERS")  
    print("  ⚠️  Bài này editorial đọc từ file - cần xử lý thủ công")
    return False

# ========== MAIN ==========
def main():
    print("🚀 FIX 8 BÀI CÒN LẠI - Custom Generators")
    print("="*60)
    
    results = {}
    results['sodep2'] = fix_sodep2()
    results['soquediem'] = fix_soquediem()
    results['bdxau_namdinh'] = fix_bdxau_namdinh()
    results['vitri_robot'] = fix_vitri_robot()
    results['xau_conlr'] = fix_xau_conlr()
    results['lehoiphim'] = fix_lehoiphim()
    results['muahang_qnam'] = fix_muahang_qnam()
    results['stickers'] = fix_stickers()
    
    success_count = sum(1 for v in results.values() if v)
    
    print("\n" + "="*60)
    print(f"✅ HOÀN THÀNH: {success_count}/8 bài")
    print("="*60)
    
    for name, status in results.items():
        icon = "✅" if status else "❌"
        print(f"  {icon} {name}")
    
    print("\n📦 Tất cả file ZIP đã sẵn sàng!")

if __name__ == "__main__":
    main()
