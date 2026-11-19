'''
day 15 - selection sort and q. find values with highest frequence in a list
list = [64, 25, 12, 22, 11]

[11, 25, 12, 22, 64]
[11, 12, 25, 22, 64]
[11, 12, 22, 25, 64]
[11, 12, 22, 25, 64]
[11, 12, 22, 25, 64]
'''
#selection sort
def find_min(list, swap):
    min = list[swap]
    for i in range(swap, len(list)):
        if list[i] <= min:
            min = list[i]
            index = i
    return index

def main():
    list = [64, 25, 12, 22, 11, 0, 3, 100, 1, 55]
    swap = 0
    for i in range(len(list)):
        index = find_min(list, swap)
        temp = list[swap]
        list[swap] = list[index]
        list[index] = temp
        swap += 1
        print(list)

main()

#q1. find values with the highest frequence
list = [1,3,2,3,2,3,3,4,5,4,5,4,5,5]
final_count = 0
ans = []
for i in range(len(list)):
    count = 0
    if list[i] not in ans:
        for j in range(0, len(list)):
            if list[j] == list[i]:
                count += 1
        if final_count < count:
            ans = []
            final_count = count
            ans.append(list[i])
        elif final_count == count:
            ans.append(list[i])
print(ans)
