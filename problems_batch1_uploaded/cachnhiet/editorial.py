# -*- coding: utf-8 -*-
"""
Editorial Solution for cachnhiet
Auto-generated from editorial.txt
"""

import sys
from io import StringIO

n = int(input())
a = []

for _ in range(n):
    a.append(int(input()))

a.sort()

k = n // 2
s_all = sum(a)

add = 0
for i in range(k):
    add += a[n - k + i] - a[i]

print(s_all + add)

