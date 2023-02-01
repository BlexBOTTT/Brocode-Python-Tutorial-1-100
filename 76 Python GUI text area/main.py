# text widget = functions like a text area, you can enter multiple lines of text
from tkinter import *

def submit():
    input = text.get("1.0", END)
    print(input)


window = Tk()

text = Text(window,
            background="light yellow",
            font=("Ink Free", 25),
            height=8,
            width=20,
            padx=10,
            pady=20,
            foreground="purple")
text.pack()

button = Button(window, text="submit", command=submit)
button.pack()

window.mainloop()