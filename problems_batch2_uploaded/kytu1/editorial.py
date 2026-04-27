# -*- coding: utf-8 -*-
"""
Editorial Solution for kytu1
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


x, y = input().split()   
L = len(x)
Q = int(input())         

for _ in range(Q):
    u, v = map(int, input().split())
    v -= 1  
    if u == 1:
        if x[v] == y[v]:
            print("YES")
        else:
            print("NO")
    else:  
        mirror = L - 1 - v  
        if x[v] == y[mirror]:
            print("YES")
        else:
            print("NO")
