from tkinter import *
import random
import time
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import os
from tkinter import *


from PIL import Image, ImageTk

root2 = Tk()
root2.geometry("409x587")
root2.title("Update")
root2.resizable(0, 0)
frame = Frame(
    root2,
    width=409,
    height=587,
    bg="#2f8be0",
)
frame.place(x=0, y=0)


def updateFunction():

    global connectn, cursor
    orderID = orderEntry.get()
    pizzaQty = pizzaEntry.get()
    burgerQty = burgerEntry.get()
    iceCreamQty = iceCreamEntry.get()
    drinksQty = drinkEntry.get()

    costpi = float(pizzaQty) * 240
    costbu = float(burgerQty) * 125
    costice = float(iceCreamQty) * 80
    costdr = float(drinksQty) * 60

    cost = costpi + costbu + costice + costdr
    ptax = round((costpi + costbu + costice + costdr) * 0.18, 2)
    sub = costpi + costbu + costice + costdr
    ser = round((costpi + costbu + costice + costdr) / 99, 2)

    overall = ptax + ser + sub
    connectn = sqlite3.connect("Restaurant.db")
    cursor = connectn.cursor()
    selectOrderID = """SELECT * FROM Restaurantrecords WHERE ordno=?"""
    cursor.execute(selectOrderID, [(orderID)])

    if cursor.fetchall():
        orderUpdate = (
            """UPDATE Restaurantrecords SET piz=?,bur=?,ice=?, dr=? WHERE ordno=?"""
        )
        cursor.execute(
            orderUpdate,
            (pizzaQty, burgerQty, iceCreamQty, drinksQty, orderID),
        )
        connectn.commit()
        orderUpdate2 = """UPDATE Restaurantrecords SET ct=?,sb=?,tax=?,sr=?,tot=? WHERE ordno = ?"""
        cursor.execute(orderUpdate2, (cost, sub, ptax, ser, overall, orderID))
        connectn.commit()
        connectn.close()
        messagebox.showinfo(title="info", message="Order succcessfully updated.")
        root2.destroy()
    else:
        messagebox.showerror(title="error", message="OrderID not found")
        orderEntry.delete(0, END)
        pizzaEntry.delete(0, END)
        burgerEntry.delete(0, END)
        iceCreamEntry.delete(0, END)
        drinkEntry.delete(0, END)


# Label
updateLabel = Label(
    root2, text="Update", font=("ariel", 20, "bold"), bg="#2f8be0", fg="white"
)
updateLabel.place(x=150, y=30)

orderNumber = Label(
    root2, text="Order No", font=("ariel", 10, "bold"), bg="#2f8be0", fg="white"
)
orderNumber.place(x=50, y=90)

pizzaLabel = Label(
    root2, text="Pizza", font=("ariel", 10, "bold"), bg="#2f8be0", fg="white"
)
pizzaLabel.place(x=50, y=160)

burgerLabel = Label(
    root2, text="Burger", font=("ariel", 10, "bold"), bg="#2f8be0", fg="white"
)
burgerLabel.place(x=50, y=230)

iceCreamLabel = Label(
    root2, text="Ice Cream", font=("ariel", 10, "bold"), bg="#2f8be0", fg="white"
)
iceCreamLabel.place(x=50, y=300)

drinksLabel = Label(
    root2, text="Drinks", font=("ariel", 10, "bold"), bg="#2f8be0", fg="white"
)
drinksLabel.place(x=50, y=370)


# entry
orderEntry = Entry(root2, width=28, font=("ariel", 15), relief=SUNKEN)
orderEntry.place(x=50, y=120)

pizzaEntry = Entry(root2, width=28, font=("ariel", 15), relief=SUNKEN)
pizzaEntry.place(x=50, y=190)

burgerEntry = Entry(root2, width=28, font=("ariel", 15), relief=SUNKEN)
burgerEntry.place(x=50, y=260)

iceCreamEntry = Entry(root2, width=28, font=("ariel", 15), relief=SUNKEN)
iceCreamEntry.place(x=50, y=330)

drinkEntry = Entry(root2, width=28, font=("ariel", 15), relief=SUNKEN)
drinkEntry.place(x=50, y=400)


# button
updateBtn = Button(
    root2,
    text="Confirm Update",
    font=("ariel, 15"),
    bg="green",
    fg="white",
    borderwidth=1,
    command=updateFunction,
)
updateBtn.place(x=130, y=450)


root2.mainloop()
