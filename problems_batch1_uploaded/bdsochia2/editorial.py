# -*- coding: utf-8 -*-
"""
Editorial Solution for bdsochia2
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


def main():
    n = int(input().strip())
    steps = 0

    while n > 1:
        if n % 2 == 0:
            n //= 2
        else:
            if n == 3 or n % 4 == 1:
                n -= 1
            else:
                n += 1
        steps += 1

    print(steps)

if __name__ == "__main__":
    main()

