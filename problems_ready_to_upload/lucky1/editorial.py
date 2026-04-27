# -*- coding: utf-8 -*-
"""
Editorial Solution for lucky1
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


import sys, math

a, b = map(int, sys.stdin.read().split())
count = 0
for x in range(a, b + 1):
    if x % 10 == 0:
        continue
    t = x
    rev = 0
    while t:
        rev = rev * 10 + t % 10
        t //= 10
    if math.gcd(x, rev) == 1:
        count += 1
print(count)
