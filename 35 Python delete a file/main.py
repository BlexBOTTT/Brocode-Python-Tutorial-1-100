import os

source = "folder 35"
destination = "C:\\Users\\Quirante\\Desktop\\folder"

try:
    if os.path.exists(destination):
        print("There is already a file there")
    else:
        os.replace(source, destination)
        print("{} was moved".format(source))

except FileNotFoundError:
    print("{} was not found".format(source))
