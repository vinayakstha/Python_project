from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3
import os

win = Tk()
win.geometry("900x600")
win.resizable(0, 0)
win.title("Log In")

# BACKGROUND IMAGE
img = Image.open("background1.jpg")
bg = ImageTk.PhotoImage(img)

photoLabel = Label(win, image=bg)
photoLabel.place(x=0, y=0)


# FRAME
frame = Frame(
    win,
    width=320,
    height=370,
    bg="white",
    highlightbackground="#2f8be0",
    highlightthickness=6,
)
frame.place(x=500, y=130)


"""-----FUNCTIONS-----"""


# show password
def showPassword():
    if passwordEntry.cget("show") == "*":
        passwordEntry.config(show="")
    else:
        passwordEntry.config(show="*")


# signup page
def sighupPage():
    win.destroy()
    os.system("python signup.py")


# forgotpassword page
def forgotPasswordPage():
    win.destroy()
    os.system("python forgotpassword.py")


# login function
def login():
    email = emailEntry.get()
    password = passwordEntry.get()

    # connecting to database
    conn = sqlite3.connect("loginfo.db")
    cursor = conn.cursor()

    if email != "" and password != "":
        findUser = """SELECT * FROM login_data WHERE email=? and password = ?"""
        cursor.execute(findUser, [(email), (password)])
        if cursor.fetchall():
            win.destroy()
            os.system("python dashbord.py")

        else:
            messagebox.showerror(title="error", message="Invalid credentials")
    else:
        messagebox.showerror(title="error", message="Invalid credentials")

    conn.commit()
    conn.close()


# LABEL

# login
loginLabel = Label(
    win, text="LOGIN", font=("ariel", 20, "bold"), bg="white", fg="#2f8be0"
)
loginLabel.place(x=520, y=140)

# email
emailLabel = Label(win, text="Email", font=("ariel", 12), bg="white", fg="#2f8be0")
emailLabel.place(x=520, y=180)

# password
passwordLabel = Label(
    win, text="Password", font=("ariel", 12), bg="white", fg="#2f8be0"
)
passwordLabel.place(x=520, y=245)


# ENTRY
# email
emailEntry = Entry(win, width=24, font=("ariel", 15), relief=SUNKEN)
emailEntry.place(x=520, y=210)

# password
passwordEntry = Entry(win, width=24, font=("ariel", 15), show="*", relief=SUNKEN)
passwordEntry.place(x=520, y=270)


# BUTTON
# forgot password
forgotPasswordBtn = Button(
    win,
    text="Forgot Password?",
    font=("ariel", 10, "underline"),
    borderwidth=0,
    fg="#2f8be0",
    bg="white",
    command=forgotPasswordPage,
)
forgotPasswordBtn.place(x=680, y=340)


# login button
loginBtn = Button(
    win,
    text="LOG IN",
    font=("ariel", 10),
    fg="white",
    bg="#2f8be0",
    width=34,
    height=2,
    borderwidth=1,
    command=login,
)
loginBtn.place(x=520, y=375)


# create an account button
createAccountBtn = Button(
    win,
    text="Create an account",
    font=("ariel", 10, "underline"),
    borderwidth=0,
    fg="#2f8be0",
    bg="white",
    command=sighupPage,
)
createAccountBtn.place(x=605, y=440)


# CHECKBUTTON
# show password
var = IntVar()
checkbtn1 = Checkbutton(
    win,
    text="Show Password",
    variable=var,
    command=showPassword,
    bg="white",
    font=("ariel", 10),
    fg="#2f8be0",
)
checkbtn1.place(x=520, y=300)

win.mainloop()
