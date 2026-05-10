# -*- coding: utf-8 -*-
"""
Editorial Solution for tica_py89
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


x, y, z = map(int, input().split())
a = (x + y) // z
if x % z + y % z < z:
    b = 0
else:
    b = min(z - x % z, z - y % z)
print(a, b)
