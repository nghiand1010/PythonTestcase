# -*- coding: utf-8 -*-
"""
Editorial Solution for tica_py168
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


t=int(input())
for _ in range(t):
    n,k=map(int,input().split()); a=sorted(map(int,input().split())); ans=10**18
    for i in range(n):
        ans=min(ans, max(a[i], a[-1]-k) - min(a[0]+k, a[i]-k))
    print(ans)
