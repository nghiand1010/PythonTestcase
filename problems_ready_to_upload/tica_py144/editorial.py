# -*- coding: utf-8 -*-
"""
Editorial Solution for tica_py144
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


q=int(input())
for _ in range(q):
    n=int(input()); a=list(map(int,input().split())); ans=0
    for i in range(n):
        for j in range(i+1,n):
            if i*a[i] > j*a[j]: ans+=1
    print(ans)
