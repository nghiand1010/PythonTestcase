"""
Custom testcase generator cho bài NUOCEP_HOAQUA
Cần 4 dòng input: a, b, c, x
Output: 3 dòng: a_còn, b_còn, c_còn
"""

import os
import shutil
import random

def run_editorial(a, b, c, x):
    """Chạy logic editorial để tính output"""
    # Logic từ editorial
    t = min(a, x)
    a -= t
    x -= t
    
    t = min(b, x)
    b -= t
    x -= t
    
    t = min(c, x)
    c -= t
    x -= t
    
    return a, b, c

def generate_testcases():
    """Sinh 11 testcase thông minh"""
    
    problem_id = "nuocep_hoaqua"
    output_dir = f"daura_{problem_id}"
    
    # Xóa thư mục cũ nếu có
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
    os.makedirs(output_dir)
    
    # 11 chiến lược test
    test_cases = [
        # (a, b, c, x, description)
        (0, 0, 0, 0, "All zero"),
        (1, 1, 1, 0, "No drinks taken"),
        (10, 10, 10, 5, "Take only from a"),
        (10, 10, 10, 15, "Take from a and b"),
        (10, 10, 10, 30, "Take all"),
        (100, 100, 100, 50, "Large - take from a only"),
        (100, 100, 100, 150, "Large - take from a and b"),
        (100, 100, 100, 250, "Large - take from a, b, c"),
        (1000, 1000, 1000, 1, "Max values, min take (x=1)"),
        (1000, 1000, 1000, 3000, "Max values, max take"),
        (random.randint(50, 500), random.randint(50, 500), 
         random.randint(50, 500), random.randint(0, 1500), "Random"),
    ]
    
    success = 0
    for i, test in enumerate(test_cases, 1):
        a, b, c, x, desc = test
        
        # Đảm bảo x không vượt quá tổng
        x = min(x, a + b + c)
        
        # Tạo input
        input_data = f"{a}\n{b}\n{c}\n{x}\n"
        
        # Chạy editorial để có output
        a_remain, b_remain, c_remain = run_editorial(a, b, c, x)
        output_data = f"{a_remain}\n{b_remain}\n{c_remain}\n"
        
        # Lưu file
        input_file = os.path.join(output_dir, f"input{i}.in")
        output_file = os.path.join(output_dir, f"output{i}.out")
        
        with open(input_file, 'w') as f:
            f.write(input_data)
        
        with open(output_file, 'w') as f:
            f.write(output_data)
        
        print(f"  ✅ Test {i}: {desc}")
        print(f"     Input: a={a}, b={b}, c={c}, x={x}")
        print(f"     Output: a={a_remain}, b={b_remain}, c={c_remain}")
        success += 1
    
    # Tạo zip
    shutil.make_archive(output_dir, 'zip', output_dir)
    print(f"\n  📦 Đã tạo {output_dir}.zip với {success} testcase")

if __name__ == "__main__":
    print("🚀 Sinh testcase cho NUOCEP_HOAQUA\n")
    generate_testcases()
    print("\n✅ HOÀN THÀNH!")
