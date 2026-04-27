# -*- coding: utf-8 -*-
"""
Editorial Solution for doi_xung_hsg
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


s = input().strip()
n = len(s)

max_len = 1

def expand(l, r):
    while l >= 0 and r < n and s[l] == s[r]:
        l -= 1
        r += 1
    return r - l - 1

for i in range(n):
    a = expand(i, i)
    b = expand(i, i + 1)
    max_len = max(max_len, a, b)

print(max_len)

