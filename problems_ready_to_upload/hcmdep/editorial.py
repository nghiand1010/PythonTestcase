# -*- coding: utf-8 -*-
"""
Editorial Solution for hcmdep
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


import sys
def g(x):
    y,n,p=1,x,2
    while p*p<=n:
        c=0
        while n%p==0:
            n//=p;c^=1
        if c:y*=p
        p+=1 if p==2 else 2
    if n>1:y*=n
    return y
print(g(int(sys.stdin.readline())))
