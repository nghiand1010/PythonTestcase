# -*- coding: utf-8 -*-
"""
Editorial Solution for tica_a21
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


def count_trailing_zeros(n):
    """Hàm đếm số chữ số 0 tận cùng trong N!"""
    count = 0
    power_of_5 = 5
    while n >= power_of_5:
        count += n // power_of_5
        power_of_5 *= 5
    return count

def find_minimum_n(k):
    """Hàm tìm N nhỏ nhất sao cho N! có ít nhất K chữ số 0 tận cùng"""
    low, high = 1, k * 5  # Dự đoán khoảng giá trị N tối đa
    result = -1
    while low <= high:
        mid = (low + high) // 2
        zeros = count_trailing_zeros(mid)
        if zeros >= k:
            result = mid
            high = mid - 1  # Tiếp tục tìm N nhỏ hơn
        else:
            low = mid + 1  # Tăng giá trị tìm kiếm
    return result

# Nhập K từ input
k = int(input())  # Nhập giá trị K
result = find_minimum_n(k)
print(result)
