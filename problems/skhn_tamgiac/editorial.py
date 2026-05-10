# -*- coding: utf-8 -*-
"""
Editorial Solution for skhn_tamgiac
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


n = int(input())
x = int(input())

tong = 0

for j in range(1, x + 1):
    bat_dau = 1 + (j - 1) * (2 * n - j + 2) // 2

    if j % 2 == 1:
        so = bat_dau + (x - j)
    else:
        so = bat_dau + (n - x)

    tong += so

print(tong)
