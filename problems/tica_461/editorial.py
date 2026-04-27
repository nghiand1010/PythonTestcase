# -*- coding: utf-8 -*-
"""
Editorial Solution for tica_461
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


def solve(x): 

	ans, temp = 0, x 
	
	# Base Case 
	if (x < 10): 
		return x 

	# Calculating the last digit 
	last = x % 10

	# Calculating the first digit 
	while (x):
		first = x % 10
		x = x // 10

	if (first <= last):
		ans = 9 + temp // 10
	else:
		ans = 8 + temp // 10

	return ans

# Driver Code
L, R = map(int, input().split(" "))


print(solve(R) - solve(L - 1))
