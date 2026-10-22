'''
day 6 - patterns pt.2
'''

import math
#simplify it
row = 6
col = 11
for i in range(0,row):
    count = 0
    for j in range(0,col):
        if i+j == math.floor(col/2):
            print("*", end= " ")
            while count != (i*2):
                print("*", end= " ")
                count += 1
        else:
            print(" ", end= " ")
    print()

print()

for i in range(0,5):
    for j in range(0,9):
        if i+j <= 8 and i<=j:
            print("*", end= " ")
        else:
            print(" ", end= " ")
    print()
