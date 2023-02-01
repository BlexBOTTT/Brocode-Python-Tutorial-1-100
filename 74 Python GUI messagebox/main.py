from tkinter import *
from tkinter import messagebox  # import messagebox library

def click():
    # messagebox.showinfo(title="this is an info message box", message="You are a person")
    # messagebox.showwarning(title="WARNING", message="You have a virus!")
    # messagebox.showerror(title="ERROR", message="something went wrong :(")

    # if messagebox.askretrycancel(title="ask ok cancel", message="Do you want to retry the thing?"):
    #    print("you did a thing")
    # else:
    #    print("You canceled a thing :(")

    # if messagebox.askyesno(title="ask yes or no", message="Do you like cake?"):
    #    print("I like cake too")
    # else:
    #    print("why do you not like cake :(")

    # answer = messagebox.askquestion(title="ask question", message="Do you like pie?")
    # if answer == "yes":
    #    print("I like pie too")
    # else:
    #    print("Why do you not like pie? :(")

    while True:
        answer = messagebox.askyesnocancel(title="Yes no cancel", message="Do you like to code?", icon="question")
        if answer is True:
            print("You like to code :)")
            break
        elif answer is False:
            print("Then why are you watching a video on coding?")
            break
        else:
            print("You have dodged the question")


window = Tk()

pepe_icon = PhotoImage(file="C:\\Users\\Quirante\\Pictures\\Pepe the frog\\Pepe doodle with glass.png")
window.iconphoto(True, pepe_icon)

button = Button(window,
                command=click,
                text="click me")
button.pack()

window.mainloop()