# -*- coding: utf-8 -*-
"""
Editorial Solution for nhat_soi
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


n, p, q = map(int, input().split())
a = list(map(int, input().split()))

a.sort()

vt = {}

for i in range(n):
    vt[a[i]] = i + 1


def tim(x):
    k = vt[x]

    if n % 2 == 1 and k == (n + 1) // 2:
        return "Andy"

    if k <= n // 2:
        if k % 2 == 1:
            return "Andy"
        else:
            return "Bob"

    d = n - k + 1

    if d % 2 == 1:
        return "Bob"
    else:
        return "Andy"


print(tim(p))
print(tim(q))

Link đề bài:
https://oj.codedream.edu.vn/problem/nshn2382
