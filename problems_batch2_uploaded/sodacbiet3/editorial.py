# -*- coding: utf-8 -*-
"""
Editorial Solution for sodacbiet3
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


def tong_binh_phuong_chu_so(n):
    s = str(n)
    tong = 0
    for ch in s:
        tong += int(ch) ** 2
    return tong

def la_nguyen_to(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

n = int(input())
S = tong_binh_phuong_chu_so(n)

if la_nguyen_to(S):
    print(1)
else:
    print(-1)
print(S)
