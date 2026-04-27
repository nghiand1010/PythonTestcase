# -*- coding: utf-8 -*-
"""
Editorial Solution for vong_tay
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


N = int(input())

a = []
while len(a) < N:
    parts = input().split()
    for x in parts:
        a.append(int(x))
        if len(a) == N:
            break

M = N - 1

for L in range(1, M + 1):
    if M % L != 0:
        continue

    ok = True
    for i in range(M):
        if a[i] != a[i % L]:
            ok = False
            break

    if ok:
        print(L)
        break

