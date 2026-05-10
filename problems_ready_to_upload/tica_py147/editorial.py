# -*- coding: utf-8 -*-
"""
Editorial Solution for tica_py147
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


q=int(input())
for _ in range(q):
    n=int(input()); a=list(map(int,input().split())); cnt=[1,0]; s=0; ans=0
    for x in a:
        s=(s+x)%2; ans+=cnt[s]; cnt[s]+=1
    print(ans)
