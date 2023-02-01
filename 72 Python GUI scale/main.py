from tkinter import *

def submit():
    print("The temperature is: " + str(scale.get()) + "c")

window = Tk()

fire_image = PhotoImage(file="flame_logo.png")
hot_label = Label(image=fire_image)
hot_label.pack()

scale = Scale(window, from_=100, to=0,
              length=600,
              orient=VERTICAL,
              font=("Futura PT Book", 20),
              tickinterval=10,  # adds numeric indicators for value
              showvalue=True,   # hide current value
              #resolution=5, # increment of slider
              troughcolor="sky blue",
              foreground="red",
              background="black")

scale.set(37)   # set current value of slider
#scale.set(((scale["from"]-scale["to"])/2)+scale['to']) # to make the slider always in middile
scale.pack()

snow_image = PhotoImage(file="snowflake_logo.png")
snow_label = Label(image=snow_image)
snow_label.pack()

button = Button(window, text="submit", command=submit)
button.pack()

window.mainloop()