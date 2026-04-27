# -*- coding: utf-8 -*-
"""
Editorial Solution for tica_git12
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


def main():
    import sys
    input = sys.stdin.read
    n = int(input().strip())
    s = 0
    for i in range(1, n + 1):
        m = 1
        for j in range(1, i + 1):
            m *= 2
        s += m
    print(s)

if __name__ == "__main__":
    main()
