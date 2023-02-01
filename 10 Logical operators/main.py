# logical operators (and,or,not) = used to check if two or more conditional statements is true

temp = eval(input("What is the temperature outside?: "))

if not temp >= 0 and temp <= 30:
    print("The temperature is good today!")
    print("go outside!")

elif not temp < 0 or temp > 30:
    print("The temperature is bad to day!")
    print("stay inside!")
