# -*- coding: utf-8 -*-
"""
Editorial Solution for tica_uocso
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


import math

n = int(input().strip())

if n == 0:
    print("INF")
else:
    m = abs(n)
    divs = []
    r = int(math.isqrt(m))
    for i in range(1, r + 1):
        if m % i == 0:
            divs.append(i)
            j = m // i
            if j != i:
                divs.append(j)
    divs.sort(reverse=True)
    print(*divs)
