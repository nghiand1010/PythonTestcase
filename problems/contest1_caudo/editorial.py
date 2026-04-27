# -*- coding: utf-8 -*-
"""
Editorial Solution for contest1_caudo
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


n = int(input())
lst = list(map(int, input().split()))
a = 1

for i in range(0, n):
    a *= lst[i]
a += n - 1
print(a)
