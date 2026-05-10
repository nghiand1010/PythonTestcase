# -*- coding: utf-8 -*-
"""
Editorial Solution for qua_noel
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


n, k, d = map(int, input().split())
a = list(map(int, input().split()))

a.sort()

i = 0
kq = 0

while i < n:
    dau = a[i]
    dem = 0

    while i < n and dem < d and a[i] - dau <= k:
        i += 1
        dem += 1

    kq += 1

print(kq)
