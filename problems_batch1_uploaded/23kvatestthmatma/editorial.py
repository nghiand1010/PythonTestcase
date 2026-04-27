# -*- coding: utf-8 -*-
"""
Editorial Solution for 23kvatestthmatma
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


k = int(input())
S = input()

shift = k % 26

res = []
for ch in S:
    if 'A' <= ch <= 'Z':
        pos = ord(ch) - ord('A')
        new_pos = (pos + shift) % 26
        res.append(chr(new_pos + ord('A')))
    else:
        res.append(ch)

print(''.join(res))

