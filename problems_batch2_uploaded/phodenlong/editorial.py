# -*- coding: utf-8 -*-
"""
Editorial Solution for phodenlong
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


import math

def solve():
    n = int(input())
    # số đèn bật = số chính phương ≤ n
    answer = int(math.isqrt(n))  # hoặc floor(sqrt(n))
    print(answer)

solve()
