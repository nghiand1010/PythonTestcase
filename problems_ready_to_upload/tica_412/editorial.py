# -*- coding: utf-8 -*-
"""
Editorial Solution for tica_412
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


def find_kth_number_not_divisible(n, k):
    # Tính số chu kỳ và phần dư
    cycles = k // (n - 1)
    remainder = k % (n - 1)
    
    # Nếu dư bằng 0, kết quả là số cuối cùng của chu kỳ trước
    if remainder == 0:
        return cycles * n - 1
    else:
        return cycles * n + remainder

# Nhập dữ liệu từ bàn phím
print()
n, k = map(int, input().split())

# Tính toán và in kết quả
result = find_kth_number_not_divisible(n, k)
print(result)
