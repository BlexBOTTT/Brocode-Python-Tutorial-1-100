from tkinter import *
from tkinter import ttk

window = Tk()

notebook = ttk.Notebook(window, )   # widget that manages a collection of wndows/displays

tab_1 = Frame(notebook) # new frame for tab 1
tab_2 = Frame(notebook) # new frame for tab 2

notebook.add(tab_1, text="tab 1")
notebook.add(tab_2, text="tab 2")
notebook.pack(expand=True, fill="both") # expand = expand to fill any space not otherwise used
                                        # fill = fill spaces on x and y axis

Label(tab_1, text="Hello, this is tab#1", width=50, height=25,).pack()
Label(tab_2, text="Hello, this is tab#2", width=50, height=25,).pack()

window.mainloop()