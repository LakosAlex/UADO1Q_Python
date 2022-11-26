from tkinter import messagebox
from HASH import *
from User import *
import pymysql
import pymysql.cursors
users = []

def connectToDB():
    connection = pymysql.connect(host="sql7.freemysqlhosting.net",
                                     port=3306,
                                     user="sql7580972",
                                     password="4sL98xD5s7",
                                     db="sql7580972",
                                     charset="utf8",
                                     cursorclass=pymysql.cursors.DictCursor)
    return connection
def readDBFile():
    users.clear()
    try:
        with open('db.txt') as f:
            for line in f:
                list = (line.strip()).split(",", 1)
                users.append(User(list[0], list[1]))
            f.close()
    except IOError:
        messagebox.showinfo("Error", "The application could not read the database file!")
def checkLogin(userLoginDto):

    if userLoginDto.username == "" or userLoginDto.password == "":
        messagebox.showinfo("Login failed!", "Username or Password is missing!")
    else:
        connection = connectToDB()
        hash = getHashedPassword(userLoginDto.password)
        try:
            with connection:
                with connection.cursor() as cursor:
                    query = "SELECT `username`, `password` FROM `user` WHERE `username`=%s"
                    cursor.execute(query, (userLoginDto.username))
                    result = cursor.fetchone()
                    print(result)
                    if result is None:
                        messagebox.showinfo("Login failed!", "Wrong credentials!")
                    else:
                        messagebox.showinfo("Login successful!", "Hey there, " + userLoginDto.username + "!")
        except pymysql.Error as e:
            messagebox.showinfo("Fail", e)
def registerUser(username, password):
    checkNumber = 0
    if username == "" or password == "" or str(username).__contains__(",") or str(password).__contains__(","):
        messagebox.showinfo("Registration failed!", "Username or Password not accepted!")
    else:
        user = User(username, password)
        for obj in users:
            if obj.username == user.username:
                messagebox.showinfo("Registration failed!", "The username " + user.username + " is already in use!")
                checkNumber = 1
        if checkNumber == 0:
            users.append(user)
            messagebox.showinfo("Registration successful!", "The user was registered!")
            refreshDB()
def refreshDB():
    try:
        file = open("db.txt", "w")
        for user in users:
            file.write(user.username + "," + user.password + "\n")
        file.close()
    except IOError:
        messagebox.showinfo("Error", "The application could not read the database file!")
    readDBFile()
def insertUserIntoDB(userEntity):
    connection = connectToDB()
    hash = getHashedPassword(userEntity.password)
    try:
        with connection:
            with connection.cursor() as cursor:
                query = "INSERT INTO `user` (`username`, `password`, `email`, `address`, `job`, `phone_number` ) " \
                      "VALUES (%s, %s, %s, %s, %s, %s)"
                cursor.execute(query, (userEntity.username, hash, userEntity.email,
                                     userEntity.address, userEntity.job, userEntity.phoneNumber))
            connection.commit()
    except pymysql.Error as e:
        messagebox.showinfo("Fail", e)



