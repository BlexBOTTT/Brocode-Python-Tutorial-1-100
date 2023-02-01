# ----------------------------
def new_game():

    guesses = []
    correct_guess = 0
    question_num = 1

    for key in questions:
        print("----------------------------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)

        guess = input("Enter A, B, C, or D: ")
        guess = guess.upper()

        guesses.append(guess)

        correct_guess += check_answer(questions.get(key), guess)

        question_num += 1

    display_score(correct_guess, guesses)


# ----------------------------
def check_answer(answer, guess):
    if answer == guess:
        print("Correct!")
        return 1
    else:
        print("Wrong")
        return 0


# ----------------------------
def display_score(correct_guess, guess):
    print("----------------------------------------------")
    print("Results:")
    print("----------------------------------------------")

    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Answers: ", end="")
    for i in guess:
        print(i, end=" ")
    print()

    score = int((correct_guess / len(questions)) * 100)
    print("Your score is:", str(score)+"%")


# ----------------------------
def play_again():

    response = input("Do you want to play again? (yes or no): ")
    response = response.upper()

    if response == "yes".upper():
        return True
    else:
        return False


questions = {"Who created Python?: ": "A",
             "What year was Python created?: ": "B",
             "Python is tributed to which comedy group?: ": "C",
             "Is the earth round?: ": "A"}

options = [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerberg"],
           ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
           ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
           ["A. True", "B. False", "C. Sometimes", "D. What's earth?"]]

new_game()

while play_again():
    new_game()

print("Bye")
