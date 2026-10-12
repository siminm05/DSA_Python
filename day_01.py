'''
day 1 - funcs for factorial and fibonacci series (recursive included)
'''

def facto(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    return fact

def fib(n):
    list = [0,1]
    i=0
    while i<n-2:
        sum = list[i] + list[i+1]
        list.append(sum)
        i += 1
    return list

# without using list
def fib_recursive1(last_num, second_Last_num, n, counter):
    print(second_Last_num) # 0 1
    new_num = last_num + second_Last_num # 0 1 = 1
    second_Last_num = last_num
    counter += 1

    if counter < n:
        fib_recursive1(new_num, second_Last_num, n, counter)


# using list
def fib_recursive2(n,list):
    length = len(list)
    new_num = list[length-1]+list[length-2]
    list.append(new_num)

    if length < n-1:
        fib_recursive2(n,list)
    return list


def main():
    list = [0,1]
    n = 5
    print("Factorial of",n, "is:",facto(n))
    print("Fibonacci series of first",n,"numbers is:",fib(n))
    print("\nFibonacci series without using list:")
    print(fib_recursive1(1,0,5,0))
    print("\nFibonacci series using list:",fib_recursive2(n,list))

main()
