# -*- coding: utf-8 -*-
"""
Editorial Solution for tica_t7_27_07
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


a = int(input())
b = int(input())

s1 = str(a)
s2 = str(b)
# m lưu giá trị bé
# n lưu giá trị lớn
if len(s1) > len(s2):
    # duyệt theo xâu s2
    ischeck = False
    for i in range(len(s2)):
        if s1[i] < s2[i]:
            m = a
            n = b
            ischeck = True
            break
        elif s1[i] > s2[i]:
            m = b
            n = a
            ischeck = True
            break
    if ischeck == False:
        m = b
        n = a
   
else:
    # duyệt theo xâu s1
    ischeck = False 
    for i in range(len(s1)):
        if s1[i] < s2[i]:
            m = a
            n = b
            ischeck = True
            break
        elif s1[i] > s2[i]:
            m = b
            n = a
            ischeck = True
            break
        
    if ischeck == False:
        m = a
        n = b
        
if a == b:
    m = a
    n  = b


# ghép số
x = 0
y = 0
tmp = ""

numbers = []

for x in range(1, 10): 
       
  for y in range(1, 10):
      
      minNumber = ""
      
      minNumber += x * str(m)
      minNumber += y * str(n)
          
      if int(minNumber) % 9 == 0:
         numbers.append(int(minNumber))
         
print(min(numbers))
