# -*- coding: utf-8 -*-
"""
Editorial Solution for tica_bangso
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


import math

def main():
    # Nhập kích thước của bảng
    N = int(input())
    # Nhập chỉ số hàng M và cột K
    M, K = map(int, input().split())
    
    R = (M - 1) * N + K
    
    R *= 2
    a = int(R ** 0.5)

    if a * (a + 1) < R:
      print(a + 1)
    else:
      print(a)

if __name__ == "__main__":
    main()
