'''
day 4 - even/odd and prime/composite and min max in list
'''
import math

#q1. find if the num is even/odd and prime/composite
num = 2
prime = True

if num % 2 == 0:
    print(num, "is even")
else:
    print(num, "is odd")


for i in range (2,math.ceil(num/2)):
    if num % i == 0:
        print(num, "is composite")
        prime = False
        break
if prime == True:
    print(num, "is prime")


#q2. find if the elements in the list are even_l/odd and prime_l/composite
list = [1,2,3,6,7,9,11]
for i in range(len(list)):
    prime_l = True
    half_l = 0
    if list[i] % 2 == 0:
        print(list[i], "is even")
    else:
        print(list[i], "is odd")

    for j in range(2,math.ceil(i/2)):
        if list[i] % j == 0:
            print(list[i], "is composite\n")
            prime_l = False
            break
    if prime_l:
        print(list[i],"is prime\n")

#q3. find min and max in a list
list = [5,4,6,2,7]
max = list[0]
min = list[0]
for i in range(1,len(list)):
    if list[i] > max:
        max = list[i]
    elif list[i] < min:
        min = list[i]

print(min, max)
