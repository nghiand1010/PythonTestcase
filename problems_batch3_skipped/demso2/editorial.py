# -*- coding: utf-8 -*-
"""
Editorial Solution for demso2
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


A, B = map(int, input().split())


def count_div(d, L, R):
    return R // d - (L - 1) // d

cnt2 = count_div(2, A, B)
cnt3 = count_div(3, A, B)
cnt6 = count_div(6, A, B)

print(cnt2 + cnt3 - cnt6)
