# -*- coding: utf-8 -*-
"""
Editorial Solution for tica_py157
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


q=int(input())
for _ in range(q):
    n=int(input()); a=list(map(int,input().split())); s=sum(a); left=0; ans=-1
    for i,x in enumerate(a,1):
        if left==s-left-x: ans=i; break
        left+=x
    print(ans)
