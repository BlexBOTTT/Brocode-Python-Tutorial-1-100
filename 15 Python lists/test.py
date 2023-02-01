# https://pynative.com/python-list-exercise-with-solutions/

def exercise_1():
    # Exercise 1: Reverse a list in Python
    # Given:
    list1 = [100, 200, 300, 400, 500]
    list1.reverse()
    # Expected output: [500, 400, 300, 200, 100]
    print(list1)


def exercise_2():
    # Exercise 2: Concatenate two lists index-wise
    # Write a program to add two lists index-wise.
    # Create a new list that contains the 0th index item from both the list,
    # then the 1st index item, and so on till the last element.
    # any leftover items will get added at the end of the new list.
    # Given:
    list1 = ["M", "na", "i", "Ke"]
    list2 = ["y", "me", "s", "lly"]
    # note: I don't know what the hell is this
    zipped_list = [i + j for i, j in zip(list1, list2)]
    # Expected output: ['My', 'name', 'is', 'Kelly']
    print(zipped_list)


def exercise_3():
    # Exercise 3: Turn every item of a list into its square
    # Given a list of numbers. write a program to turn every item of a list into its square.
    # Given:
    numbers = [1, 2, 3, 4, 5, 6, 7]
    for i in numbers:
        # Expected output: [1, 4, 9, 16, 25, 36, 49]
        print(pow(i, 2), end=" ")


def exercise_4():
    # Exercise 4: Concatenate two lists in the following order
    # Given:
    list1 = ["Hello ", "take "]
    list2 = ["Dear", "Sir"]
    new_list = [i + j for i in list1 for j in list2]
    # Expected output: ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']
    print(new_list)


def exercise_5():
    # Exercise 5: Iterate both lists simultaneously
    # Given a two Python list. Write a program to iterate both lists simultaneously
    # and display items from list1 in original order and items from list2 in reverse order.
    # Given:
    list1 = [10, 20, 30, 40]
    list2 = [100, 200, 300, 400]
    for i, j in zip(list1, list2[::-1]):
        # Expected output:
        # 10 400
        # 20 300
        # 30 200
        # 40 100
        print(i, j)


def exercise_6():
    # Exercise 6: Remove empty strings from the list of strings
    # Given:
    list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
    new_list = list(filter(None, list1))
    # Expected output: ["Mike", "Emma", "Kelly", "Brad"]
    print(new_list)


def exercise_7():
    # Exercise 7: Add new item to list after a specified item
    # Write a program to add item 7000 after 6000 in the following Python List
    # Given:
    list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

    # understand indexing
    # list1[0] = 10
    # list1[1] = 20
    # list1[2] = [300, 400, [5000, 6000], 500]
    # list1[2][2] = [5000, 6000]
    # list1[2][2][1] = 6000

    list1[2][2].append(7000)

    # Expected output: [10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]
    print(list1)


def exercise_8():
    # Exercise 8: Extend nested list by adding the sublist
    # You have given a nested list. Write a program to extend it by adding the sublist ["h", "i", "j"] in such a way that it will look like the following list.
    # Given:
    list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
    # sub list to add
    sub_list = ["h", "i", "j"]

    # understand indexing
    # list1[2] = ['c', ['d', 'e', ['f', 'g'], 'k'], 'l']
    # list1[2][1] = ['d', 'e', ['f', 'g'], 'k']
    # list1[2][1][2] = ['f', 'g']

    list1[2][1][2].extend(sub_list)

    # Expected Output: ['a', 'b', ['c', ['d', 'e', ['f', 'g', 'h', 'i', 'j'], 'k'], 'l'], 'm', 'n']
    print(list1)

def exercise_9():
    # Exercise 9: Replace list’s item with new value if found
    # You have given a Python list. Write a program to find value 20 in the list,
    # and if it is present, replace it with 200. Only update the first occurrence of an item.
    # Given:
    list1 = [5, 10, 15, 20, 25, 50, 20]

    first_index = list1.index(20)

    list1[first_index] = 200

    # Expected output: [5, 10, 15, 200, 25, 50, 20]
    print(list1)

def exercise_10():
    # Exercise 10: Remove all occurrences of a specific item from a list.
    # Given a Python list, write a program to remove all occurrences of item 20.
    # Given:
    list1 = [5, 20, 15, 20, 25, 50, 20]

    while 20 in list1:
        list1.remove(20)
    # Expected output: [5, 15, 25, 50]
    print(list1)

exercise_10()
