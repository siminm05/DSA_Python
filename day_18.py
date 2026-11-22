'''
day 18 - Insertion sort code & q1. decimal to binary
'''
list = [12, 11, 13, 5, 6]
list = [10,9,8,7,6,5,4,3,2,1]
list = [3,56,2,45,7,0,6,8,8]
list = [8,8,8,1,8,8,7]
#list = [1,2,3,4,5,6,7,8,9,10]
#list = [1,2,3,4,6,5,7,8,9]
'''#insertion sort
[11, 12, 13, 5, 6]
[11, 12, 13, 5, 6]

[5, 11, 12, 13, 6]
[5, 6, 11, 12, 13]'''

for i in range(1, len(list)):
    count = 0
    for j in range (i-1, -1, -1):
        if list[i] < list[j]:
            count += 1
        else:
            break

    if count > 0:
        temp = list[i]
        for k in range(i, i-count, -1):
            list[k] = list[k-1]
        list[i-count] = temp
        temp = list[i]
        k = i
        while k > i -count:
            list[k] = list[k-1]
            k-=1
        list[i-count] = temp
print(list)

#q1. Convert decimal number to binary
num = 8
binary = 8
ans = ""
while binary >= 1:
    if num >= binary:
        num = num - binary
        ans = ans + "1"
    else:
        ans = ans + "0"
    binary = binary/2
print(ans)
