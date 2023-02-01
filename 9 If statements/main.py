# if statement = a block of code that will execute if it's condition is true

age = eval(input("How old are you?: "))

if age >= 18:
    print("You are an adult!")
elif age == 100:
    print("You are a century old!")
elif age < 0:
    print("You haven't been born yet!")
else:
    print("error")
    print("You are a child")
