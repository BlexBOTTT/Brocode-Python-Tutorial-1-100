# https://pynative.com/python-input-and-output-exercise/


exercise = int(input("What exercise 1-10?: "))


# Exercise 1: Accept numbers from a user
# Write a program to accept two numbers from the user and calculate multiplication

if exercise == 1:

    input1_ex1 = int(input("Enter 1st: "))
    input2_ex1 = int(input("Enter 2nd: "))

    product_ex1 = input1_ex1 * input2_ex1
    print("The product:", product_ex1)


# Exercise 2: Display three string “Name”, “Is”, “James” as “Name**Is**James”
# Use the print() function to format the given words in the mentioned format. Display the ** separator between each string.
# For example: print('Name', 'Is', 'James') will display Name**Is**James

if exercise == 2:

    print('Name', 'Is', 'James', sep="**")

# Exercise 3: Convert Decimal number to octal using print() output formatting
# Given: num = 8
# Output: The octal number of decimal number 8 is 10

if exercise == 3:

    num_ex3 = 8
    print("%o" % num_ex3)

# Exercise 4: Display float number with 2 decimal places using print()
# Given: num = 458.541315
# Output: 458.54

if exercise == 4:

    num_ex4 = 458.541315
    print("%.2f" % num_ex4)

# Exercise 5: Accept a list of 5 float numbers as an input from the user
# Output: [78.6, 78.6, 85.3, 1.2, 3.5]

if exercise == 5:

    numbers_ex5 = []

    # 5 is the list size
    # run loop 5 times
    for i in range(1,5+1):
        print("Enter float number:", i, ":")
        # accept float number from user
        item = float(input("Answer: "))
        # add it to the list
        numbers_ex5.append(item)

    print("The float list:", numbers_ex5)

# Exercise 6

if exercise == 6:

    print("unavailable, current knowledge not yet capable")

# Exercise 7: Accept any three string from one input() call
# Write a program to take three names as input from a user in the single input() function call
# Output: Enter three string Emma Jessa Kelly
#         Name1: Emma
#         Name2: Jessa
#         Name3: Kelly

if exercise == 7:

    str1_ex7, str2_ex7, str3_ex7 = input("Enter three string: ").split()
    print("Name1:", str1_ex7)
    print("Name1:", str2_ex7)
    print("Name1:", str3_ex7)

# CURRENT KNOWLEDGE NOT YET CAPABLE TO ANSWER THIS
# Exercise 8: Write a program to use string.format() method to format the following three variables as per the expected output
#Given:

if exercise == 8:

    totalMoney_ex8 = 1000
    quantity_ex8 = 3
    price_ex8 = 450
    statement1 = "I have {1} dollars so I can buy {0} football for {2:.2f} dollars."
    print(statement1.format(quantity_ex8, totalMoney_ex8, price_ex8))

# Exercise 9

if exercise == 9:

    print("unavailable, current knowledge not yet capable")

# Exercise 10

if exercise == 10:

    print("unavailable, current knowledge not yet capable")