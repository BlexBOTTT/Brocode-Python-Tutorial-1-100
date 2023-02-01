from tkinter import *

# label = an area widget that holds text and/or image within a window

window = Tk()
window.title("ikaw bobo putanginamo ka")

# icon
icon = PhotoImage(file="bobo_icon.png")
window.iconphoto(True, icon)
#window.geometry("420x210")

# photo
image = PhotoImage(file="C:\\Users\\Quirante\\Pictures\\Pepe the frog\\Peepo happy cheer.png")


label = Label(window,   # the text is default placed in top middle
              text="Lorem Ipsum is simply dummy text of the printing \n"
                   "and typesetting industry.\n"
                   "Lorem Ipsum has been the industry's \n"
                   "standard dummy text ever since the 1500s.\n",
              font=("Times new roman", 20), # change font size
              foreground="black",     # can also use fg
              background="gray",   # can also use fg
              relief=GROOVE,    # simulate 3-d object outside the widget: FLAT, RAISED, SUNKEN, GROOVE, RIDGE
              border=10,
              padx=20,          # padding x
              pady=20,          # padding y
              image=image,      # inserting variable with image
              compound="left")  # decides where to place image in window: right, left, bottom, top
label.pack()

#label.place(x=110, y=100)

window.mainloop()