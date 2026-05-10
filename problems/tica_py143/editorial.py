# -*- coding: utf-8 -*-
"""
Editorial Solution for tica_py143
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


t=int(input())
for _ in range(t):
    n=int(input()); a=list(map(int,input().split())); k=int(input()); a.sort(); print(a[k-1])
