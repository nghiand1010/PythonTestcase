# -*- coding: utf-8 -*-
"""
Editorial Solution for tica_py100
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


MAXN = 1000000
is_prime = [True] * (MAXN + 1)
is_prime[0] = is_prime[1] = False
for i in range(2, int(MAXN ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, MAXN + 1, i):
            is_prime[j] = False
pre = [0] * (MAXN + 1)
for i in range(1, MAXN + 1):
    pre[i] = pre[i - 1]
    if is_prime[i] and str(i) == str(i)[::-1]:
        pre[i] += i

t = int(input())
for _ in range(t):
    l, r = map(int, input().split())
    if l > r:
        l, r = r, l
    print(pre[r] - pre[l - 1])
