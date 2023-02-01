from tkinter import *
from tkinter import filedialog

def save_file():
    file = filedialog.asksaveasfile(initialdir="C:\\Users\\Quirante\\PycharmProjects\\Self Studty Brocode\\78 Python GUI save a file (filedialog)",
                                    defaultextension=".txt",
                                    filetypes=[("Text file", ".txt"),
                                               ("HTML file", ".html"),
                                               ("All files", ".html*")
                                               ])

    if file is None:
        return
    file_text = str(text.get(1.0, END))
    #file_text = input("Enter some text I guess: ")
    file.write(file_text)
    file.close()

window = Tk()

button = Button(text="Save", command=save_file)
button.pack()

text = Text(window)
text.pack()

window.mainloop()