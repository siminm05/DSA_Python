'''
day 2 - list, tuple, set and dictionary
'''

#q1. create a list of tuples containing a number and its square
nums = [(2,4), (3,9), (4,16)]
# print each tuple
for i in nums:
    print(i)
# print which value in the tuple
for i in nums:
    for j in i:
        print(j)

#q2. try adding a value in a tuple
tuple = (1,2)
#tuple.append(3)
print(tuple)

# u can't add, remove or update a tuple as they r immutable

#q3. create a list of dictionaries
students = [
    {"name" : "alex", "roll_number" : 1, "percentage" : 80},
    {"name" : "john", "roll_number" : 2, "percentage" : 80},
    {"name" : "felix", "roll_number" : 3, "percentage" : 80},
    {"name" : "simin", "roll_number" : 4, "percentage" : 70},
    {"name" : "derya", "roll_number" : 5, "percentage" : 80}
]

# print each student's name
for i in students:
    print(i["name"])
    #print(students[i]["name"])

#q4. create a set with duplicates values and print the set
set = {1,2,3,3}
print(set)

#q5. use cases of sets
A = {1,2,3,4}
B = {2,3,4}

print(A.union(B))
print(A.intersection(B))
print(A.difference(B))
print(B.difference(A))

#q6. create a tuple with a single value
tuple = (5,)

'''
a "," is added because "()" is used for other operations (eg. mathematical) and is not just defined for tuples
'''
