from tkinter import *
from Ball import *
import time

window = Tk()

WIDTH = 768
HEIGHT = 1024

canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

bg = PhotoImage(file="anime girl.png")
background = canvas.create_image(0, 0, image=bg, anchor=NW)

volley_ball = Ball(canvas,0,0,100,1,1,"white")
tennis_ball = Ball(canvas,0,0,50,4,3,"yellow")
basket_ball = Ball(canvas,0,0,125,8,7,"orange")

while True:
    volley_ball.move()
    tennis_ball.move()
    basket_ball.move()
    window.update()
    time.sleep(0.01)

window.mainloop()