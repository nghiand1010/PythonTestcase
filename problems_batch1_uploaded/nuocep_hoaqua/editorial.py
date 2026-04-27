# -*- coding: utf-8 -*-
"""
Editorial Solution for nuocep_hoaqua
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


def solve():
    a = int(input())
    b = int(input())
    c = int(input())
    x = int(input())

    t = min(a, x)
    a -= t
    x -= t

    t = min(b, x)
    b -= t
    x -= t

    t = min(c, x)
    c -= t
    x -= t

    print(a)
    print(b)
    print(c)

solve()


