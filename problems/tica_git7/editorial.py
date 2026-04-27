# -*- coding: utf-8 -*-
"""
Editorial Solution for tica_git7
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


def main():
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().split())
        if a == 3:
            if b > 3:
                print("NO")
            else:
                print("YES")
        elif a == 2:
            if b > 3:
                print("NO")
            else:
                print("YES")
        elif a == 1:
            if b > 1:
                print("NO")
            else:
                print("YES")
        else:
            print("YES")

if __name__ == "__main__":
    main()
