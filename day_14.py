'''
day 14 - pratice questions with list - level 1 
'''

#q1. subarray with sum = k
list = [1,1,1,1,4,4,2,3,2,1]
k = 8
# [1,1]
print("Q1 -")
for i in range(0, len(list)):
    ans = []
    sum = 0
    for j in range(i, len(list)):
        sum += list[j]
        if sum <= k:
            ans.append(list[j])
        else:
            break
        if sum == k:
            print(ans)

#q2. longest unique sequence
string = "abcd aaaaaabcdefghijklmnopqrstuvwxyz"
ans = ""
longest_ans = ""

for i in range(0, len(string)):
    ans = ""
    for j in range(i, len(string)):
        if string[j] not in ans:
            ans += string[j]
        else:
            break
    if len(ans) > len(longest_ans):
        longest_ans = ans
print("\nQ2 - Longest Sequence:", longest_ans)

#q3. find the second largest number from a list
list = [2,5,8,3,5,0,9,1,11,6,10]
largest = list[0]
for i in range(0, len(list)):
    if list[i] >= largest:
        largest = list[i]

second_largest = list[0]
for j in range(0, len(list)):
    if list[j] < largest and list[j] > second_largest:
        second_largest = list[j]
print("\nQ3 - Second Largest Number:", second_largest)
