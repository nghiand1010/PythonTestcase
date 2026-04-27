# -*- coding: utf-8 -*-
"""
Editorial Solution for dayso_bimat
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


N = int(input().strip())
k = N // 2

if N % 2 == 0:
    print(5 * k)
else:
    print(5 * k + 1)


