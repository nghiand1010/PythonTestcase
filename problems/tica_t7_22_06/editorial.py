# -*- coding: utf-8 -*-
"""
Editorial Solution for tica_t7_22_06
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


a = int(input())
n = int(input())
m = int(input())
l = len(str(a))
x = l * (2 ** n)
if m > x:
    print(-1)
else:
    for i in range(n):
        a = str(a)
        x = a[::-1]
        a += x
    print(a[m - 1])
