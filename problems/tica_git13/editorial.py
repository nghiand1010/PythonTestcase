# -*- coding: utf-8 -*-
"""
Editorial Solution for tica_git13
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


def main():
    n = int(input())
    s = 0
    for i in range(1, 13):
        if i in {1, 3, 5, 7, 8, 10, 12}:
            x = 31
        elif i == 2:
            if (n % 4 == 0 and n % 100 != 0) or (n % 400 == 0):
                x = 29
            else:
                x = 28
        else:
            x = 30
        for j in range(1, x + 1):
            s += (j // 10) + (j % 10) + (i // 10) + (i % 10) + (n // 1000) + (n // 100) % 10 + (n // 10) % 10 + n % 10
    print(s)

if __name__ == "__main__":
    main()
