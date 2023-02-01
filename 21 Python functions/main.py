# function = a block of code which is executed only when it is called.

def hello(first_name, last_name, age):
    print("Hello!", first_name, last_name)
    print("You are", age, "years old")
    print("Have a nice day!")

def main():
    first_name = input("Enter name:")
    last_name = input("Enter name:")
    age = eval(input("Enter name:"))

    hello(first_name, last_name, age)

main()