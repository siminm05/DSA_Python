'''
day 9 - patterns pt.1 (level 1)
'''

num = 5
space = num-1
count = 0

for i in range(0,num):
    for j in range(0, space):
        print(" ", end = " ")
    for k in range(0, count+1):
        print(chr(k+65), end = " ")
    for l in range(count, 0, -1):
        print(chr(l+64), end = " ")
    count += 1
    space -= 1
    print()

print("---------------")

num = int(input("Enter a num: "))
space = 0
count = num

for i in range(0, num):
    for j in range(0, space):
        print(" ", end = " ")
    for k in range(0, count):
        print(chr(k+65), end = " ")
    for l in range(count-1, 0, -1):
        print(chr(l+64), end = " ")
    count -= 1
    space += 1
    print()

print("---------------")
