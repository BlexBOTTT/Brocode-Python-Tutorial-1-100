
# Opening file in desktop
#with open("C:\\Users\\Quirante\\Desktop\\test.txt") as file:
#    print(file.read())

print()

# Opening the file in pycharm
try:
    with open("text.tx") as file:
        print(file.read())

except FileNotFoundError:
    print("The file was not found!")