from tkinter import *
from tkinter import colorchooser

def click():
    color = colorchooser.askcolor()
    color_hex = color[1]
    window.config(bg=color_hex)

window = Tk()

logo_icon = PhotoImage(file="C:\\Users\\Quirante\\Pictures\\Pepe the frog\\Pepe Cheers.png")
window.iconphoto(True, logo_icon)

window.geometry("420x420")

button = Button(text="click me", command=click)
button.pack()


window.mainloop()