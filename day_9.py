'''
day 9 - patterns pt.2 (level 1)
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

list = []
num = int(input("Enter a num: "))
for i in range(num):
    row = []
    for j in range(num):
        if j == 0 or i == j:
            row.append(1)
        elif i >= 2 and j <= num-2:
            sum = 0
            sum = list[i-1][j-1] + list[i-1][j]
            row.append(sum)
        else:
            row.append(" ")
    list.append(row)

space = num-1
for i in list:
    for k in range(space):
        print(" ", end= " ")
    for j in i:
        print(j, end = " ")
        print(" ", end= " ")
    print()
    space -= 1
