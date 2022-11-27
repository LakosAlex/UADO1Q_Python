from tkinter import messagebox
from HASH import *
import pymysql
import pymysql.cursors
from User import UserTreeViewDto

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
def checkLogin(userLoginDto):

    if userLoginDto.username == "" or userLoginDto.password == "":
        messagebox.showinfo("Login failed!", "Username or Password is missing!")
    else:
        connection = connectToDB()
        hash = getHashedPassword(userLoginDto.password)
        try:
            with connection:
                with connection.cursor() as cursor:
                    query = "SELECT `username`, `password` FROM `user` WHERE `username`=%s AND `password`=%s"
                    cursor.execute(query, (userLoginDto.username, hash))
                    result = cursor.fetchone()
                    print(result)
                    if result is None:
                        messagebox.showinfo("Login failed!", "Wrong credentials!")
                    else:
                        messagebox.showinfo("Login successful!", "Hey there, " + userLoginDto.username + "!")
        except pymysql.Error as e:
            messagebox.showinfo("Login failed!", e)
def insertUserIntoDB(userEntity):
    connection = connectToDB()
    hash = getHashedPassword(userEntity.password)
    if userEntity.username and userEntity.password and userEntity.email and userEntity.address and userEntity.job and userEntity.phoneNumber:
        try:
            with connection:
                with connection.cursor() as cursor:
                    query = "INSERT INTO `user` (`username`, `password`, `email`, `address`, `job`, `phone_number` ) " \
                            "VALUES (%s, %s, %s, %s, %s, %s)"
                    cursor.execute(query, (userEntity.username, hash, userEntity.email,
                                           userEntity.address, userEntity.job, userEntity.phoneNumber))
                connection.commit()
                messagebox.showinfo("Registration", "Registration successful!")
        except pymysql.Error as e:
            messagebox.showinfo("Registration failed", e)
    else:
        messagebox.showinfo("Registration failed", "Please fill in all the entries!")
def getAllUsers():
    users = []
    connection = connectToDB()
    try:
        with connection:
            with connection.cursor() as cursor:
                query = "SELECT `username`, `email` FROM `user`"
                cursor.execute(query)
                result = cursor.fetchall()
                if result is None:
                    messagebox.showinfo("Loading users", "Loading users was unsuccessful!")
                else:
                    for user in result:
                        print(user)
                        users.append(UserTreeViewDto(user["username"], user["email"]))
                    return users
    except pymysql.Error as e:
        messagebox.showinfo("Loading users failed!", e)



