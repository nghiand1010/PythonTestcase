# -*- coding: utf-8 -*-
"""
Editorial Solution for tica_py146
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


q=int(input())
for _ in range(q):
    n=int(input()); a=list(map(int,input().split())); l=0; r=n-1
    while l<r:
        if a[l]>a[r]: l+=1
        else: r-=1
    print(a[l])
