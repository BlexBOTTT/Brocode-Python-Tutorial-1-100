#CTRL + / to remove comments

#PART 1
# PART 1 BELOW

# from tkinter import *
#
# def move_up(event):
#     label.place(x=label.winfo_x(), y=label.winfo_y() - 15)
# def move_down(event):
#     label.place(x=label.winfo_x(), y=label.winfo_y() + 15)
# def move_left(event):
#     label.place(x=label.winfo_x() - 15, y=label.winfo_y())
# def move_right(event):
#     label.place(x=label.winfo_x() + 15, y=label.winfo_y())
#
# window = Tk()
#
# window.geometry("500x500")
#
# window.bind("<w>", move_up)
# window.bind("<s>", move_down)
# window.bind("<a>", move_left)
# window.bind("<d>", move_right)
#
# window.bind("<Up>", move_up)
# window.bind("<Down>", move_down)
# window.bind("<Left>", move_left)
# window.bind("<Right>", move_right)
#
# road_bike = PhotoImage(file="road bike png.png")
# label = Label(window, image=road_bike)
# label.place(x=0, y=0)
#
# window.mainloop()


from tkinter import *

def move_up(event):
    canvas.move(my_image, 0, -10)
def move_down(event):
    canvas.move(my_image, 0, 10)
def move_left(event):
    canvas.move(my_image, -10, 0)
def move_right(event):
    canvas.move(my_image, 10, 0)

window = Tk()

window.bind("<w>", move_up)
window.bind("<a>", move_left)
window.bind("<s>", move_down)
window.bind("<d>", move_right)

window.bind("<Up>", move_up)
window.bind("<Left>", move_left)
window.bind("<Down>", move_down)
window.bind("<Right>", move_right)

canvas = Canvas(window, width=500, height=500)
canvas.pack()

road_bike = PhotoImage(file="road bike png.png")
my_image = canvas.create_image(0, 0, image=road_bike, anchor=NW)

window.mainloop()

