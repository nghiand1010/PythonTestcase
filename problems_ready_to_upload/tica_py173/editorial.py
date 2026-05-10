# -*- coding: utf-8 -*-
"""
Editorial Solution for tica_py173
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


n=int(input()); a=list(map(int,input().split())); mx=max(a); ans=cur=0
for x in a:
    if x==mx: cur+=1; ans=max(ans,cur)
    else: cur=0
print(ans)
