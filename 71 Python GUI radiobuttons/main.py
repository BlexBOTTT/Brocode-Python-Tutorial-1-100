from tkinter import *

# radio button = similar to checkbox, but you can only select one from a group

food = ["pizza", "hamburger", "hotdog"]

def order():
    if x.get() == 0:
        print("You ordered pizza")
    elif x.get() == 1:
        print("You ordered hamburger")
    elif x.get() == 2:
        print("You ordered hotdog")
    else:
        print("huh?")
window = Tk()

pizza_image = PhotoImage(file="pizza_logo.png")
hamburger_image = PhotoImage(file="hamburger_logo.png")
hotdog_image = PhotoImage(file="hotdog_logo.png")

food_images = [pizza_image, hamburger_image, hotdog_image]

x = IntVar()

for index in range(len(food)):
    radio_button = Radiobutton(window,
                               text=food[index],    # add dext to radio button
                               variable=x,          # groups radiobuttons together if they share the same variables
                               value=index,         # assigns each radio button a different value
                               padx=15,             # adds padding on x-axis
                               font=("Futura PT Book", 25),
                               image=food_images[index],    # adds images to raidobutton
                               compound="left",     # adds image and text to the left
                               indicatoron=False,    # eliminates circle indicators
                               width=375,           # sets width of radio buttons
                               command=order        # set command of radio buttons to function
                               )


    radio_button.pack(anchor=W)

window.mainloop()