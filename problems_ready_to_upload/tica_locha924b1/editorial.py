# -*- coding: utf-8 -*-
"""
Editorial Solution for tica_locha924b1
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


def count_unique_integers(a, b, c, d):
    # Tính số lượng phần tử trong mỗi đoạn
    count1 = b - a + 1
    count2 = d - c + 1
    
    # Tính phần giao của hai đoạn
    start = max(a, c)
    end = min(b, d)
    intersection = max(0, end - start + 1)
    
    # Tổng số lượng số nguyên khác nhau
    result = count1 + count2 - intersection
    return result

# Đọc dữ liệu từ input
a, b, c, d = map(int, input().split())

# Tính và in kết quả
print(count_unique_integers(a, b, c, d))
