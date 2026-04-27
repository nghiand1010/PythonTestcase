# -*- coding: utf-8 -*-
"""
Editorial Solution for bdxau_namdinh
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


S = input().strip()
n, i = map(int, input().split())

def block_len(k, n, limit):
    length = 1
    for _ in range(n):
        length *= k
        if length >= limit:
            return limit
    return length

pos = 0

for ch in S:
    k = ord(ch) - ord('0')
    L = block_len(k, n, i)
    if pos + L >= i:
        print(ch)
        break
    pos += L

