# -*- coding: utf-8 -*-
"""
Editorial Solution for tica_git17
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


def main():
    import sys
    input = sys.stdin.read
    a, b = map(int, input().split())
    
    if a > b:
        print(b, (a - b) // 2)
    elif a == b:
        print(a, 0)
    else:
        print(a, (b - a) // 2)

if __name__ == "__main__":
    main()
