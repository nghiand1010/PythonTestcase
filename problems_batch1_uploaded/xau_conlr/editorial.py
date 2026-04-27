# -*- coding: utf-8 -*-
"""
Editorial Solution for xau_conlr
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


y = input().rstrip('\n')
n = int(input())

out = []
for _ in range(n):
    L, R = map(int, input().split())
    out.append(y[L:R+1])

print("\n".join(out))

