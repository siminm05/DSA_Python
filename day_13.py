'''
day 13 - practice with list - level 1
'''

#q1. find the longest continuous common string
#list = ["flower", "flow", "flight"]
list = ["flower", "fruit", "fair"]
#list = ["flower", "flow", "vegetable"]

string = ""
i = list[0]
for j in i: #f l o w e r
    present = False
    for k in range(1, len(list)): #fruit, flight, ...
        if j in list[k]:
            present = True
        else:
            present = False
            break

    if present:
        string += j
    else:
        break

print("Q1 - Continuous String:",string)


#q2. remove duplicates from a sorted list
list = [3,3,4]
#output = [3,4,-1]
#num of elements = k = 2
j = len(list)-1
i = 0
while list[i] != -1 and i < len(list)-1:
    if list[i] == list[i+1]:
        for k in range(i+1, j):
            list[k] = list[k+1]
        list[j] = -1
        j -= 1
        continue
    else:
        i += 1

print("Q2 - No Duplicate",list)
