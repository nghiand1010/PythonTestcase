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
        runAlgoContent()


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
    def convertFive(n):
        if n == 0:
            return 5
        y = [c for c in str(n)]
        for i in range(len(y)):
            if y[i] == '0':
                y[i] = '5'
        return int("".join(y))

    t = int(input())
    while t != 0:
        t -= 1
        v = int(input())
        print(convertFive(v))

    #ket thuc


for i in range(1,12):
    #T= tao_so_ngau_nhien(2,min((i+1)**(i),10**2))
    T1=tao_so_ngau_nhien(1,10**5)
    T2=tao_so_ngau_nhien(0,10**12)
    #THEM
    #T3=tao_so_ngau_nhien(T2,T1)
    #T4 = tao_so_ngau_nhien(1,10)
    #T5= tao_so_ngau_nhien(1, 10)
    #p=tao_so_ngau_nhien(1,min((i+1)**(i),10**6))
  # p1= tao_so_ngau_nhien(1, min((i + 1) ** (i), 10 ** 3))

    # s=generate_random_string_letter(T)




    # n = tao_so_ngau_nhien(2, min((i + 1) ** (i), 100000))
    # n=tao_so_ngau_nhien(1,255)
    # s=generate_random_string_letter(n)
    #

    # k = tao_so_ngau_nhien(1, min((i+1)**(i),20))

    # k=tao_so_ngau_nhien(1,T+n)
    #
    # a = tao_mang_ngau_nhien(T, 1, 30)
    # a = "\n".join(map(str, a))
    # k=generate_unique_integers(1,T,T-1)
    # k=" ".join(map(str, k))

    # s=str(k)+s


   #1 test=''
   #2 for j in range(1,T+1):
        # n=tao_so_ngau_nhien(2,min((j+1)**(j),1000000 ))
        #
        # x=tao_so_ngau_nhien(1,n)
        #
        # z=tao_so_ngau_nhien(1,n)
        # z2=tao_so_ngau_nhien(1,min(100,n//2))
        # a = tao_mang_ngau_nhien(3, 1, 100000)
        # a = " ".join(map(str, a))

        # s=generate_random_string_letter(n)
        # s=s.upper()
   #3     s = generate_random_string_withchars('abc',3)
        # s=str(x)+s
        # s=s.lower()
    #4    test=f'{test}{s}\n'


   # mang=generate_random_floats_array(n,0,100)
   # input_value=f'{n}\n{" ".join(map(str, mang))}'
    #input_value = f'{" ".join(map(str, mang))}'
    # test=test.strip()

    #input_value = f'{T1}'
    input_value = f'{T1}\n{T2}'
    #input_value = f'{T1}\n{T2}\n{T3}'
    #input_value = f'{T}\n{T1}\n{T2}\n{T3}\n{T4}\n{T5}'
    with open(f'{filename}/input{i}.in', "w", encoding="utf-8") as f:
        f.write(input_value)
    out_put=run_algo(input_value)

    sys.stdout = open(f'{filename}/output{i}.out', 'w', encoding="utf-8")
    sys.stdout.write(out_put)
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