# -*- coding: utf-8 -*-
"""
Editorial Solution for tica_465
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


def count_numbers(A, B, C):
    # Số lượng X trong đoạn [A, B]
    total = B - A + 1
    # Số lượng X chia hết cho C trong đoạn [A, B]
    divisible_by_C = B // C - (A - 1) // C
    # Số lượng X không chia hết cho C
    result = total - divisible_by_C
    return result

# Nhập dữ liệu từ bàn phím
print()
A, B, C = map(int, input().split())

# Tính toán kết quả
output = count_numbers(A, B, C)

# In ra kết quả
print(output)
