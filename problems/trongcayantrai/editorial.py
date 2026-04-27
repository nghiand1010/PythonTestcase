# -*- coding: utf-8 -*-
"""
Editorial Solution for trongcayantrai
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


m = int(input())
n = int(input())

k1 = int((n - 1.5 * 2) // 3 + 1)
k2 = int((m - 1.5 * 2) // 3 + 1)
print(k1 * k2)
