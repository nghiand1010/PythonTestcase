# -*- coding: utf-8 -*-
"""
Editorial Solution for tica_git21
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


# This code is translated from C++ to Python
def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    number_of_elements = int(data[0])
    target_sum = int(data[1])
    elements = list(map(int, data[2:2 + number_of_elements]))
    
    elements.sort()
    count = 0
    
    for i in range(number_of_elements - 1, -1, -1):
        current_element = elements[i]
        times = target_sum // current_element
        target_sum -= current_element * times
        count += times
    
    if target_sum > 0:
        print("-1")
    else:
        print(count)

if __name__ == "__main__":
    main()
