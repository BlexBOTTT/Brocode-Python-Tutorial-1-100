from tkinter import *

def open_file():
    print("file has opened")

def save_file():
    print("file has opened")

def cut():
    print("You cut some text")

def copy():
    print("You copied some text")

def paste():
    print("You pasted some text")


window = Tk()

open_image = PhotoImage(file="open.png")
save_image = PhotoImage(file="save.png")
exit_image = PhotoImage(file="stop.png")

menu_bar = Menu(window)
window.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0,
                 font=("Futura PT Book", 0))
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=open_file, image=open_image, compound="left")
file_menu.add_command(label="Save", command=save_file, image=save_image, compound="left")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=quit, image=exit_image, compound="left")

edit_menu = Menu(menu_bar, tearoff=0,
                 font=("Futura PT Book", 0))
menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=cut)
edit_menu.add_command(label="Copy", command=copy)
edit_menu.add_command(label="Paste", command=paste)

window.mainloop()