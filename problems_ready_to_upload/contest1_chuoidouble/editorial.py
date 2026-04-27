# -*- coding: utf-8 -*-
"""
Editorial Solution for contest1_chuoidouble
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


s = input()
a = ""
lst = [0] * 26

for i in range(0, len(s)):
    lst[ord(s[i]) - 97] += 1
for i in range(0, 26):
    a += chr(i + 97) * lst[i]
print(a + a[::-1])
