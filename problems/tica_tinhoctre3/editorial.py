# -*- coding: utf-8 -*-
"""
Editorial Solution for tica_tinhoctre3
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


import sys

# 1) Xây chuỗi A sao cho đủ 36 ký tự
S = "HOITHITINHOCTRE"
# Hãy lặp S hai lần để chắc chắn có ít nhất 36 ký tự:
A = (S + S)  # độ dài = 30; vẫn thiếu 6 ký tự → lặp thêm
A = A + S    # bây giờ A có 45 ký tự, đủ để lấy đến A[36]

# 2) Đọc N

N = int(input())

# 3) Tìm r sao cho r(r+1)/2 >= N
r = 1
while r*(r+1)//2 < N:
    r += 1

# 4) Tìm c = N - T(r-1)
T_prev = (r-1)*r // 2
c = N - T_prev  # 1-based

# 5) Lấy ký tự thứ N của A (cần trừ đi 1 vì Python 0-based)
ch = A[N-1]

# 6) Tính khoảng cách đến ba cạnh của tam giác 8 tầng
d_left  = c - 1        # khoảng cách đến cạnh trái: c=1 → d_left=0
d_right = r - c        # khoảng cách đến cạnh phải: c=r → d_right=0
d_bot   = 8 - r        # khoảng cách đến đáy: r=8 → d_bot=0
d = min(d_left, d_right, d_bot)

# 7) Xác định màu theo d
if d == 0:
    color = "Vang"
elif d == 1:
    color = "Xanh"
else:  # d == 2
    color = "Cam"

# 8) Xuất kết quả
print(ch)
print(color)
