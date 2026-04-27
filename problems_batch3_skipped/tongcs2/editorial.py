# -*- coding: utf-8 -*-
"""
Editorial Solution for tongcs2
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


def main():
    n = int(input().strip())    # Tổng cần đạt (1 ≤ n ≤ 45)
    rem = n
    digits = []

    # Bước chọn chữ số theo tham lam
    for d in range(9, 0, -1):
        if rem == 0:
            break
        if rem >= d:
            digits.append(d)
            rem -= d

    # rem luôn về 0 vì n ≤ 45
    # Sắp tăng dần để tạo số nhỏ nhất
    digits.sort()

    # Ghép chữ số lại thành số
    x = 0
    for d in digits:
        x = x * 10 + d

    print(x)

if __name__ == "__main__":
    main()
