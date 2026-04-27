# -*- coding: utf-8 -*-
"""
Editorial Solution for rutthe2
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


# Bài 381A phiên bản đơn giản: dãy thẻ 1..N, không dùng mảng

n = int(input().strip())

# n = 2k hoặc 2k + 1
k = n // 2

if n % 2 == 0:
    # N chẵn: N = 2k
    # Sereja lấy các số chẵn 2, 4, ..., 2k
    sereja = k * (k + 1)          # tổng các số chẵn
    total = n * (n + 1) // 2      # tổng 1..N
    dima = total - sereja         # phần còn lại cho Dima
else:
    # N lẻ: N = 2k + 1
    # Sereja: 1, 3, ..., 2k+1  (k+1 số)
    # Dima:   2, 4, ..., 2k    (k số)
    sereja = (k + 1) * (k + 1)    # (k+1)^2
    dima = k * (k + 1)            # k(k+1)

print(sereja, dima)
