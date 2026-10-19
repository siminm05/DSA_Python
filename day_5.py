'''
day 5 - patterns (interview question)
'''

for i in range(6):
    for j in range(5):
        print(i, j, end=" ", sep="")
    print()

row = int(input("Enter row: ")) 
col = int(input("Enter column: ")) 
for i in range(0,row): 
    for j in range(0,col):
        if i+j <= col-1:
            print("*", end=" ")
    print()

# 1 12 123 1234 12345  
for i in range(5):
    for j in range(5):
        if i >= j:
            print(j+1, end=" ")
    print()
    
#1 22 333 4444 55555
for i in range(5):
    for j in range(5):
        if i >= j:
            print(i+1, end=" ")
    print()
    
#upper right triange - 11111  2222   333    44      5
for i in range(5):
    for j in range(5):
        if j >= i:
            print(i+1, end=" ")
        else:
            print(" ", end=" ")
    print()

#upper right triangle - 12345 1234 123 12 1
for i in range(5):
    for j in range(5):
        if j >= i:
            print(j+1, end=" ")
        else:
            print(" ", end=" ")
    print()

# upper left triangle
for i in range(5):
    for j in range(5):
        if i+j <= 4:
            print("*", end=" ")
    print()

#upper right
for i in range(5):
    for j in range(5):
        if j >= i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

#lower left
for i in range(5):
    for j in range(5):
        if i>=j:
            print("*", end=" ")
    print()

#lower right
for i in range(5):
    for j in range(5):
        if i+j >= 4:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
