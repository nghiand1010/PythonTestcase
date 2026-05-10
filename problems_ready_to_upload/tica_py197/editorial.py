# -*- coding: utf-8 -*-
"""
Editorial Solution for tica_py197
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


q=int(input())
for _ in range(q):
    n,k=map(int,input().split()); a=list(map(int,input().split())); l=max(1,max(x-k for x in a)); r=min(x+k for x in a); print(r if l<=r else -1)
