from tkinter import *

# widgets = GUI elements: buttons, textboxes, labels, images
# windows = serves as a container to hold or contain these widgets

window = Tk()   # instantiate an instance of a window

window.geometry("420x420")  # changes window size

window.title("ikaw bobo putangina mo ka")

icon = PhotoImage(file="C:\\Users\\Quirante\\Pictures\\bobo_icon.png")  # can use (bobo_icon.png) if the file is here
window.iconphoto(True, icon)

window.config(background="#fc03e8") # can also use the name like red, green, blue


window.mainloop()   # place window on computer screen, listen for events


