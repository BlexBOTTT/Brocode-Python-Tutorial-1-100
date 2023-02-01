# index operator [] = gives access to a sequence’s element (str,list,tuples)

name = input("Enter name: ")

if name[0].islower():
    name = name.capitalize()

first_name = name[0:4].upper()
last_name = name[5:].lower()
last_character = name[::-1]

#print(name)
#print(first_name)
#print(last_name)
print(last_character)