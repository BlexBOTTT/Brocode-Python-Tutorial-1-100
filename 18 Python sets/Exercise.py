# https://pynative.com/python-set-exercise-with-solutions/

def exercise1():
        # Exercise 1: Add a list of elements to a set
        # Given a Python list, Write a program to add all its elements into a given set.
        # Given:
        sample_set = {"Yellow", "Orange", "Black"}
        sample_list = ["Blue", "Green", "Red"]

        sample_set.update(sample_list)

        # Note: Set is unordered.
        # Expected output: {'Green', 'Yellow', 'Black', 'Orange', 'Red', 'Blue'}
        print(sample_set)

def exercise2():
    # Exercise 2: Return a new set of identical items from two sets
    # Given:
    set1 = {10, 20, 30, 40, 50}
    set2 = {30, 40, 50, 60, 70}

    new_set = set1.intersection(set2)

    # Expected output: {40, 50, 30}
    print(new_set)
    # Alternate: print(set1.intersection(set2))

def exercise3():
    # Exercise 3: Get Only unique items from two sets
    # Write a Python program to return a new set with
    # unique items from both sets by removing duplicates.
    # Given:
    set1 = {10, 20, 30, 40, 50}
    set2 = {30, 40, 50, 60, 70}

    # Expected output: {70, 40, 10, 50, 20, 60, 30}
    print(set1.union(set2))

def exercise4():
    # Exercise 4: Update the first set with items that don’t exist in the second set
    # Given two Python sets, write a Python program to update the first set with
    # items that exist only in the first set and not in the second set.
    # Given:

    set1 = {10, 20, 30}
    set2 = {20, 40, 50}

    new_set = set1.difference(set2)

    print(new_set)
    # Expected output: set1 {10, 30}

def exercise5():
    # Exercise 5: Remove items from the set at once
    # Write a Python program to remove items 10, 20, 30 from the following set at once.
    # Given:
    set1 = {10, 20, 30, 40, 50}

    set1.difference_update({10, 20, 30})

    # Expected output: {40, 50}
    print(set1)

def exercise6():
    # Exercise 6: Return a set of elements present in Set A or B, but not both
    # Given:
    set1 = {10, 20, 30, 40, 50}
    set2 = {30, 40, 50, 60, 70}

    set1.symmetric_difference(set2)

    # Expected output: {20, 70, 10, 60}
    print(set1)

def exercise7():
    # Exercise 7: Check if two sets have any elements in common.
    # If yes, display the common elements
    set1 = {10, 20, 30, 40, 50}
    set2 = {60, 70, 80, 90, 10}

    # Expected output:
    if set1.isdisjoint(set2):
        # Two sets have items in common
        print("Two sets have no items in common")
    else:
        print("Two sets have items in common")
        print(set1.intersection(set2))

def exercise8():
    # Exercise 8: Update set1 by adding items from set2, except common items
    # Given:
    set1 = {10, 20, 30, 40, 50}
    set2 = {30, 40, 50, 60, 70}

    set1.symmetric_difference_update(set2)

    # Expected output: {70, 10, 20, 60}
    print(set1)

def exercise9():
    # Exercise 9: Remove items from set1 that are not common to both set1 and set2
    # Given:
    set1 = {10, 20, 30, 40, 50}
    set2 = {30, 40, 50, 60, 70}

    set1.intersection_update(set2)
    # Expected output: {40, 50, 30}
    print(set1)

