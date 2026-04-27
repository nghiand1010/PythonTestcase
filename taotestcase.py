import os
import random
import string
import sys
import zipfile
from shutil import rmtree
import shutil
import io
import subprocess
import sys
import os
import glob




import math
from collections import Counter
from math import isqrt
from _decimal import Decimal

filename = "daura"


rmtree(f'{filename}')
try:
    os.mkdir(f'{filename}')
    os.remove(f'{filename}' + '.zip')
except OSError:
    pass

def generate_random_strings_with_space(n):
    random_strings = []
    for _ in range(n):
        length = random.randint(1, 10)  # Độ dài ngẫu nhiên từ 1 đến 10
        random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
        random_strings.append(random_string)
    return ' '.join(random_strings)

def generate_random_string(length):

    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(length))

def generate_random_string_letter(length):

    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))

def generate_random_string_withchars(allowed_chars, length):
    return ''.join(random.choice(allowed_chars) for _ in range(length))


def tao_mang_ngau_nhien(n,min=0,max=1000000):
    mang = [random.randint(min, max) for _ in range(n)]
    return mang
def generate_random_floats_array(size, low, high):
    random_floats = np.random.uniform(low, high, size)
    return random_floats

def generate_unique_integers(min_value, max_value, count):
    if count > (max_value - min_value + 1):
        raise ValueError("Số lượng phần tử không được lớn hơn phạm vi giá trị")
    return random.sample(range(min_value, max_value + 1), count)


def is_prime(n):
    """Kiểm tra xem một số có phải số nguyên tố không"""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# def tao_so_ngau_nhien(max_value):
#     so_ngau_nhien = random.randint(0, max_value)
#     return so_ngau_nhien
def tao_so_ngau_nhien(min_value,max_value):
    so_ngau_nhien = random.randint(min_value, max_value)
    return so_ngau_nhien
def tao_so_ngau_nhien_thuc(min_value,max_value):
    so_ngau_nhien = random.uniform(min_value, max_value)
    return so_ngau_nhien

def generate_4_digit_prime():
    """Tạo một số nguyên tố có 4 chữ số"""
    import random
    while True:
        # Tạo số ngẫu nhiên từ 1000 đến 9999
        number = random.randint(1000, 9999)
        if is_prime(number):
            return number

def run_algo(chuoi_dau_vao, algo_file='main.py'):

    # Chuỗi bạn muốn Python đọc như từ console
    # Tạo đối tượng StringIO từ chuỗi đầu vào
    input_io = io.StringIO(chuoi_dau_vao)
    # Đối tượng StringIO để lưu đầu ra của `print`
    output_io = io.StringIO()
    # Tạo bản sao của `sys.stdin` và `sys.stdout` ban đầu
    stdin_goc = sys.stdin
    stdout_goc = sys.stdout

    try:
        # Tạm thời chuyển hướng `sys.stdin` và `sys.stdout`
        sys.stdin = input_io
        sys.stdout = output_io

        #thuật toán viết ở đây
        # Đọc và thực thi code từ file
        with open(algo_file, 'r', encoding='utf-8') as f:
            algo_code = f.read()
        
        # Tạo global namespace riêng để exec có thể truy cập biến đúng cách
        exec_globals = {}
        exec(algo_code, exec_globals)


    finally:
        # Đặt lại `sys.stdin` và `sys.stdout` về trạng thái ban đầu
        sys.stdin = stdin_goc
        sys.stdout = stdout_goc

    # Lấy nội dung từ đối tượng `output_io`
    output_content = output_io.getvalue()
    # Đóng đối tượng `StringIO`
    output_io.close()
    # Hiển thị nội dung đã lưu
    return  output_content

def compile(file_path='temp.cpp'):
    # Kiểm tra file tồn tại
    if not os.path.exists(file_path):
        print(f"File {file_path} không tồn tại!")
        return

    # Đặt tên file thực thi (Linux/Mac: ./program, Windows: program.exe)
    exe_file = "program.exe" if os.name == "nt" else "./program"

    # Biên dịch C++ bằng g++
    compile_cmd = ["g++", file_path, "-o", exe_file]
    compile_process = subprocess.run(compile_cmd, capture_output=True, text=True)

    # Kiểm tra lỗi biên dịch
    if compile_process.returncode != 0:
        print("Lỗi biên dịch:\n", compile_process.stderr)
        return

    print("Biên dịch thành công, chạy chương trình...")


