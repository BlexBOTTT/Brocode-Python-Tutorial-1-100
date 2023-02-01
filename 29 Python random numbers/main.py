import random


x = random.randint(1, 6)
# random number ranging 0 to 1
y = random.random()
print(x)
print(y)

myList = ["rock", "paper", "scissors"]
# choice = randomly choose an element in variable myList
z = random.choice(myList)
print(z)

cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, "J", "Q", "K", "A"]
# shuffles elements inside a variable
random.shuffle(cards)
print(cards)

