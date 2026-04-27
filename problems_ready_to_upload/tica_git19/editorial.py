# -*- coding: utf-8 -*-
"""
Editorial Solution for tica_git19
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


# This Python code is a translation of a C++ program that reads inputs and performs a spiral matrix filling.
def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    test_cases = int(data[0])
    index = 1
    
    for _ in range(test_cases):
        n, x, y = map(int, data[index].split())
        x -= 1
        y -= 1
        matrix = [[0] * n for _ in range(n)]
        lower_bound = n
        upper_bound = n
        current_value = 1
        p = 0
        found = False
        
        while current_value <= n * n:
            for i in range(p, upper_bound):
                if p == x and i == y:
                    print(current_value)
                    found = True
                    break
                matrix[p][i] = current_value
                current_value += 1
            if found: break
            
            for i in range(p + 1, lower_bound):
                if i == x and upper_bound - 1 == y:
                    print(current_value)
                    found = True
                    break
                matrix[i][upper_bound - 1] = current_value
                current_value += 1
            if found: break
            
            for i in range(upper_bound - 2, p - 1, -1):
                if lower_bound - 1 == x and i == y:
                    print(current_value)
                    found = True
                    break
                matrix[lower_bound - 1][i] = current_value
                current_value += 1
            if found: break
            
            for i in range(lower_bound - 2, p, -1):
                if i == x and p == y:
                    print(current_value)
                    found = True
                    break
                matrix[i][p] = current_value
                current_value += 1
            if found: break
            
            p += 1
            lower_bound -= 1
            upper_bound -= 1
        index += 1

if __name__ == "__main__":
    main()
