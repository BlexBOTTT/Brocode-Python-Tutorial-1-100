from tkinter import *

def do_something(event):
    print("Mouse coordinates:", str(event.x) + "," + str(event.y))


window = Tk()

#window.bind("<Button-1>", do_something)     # left mouse click
#window.bind("<Button-2>", do_something)     # scroll button
#window.bind("<Button-3>", do_something)     # right mouse click
#window.bind("<ButtonRelease>", do_something)     # right mouse click
#window.bind("<Enter>", do_something)        # enter cursor to window
window.bind("<Leave>", do_something)        # leave cursor from window
window.bind("<Motion>", do_something)       # Where mouse moves

window.mainloop()