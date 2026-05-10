# -*- coding: utf-8 -*-
"""
Editorial Solution for tica_py98
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


def sphenic(n):
    cnt = 0
    p = 2
    while p * p <= n:
        if n % p == 0:
            c = 0
            while n % p == 0:
                n //= p
                c += 1
            if c > 1:
                return False
            cnt += 1
        p += 1
    if n > 1:
        cnt += 1
    return cnt == 3

t = int(input())
for _ in range(t):
    print(1 if sphenic(int(input())) else 0)
