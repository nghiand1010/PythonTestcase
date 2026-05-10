# -*- coding: utf-8 -*-
"""
Editorial Solution for tica_py154
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


q=int(input())
for _ in range(q):
    n=int(input()); a=list(map(int,input().split())); mx=-1; ans=0
    for x in a:
        if x>=mx: ans+=1; mx=x
    print(ans)
