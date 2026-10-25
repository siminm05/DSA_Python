'''
day 7 HW - patterns (level 0 complete)
'''

for i in range(5):
    for j in range(i+1):
        print(chr(65+j), end=" ")
    print()

print("--------------")

for i in range(5):
    for j in range(5-i):
        print(chr(65+j), end=" ")
    print()

print("--------------")

num = int(input("Enter a number: "))
for i in range(5):
    for j in range(i+1):
        print(num, end=" ")
        num += 1
    print()

print("--------------")

for i in range(5):
    for j in range(5):
        if i == 0 or i == 4:
            print(j+1, end=" ")
        elif j ==0 or j == 4:
            print(j+1, end=" ")
        else:
            print(" ", end=" ")
    print()
