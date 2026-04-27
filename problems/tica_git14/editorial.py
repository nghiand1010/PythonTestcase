# -*- coding: utf-8 -*-
"""
Editorial Solution for tica_git14
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


import sys

def main():
    input = sys.stdin.read
    data = input().split()
    n = int(data[0])
    k = int(data[1])
    a = list(map(int, data[2:n+2]))
    a.sort()
    print(a[k])

if __name__ == "__main__":
    main()
