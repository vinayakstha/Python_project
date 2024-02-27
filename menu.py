from tkinter import *
import random
import time
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import os
from tkinter import *

from PIL import Image, ImageTk

root = Tk()
root.geometry("409x587")
root.title("Menu")
root.resizable(0, 0)

img = Image.open("menuimg4.jpg")
bg = ImageTk.PhotoImage(img)

photoLabel = Label(root, image=bg)
photoLabel.place(x=0, y=0)

root.mainloop()
