# -*- coding: utf-8 -*-
"""
Editorial Solution for tica_py164
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


n=int(input()); a=list(map(int,input().split())); from collections import Counter; c=Counter(a)
for x in sorted(c): print(f'{x}: {c[x]}')
