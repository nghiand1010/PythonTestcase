# -*- coding: utf-8 -*-
"""
Editorial Solution for thietbi_daynui
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


n, d = map(int, input().split())
h = list(map(int, input().split()))

dem = 0

for i in range(n - 1):
    if abs(h[i + 1] - h[i]) > d:
        dem += 1

print(dem)
