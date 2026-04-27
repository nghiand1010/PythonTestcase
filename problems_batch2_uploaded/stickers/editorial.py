# -*- coding: utf-8 -*-
"""
Editorial Solution for stickers
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


def count_digits(s):
    cnt = [0] * 10
    for ch in s:
        cnt[ord(ch) - 48] += 1
    return cnt

T = input().strip()
S = input().strip()

cntT = count_digits(T)
cntS = count_digits(S)

INF = 10**18
ans = INF

for d in [0, 1, 3, 4, 7, 8]:
    if cntS[d] > 0:
        ans = min(ans, cntT[d] // cntS[d])

need25 = cntS[2] + cntS[5]
if need25 > 0:
    ans = min(ans, (cntT[2] + cntT[5]) // need25)

need69 = cntS[6] + cntS[9]
if need69 > 0:
    ans = min(ans, (cntT[6] + cntT[9]) // need69)

if ans == INF:
    ans = 0

print(ans)
