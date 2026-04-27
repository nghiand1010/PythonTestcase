# -*- coding: utf-8 -*-
"""
Editorial Solution for tica_git2
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


t = int(input())

a = [0] * 51
a[1] = 1
a[2] = 2
a[3] = 4
a[4] = 8

for i in range(5, 51):
    a[i] = a[i - 1] + a[i - 2] + a[i - 3] + a[i - 4]

for _ in range(t):
    n = int(input())
    print(a[n])
