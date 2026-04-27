# -*- coding: utf-8 -*-
"""
Editorial Solution for tica_205
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


import math

def lcm(a, b):
    """Tính bội số chung nhỏ nhất (LCM) của 2 số a và b"""
    return (a // math.gcd(a, b)) * b

def main():
    n = int(input())  # Nhập số lượng n
    kq = 1
    for _ in range(n):
        t = int(input())  # Nhập từng số
        kq = lcm(kq, t)
    print(kq)

# Gọi hàm main
if __name__ == "__main__":
    main()
