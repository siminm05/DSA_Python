'''
day 7 - patterns pt.3
'''

import math

num = 7
half = math.floor(num/2)

star = 1
space = math.floor(num/2)

for i in range(0,half):
    for j in range(0,space):
        print(" ",end=" ")
    for k in range(0,star):
        print("*",end=" ")
    space -=1
    star +=2
    print()

star = num
space = 0
for i in range(half,num):
    for j in range(0,space):
        print(" ",end=" ")
    for k in range(0,star):
        print("*",end=" ")
    star -= 2
    space += 1
    print()


num = 5
for i in range(0,num):
    for j in range(0,num):
        if i == 0 or i == num-1:
            print("*",end=" ")
        elif j == 0 or j == num-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


num = 5
for i in range(0,num):
    for j in range(0,num):
        if j == 0:
            print("*",end=" ")
        elif i == num-1:
            print("*",end=" ")
        elif i == j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
