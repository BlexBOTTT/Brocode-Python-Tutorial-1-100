# https://pynative.com/python-dictionary-exercise-with-solutions/

def exercise1():
    # Exercise 1: Convert two lists into a dictionary
    # Below are the two lists. Write a Python program to convert them into a dictionary in a way that item from list1 is the key and item from list2 is the value
    # Given:
    keys = ['Ten', 'Twenty', 'Thirty']
    values = [10, 20, 30]

    new_dict = dict(zip(keys, values))

    # Expected output: {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
    print(new_dict)

    # Alternate Solution
    # res_dict = dict()
    #
    # for i in range(len(keys)):
    #     res_dict.update({keys[i]: values[i]})
    # print(res_dict)

def exercise2():
    # Exercise 2: Merge two Python dictionaries into one
    dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
    dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

    dict1.update(dict2)

    #Expected output: {'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
    print(dict1)

def exercise3():
    # Exercise 3: Print the value of key ‘history’ from the below dict
    sampleDict = {
        "class": {
            "student": {
                "name": "Mike",
                "marks": {
                    "physics": 70,
                    "history": 80
                }
            }
        }
    }
    # Expected output: 80
    print(sampleDict["class"]["student"]["marks"]["history"])

def exercise4():
    # Exercise 4: Initialize dictionary with default values
    # In Python, we can initialize the keys with the same values.
    # Given:
    employees = ['Kelly', 'Emma']
    defaults = {"designation": 'Developer', "salary": 8000}

    newdict = dict.fromkeys(employees, defaults)

    # Expected output:
    # {'Kelly': {'designation': 'Developer', 'salary': 8000},
    # 'Emma': {'designation': 'Developer', 'salary': 8000}}
    print(newdict)

def exercise5():
    # Exercise 5: Create a dictionary by extracting the keys from a given dictionary
    # Write a Python program to create a new dictionary by extracting the mentioned
    # keys from the below dictionary.
    # Given dictionary:
    sample_dict = {
        "name": "Kelly",
        "age": 25,
        "salary": 8000,
        "city": "New york"}

    keys = ["name", "salary"]

    new_dict = {k: sample_dict[k] for k in keys}
    print(new_dict)

    # alternate solution:
    # sampleDict = {
    #   "name": "Kelly",
    #   "age":25,
    #   "salary": 8000,
    #   "city": "New york" }
    #
    # keys = ["name", "salary"]
    #
    # newDict = {k: sampleDict[k] for k in keys}
    # print(newDict)

def exercise6():
    # Exercise 6: Delete a list of keys from a dictionary
    # Given:
    sample_dict = {
         "name": "Kelly",
         "age": 25,
         "salary": 8000,
         "city": "New york"
     }

    # Keys to remove
    keys = ["name", "salary"]

    for k in keys:
        sample_dict.pop(k)
    # Expected output: {'city': 'New york', 'age': 25}
    print(sample_dict)

def exercise7():
    # We know how to check if the key exists in a dictionary.
    # Sometimes it is required to check if the given value is present.
    # Write a Python program to check if value 200 exists in the following dictionary.
    # Given:
    sample_dict = {'a': 100, 'b': 200, 'c': 300}

    if 200 in sample_dict.values():
        print("200 present in a dict")
    #Expected output: 200 present in a dict

def exercise8():
    # Exercise 8: Rename key of a dictionary
    # Write a program to rename a key city to a location in the following dictionary.
    # Given:
     sample_dict = {
       "name": "Kelly",
       "age":25,
       "salary": 8000,
       "city": "New york"
     }

     sample_dict["location"] = sample_dict.pop("city")

    # Expected output: {'name': 'Kelly', 'age': 25, 'salary': 8000, 'location': 'New york'}
     print(sample_dict)

def exercise9():
    # Exercise 9: Get the key of a minimum value from the following dictionary
     sample_dict = {
       'Physics': 82,
       'Math': 65,
       'history': 75
     }
     # Expected output: Math
     print(min(sample_dict))

def exercise10():
    # Exercise 10: Change value of a key in a nested dictionary
    # Write a Python program to change Brad’s salary to 8500 in the following dictionary.
    # Given:
     sample_dict = {
         'emp1': {'name': 'Jhon', 'salary': 7500},
         'emp2': {'name': 'Emma', 'salary': 8000},
         'emp3': {'name': 'Brad', 'salary': 500}
     }

     sample_dict['emp3']["salary"] = 8500

     print(sample_dict)

exercise10()
