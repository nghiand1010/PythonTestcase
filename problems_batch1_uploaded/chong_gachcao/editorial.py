# -*- coding: utf-8 -*-
"""
Editorial Solution for chong_gachcao
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


n = int(input())
a = list(map(int, input().split()))

a.sort()

h = 0
for x in a:
    if x >= h:
        h += 1

print(h)

