# -*- coding: utf-8 -*-
"""
Editorial Solution for tica_py160
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


t=int(input())
for _ in range(t):
    n,m=map(int,input().split()); a=sorted(map(int,input().split())); k=n-m; print(sum(a[-k:])-sum(a[:k]))
