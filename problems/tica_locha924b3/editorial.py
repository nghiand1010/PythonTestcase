# -*- coding: utf-8 -*-
"""
Editorial Solution for tica_locha924b3
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


def max_difference(n, arr):
    min_value = arr[0]  # Giá trị nhỏ nhất ban đầu
    max_diff = float('-inf')  # Hiệu lớn nhất khởi tạo âm vô cùng

    for j in range(1, n):
        # Cập nhật max_diff với hiệu giữa a[j] và min_value
        max_diff = max(max_diff, arr[j] - min_value)
        
        # Cập nhật giá trị nhỏ nhất
        min_value = min(min_value, arr[j])

    return max_diff

# Đọc đầu vào
n = int(input())
arr = list(map(int, input().split()))

# Tính kết quả và in ra
print(max_difference(n, arr))
