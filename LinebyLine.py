import io
import sys

# Chuỗi bạn muốn Python đọc
chuoi = "Đây là một mô phỏng đầu vào.\n"

# Tạo đối tượng StringIO từ chuỗi
string_io = io.StringIO(chuoi)

# Đọc chuỗi như thể nó là đầu vào từ hàm input()
input_truoc = sys.stdin
sys.stdin = string_io

# Sử dụng hàm input() để đọc đầu vào
noi_dung_nhap = input("Nhập nội dung: ")

# Đặt lại sys.stdin về trạng thái ban đầu
sys.stdin = input_truoc

print("Bạn đã nhập:", noi_dung_nhap)
