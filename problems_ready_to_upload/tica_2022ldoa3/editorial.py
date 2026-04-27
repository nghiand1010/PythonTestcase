# -*- coding: utf-8 -*-
"""
Editorial Solution for tica_2022ldoa3
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


def tinh_tong(n):
    sum = 0
    while n > 0:
        sum = sum + n % 10
        n = n // 10
    return sum
n = int(input())
sohang = n * 2 - 1
if tinh_tong(sohang) % 2 == 0:
    sohang = sohang - 1
print(sohang)
