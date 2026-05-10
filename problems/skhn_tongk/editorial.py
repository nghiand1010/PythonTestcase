# -*- coding: utf-8 -*-
"""
Editorial Solution for skhn_tongk
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


k = int(input())

q = k // 3
r = k % 3

tong = 3 * q * (3 * q + 1) // 2

if r >= 1:
    tong += 3 * q + 3

if r >= 2:
    tong += 3 * q + 2

print(tong % 2026)
