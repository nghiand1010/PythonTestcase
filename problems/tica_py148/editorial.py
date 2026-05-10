# -*- coding: utf-8 -*-
"""
Editorial Solution for tica_py148
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


q=int(input())
for _ in range(q):
    n=int(input()); a=list(map(int,input().split())); p=a.index(1); ok1=all(a[(p+i)%n]==i+1 for i in range(n)); ok2=all(a[(p-i)%n]==i+1 for i in range(n)); print('YES' if ok1 or ok2 else 'NO')
