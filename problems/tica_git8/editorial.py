# -*- coding: utf-8 -*-
"""
Editorial Solution for tica_git8
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


def main():
    # Replace with input file logic if needed, for now assume standard input
    test = int(input())
    
    for _ in range(test):
        res = 0
        n, l, m = map(float, input().split())
        
        while n < m:
            res += 1
            n += (n * l) / 100
        
        print(res)

if __name__ == "__main__":
    main()
