# -*- coding: utf-8 -*-
"""
Editorial Solution for tica_py95
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


def factor(n):
    res = []
    p = 2
    while p * p <= n:
        if n % p == 0:
            c = 0
            while n % p == 0:
                n //= p
                c += 1
            res.append((p, c))
        p += 1
    if n > 1:
        res.append((n, 1))
    return res

t = int(input())
for _ in range(t):
    n = int(input())
    print(' '.join(str(x) for p, c in factor(n) for x in (p, c)))
