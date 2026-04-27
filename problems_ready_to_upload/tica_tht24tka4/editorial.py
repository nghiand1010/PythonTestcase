# -*- coding: utf-8 -*-
"""
Editorial Solution for tica_tht24tka4
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


N, A, B, C = map(int, input().split())
if (B - C) < A and N >= B:
    X = (N - B) // (B - C)
    S = X + 1
    N -= (X + 1) * (B - C)
    S += N // A
else:
    S = N // A
print(S)
