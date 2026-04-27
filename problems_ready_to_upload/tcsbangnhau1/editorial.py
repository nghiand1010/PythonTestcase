# -*- coding: utf-8 -*-
"""
Editorial Solution for tcsbangnhau1
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


def tcs(x):
    s = 0
    while (x > 0):
        s += x % 10
        x //= 10
    return s

def count(n):
    cnt = 0
    for x in range(1000, 10000):
        if (tcs(x) == n):
            cnt+=1
    return cnt        

T = int(input())
for _ in range(T):
    n = int(input())
    print(count(n))
