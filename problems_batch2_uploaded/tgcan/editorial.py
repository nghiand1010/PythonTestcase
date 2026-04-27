# -*- coding: utf-8 -*-
"""
Editorial Solution for tgcan
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


import math

# Function to calculate the area of a triangle using Heron's formula
def calculate_area(a, b, c):
    s = (a + b + c) / 2  # Semi-perimeter
    if s > a and s > b and s > c:  # Check if triangle inequality is satisfied
        return math.sqrt(s * (s - a) * (s - b) * (s - c))
    return 0

# Input values for a and b
a = int(input())
b = int(input())

# Calculate areas for both cases where c = a and c = b
area_c_a = calculate_area(a, b, a)
area_c_b = calculate_area(a, b, b)

# Determine the value of c that gives the largest area
if area_c_a >= area_c_b:
    c = a
else:
    c = b

# Output the result
print(c)
