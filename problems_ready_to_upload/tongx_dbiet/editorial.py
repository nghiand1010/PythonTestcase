# -*- coding: utf-8 -*-
"""
Editorial Solution for tongx_dbiet
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


def tong_bp(n):
    return n * (n + 1) * (2 * n + 1) // 6


def tong_doan(l, r):
    return tong_bp(r) - tong_bp(l - 1)


m = int(input())
n = int(input())
x = int(input())
y = int(input())

# Giá trị ô được chọn
g = x * x + y * y

# Đường chéo chính "\"
a = min(x - 1, y - 1)
b = min(m - x, n - y)

r1 = x - a
r2 = x + b
c1 = y - a
c2 = y + b

tong1 = tong_doan(r1, r2) + tong_doan(c1, c2)

# Đường chéo phụ "/"
c = min(x - 1, n - y)
d = min(m - x, y - 1)

r3 = x - c
r4 = x + d
c3 = y + c
c4 = y - d

tong2 = tong_doan(r3, r4) + tong_doan(c4, c3)

ket_qua = tong1 + tong2 - g

print(ket_qua)
