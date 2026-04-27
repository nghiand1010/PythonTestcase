# -*- coding: utf-8 -*-
"""
Editorial Solution for tica_tbltkhdkbaib
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


def t(m, n):  
    p = 2 * (m + n)  
    i = (m - 1) * n + (n - 1) * m  
    t = p + i  
    return t  
m, n = map(int, input().split()) 
print(t(m, n))
