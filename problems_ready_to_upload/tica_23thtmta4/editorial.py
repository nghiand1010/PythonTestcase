# -*- coding: utf-8 -*-
"""
Editorial Solution for tica_23thtmta4
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


def S(n):
    res = (n // len(s)) * tong
    for i in range(n % len(s)):
        res += int(s[i])
    return res

a = input()
l = int(input())
r = int(input())

s = a + a[::-1]
tong = sum(int(ch) for ch in s)
result = S(r) - S(l - 1)
print(result)
