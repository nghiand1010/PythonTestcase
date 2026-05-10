# -*- coding: utf-8 -*-
"""
Editorial Solution for tica_py185
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


n=int(input()); a=list(map(int,input().split())); s=sum(a); ans=[]
for i,x in enumerate(a,1):
    b=a[:i-1]+a[i:]; m=max(b) if b else 0
    if s-x-m==m: ans.append(i)
print(len(ans)); print(*ans)