def run_cpp(user_input=''):
    # Đặt tên file thực thi (Linux/Mac: ./program, Windows: program.exe)
    exe_file = "program.exe" if os.name == "nt" else "./program"
    # Chạy chương trình C++
    process = subprocess.Popen(
        [exe_file],  # Chạy file thực thi
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    # Gửi dữ liệu vào chương trình C++
    # user_input = "Hello từ Python!\n"
    output, error = process.communicate(input=user_input)

    # In kết quả
    print(output.strip())

    # Kiểm tra lỗi (nếu có)
    if error:
        print("Lỗi khi chạy:", error)
    return output.strip()

def runAlgoContent():
    #băt dau
    s = input()

    a = []
    so = []
    t = 0

    for ch in s:
        if '0' <= ch <= '9':
            a.append(ch)
            so.append(ch)
        else:
            if so:
                t += int(''.join(so))
                so = []

    if so:
        t += int(''.join(so))

    a = ''.join(a)

    if a == "":
        print(0)
        print("KHONG")
        print(0)
    else:
        print(int(a))

        vt = -1
        for i in range(len(a)):
            if a[i] == '0' or a[i] == '5':
                vt = i

        if vt == -1:
            print("KHONG")
        else:
            print(int(a[:vt + 1]))

    print(t)

    #ket thuc


# Tạo test cases
# Dòng 1: n và S (2 ≤ n ≤ 10^5, S ≤ 10^6)
# Dòng 2: n số nguyên dương a1, a2, ..., an (1 ≤ ai ≤ 10^6)
for i in range(1, 12):
    if i == 1:
        # Test case 1: n nhỏ nhất, đảm bảo có cặp
        n = 2
        S = 10
        a = [3, 7]  # có 1 cặp
    elif i == 2:
        # Test case 2: Có nhiều cặp giống nhau
        n = tao_so_ngau_nhien(10, 50)
        S = 100
        a = [50] * n  # tất cả đều tạo cặp với nhau
    elif i == 3:
        # Test case 3: S nhỏ, tạo cặp
        n = tao_so_ngau_nhien(5, 20)
        S = tao_so_ngau_nhien(10, 100)
        # Tạo một nửa mảng, nửa còn lại là phần bù
        a = tao_mang_ngau_nhien(n//2, 1, S-1)
        for x in a[:n//2]:
            a.append(S - x)
        random.shuffle(a)
        a = a[:n]
    elif i == 4:
        # Test case 4: n lớn, S trung bình, có một số cặp
        n = tao_so_ngau_nhien(500, 1000)
        S = tao_so_ngau_nhien(100, 1000)
        a = tao_mang_ngau_nhien(n, 1, S)
        # Thêm một số cặp chắc chắn
        for j in range(10):
            x = tao_so_ngau_nhien(1, S-1)
            a[j*2] = x
            a[j*2+1] = S - x
    elif i == 5:
        # Test case 5: Tất cả ai = 1, S = 2
        n = tao_so_ngau_nhien(10, 100)
        S = 2
        a = [1] * n
    elif i == 6:
        # Test case 6: Không có cặp nào
        n = tao_so_ngau_nhien(10, 50)
        S = 10
        a = tao_mang_ngau_nhien(n, 100, 1000)  # tất cả đều lớn hơn S
    elif i == 7:
        # Test case 7: n trung bình, nhiều cặp khác nhau
        n = tao_so_ngau_nhien(100, 500)
        S = tao_so_ngau_nhien(100, 5000)
        a = tao_mang_ngau_nhien(n, 1, S)
    elif i == 8:
        # Test case 8: S lớn, mảng có giá trị vừa phải
        n = tao_so_ngau_nhien(100, 500)
        S = tao_so_ngau_nhien(10**5, 10**6)
        a = tao_mang_ngau_nhien(n, 1, S)
        # Thêm một số cặp
        for j in range(5):
            x = tao_so_ngau_nhien(1, S-1)
            a.append(x)
            a.append(S - x)
        n = len(a)
    elif i == 9:
        # Test case 9: Mảng tăng dần với cặp
        n = tao_so_ngau_nhien(50, 200)
        S = tao_so_ngau_nhien(100, 1000)
        a = sorted(tao_mang_ngau_nhien(n, 1, S))
    elif i == 10:
        # Test case 10: Giá trị trùng lặp nhiều
        n = tao_so_ngau_nhien(50, 200)
        S = tao_so_ngau_nhien(50, 500)
        base_val = S // 2
        a = [base_val] * (n // 2) + tao_mang_ngau_nhien(n - n//2, 1, S)
        random.shuffle(a)
    else:
        # Test case 11: Ngẫu nhiên với một số cặp đảm bảo
        n = tao_so_ngau_nhien(100, 500)
        S = tao_so_ngau_nhien(100, 10000)
        a = tao_mang_ngau_nhien(n-20, 1, S)
        # Thêm 10 cặp chắc chắn
        for j in range(10):
            x = tao_so_ngau_nhien(1, S-1)
            a.append(x)
            a.append(S - x)
        random.shuffle(a)
    
    # Tạo nội dung test case
    input_value = f"{n} {S}\n"
    input_value += " ".join(map(str, a)) + "\n"
    
    with open(f'{filename}/input{i}.in', "w", encoding="utf-8") as f:
        f.write(input_value)
    
    out_put = run_algo(input_value, 'algo.py')

    with open(f'{filename}/output{i}.out', 'w', encoding="utf-8") as f:
        f.write(out_put.rstrip('\n'))
    
    print(f"Đã tạo test case {i}:")
    print(input_value)
    print("-" * 50)

print(f"\n✅ Đã tạo xong 11 test cases trong thư mục '{filename}/'")
    #hết nội dung

def read_all_in_files(directory):
    files = glob.glob(f"{directory}/*.in")  # Lấy danh sách các file .in trong thư mục
    files.sort(key=os.path.getctime)
    contents = []

    for file in files:
        with open(file, 'r', encoding='utf-8') as f:
            contents.append(f.read())  # Đọc toàn bộ nội dung file và thêm vào danh sách

    return contents


def copy_folder(source_folder, destination_folder):
    """
    Sao chép tất cả file trong thư mục nguồn sang thư mục đích.

    - Nếu thư mục đích chưa tồn tại, nó sẽ được tạo.
    - Chỉ sao chép file, không sao chép thư mục con.
    """
    if not os.path.exists(source_folder):
        print(f"Lỗi: Thư mục nguồn '{source_folder}' không tồn tại!")
        return

    # Đảm bảo thư mục đích tồn tại
    os.makedirs(destination_folder, exist_ok=True)

    # Lặp qua tất cả các file trong thư mục nguồn
    for filename in os.listdir(source_folder):
        source_path = os.path.join(source_folder, filename)
        destination_path = os.path.join(destination_folder, filename)

        if os.path.isfile(source_path):  # Chỉ sao chép file, bỏ qua thư mục con
            shutil.copy2(source_path, destination_path)  # Giữ nguyên metadata
            print(f"Đã sao chép: {filename}")

    print("Hoàn thành sao chép tất cả file!")

# Thay 'path/to/directory' bằng đường dẫn thư mục của bạn
# directory_path = "daura"
# templateinput_path = "templateinput"
# copy_folder(templateinput_path, directory_path)  # Sao chép file
#
# all_contents = read_all_in_files(directory_path)
# compile()
# for i, content in enumerate(all_contents):
#     out_put = run_cpp(content)
#     with open(f'{filename}/output{i+1}.out', "w", encoding="utf-8") as f:
#         f.write(out_put)
# sys.stdout.close()
shutil.make_archive(f'{filename}', 'zip',f'{filename}')