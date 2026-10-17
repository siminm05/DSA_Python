'''
day 3 - matrix (row and col sum) and search element in list
'''

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
'''
00 01 02
10 11 12
20 21 22
'''

#q1. print sum of each row and col of the matrix
length = len(matrix)
sum_row, sum_col = 0, 0
j, counter = 0, 0

for i in range(0,3):
    for j in range(0,3):
        sum_row += matrix[i][j] #row
        sum_col += matrix[j][i] #col
        counter += 1
    print("Row", counter, "=", sum_row)
    print("Col",counter, "=",sum_col)
    sum_row, sum_col = 0, 0

#q2. search element in a list. if found, print the index else print not found
list = [6,4,8,3,1]
el = 5
found = False
for i in range(len(list)):
    if list[i] == el:
        print("Found", el, "at index", i)
        found = True
        break

if found == False:
    print("not found")
