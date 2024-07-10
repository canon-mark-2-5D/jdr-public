from tkinter import *
from tkinter import filedialog

lien = None

def openfn():
    filename = filedialog.askopenfilename(title='open')
    return filename

def open_link():
    global lien 
    lien = openfn()
    return lien

def create_window():
    root = Tk()
    root.geometry("550x300+300+150")
    root.resizable(width=True, height=True)

    btn = Button(root, text='take enemis', command=open_link)
    btn.pack()

    root.mainloop()