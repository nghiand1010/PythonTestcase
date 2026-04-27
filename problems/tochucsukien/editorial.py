# -*- coding: utf-8 -*-
"""
Editorial Solution for tochucsukien
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


def solve():
    n = int(input())
    t = int(input())
    X = int(input())
    
    remaining = X
    for g in range(t):
        if g == 0:
            size_g = n // t
        else:
            if g <= n:
                size_g = 1 + (n - g) // t
            else:
                size_g = 0
        if remaining <= size_g:
            offset = remaining - 1
            if g == 0:
                ans = t * (offset + 1)
            else:
                ans = g + offset * t
            print(ans)
            return
        else:
            remaining -= size_g
    print(0)

if __name__ == '__main__':
    solve()
