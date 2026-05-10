# -*- coding: utf-8 -*-
"""
Editorial Solution for tica_py183
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


n=int(input()); p=list(map(int,input().split())); seen=[False]*n; ans=0
for i in range(n):
    if not seen[i]:
        ans+=1; j=i
        while not seen[j]: seen[j]=True; j=p[j]-1
print(ans)
