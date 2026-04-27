# -*- coding: utf-8 -*-
"""
Editorial Solution for tica_git5
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


# Chuyển đổi từ C++ sang Python

# Đọc giá trị n và k
n = int(input())
k = int(input())

# Kiểm tra điều kiện
if k % (n - 1) == 0:
    print(n * (k // (n - 1)) - 1, n * (k // (n - 1)))
else:
    print(k + (k // (n - 1)), k + (k // (n - 1)))
