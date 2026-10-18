'''
day 2 HW - write basic list functions
'''
def add_at_end(list1):
    num = input("enter the number u want to add at the end: ")
    list2 = [0] * (len(list1) + 1)
    for i in range(0,len(list1)):
        list2[i] = int(list1[i])
    list2[len(list1)] = int(num)
    print(list2)

def add_at_index(list1):
    index_add = int(input("enter the index u want to add at: "))
    num = int(input("enter the number u want to add at index: "))

    list2 = [0] * (len(list1) + 1)
    for i in range(0,index_add):
        list2[i] = int(list1[i])
    list2[index_add] = int(num)
    for i in range(index_add+1, len(list2)):
        list2[i] = int(list1[i-1])
    print(list2)

def remove_last_num(list1):
    print(list1[0:len(list1)-1])
    '''list2 = [0] * (len(list1)-1)
    for i in range(0,len(list1)-1):
        list2[i] = list1[i]
    print(list2)'''

def remove_index(list1):
    index_remove = int(input("enter the index u want to remove: "))

    for i in range(index_remove, len(list1)-1):
            list1[i] = list1[i+1]
    print(list1[0:len(list1)-1])

    '''list2 = [0] * (len(list1)-1)
    for i in range(0,len(list1)):
        if i<index:
            list2[i] = list1[i]
        elif i == index:
            continue
        elif i > index:
            list2[i-1] = list1[i]
            
    print(list2)'''

def update_num(list1):
    update_index = int(input("enter the index u want to update: "))
    num = input("enter the number: ")

    for i in range(update_index, update_index+1):
            list1[i] = int(num)
            break
    print(list1)
    '''list2 = [0] * (len(list1))
    for i in range(0,len(list1)):
        if i == update_index:
            list2[i] = num
            continue
        list2[i] = list1[i]
    print(list2)'''

def main():
    list1 = [0,1,2,3,4]

    add_at_end(list1)
    add_at_index(list1)
    remove_last_num(list1)
    remove_index(list1)
    update_num(list1)

main()
