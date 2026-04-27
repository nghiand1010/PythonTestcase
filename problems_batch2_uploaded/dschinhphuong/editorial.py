# -*- coding: utf-8 -*-
"""
Editorial Solution for dschinhphuong
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


import math

n = int(input())
arr = []
while len(arr) < n:
    arr += list(map(int, input().split()))

cnt = 0
for a in arr[:n]:
    k = math.isqrt(a)
    if k * k == a:
        cnt += 1

print(cnt)
