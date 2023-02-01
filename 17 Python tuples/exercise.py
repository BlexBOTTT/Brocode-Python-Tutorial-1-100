# https://pynative.com/python-tuple-exercise-with-solutions/

# Exercise 1: Reverse the tuple.
# Given: tuple1 = (10, 20, 30, 40, 50)
# Output: (50, 40, 30, 20, 10)

tuple_ex1 = (10, 20, 30, 40, 50)
tuple_ex1 = tuple_ex1[::-1]
print(tuple_ex1)
print()

# Exercise 2: The given tuple is a nested tuple. write a Python program to print the value 20.
# The given tuple is a nested tuple. write a Python program to print the value 20.
# Given: tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))
# Output: 20

tuple_ex2 = ("Orange", [10, 20, 30], (5, 15, 25))

# understand indexing
# tuple1[0] = 'Orange'
# tuple1[1] = [10, 20, 30]
# list1[1][1] = 20

print(tuple_ex2[1][1])
print()

# Exercise 3: Create a tuple with single item 50

tuple_ex3 = (50, )

print(tuple_ex3)
print(type(tuple_ex3))
print()

# Exercise 4: Unpack the tuple into 4 variables
# Write a program to unpack the following tuple into four variables and display each variable.
# Given: tuple1 = (10, 20, 30, 40)
# Output: tuple1 = (10, 20, 30, 40)
#         # Your code
#         print(a) # should print 10
#         print(b) # should print 20
#         print(c) # should print 30
#         print(d) # should print 40

tuple_ex4 = (10, 20, 30, 40)

a_ex4 = tuple_ex4[0]    # or a_ex4, b_ex4, c_ex4, d_ex4 = tuple1
b_ex4 = tuple_ex4[1]
c_ex4 = tuple_ex4[2]
d_ex4 = tuple_ex4[3]

print(a_ex4)
print(b_ex4)
print(c_ex4)
print(d_ex4)
print()

# Exercise 5: Swap two tuples in Python
# Given: tuple1 = (11, 22)
#        tuple2 = (99, 88)
# Output: tuple1: (99, 88)
#         tuple2: (11, 22)

tuple1_ex5 = (11, 22)
tuple2_ex5 = (99, 88)

temp_ex5 = tuple1_ex5
tuple1_ex5 = tuple2_ex5
tuple2_ex5 = temp_ex5

print(tuple1_ex5)   # (99, 88)
print(tuple2_ex5)   # (11, 22)
print()

# Exercise 6: Copy specific elements from one tuple to a new tuple
# Write a program to copy elements 44 and 55 from the following tuple into a new tuple.
# Given: tuple1 = (11, 22, 33, 44, 55, 66)
# Output: tuple2: (44, 55)

tuple1_ex6 = (11, 22, 33, 44, 55, 66)
tuple2_ex6 = tuple1_ex6[3:5]    # or tuple1_ex6[3:-1]
print(tuple2_ex6)
print()

# Exercise 7: Modify the tuple
# Given is a nested tuple.
# Write a program to modify the first item (22) of a list inside a following tuple to 222
# Given: tuple1 = (11, [22, 33], 44, 55)
# Output: tuple1 = (11, [222, 33], 44, 55)

tuple1_ex7 = (11, [22, 33], 44, 55)
tuple1_ex7[1][0] = 222
print(tuple1_ex7)
print()

# INCOMPLETE NO-8
# Exercise 8: Sort a tuple of tuples by 2nd item
# Given: tuple1 = (('a', 23),('b', 37),('c', 11), ('d',29))
# Output: tuple1 = (('c', 11), ('a', 23), ('d', 29), ('b', 37))

tuple1_ex8 = (('a', 23), ('b', 37), ('c', 11), ('d', 29))
# tuple1_ex8 = ??????????????
# tuple1_ex8 = tuple(sorted(list(tuple1_ex8), key=lambda x: x[1]))
print("incomplete")
print(tuple1_ex8)
print()

# Exercise 9: Counts the number of occurrences of item 50 from a tuple
# Given: tuple1 = (50, 10, 60, 70, 50)
# Output: 2
tuple1_ex9 = (50, 10, 60, 70, 50)
print(tuple1_ex9.count(50))
print()


# Exercise 10: Check if all items in the tuple are the same
# Given: tuple1 = (45, 45, 45, 45)
# Output: True


def check(t):
    return all(i == t[0] for i in t)


tuple1_ex10 = (45, 45, 45, 45)

print(check(tuple1_ex10))
print()
