# -*- coding: utf-8 -*-
"""
Editorial Solution for tichuoc
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


N = int(input())

prod = 1
found = False
for i in range(2, N, 2):
    if N % i == 0:
        prod *= i
        found = True

print(prod if found else 0)
