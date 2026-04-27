import os
import random
import shutil

filename = "daura"

# Xóa và tạo lại thư mục
if os.path.exists(filename):
    shutil.rmtree(filename)
os.mkdir(filename)

def tao_so_ngau_nhien(min_value, max_value):
    """Tạo số ngẫu nhiên trong khoảng"""
    return random.randint(min_value, max_value)

def tao_mang_ngau_nhien(n, min_val, max_val):
    """Tạo mảng n số ngẫu nhiên"""
    return [random.randint(min_val, max_val) for _ in range(n)]

def generate_testcase(test_num):
    """Tạo một test case cho bài toán cung thủ"""
    
    if test_num == 1:
        # Test case 1: N nhỏ nhất (N=1)
        N = 1
        k = [tao_so_ngau_nhien(1, 48)]
    elif test_num == 2:
        # Test case 2: N lớn nhất (N=15)
        N = 15
        k = tao_mang_ngau_nhien(N, 1, 48)
    elif test_num == 3:
        # Test case 3: Tất cả k = 1 (nhỏ nhất)
        N = tao_so_ngau_nhien(5, 10)
        k = [1] * N
    elif test_num == 4:
        # Test case 4: Tất cả k = 48 (lớn nhất)
        N = tao_so_ngau_nhien(5, 10)
        k = [48] * N
    elif test_num == 5:
        # Test case 5: N nhỏ với giá trị k ngẫu nhiên
        N = tao_so_ngau_nhien(1, 5)
        k = tao_mang_ngau_nhien(N, 1, 48)
    elif test_num == 6:
        # Test case 6: N trung bình với giá trị k ngẫu nhiên
        N = tao_so_ngau_nhien(6, 10)
        k = tao_mang_ngau_nhien(N, 1, 48)
    elif test_num == 7:
        # Test case 7: N lớn với giá trị k nhỏ
        N = tao_so_ngau_nhien(12, 15)
        k = tao_mang_ngau_nhien(N, 1, 10)
    elif test_num == 8:
        # Test case 8: N lớn với giá trị k lớn
        N = tao_so_ngau_nhien(12, 15)
        k = tao_mang_ngau_nhien(N, 40, 48)
    elif test_num == 9:
        # Test case 9: Giá trị k tăng dần
        N = tao_so_ngau_nhien(8, 12)
        k = sorted(tao_mang_ngau_nhien(N, 1, 48))
    elif test_num == 10:
        # Test case 10: Giá trị k giảm dần
        N = tao_so_ngau_nhien(8, 12)
        k = sorted(tao_mang_ngau_nhien(N, 1, 48), reverse=True)
    else:
        # Test case ngẫu nhiên hoàn toàn
        N = tao_so_ngau_nhien(1, 15)
        k = tao_mang_ngau_nhien(N, 1, 48)
    
    # Tạo nội dung test case
    content = f"{N}\n"
    content += " ".join(map(str, k)) + "\n"
    
    return content

# Tạo 11 test case
num_tests = 11
for i in range(1, num_tests + 1):
    testcase_content = generate_testcase(i)
    
    # Ghi vào file
    with open(f"{filename}/input{i}.in", "w") as f:
        f.write(testcase_content)
    
    print(f"Đã tạo test case {i}:")
    print(testcase_content)
    print("-" * 50)

print(f"\n✅ Đã tạo xong {num_tests} test cases trong thư mục '{filename}/'")

# Tạo file zip (optional)
try:
    shutil.make_archive(filename, 'zip', filename)
    print(f"✅ Đã tạo file {filename}.zip")
except Exception as e:
    print(f"⚠️ Không thể tạo file zip: {e}")
