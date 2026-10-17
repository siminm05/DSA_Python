'''
day 2 HW - write basic list functions
'''
def add_at_end(list1, num):
    list2 = [0] * (len(list1) + 1)
    for i in range(0,len(list1)):
        list2[i] = int(list1[i])
    list2[len(list1)] = int(num)
    return list2

def add_at_index(list1, index_add, num):
    list2 = [0] * (len(list1) + 1)
    for i in range(0,index_add):
        list2[i] = int(list1[i])
    list2[index_add] = int(num)
    for i in range(index_add+1, len(list2)):
        list2[i] = int(list1[i-1])
    print(list2)

def remove_last_num(list1):
    list2 = [0] * (len(list1)-1)
    for i in range(0,len(list1)-1):
        list2[i] = list1[i]
    print(list2)

def remove_index(list1, index):
    list2 = [0] * (len(list1)-1)
    for i in range(0,len(list1)):
        if i<index:
            list2[i] = list1[i]
        elif i == index:
            continue
        elif i > index:
            list2[i-1] = list1[i]

    print(list2)

def update_num(list1, update_index, num):
    list2 = [0] * (len(list1))
    for i in range(0,len(list1)):
        if i == update_index:
            list2[i] = num
            continue
        list2[i] = list1[i]
    print(list2)

def main():
    list1 = [0,1,2,3,4]
    num1 = input("enter the number u want to add at the end: ")
    print(add_at_end(list1, num1))

    index_add = int(input("enter the index: "))
    num2 = int(input("enter the number u want to add at index: "))
    print(add_at_index(list1, index_add, num2))

    remove_last_num(list1)

    index_remove = int(input("enter the index u want to remove: "))
    print(remove_index(list1, index_remove))

    update_index = int(input("enter the index u want to update: "))
    num3 = input("enter the number: ")
    print(update_num(list1, update_index, num3))

main()



