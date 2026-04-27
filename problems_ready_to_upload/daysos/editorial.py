# -*- coding: utf-8 -*-
"""
Editorial Solution for daysos
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


import math

MOD = 10007


def solve():
    N = int(input())
    def sum_odd_total(n):
        s1 = n * (n + 1) // 2
        s2 = n * (n + 1) * (2 * n + 1) // 6
        s3 = s1 * s1
        return (4 * s3 - 6 * s2 + 4 * s1 - n) % MOD
    def sum_even_total(n):
        s1 = n * (n + 1) // 2
        s3 = s1 * s1
        return (4 * s3 + 2 * s1) % MOD
    total = 0
    if N % 2 == 1:
        k = int(math.ceil(math.sqrt((N + 1) / 2.0)))
        pos = (N + 1) // 2 - (k - 1) ** 2
        T_partial = (pos * (2 * (k - 1) ** 2 + pos)) % MOD
        T_complete = (sum_odd_total(k - 1) + sum_even_total(k - 1)) % MOD
        total = (T_complete + T_partial) % MOD
    else:
        k = int(math.ceil((-1 + math.sqrt(1 + 2 * N)) / 2.0))
        pos = 2 * k - (N // 2) + k * (k - 1) + 1
        T_partial = (2 * pos * (k * (k - 1) + 2 * k + 1) - pos * (pos + 1)) % MOD
        T_complete = (sum_odd_total(k) + sum_even_total(k - 1)) % MOD
        total = (T_complete + T_partial) % MOD
    print(str(total))


solve()
