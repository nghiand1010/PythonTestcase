# -*- coding: utf-8 -*-
"""
Editorial Solution for tich_2so
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


n = int(input())
a = list(map(int, input().split()))

a.sort()

t1 = a[0] * a[1]
t2 = a[n - 1] * a[n - 2]

print(max(t1, t2))
