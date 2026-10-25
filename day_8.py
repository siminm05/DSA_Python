'''
day 8 - patterns - level 1
'''

import math
num = 9
half = math.floor(num/2)
start_space = math.floor(num/2)
center_space = -1

for i in range(0,num):
    for j in range(0, start_space):
        print(" ", end=" ")
    print("*", end=" ")
    for k in range(0, center_space):
        print(" ", end=" ")
    if center_space > 0:
        print("*", end=" ")
    if i < half:
        start_space -= 1
        center_space += 2
    else:
        start_space += 1
        center_space -= 2
    print()

print("__________________")

count = 5
space = 0
for i in range(0,5):
    for j in range(0,space):
        print(" ", end=" ")
    for k in range(1,count+1):
        print(k, end=" ")
    for l in range(count-1,0,-1):
        print(l, end=" ")
    space += 1
    count -= 1
    print()

print("__________________")

def prt_star(star):
    for j in range(0,star):
        print("*", end=" ")

def main():
    num = int(input("Enter a +ve num: "))
    space = num
    star = 0
    for i in range(0,num):
        if i < num/2:
            star += 1
            space -= 2
            prt_star(star)
            for k in range(0, space):
                print(" ", end=" ")
            prt_star(star)
            print()
        else:
            prt_star(star)
            for k in range(0, space):
                print(" ", end=" ")
            prt_star(star)
            print()
            star -= 1
            space += 2

main()
