# -*- coding: utf-8 -*-
"""
Editorial Solution for lichbyteland
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


def main():
    w = int(input())
    d, m = map(int, input().split())

    # Tính tổng số ngày của các tháng trước tháng m
    prev_months = m - 1
    days = (prev_months // 2) * (31 + 30)    # Mỗi 2 tháng liên tiếp là 31+30 = 61 ngày
    if prev_months % 2 == 1:
        days += 31                           # Nếu còn lại tháng lẻ, cộng thêm 31 ngày
    days += (d - 1)                          # Cộng số ngày trong tháng hiện tại (trừ ngày đầu)

    # Tính thứ
    thu = (w + days - 1) % 7 + 1

    print(thu)

main()
