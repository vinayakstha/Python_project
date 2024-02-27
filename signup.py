from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3
import os

win2 = Tk()
win2.geometry("900x600")
win2.resizable(0, 0)
win2.title("Sign Up")

# BACKGROUND IMAGE
img = Image.open("C:\\Users\\Acer\\Desktop\\first_sem\\first_sem\\background1.jpg")
bg = ImageTk.PhotoImage(img)

photoLabel = Label(win2, image=bg)
photoLabel.place(x=0, y=0)


# FRAME
frame = Frame(
    win2,
    width=320,
    height=370,
    bg="white",
    highlightbackground="#2f8be0",
    highlightthickness=6,
)
frame.place(x=500, y=130)


"""-----FUNCTIONS-----"""


# show password function
def showPassword():
    if createPasswordEntry.cget("show") == "*":
        createPasswordEntry.config(show="")
    else:
        createPasswordEntry.config(show="*")


# show password function2
def showPassword2():
    if confirmPasswordEntry.cget("show") == "*":
        confirmPasswordEntry.config(show="")
    else:
        confirmPasswordEntry.config(show="*")


# back to login page
def backLoginPage():
    win2.destroy()
    os.system("python C:\\Users\\Acer\\Desktop\\first_sem\\first_sem\\login.py")


# sign up function
def signUpFunction():
    email = emailEntry.get()
    createPassword = createPasswordEntry.get()
    confirmPassword = confirmPasswordEntry.get()

    # creating database
    conn = sqlite3.connect("loginfo.db")

    tableQuery = """CREATE TABLE IF NOT EXISTS login_data
            (email TEXT NOT NULL, password TEXT NOT NULL)
"""
    conn.execute(tableQuery)

    # insert data
    dataInsertQuery = """INSERT INTO login_data(email, password) VALUES
        (?,?)
    """
    dataInsertTuple = (email, confirmPassword)
    cursor = conn.cursor()
    if email != "" and createPassword != "" and confirmPassword != "":
        if createPassword == confirmPassword:
            emailSelect = """SELECT * FROM login_data WHERE email=?"""
            cursor.execute(emailSelect, [(email)])
            if cursor.fetchall():
                messagebox.showerror(title="Error", message="Account already exists")
                # emailEntry.delete(0, END)
                # createPasswordEntry.delete(0, END)
                # confirmPasswordEntry.delete(0, END)
            else:
                cursor.execute(dataInsertQuery, dataInsertTuple)
                messagebox.showinfo(
                    title="information", message="Account created successfully"
                )
                emailEntry.delete(0, END)
                createPasswordEntry.delete(0, END)
                confirmPasswordEntry.delete(0, END)
        else:
            messagebox.showerror(
                title="Error", message="Passwords do not match. Please try again."
            )
    else:
        messagebox.showerror(title="Error", message="Please fill all informations")
        # emailEntry.delete(0, END)
        # createPasswordEntry.delete(0, END)
        # confirmPasswordEntry.delete(0, END)
    conn.commit()

    conn.close()


# LABEL

# login
signupLabel = Label(
    win2, text="SIGN UP", font=("ariel", 20, "bold"), bg="white", fg="#2f8be0"
)
signupLabel.place(x=520, y=140)

# email
emailLabel = Label(win2, text="Email", font=("ariel", 12), bg="white", fg="#2f8be0")
emailLabel.place(x=520, y=180)

# create password
createPasswordLabel = Label(
    win2, text="Create Password", font=("ariel", 12), bg="white", fg="#2f8be0"
)
createPasswordLabel.place(x=520, y=245)

# confirm password
confirmPasswordLabel = Label(
    win2, text="Confirm Password", font=("ariel", 12), bg="white", fg="#2f8be0"
)
confirmPasswordLabel.place(x=520, y=325)

# ENTRY
# email
emailEntry = Entry(win2, width=24, font=("ariel", 15), relief=SUNKEN)
emailEntry.place(x=520, y=210)

# create password
createPasswordEntry = Entry(win2, width=24, font=("ariel", 15), show="*", relief=SUNKEN)
createPasswordEntry.place(x=520, y=270)

# confirm password
confirmPasswordEntry = Entry(
    win2, width=24, font=("ariel", 15), show="*", relief=SUNKEN
)
confirmPasswordEntry.place(x=520, y=350)


# BUTTON


# back button
backBtn = Button(
    win2,
    text="BACK",
    font=("ariel", 10),
    fg="white",
    bg="#2f8be0",
    width=15,
    height=2,
    borderwidth=1,
    command=backLoginPage,
)
backBtn.place(x=520, y=430)

# sign up button
signUpBtn = Button(
    win2,
    text="SIGN UP",
    font=("ariel", 10),
    fg="white",
    bg="#2f8be0",
    width=15,
    height=2,
    borderwidth=1,
    command=signUpFunction,
)
signUpBtn.place(x=662, y=430)


# CHECKBUTTON
# show password
var = IntVar()
checkbtn1 = Checkbutton(
    win2,
    text="Show Password",
    variable=var,
    command=showPassword,
    bg="white",
    font=("ariel", 10),
    fg="#2f8be0",
)
checkbtn1.place(x=520, y=300)

var2 = IntVar()
checkbtn2 = Checkbutton(
    win2,
    text="Show Password",
    variable=var2,
    command=showPassword2,
    bg="white",
    font=("ariel", 10),
    fg="#2f8be0",
)
checkbtn2.place(x=520, y=380)

win2.mainloop()
