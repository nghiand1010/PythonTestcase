import os
import random
import string
import sys
import zipfile
from shutil import rmtree
import shutil
import io
import numpy as np
import subprocess
import sys
import os

import math
from collections import Counter

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

def run_algo(chuoi_dau_vao):

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
        # Nội dung bài giải
        # runAlgoContent()


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

def compile_and_run_cpp(user_input='',file_path='temp.cpp'):
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

# def runAlgoContent():
#     compile_and_run_cpp()


for i in range(1,11):
    n= tao_so_ngau_nhien(2,min((i+1)**(i),1000000000))
    # s=tao_so_ngau_nhien(1,min((i+1)**(i),10000))
    # k = tao_so_ngau_nhien(1, min((i+1)**(i),10000))
    # n = tao_so_ngau_nhien(1,min((i+1)**(i),10000))

    #
    # n = tao_so_ngau_nhien(1,  i**2)
    # m = tao_so_ngau_nhien(1,  i**2 )
    # a = tao_so_ngau_nhien(1,  100)
    # b = tao_so_ngau_nhien(1,  y)
    # n= tao_so_ngau_nhien(1,100)


    # s = tao_so_ngau_nhien(1, min(i ** (i), 1000000000))
    # n=tao_so_ngau_nhien(1900,2100)
    # k = tao_so_ngau_nhien(0, 100)

    # b = tao_so_ngau_nhien(a, 100000000000)
    # c = tao_so_ngau_nhien(1, 100000000000)
    # d = tao_so_ngau_nhien(1, 1000000000)
    # mang=tao_mang_ngau_nhien(n+1,-100,100)
    # mang=mang+tao_mang_ngau_nhien(n,1500,2000)
    # mang=" ".join(map(str, mang))

    # mang2 = tao_mang_ngau_nhien(m+1, -100, 100)
    # mang=mang+tao_mang_ngau_nhien(n,1500,2000)
    # mang2 = " ".join(map(str, mang2))

    # mang2 = tao_mang_ngau_nhien(n, -2000, -1500)
    # mang2 = mang2 + tao_mang_ngau_nhien(n, 1500, 2000)
    # mang2 = " ".join(map(str, mang2))
    # k=tao_so_ngau_nhien(2,1000000000)


    # A=tao_so_ngau_nhien(1,B)

    # s=generate_random_string_withchars('01',i*9)
    # m= tao_so_ngau_nhien(n)
    # z = generate_unique_integers(1,n,m)
    # a= tao_mang_ngau_nhien(4,-1000000000000000000,1000000000000000000)

    # test=''
    # for j in range(1,n+1):
    #     # x = tao_so_ngau_nhien(1, 20)
    #     # y = tao_so_ngau_nhien(x, 100)
    #     # z = tao_so_ngau_nhien(1950, 2000)
    #     # s = tao_so_ngau_nhien(5, 50)
    #     # class0 = generate_random_string(s)
    #     mang=tao_mang_ngau_nhien(6,0,100000)
    #     mang = " ".join(map(str, mang))
    #     test=f'{test}{mang}\n'

    #k=tao_so_ngau_nhien(100)
    # mang=tao_mang_ngau_nhien(n,-10,10)
    # test = generate_random_string_withchars('01', n)
    # class0=generate_random_string_letter(n)
    # class1 = generate_random_string_letter(n).lower()
   #  class0=generate_random_string_withchars('HT',40)
    # class1 = generate_random_string_withchars('hello', b)
   # mang=generate_random_floats_array(n,0,100)
   # input_value=f'{n}\n{" ".join(map(str, mang))}'
    #input_value = f'{" ".join(map(str, mang))}'

    input_value = f'{n}'
    # input_value = f'BACE\nGgaudQNS\n#'
    # print(input)
    # sys.stdout = open(f'{filename}/input{i}.in', 'w', encoding="utf-8")
    # sys.stdout.write(input_value)
    with open(f'{filename}/input{i}.in', "w", encoding="utf-8") as f:
        f.write(input_value)
    # out_put=run_algo(input_value)
    out_put=compile_and_run_cpp(input_value)
    with open(f'{filename}/output{i}.out', "w", encoding="utf-8") as f:
        f.write(out_put)
    # sys.stdout = open(f'{filename}/output{i}.out', 'w', encoding="utf-8")
    # sys.stdout.write(out_put)
    #hết nội dung

# sys.stdout.close()
shutil.make_archive(f'{filename}', 'zip',f'{filename}')