'''
day 12 - sort and merge list (practice) with pointers
'''

def min(list):
    min = list[0]
    if len(list) == 0:
        return -1
    elif len(list) > 0:
        for i in range (1, len(list)):
            if list[i] < min:
                min = list[i]
    return min

#gets 2 unsorted lists -> finds the min value from each list -> adds it into a new list
def using_min(list1, list2):
    sorted = []
    while len(list1) > 0 and len(list2) > 0:
        a = min(list1)
        b = min(list2)
        if a <= b or a == -1:
            sorted.append(a)
            list1.remove(a)
        else:
            sorted.append(b)
            list2.remove(b)

    print("Unsorted Lists Merge:", sorted)

#gets 2 sorted lists -> compares the first value of both lists with each other -> add the min value into a new list
#-> updates the pointer accordingly
def merge(list1, list2):
    merge = []
    i, j = 0, 0
    while i < len(list1) or j < len(list2):
        if i == len(list1):
            merge.append(list2[j])
            j += 1
        elif j == len(list2):
            merge.append(list1[i])
            i += 1
        elif list1[i] <= list2[j]:
            merge.append(list1[i])
            i += 1
        else:
            merge.append(list2[j])
            j += 1
    print("Sorted List Merge: ", merge)


def main():
    list1 = [4, 62, 7, 3, 91]
    list2 = [56, 0, 72, 3, 100]
    using_min(list1, list2)

    list1 = [3, 4, 7, 62, 91]
    list2 = [0, 3, 56, 70, 100, 111, 456, 234, 678]
    merge(list1, list2)

main()
