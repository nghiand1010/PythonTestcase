# -*- coding: utf-8 -*-
"""
Editorial Solution for hsgioi
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


def f(a, b, k):
    if a >= k:
        return 0
    if b == 0:
        return None
    return (k - a + b - 1) // b

def s():
    n, c, k = map(int, input().split())
    t = []
    for _ in range(n):
        a, b = map(int, input().split())
        v = f(a, b, k)
        if v is not None:
            t.append(v)
    t.sort()
    r = u = 0
    for x in t:
        if u + x > c:
            break
        u += x
        r += 1
    print(r)

s()
