import os
import random
import sys
import zipfile
from shutil import rmtree
import shutil


filename = "daura"


rmtree(f'{filename}')
try:
    os.mkdir(f'{filename}')
    os.remove(f'{filename}' + '.zip')
except OSError:
    pass


# tên file




import random

def sinh_mang_ngau_nhien(n, a, b):
    return [random.randint(a, b) for _ in range (n)]

input = [[9],[6],[3],[888888],[111111119],[1369]]
output =[]# [['YES'], ['YES'], ['NO'], ['NO'], ['YES'], ['YES']]
num=3
# lenval=min(len(tmpa),150)
# for x in range(lenval):
#     if x%num==0:
#         a.append(tmpa[x])
#     elif x%num==2:
#         b.append(tmpa[x])
tf = len(input)
# a = [[111],]
# b=[[2],[3],[1],[8],[5]]
for val in input:
    n=val[0]
    k = n * (n + 1) / 2 - n + 1
    a = "TINHOCTRE"
    if k % 9 == 0:
        output.append(["E"])
    else:
        m = k % 9
        output.append([a[int(m - 1)]])
    # output.append([n])

for i in range(1, tf + 1):
    sys.stdout = open(f'{filename}/input{i}.in', 'w', encoding="utf-8")
    k = len(input[i-1])
    for j in range(k):
        sys.stdout.write(str(input[i - 1][j]) + "\n")
    k = len(output[i-1])
    sys.stdout = open(f'{filename}/output{i}.out', 'w', encoding="utf-8")
    for j in range(k):
        num=output[i - 1][j]
        # if isinstance(num, int):
        #     num = '{:.2f}'.format(num)
        if j<k-1:
            sys.stdout.write(str(num) + "\n")
        else:
            sys.stdout.write(str(num))


#
# print test case(s) to input.txt
#

sys.stdout.close()
shutil.make_archive(f'{filename}', 'zip',f'{filename}')
