### Importing required libraries ###
from tkinter import *
import random
import time
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import os
from tkinter import *


# It is definition of System
def system():
    from PIL import Image, ImageTk

    root = Tk()
    root.geometry("1700x800")
    root.title("Restaurant Management System")

    img = Image.open("logoimage3.png")
    bg = ImageTk.PhotoImage(img)

    photoLabel = Label(root, image=bg)
    photoLabel.place(x=10, y=7)

    def Database():
        global connectn, cursor
        connectn = sqlite3.connect("Restaurant.db")
        cursor = connectn.cursor()
        # creating bill table
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS Restaurantrecords(ordno text,piz text,bur text,ice text, dr text, ct text,sb text,tax text,sr text,tot text)"
        )

    # variable datatype assignment
    orderno = StringVar()
    pizza = StringVar()
    burger = StringVar()
    icecream = StringVar()
    drinks = StringVar()
    cost = StringVar()
    subtotal = StringVar()
    tax = StringVar()
    service = StringVar()
    total = StringVar()

    # defining total function
    def tottal():
        # fetching the values from entry box
        order = orderno.get()
        # pi = float(pizza.get())
        # bu = float(burger.get())
        # ice = float(icecream.get())
        # dr = float(drinks.get())
        pi = round(float(pizza.get()), 2)
        bu = round(float(burger.get()), 2)
        ice = round(float(icecream.get()), 2)
        dr = round(float(drinks.get()), 2)

        # computing the cost of items

        costpi = pi * 240
        costbu = bu * 125
        costice = ice * 80
        costdr = dr * 60

        # computing the charges
        costofmeal = costpi + costbu + costice + costdr
        ptax = round((costpi + costbu + costice + costdr) * 0.18, 2)
        sub = costpi + costbu + costice + costdr
        ser = round((costpi + costbu + costice + costdr) / 99, 2)
        paidtax = str(ptax)
        Service = str(ser)
        overall = str(ptax + ser + sub)
        # paidtax = "{:.2f}".format(ptax)
        # service = "{:.2f}".format(ser)
        # overall = "{:.2f}".format(ptax + ser + sub)

        # Displaying the values
        cost.set(costofmeal)
        tax.set(ptax)
        subtotal.set(sub)
        service.set(ser)
        total.set(overall)

    # defining reset function
    def reset():
        orderno.set("")
        pizza.set("")
        burger.set("")
        icecream.set("")
        drinks.set("")
        cost.set("")
        subtotal.set("")
        tax.set("")
        service.set("")
        total.set("")

    # defining exit function
    def exit():
        root.destroy()
        os.system("python login.py")

    # Topframe
    topframe = Frame(
        root, width=1600, height=50, highlightbackground="#2f8be0", highlightthickness=4
    )
    topframe.pack(side=TOP)

    # Leftframe
    leftframe = Frame(
        root,
        width=920,
        height=1000,
        highlightbackground="#5f5f5f",
        highlightthickness=4,
    )
    leftframe.pack(side=LEFT)

    # rightframe
    rightframe = Frame(
        root, width=400, height=700, highlightbackground="#5f5f5f", highlightthickness=4
    )
    rightframe.pack(side=RIGHT)

    ################## display data ####################
    def DisplayData():
        Database()
        my_tree.delete(*my_tree.get_children())
        cursor = connectn.execute("SELECT * FROM Restaurantrecords")
        fetch = cursor.fetchall()
        for data in fetch:
            my_tree.insert("", "end", values=(data))
        cursor.close()
        connectn.close()

    style = ttk.Style()
    style.configure(
        "Treeview", foreground="black", rowheight=40, fieldbackground="white"
    )
    style.map("Treeview", background=[("selected", "lightgreen")])

    ###########  Creating table #############
    my_tree = ttk.Treeview(rightframe)
    my_tree["columns"] = (
        "ordno",
        "piz",
        "bur",
        "ice",
        "dr",
        "ct",
        "sb",
        "tax",
        "sr",
        "tot",
    )

    ############ creating  for table ################
    horizontal_bar = ttk.Scrollbar(rightframe, orient="horizontal")
    horizontal_bar.configure(command=my_tree.xview)
    my_tree.configure(xscrollcommand=horizontal_bar.set)
    horizontal_bar.pack(fill=X, side=BOTTOM)

    vertical_bar = ttk.Scrollbar(rightframe, orient="vertical")
    vertical_bar.configure(command=my_tree.yview)
    my_tree.configure(yscrollcommand=vertical_bar.set)
    vertical_bar.pack(fill=Y, side=RIGHT)

    # defining column for table
    my_tree.column("#0", width=0, minwidth=0)
    my_tree.column("ordno", anchor=CENTER, width=80, minwidth=25)
    my_tree.column("piz", anchor=CENTER, width=60, minwidth=25)
    my_tree.column("bur", anchor=CENTER, width=50, minwidth=25)
    my_tree.column("ice", anchor=CENTER, width=80, minwidth=25)
    my_tree.column("dr", anchor=CENTER, width=50, minwidth=25)
    my_tree.column("ct", anchor=CENTER, width=50, minwidth=25)
    my_tree.column("sb", anchor=CENTER, width=100, minwidth=25)
    my_tree.column("tax", anchor=CENTER, width=50, minwidth=25)
    my_tree.column("sr", anchor=CENTER, width=100, minwidth=25)
    my_tree.column("tot", anchor=CENTER, width=50, minwidth=25)

    # defining  headings for table
    my_tree.heading("ordno", text="Order No", anchor=CENTER)
    my_tree.heading("piz", text="Pizza", anchor=CENTER)
    my_tree.heading("bur", text="Burger", anchor=CENTER)
    my_tree.heading("ice", text="Ice cream", anchor=CENTER)
    my_tree.heading("dr", text="Drinks", anchor=CENTER)
    my_tree.heading("ct", text="Cost", anchor=CENTER)
    my_tree.heading("sb", text="Subtotal", anchor=CENTER)
    my_tree.heading("tax", text="Tax", anchor=CENTER)
    my_tree.heading("sr", text="Service", anchor=CENTER)
    my_tree.heading("tot", text="Total", anchor=CENTER)

    my_tree.pack()
    DisplayData()

    # defining add function to add record
    def add():
        Database()
        # getting  data
        orders = orderno.get()
        pizzas = pizza.get()
        burgers = burger.get()
        ices = icecream.get()
        drinkss = drinks.get()
        costs = cost.get()
        subtotals = subtotal.get()
        taxs = tax.get()
        services = service.get()
        totals = total.get()

        orderNumberSelect = """SELECT * FROM Restaurantrecords WHERE ordno=?"""
        cursor.execute(orderNumberSelect, [(orderno.get())])
        if cursor.fetchall():
            messagebox.showerror(title="Error", message="Order number already exists")
        else:
            if (
                orders == ""
                or pizzas == ""
                or burgers == ""
                or ices == ""
                or drinkss == ""
                or costs == ""
                or subtotals == ""
                or taxs == ""
                or services == ""
                or totals == ""
            ):
                messagebox.showinfo("Warning", "Please fill the empty field!!!")
            else:
                connectn.execute(
                    "INSERT INTO Restaurantrecords (ordno, piz, bur , ice ,dr ,ct ,sb ,tax, sr, tot) VALUES (?,?,?,?,?,?,?,?,?,?)",
                    (
                        orders,
                        pizzas,
                        burgers,
                        ices,
                        drinkss,
                        costs,
                        subtotals,
                        taxs,
                        services,
                        totals,
                    ),
                )
                connectn.commit()
                messagebox.showinfo("Message", "Stored successfully")
            # refresh table data
            DisplayData()
            connectn.close()

    # defining function to access data from sqlite datrabase
    def DisplayData():
        Database()
        my_tree.delete(*my_tree.get_children())
        cursor = connectn.execute("SELECT * FROM Restaurantrecords")
        fetch = cursor.fetchall()
        for data in fetch:
            my_tree.insert("", "end", values=(data))
        cursor.close()
        connectn.close()

    # defining function to delete record
    def Delete():
        # open database
        Database()
        if not my_tree.selection():
            messagebox.showwarning("Warning", "Select data to delete")
        else:
            result = messagebox.askquestion(
                "Confirm",
                "Are you sure you want to delete this record?",
                icon="warning",
            )
        if result == "yes":
            curItem = my_tree.focus()
            contents = my_tree.item(curItem)
            selecteditem = contents["values"]
            my_tree.delete(curItem)
            cursor = connectn.execute(
                "DELETE FROM Restaurantrecords WHERE ordno= %d" % selecteditem[0]
            )
            connectn.commit()
            cursor.close()
            connectn.close()

    # Time
    localtime = time.asctime(time.localtime(time.time()))
    # Top part
    main_lbl = Label(
        topframe,
        font=("Calibri", 25, "bold"),
        text="Mitho Mitho Mitho",
        fg="#2f8be0",
        anchor=W,
    )
    main_lbl.grid(row=0, column=0)
    main_lbl = Label(
        topframe,
        font=(
            "Calibri",
            15,
        ),
        text=localtime,
        fg="#014221",
        anchor=W,
    )
    main_lbl.grid(row=1, column=0)

    ### Labels
    # items
    ordlbl = Label(
        leftframe,
        font=("Calibri", 16, "bold"),
        text="Order No.",
        fg="black",
        bd=5,
        anchor=W,
    ).grid(row=1, column=0)
    ordtxt = Entry(
        leftframe,
        font=("Calibri", 16, "bold"),
        bd=6,
        insertwidth=4,
        justify="right",
        textvariable=orderno,
    ).grid(row=1, column=1)
    # Pizza
    pizlbl = Label(
        leftframe,
        font=("Calibri", 16, "bold"),
        text="Pizza",
        fg="black",
        bd=5,
        anchor=W,
    ).grid(row=2, column=0)
    piztxt = Entry(
        leftframe,
        font=("Calibri", 16, "bold"),
        bd=6,
        insertwidth=4,
        justify="right",
        textvariable=pizza,
    ).grid(row=2, column=1)
    # burger
    burlbl = Label(
        leftframe,
        font=("Calibri", 16, "bold"),
        text="Burger",
        fg="black",
        bd=5,
        anchor=W,
    ).grid(row=3, column=0)
    burtxt = Entry(
        leftframe,
        font=("Calibri", 16, "bold"),
        bd=6,
        insertwidth=4,
        justify="right",
        textvariable=burger,
    ).grid(row=3, column=1)

    # icecream
    icelbl = Label(
        leftframe,
        font=("Calibri", 16, "bold"),
        text="Ice Cream",
        fg="black",
        bd=5,
        anchor=W,
    ).grid(row=4, column=0)
    icetxt = Entry(
        leftframe,
        font=("Calibri", 16, "bold"),
        bd=6,
        insertwidth=4,
        justify="right",
        textvariable=icecream,
    ).grid(row=4, column=1)
    # drinks
    drinklbl = Label(
        leftframe,
        font=("Calibri", 16, "bold"),
        text="Drinks",
        fg="black",
        bd=5,
        anchor=W,
    ).grid(row=5, column=0)
    drinktxt = Entry(
        leftframe,
        font=("Calibri", 16, "bold"),
        bd=6,
        insertwidth=4,
        justify="right",
        textvariable=drinks,
    ).grid(row=5, column=1)
    # cost
    costlbl = Label(
        leftframe, font=("Calibri", 16, "bold"), text="Cost", bd=5, anchor=W
    ).grid(row=6, column=0)
    costtxt = Entry(
        leftframe,
        font=("Calibri", 16, "bold"),
        bd=6,
        insertwidth=4,
        justify="right",
        textvariable=cost,
    ).grid(row=6, column=1)
    # subtotal
    sublbl = Label(
        leftframe, font=("Calibri", 16, "bold"), text="Subtotal", bd=5, anchor=W
    ).grid(row=7, column=0)
    subtxt = Entry(
        leftframe,
        font=("Calibri", 16, "bold"),
        bd=6,
        insertwidth=4,
        justify="right",
        textvariable=subtotal,
    ).grid(row=7, column=1)
    # tax
    taxlbl = Label(
        leftframe, font=("Calibri", 16, "bold"), text="Tax", bd=5, anchor=W
    ).grid(row=8, column=0)
    taxtxt = Entry(
        leftframe,
        font=("Calibri", 16, "bold"),
        bd=6,
        insertwidth=4,
        justify="right",
        textvariable=tax,
    ).grid(row=8, column=1)
    # service
    servicelbl = Label(
        leftframe, font=("Calibri", 16, "bold"), text="Service", bd=5, anchor=W
    ).grid(row=9, column=0)
    servicetxt = Entry(
        leftframe,
        font=("Calibri", 16, "bold"),
        bd=6,
        insertwidth=4,
        justify="right",
        textvariable=service,
    ).grid(row=9, column=1)
    # total
    totallbl = Label(
        leftframe, font=("Calibri", 16, "bold"), text="Total", bd=5, anchor=W
    ).grid(row=10, column=0)
    totaltxt = Entry(
        leftframe,
        font=("Calibri", 16, "bold"),
        bd=6,
        insertwidth=4,
        justify="right",
        textvariable=total,
    ).grid(row=10, column=1)
    # ---button--

    totbtn = Button(
        leftframe,
        font=("Calibri", 16, "bold"),
        text="Total",
        bg="#2f8be0",
        fg="white",
        bd=3,
        padx=5,
        pady=5,
        width=6,
        borderwidth=1,
        command=tottal,
    ).grid(row=6, column=3)

    resetbtn = Button(
        leftframe,
        font=("Calibri", 16, "bold"),
        text="Reset",
        bg="#2f8be0",
        fg="white",
        bd=3,
        padx=5,
        pady=5,
        width=6,
        borderwidth=1,
        command=reset,
    ).grid(row=4, column=3)

    exitbtn = Button(
        leftframe,
        font=("Calibri", 16, "bold"),
        text="Logout",
        bg="#2f8be0",
        fg="white",
        bd=3,
        padx=5,
        pady=5,
        width=12,
        command=exit,
        borderwidth=1,
    ).grid(row=8, column=2)

    addbtn = Button(
        leftframe,
        font=("Calibri", 16, "bold"),
        text="Add",
        bg="#2f8be0",
        fg="white",
        bd=3,
        padx=5,
        pady=6,
        width=6,
        borderwidth=1,
        command=add,
    ).grid(row=2, column=3)

    deletebtn = Button(
        leftframe,
        font=("Calibri", 16, "bold"),
        text="Delete Record",
        bg="#2f8be0",
        fg="white",
        bd=3,
        padx=5,
        pady=5,
        width=12,
        borderwidth=1,
        command=Delete,
    ).grid(row=4, column=2)

    ########################### feedback form ################################

    def updateFunction():
        Database()
        os.system("python update.py")

    # Feedbackbutton
    Update = Button(
        leftframe,
        font=("Calibri", 16, "bold"),
        text="Update",
        fg="white",
        bg="#2f8be0",
        bd=3,
        padx=5,
        pady=5,
        width=12,
        borderwidth=1,
        command=updateFunction,
    ).grid(row=6, column=2)

    ##################### Menu card ################################
    def menu():
        os.system("python menu.py")

    # menubutton
    menubtn = Button(
        leftframe,
        font=("Calibri", 16, "bold"),
        text="Menu Card",
        bg="#2f8be0",
        bd=3,
        padx=6,
        pady=6,
        width=12,
        borderwidth=1,
        command=menu,
        fg="white",
    ).grid(row=2, column=2)

    root.mainloop()


system()