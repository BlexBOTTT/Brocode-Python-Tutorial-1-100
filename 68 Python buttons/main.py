from tkinter import *

# button = you click it, then it does stuff

count = 0

def click():
    global count
    count += 1
    print("you clicked the button", count, "times")

window = Tk()

#photo = PhotoImage(file="C:\\Users\\Quirante\\Pictures\\Pepe the frog\\pepega happy.png")

button = Button(window,
                text="click me",
                command=click,
                font=("Comic sans", 30),
                foreground="green",
                background="black",
                relief=GROOVE,
                border=10,
                padx=25,
                pady=50,
                activeforeground="green",
                activebackground="black",
                state=ACTIVE,
                #image=photo,
                compound="top")
button.pack()

window.mainloop()