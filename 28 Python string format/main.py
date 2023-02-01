# str.format() =    optional method that gives users
#                   more control when displaying output

#animal = "cow"
#item = "moon"

#print("The "+animal+" jumped over the "+item)

# {} = format fields
#print("The {} jumped over the {}".format(animal, item))

# Positional argument
#print("The {1} jumped over the {0}".format(animal, item))

# Keyword argument
#print("The {animal} jumped over the {item}".format(animal="cow", item="moon"))

# Formatting via variables
#text = "The {} jumped over the {}"
#print(text.format(animal, item))

# ---------------------------------------------------------------------------------------

#name = "blex"

#print("Hello, my name is {}".format(name))

# Padding to right (DEFAULT)
#print("Hello, my name is {:10}. Nice to meet you".format(name))
# Output: Hello, my name is blex      . Nice to meet you

# Also padding to right (DEFAULT)
#print("Hello, my name is {:<10}. Nice to meet you".format(name))
# Output: Hello, my name is blex      . Nice to meet you

# Padding to the left
#print("Hello, my name is {:>10}. Nice to meet you".format(name))
# Output: Hello, my name is       blex. Nice to meet you

# Padding to center
#print("Hello, my name is {:^10}. Nice to meet you".format(name))
# Output: Hello, my name is    blex   . Nice to meet you

# NOTE: YOU CAN ADD KEYWORD/POSITONAL ARGUMENT BEFORE PRECEDING COLON
# Example: Positional = {0:10}, Keyword = {name:10}

# ---------------------------------------------------------------------------------------

number_pi = 1000

# displays the first two decimals by #f = floating point number
print("The number pi is {:.2f}".format(number_pi))
# Output: 1000.000

# Using a , after colon adds comma in thousandths places
print("The number is {:,}".format(number_pi))
# Output: 1,000

# Using b after colon represents the binary representation of number
print("The number is {:b}".format(number_pi))
# Output: 1111101000

# Using o after colon represents the octal representation
print("The number is {:o}".format(number_pi))
# Output: 1750

# Using E or e after colon represents the scientific notation
print("The number is {:e}".format(number_pi))
# Output E = uppercase: 1.000000E+03
# Output e = lowercase: 1.000000e+03