# -*- coding: utf-8 -*-
"""
Editorial Solution for tica_py142
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


t=int(input())
for _ in range(t):
    n=int(input()); a=list(map(int,input().split())); print(sum(a[:n//2])*sum(a[n//2:]))
