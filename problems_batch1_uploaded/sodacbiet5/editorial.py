# -*- coding: utf-8 -*-
"""
Editorial Solution for sodacbiet5
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


n = input().strip()
L = len(n)

if L < 2:
    print("NO")
else:
    ok = True

    i = 0
    while i < L:
        if n[i] not in "1234":
            ok = False
            break
        i += 1

    if ok:
        a = int(n[0])
        b = int(n[1])

        if a == b:
            ok = False
        else:
            i = 0
            while i < L:
                digit = int(n[i])
                if i % 2 == 0:
                    if digit != a:
                        ok = False
                        break
                else:
                    if digit != b:
                        ok = False
                        break
                i += 1

    if not ok:
        print("NO")
    else:
        rank = 1
        d = 1
        while d <= 4:
            if d != a and d < b:
                rank += 1
            d += 1

        pos_pair = (a - 1) * 3 + rank
        index = 12 * (L - 2) + pos_pair
        print(index)

