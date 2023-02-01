# frame = a rectangular container to group and hold widgets

from tkinter import *

window = Tk()

frame = Frame(window,
              background="pink",
              border="5",
              relief=SUNKEN)
frame.place(x=100, y=100)

Button(frame, text="W", font=("Futura PT Book", 25), width=3).pack(side=TOP)
Button(frame, text="A", font=("Futura PT Book", 25), width=3).pack(side=LEFT)
Button(frame, text="S", font=("Futura PT Book", 25), width=3).pack(side=LEFT)
Button(frame, text="D", font=("Futura PT Book", 25), width=3).pack(side=LEFT)

window.mainloop()

