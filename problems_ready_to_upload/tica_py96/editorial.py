# -*- coding: utf-8 -*-
"""
Editorial Solution for tica_py96
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    ans = -1
    p = 2
    while p * p <= n and k > 0:
        while n % p == 0:
            k -= 1
            n //= p
            if k == 0:
                ans = p
                break
        p += 1
    if k == 1 and n > 1:
        ans = n
    print(ans)
