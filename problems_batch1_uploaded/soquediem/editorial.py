# -*- coding: utf-8 -*-
"""
Editorial Solution for soquediem
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


sticks = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]

M, P = map(int, input().split())

cnt = 0
for x in range(100, 1000):
    if x % M != 0:
        continue

    a = x // 100
    b = (x // 10) % 10
    c = x % 10

    if a == b or b == c or a == c:
        continue

    total = sticks[a] + sticks[b] + sticks[c]
    if total % 2 == P:
        cnt += 1

print(cnt)

