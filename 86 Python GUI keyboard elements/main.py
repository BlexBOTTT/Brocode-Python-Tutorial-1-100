from tkinter import *

def do_something(event):
    #rint("You pressed: ", event.keysym)
    label.config(text=event.keysym)



window = Tk()

window.bind("<Key>", do_something)

label = Label(window, font=("Futura PT Book", 100))
label.pack()

window.mainloop()