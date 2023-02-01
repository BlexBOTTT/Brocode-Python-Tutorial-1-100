from tkinter import *

# entry widget = textbox that accepts a single line of user input

def submit():
    username = entry.get()
    print("Hello", username)
    entry.config(state=DISABLED)

def delete():
    entry.delete(0, END)

def backspace():
    entry.delete(len(entry.get())-1, END)

window = Tk()

entry = Entry(window,
              font=("Futura PT Book", 40),
              border=10,
              foreground="green",
              background="gray",
              show="*"
              )
entry.insert(0, "spongebob")
entry.pack(side=RIGHT)

submit_button = Button(window, text="submit", command=submit)
submit_button.pack()

delete_button = Button(window, text="delete", command=delete)
delete_button.pack()

backspace_button = Button(window, text="backspace", command=backspace)
backspace_button.pack()

window.mainloop()