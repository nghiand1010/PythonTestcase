# -*- coding: utf-8 -*-
"""
Editorial Solution for kiemtra_hoanhao
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


import math

def kiemtra_hoanhao(n) :
    if n <= 1:
        return False
    s = 1  # tổng các ước thực sự (không tính n)

    r = math.isqrt(n)
    for d in range(2, r + 1):
        if n % d == 0:
            s += d
            q = n // d
            if q != d:
                s += q

    return s == n


n = int(input())  
if kiemtra_hoanhao(n):
    print("YES")
else:
    print("NO")
