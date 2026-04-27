# -*- coding: utf-8 -*-
"""
Editorial Solution for tica_git18
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


# This code is a simple console application for checking conditions based on input values.

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    test_cases = int(data[0])
    index = 1
    
    for _ in range(test_cases):
        n = int(data[index])
        m = int(data[index + 1])
        k = int(data[index + 2])
        index += 3
        
        is_valid = True
        max_n = 145
        max_m = 180
        remaining_k = 900
        
        if n > max_n:
            is_valid = False
        else:
            max_m -= n
            remaining_k -= n
            if m > max_m:
                is_valid = False
            else:
                remaining_k -= m
                if k > remaining_k:
                    is_valid = False
        
        if is_valid:
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()
