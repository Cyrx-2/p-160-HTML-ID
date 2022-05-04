from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import os
from tkinter import messagebox

root = Tk()
root.minsize(650,650)
root.maxsize(650,650)

openImg = ImageTk.PhotoImage(Image.open("open.png"))
saveImg = ImageTk.PhotoImage(Image.open("save.png"))
exitImg = ImageTk.PhotoImage(Image.open("exit.png"))

labelFileName = Label(root, text= "File name")
labelFileName.place(relx=0.28, rely= 0.03, anchor = CENTER)

inputFileName = Entry(root)
inputFileName.place(relx=0.46, rely= 0.03, anchor = CENTER)

my_text = Text(root, height = 35, width = 80)
my_text.place(relx = 0.5, rely = 0.55, anchor = CENTER)
my_text.config(bg = "#535c75")

root.mainloop()