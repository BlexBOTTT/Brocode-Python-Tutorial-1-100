
text = "\nHave a nice day, see ya!"

with open("test.txt", "a") as file:
    file.write(text)

print(text)