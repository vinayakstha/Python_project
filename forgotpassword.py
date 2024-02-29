from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3
import os

win3 = Tk()
win3.geometry("900x600")
win3.resizable(0, 0)
win3.title("Password Reset")

# BACKGROUND IMAGE
img = Image.open("background1.jpg")
bg = ImageTk.PhotoImage(img)

photoLabel = Label(win3, image=bg)
photoLabel.place(x=0, y=0)


# FRAME
frame = Frame(
    win3,
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
    if newPasswordEntry.cget("show") == "*":
        newPasswordEntry.config(show="")
    else:
        newPasswordEntry.config(show="*")


# show password function2
def showPassword2():
    if confirmPasswordEntry.cget("show") == "*":
        confirmPasswordEntry.config(show="")
    else:
        confirmPasswordEntry.config(show="*")


# back to login page
def backLogin():
    win3.destroy()
    os.system("python login.py")


# password reset function
def resetPassword():
    email = emailEntry.get()
    newPassword = newPasswordEntry.get()
    confirmPassword = confirmPasswordEntry.get()
    if emailEntry != "" and newPassword != "" and confirmPassword != "":
        conn = sqlite3.connect("loginfo.db")
        cursor = conn.cursor()
        if newPassword == confirmPassword:
            selectEmail = """SELECT * FROM login_data WHERE email=?"""
            cursor.execute(selectEmail, [(email)])
            if cursor.fetchall():
                passwordUpdate = """UPDATE login_data SET password=? WHERE email=?"""
                cursor.execute(passwordUpdate, [(newPassword), (email)])
                messagebox.showinfo(
                    title="info", message="Password succcessfully updated."
                )
                emailEntry.delete(0, END)
                newPasswordEntry.delete(0, END)
                confirmPasswordEntry.delete(0, END)
            else:
                messagebox.showerror(title="error", message="invalid credentials")
        else:
            messagebox.showerror(title="error", message="Passwords do not match")
        conn.commit()
        conn.close()
    else:
        messagebox.showerror(title="error", message="invalid credentials")


# LABEL

# login
resetPasswordLabel = Label(
    win3, text="RESET PASSWORD", font=("ariel", 20, "bold"), bg="white", fg="#2f8be0"
)
resetPasswordLabel.place(x=520, y=140)

# email
emailLabel = Label(win3, text="Email", font=("ariel", 12), bg="white", fg="#2f8be0")
emailLabel.place(x=520, y=180)

# create password
newPasswordLabel = Label(
    win3, text="New Password", font=("ariel", 12), bg="white", fg="#2f8be0"
)
newPasswordLabel.place(x=520, y=245)

# confirm password
confirmPasswordLabel = Label(
    win3, text="Confirm Password", font=("ariel", 12), bg="white", fg="#2f8be0"
)
confirmPasswordLabel.place(x=520, y=325)

# ENTRY
# email
emailEntry = Entry(win3, width=24, font=("ariel", 15), relief=SUNKEN)
emailEntry.place(x=520, y=210)

# create password
newPasswordEntry = Entry(win3, width=24, font=("ariel", 15), show="*", relief=SUNKEN)
newPasswordEntry.place(x=520, y=270)

# confirm password
confirmPasswordEntry = Entry(
    win3, width=24, font=("ariel", 15), show="*", relief=SUNKEN
)
confirmPasswordEntry.place(x=520, y=350)


# BUTTON


# back button
backBtn = Button(
    win3,
    text="BACK",
    font=("ariel", 10),
    fg="white",
    bg="#2f8be0",
    width=15,
    height=2,
    borderwidth=1,
    command=backLogin,
)
backBtn.place(x=520, y=430)

# reset button
resetBtn = Button(
    win3,
    text="RESET",
    font=("ariel", 10),
    fg="white",
    bg="#2f8be0",
    width=15,
    height=2,
    borderwidth=1,
    command=resetPassword,
)
resetBtn.place(x=662, y=430)


# CHECKBUTTON
# show password
var = IntVar()
checkbtn1 = Checkbutton(
    win3,
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
    win3,
    text="Show Password",
    variable=var2,
    command=showPassword2,
    bg="white",
    font=("ariel", 10),
    fg="#2f8be0",
)
checkbtn2.place(x=520, y=380)

win3.mainloop()
