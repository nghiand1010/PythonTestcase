# -*- coding: utf-8 -*-
"""
Editorial Solution for tica_py169
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


def prime(x):
    if x<2: return False
    i=2
    while i*i<=x:
        if x%i==0: return False
        i+=1
    return True
n=int(input()); a=list(map(int,input().split())); best_len=0; best_sum=-1; cur=[a[0]]
for x in a[1:]:
    if x>cur[-1]: cur.append(x)
    else:
        s=sum(cur)
        if prime(s) and (len(cur)>best_len or len(cur)==best_len and s>best_sum): best_len=len(cur); best_sum=s
        cur=[x]
s=sum(cur)
if prime(s) and (len(cur)>best_len or len(cur)==best_len and s>best_sum): best_len=len(cur); best_sum=s
print(best_sum if best_len else -1)
