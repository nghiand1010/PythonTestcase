# -*- coding: utf-8 -*-
"""
Editorial Solution for tica_py94
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


t = int(input())
for _ in range(t):
    s, d = map(int, input().split())
    if s > 9 * d:
        print(-1)
        continue
    a = [0] * d
    s -= 1
    for i in range(d - 1, 0, -1):
        x = min(9, s)
        a[i] = x
        s -= x
    a[0] = s + 1
    print(''.join(map(str, a)))
