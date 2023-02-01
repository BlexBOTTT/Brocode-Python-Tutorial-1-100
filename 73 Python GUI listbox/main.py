from tkinter import *

def delete():
    for index in reversed(listbox.curselection()):
        listbox.delete(index)

    listbox.config(height=listbox.size())

def add():
    listbox.insert(listbox.size(), entry_box.get())
    listbox.config(height=listbox.size())

def submit():

    food = []
    for index in listbox.curselection():
        food.insert(index, listbox.get(index))

    for index in food:
        print("You have ordered", index)
    # print("You ordered", listbox.get(listbox.curselection()))

window = Tk()

listbox = Listbox(window,
                  background="#f7ffde",
                  font=("Futura PT Book", 25),
                  width=12,
                  selectmode=MULTIPLE
                  )
listbox.pack()

listbox.insert(1, "pizza")
listbox.insert(2, "pasta")
listbox.insert(3, "garlic bred")
listbox.insert(4, "soup")
listbox.insert(5, "salad")

listbox.config(height=listbox.size())

entry_box = Entry(window)
entry_box.pack()

add_button = Button(window, text="add", command=add)
add_button.pack()

delete_button = Button(window, text="delete", command=delete)
delete_button.pack()

submit_button = Button(window, text="submit", command=submit)
submit_button.pack()

window.mainloop()