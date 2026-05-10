# -*- coding: utf-8 -*-
"""
Editorial Solution for tica_py167
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


t=int(input())
for _ in range(t):
    n=int(input()); a=sorted(map(int,input().split())); res=[]; l=0; r=n-1
    while l<=r:
        res.append(a[r]); r-=1
        if l<=r: res.append(a[l]); l+=1
    print(*res)
