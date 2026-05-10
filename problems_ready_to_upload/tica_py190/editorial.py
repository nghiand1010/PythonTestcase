# -*- coding: utf-8 -*-
"""
Editorial Solution for tica_py190
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


q=int(input())
for _ in range(q):
    n=int(input()); a=list(map(int,input().split())); ans=0
    for k in range(1,n+1):
        if sum(1 for x in a if x>=k)>=k: ans=k
    print(ans)
