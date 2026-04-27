# -*- coding: utf-8 -*-
"""
Editorial Solution for tongcs2022
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


N = int(input())

cycle = [2, 0, 2, 2]
cycle_sum = sum(cycle)  # = 6

full = N // 4
rem = N % 4

total = full * cycle_sum

for i in range(rem):
    total += cycle[i]

print(total)

