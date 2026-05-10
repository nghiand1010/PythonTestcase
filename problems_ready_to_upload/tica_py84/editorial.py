# -*- coding: utf-8 -*-
"""
Editorial Solution for tica_py84
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


q = int(input())
for _ in range(q):
    b, p, f = map(int, input().split())
    h, c = map(int, input().split())
    banh = b // 2
    ans = 0
    if h >= c:
        x = min(p, banh)
        ans += x * h
        banh -= x
        y = min(f, banh)
        ans += y * c
    else:
        y = min(f, banh)
        ans += y * c
        banh -= y
        x = min(p, banh)
        ans += x * h
    print(ans)
