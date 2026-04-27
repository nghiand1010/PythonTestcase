# -*- coding: utf-8 -*-
"""
Editorial Solution for tica_hoanvi1
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


from math import factorial

def find_kth_permutation(n, k):
    nums = list(range(1, n + 1))  # Danh sách các số từ 1 đến n
    k -= 1  # Đổi k thành chỉ số 0-based
    result = []

    for i in range(n, 0, -1):
        fact = factorial(i - 1)  # (n-1)! cho bước hiện tại
        index = k // fact  # Tìm phần tử đứng đầu
        result.append(nums.pop(index))  # Thêm phần tử vào kết quả và xóa khỏi dãy
        k %= fact  # Cập nhật k cho bước tiếp theo
    
    return result

# Đọc đầu vào
n, k = map(int, input().split())

# Tìm hoán vị thứ k và in kết quả
print(" ".join(map(str, find_kth_permutation(n, k))))
