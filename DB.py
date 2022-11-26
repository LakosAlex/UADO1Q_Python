from tkinter import messagebox
from User import *

users = []
def readDBFile():
    users.clear()
    try:
        with open('db.txt') as f:
            for line in f:
                list = (line.strip()).split(",", 1)
                users.append(User(list[0], list[1]))
    except IOError:
        messagebox.showinfo("Error", "The application could not read the database file!")

def checkLogin(username, password):
    checkNumber = 0
    if username == "" or password == "":
        messagebox.showinfo("Login failed!", "Username or Password is missing!")
    else:
        user = User(username, password)
        for obj in users:
            if obj.username == user.username and obj.password == user.password:
                messagebox.showinfo("Login successful!", "Hey there, " + user.username + "!")
                checkNumber = 1
        if checkNumber == 0:
            messagebox.showinfo("Login failed!", "Wrong credentials!")