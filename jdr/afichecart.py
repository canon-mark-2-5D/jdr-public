from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import os
import json
def afiche():
 with open("./persos/ficheperso.json", "r") as fr: # sa import la positon pour complété l'url 
   aa = json.load(fr)
   filurl = (aa["posistion"])
   txt = f"./image/{filurl}.jpg"
 root = Tk()
 root.geometry("550x300+300+150")
 root.resizable(width=True, height=True)

 def open_img():
    img = Image.open(txt)
    img = img.resize((250, 250), Image.Resampling.BOX)
    img = ImageTk.PhotoImage(img)
    panel = Label(root, image=img)
    panel.image = img
    panel.pack()

 btn = Button(root, text='gps', command=open_img).pack()

 root.mainloop()

