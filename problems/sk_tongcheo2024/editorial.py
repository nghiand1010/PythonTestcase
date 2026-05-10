# -*- coding: utf-8 -*-
"""
Editorial Solution for sk_tongcheo2024
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


MOD = 10**9 + 7

def tong(L, R):
    return (R - L + 1) * (L + R) // 2

N, Q = map(int, input().split())

for i in range(Q):
    x, y = map(int, input().split())

    d = x - y
    L1 = max(1, d + 1)
    R1 = min(N, N + d)
    sm = 0
    if L1 <= R1:
        c1 = R1 - L1 + 1
        s1 = tong(L1, R1)
        sm = (N + 1) * s1 - (N + d) * c1

    s = x + y
    L2 = max(1, s - N)
    R2 = min(N, s - 1)
    sa = 0
    if L2 <= R2:
        c2 = R2 - L2 + 1
        s2 = tong(L2, R2)
        sa = (N - 1) * s2 + (s - N) * c2

    v = (x - 1) * N + y
    ans = (sm + sa - v) % MOD
    print(ans)
