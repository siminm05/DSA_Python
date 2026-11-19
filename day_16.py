'''
day 16 - list questions (interview - easy-med level)

q1. Given two sorted arrays, arr1 and arr2, write a function to
find the union of these two arrays. The union of two arrays is
a list that includes all elements from both arrays.
Since the arrays are sorted, the union should also be sorted.
Duplicates from each array should be preserved in the result.
'''
def union(list1, list2):
    i = 0
    j = 0
    ans = []
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            ans.append(list1[i])
            i+=1
        elif list2[j] < list1[i]:
            ans.append(list2[j])
            j += 1

    while i < len(list1):
        ans.append(list1[i])
        i += 1
    while j < len(list2):
        ans.append(list2[j])
        j += 1

    return ans

def main():
    list1 = [1,2,3,4, 5, 6, 9, 10]
    list2  = [1, 4,5,6,7,8, 14, 16]
    ans = union(list1, list2)
    print("q1. Union of 2 lists with duplicates:",ans)

main()

'''
q2. Given a binary array nums, 
return the maximum number of consecutive 1s in the array.
'''
binary = "0000000"
final_count = 0
for i in range(0, len(binary)):
    count = 0
    if binary[i] == '1':
        for j in range(i, len(binary)):
            if binary[j] == '1':
                count += 1
            else:
                break
    if final_count < count:
        final_count = count
print("q2. Max num of consecutive 1's:",final_count)
