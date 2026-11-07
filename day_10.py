'''
day 10 - bubble sort
'''

def bubble_sort(list):
    length = len(list)
    j = 0
    if length != 0:
        while j != length - 1:
            print(j+1, "pass")
            for i in range(1, length):
                if list[i-1] > list[i]:
                    temp = list[i-1]
                    list[i-1]= list[i]
                    list[i] = temp
                print(list)
            print()
            j += 1

        print(list)



def main():
    list1 = [5, 4, 3, 2, 1, 0]
    list2 = [1, 2, 3, 4, 5]
    list3 = [10, 2, 9, 1, 8, 3, 7, 4, 6, 5]
    list4 = [7, 7, 7, 7, 7]
    list5 = [42]
    list6 = [2, 1]
    list7 = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    list8 = [-5, 3, -1, 0, 8, -2, 7]
    list9 = []
    list10 = [3.14, 2.71, 1.41, 0.57, 2.23]
    list11 = [1, 2, 3, 5, 4, 6, 7, 8, 9, 10]
    bubble_sort(list11)

main()
