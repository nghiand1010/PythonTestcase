# -*- coding: utf-8 -*-
"""
Editorial Solution for hk_matma
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


s = input()
a = []

for i in range(len(s)):
    c = s[i]
    k = (i + 1) % 26

    if 'a' <= c <= 'z':
        g = ord('a')
    else:
        g = ord('A')

    v = ord(c) - g

    if (i + 1) % 2 == 1:
        v = (v + k) % 26
    else:
        v = (v - k) % 26

    a.append(chr(g + v))

print(''.join(a))
