# -*- coding: utf-8 -*-
"""
Editorial Solution for tica_py83
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


t = int(input())
for _ in range(t):
    n, s, q = map(int, input().split())
    print(max(n - s, n - q) + 1)
