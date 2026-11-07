'''
day 11 - binary search (with and without recursion)
'''

def bubble_sort(list):
    length = len(list)
    j = 0
    if length != 0:
        while j != length - 1:
            #print(j+1, "pass")
            for i in range(1, length):
                if list[i-1] > list[i]:
                    temp = list[i-1]
                    list[i-1]= list[i]
                    list[i] = temp
                #print(list)
            #print()
            j += 1

        print(list)
        return list

def binary_rec(sorted_list, start, end, target):
    #found = False
    if start <= end:
        middle_index = (start + end) // 2
        if target == sorted_list[middle_index]:
            return middle_index
        elif target < sorted_list[middle_index]:
            end = middle_index - 1
            return binary_rec(sorted_list, start, end, target)
        else:
            start = middle_index + 1
            return binary_rec(sorted_list, start, end, target)



def binary_search(list, start, end, target):
    middle = 0
    found = False

    while found == False and start <= end:
        middle = (start + end) //2
        if list[middle] == target:
            found = True
        else:
            if list[middle] < target:
                start = middle + 1
            else:
                end = middle - 1
            continue

    print (middle+1)


def main():
    list = [-5, 3, -1, 0, 8, -2, 7, 10,43,56,78,90,21,34,35,36,67, 5]
    sorted_list = bubble_sort(list)
    target = 10
    print(binary_search(sorted_list,0, len(sorted_list)-1, target))
    print(binary_rec(sorted_list,0, len(sorted_list)-1, target))


main()
