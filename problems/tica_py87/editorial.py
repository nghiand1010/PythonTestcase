# -*- coding: utf-8 -*-
"""
Editorial Solution for tica_py87
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


q = int(input())
for _ in range(q):
    x1, x2, x3, d = map(int, input().split())
    a, b, c = sorted([x1, x2, x3])
    print(max(0, d - (b - a)) + max(0, d - (c - b)))
