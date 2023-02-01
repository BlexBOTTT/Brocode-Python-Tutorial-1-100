# https://www.youtube.com/watch?v=k8SXsT5TLxQ&t=64s

exercise = eval(input("Exercise number: "))

# Exercise 1: Half triangle
# 1
# 12
# 123
# 1234
# 12345
if exercise == 1:

    for i in range(5):
        for j in range(i + 1):
            print(j + 1, end="")
        print()

# Exercise 1: Half triangle reversed
# 12345
# 1234
# 123
# 12
# 1
if exercise == 2:

    for i in range(5):
        for j in range(5 - i):
            print(j + 1, end="")
        print()

# Exercise 3: Square
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
if exercise == 3:

    for i in range(5):
        for j in range(5):
            print(j + 1, end=" ")
        print()

# Exercise 4 NOT NESTED LOOP
# Number occurrence finder in a sample list

if exercise == 4:
    print()

    # variables
    occurrence = 0
    sample_list = [15, 20, 13, 30, 35, 40, 16, 18, 20, 18, 20, 18]

    # num searcher
    search_num = eval(input("Enter number for search: "))

    print("Sample list below:")
    # code iteration specifier
    for i in sample_list:
        # counter
        if i == search_num:
            occurrence = occurrence + 1
        print(i, end=" ")

    # display counter
    print("\n")
    print("Occurrences:", occurrence)

