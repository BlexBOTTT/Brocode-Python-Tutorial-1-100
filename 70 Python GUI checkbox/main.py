from tkinter import *

def display():
    if x.get() == 1:
        print("You agreed")
    else:
        print("You don't agree :(")

window = Tk()

x = IntVar()

logo_photo = PhotoImage(file="pepega.png")

check_button = Checkbutton(window,
                           text="I agree to something",
                           font=("Futura PT Book", 25),
                           foreground="green",
                           background="black",
                           activeforeground="green",
                           activebackground="black",
                           padx=25,
                           pady=10,
                           variable=x,
                           onvalue=1,
                           offvalue=0,
                           command=display,
                           image=logo_photo,
                           compound="right")

check_button.pack()
window.mainloop()
