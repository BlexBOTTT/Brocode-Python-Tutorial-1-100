from tkinter import *
from time import *


# the function update where display the date and time in real time
def update():
    time_string = strftime("%I:%M:%S %p")
    time_label.config(text=time_string)

    day_string = strftime("%A")
    day_label.config(text=day_string)

    date_string = strftime("%B %d, %Y")
    date_label.config(text=date_string)

    window.after(1000, update)

window = Tk()

time_label = Label(window, font=("Futura PT Book", 50),
                   fg="green",
                   bg="black")
time_label.pack()

day_label = Label(window, font=("arial", 25),
                   fg="black")
day_label.pack()

date_label = Label(window, font=("arial", 35),
                   fg="black")
date_label.pack()


# initiates the function update(), (function is named above)
update()

window.mainloop()
