# -*- coding: utf-8 -*-
"""
Editorial Solution for tica_py93
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    x = ''
    y = ''
    for i, d in enumerate(a):
        if i % 2 == 0:
            x += str(d)
        else:
            y += str(d)
    print(int(x or '0') + int(y or '0'))
