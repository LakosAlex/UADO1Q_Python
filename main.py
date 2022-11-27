import tkinter
from tkinter.filedialog import asksaveasfile
from tkinter.ttk import Treeview
import DB
from faker import *
import User

mainFrm = tkinter.Tk()
mainFrm.title("Login App")
mainFrm.configure(bg='black')
innerFrm = tkinter.Frame(mainFrm, bg='#F5F1EA')
innerFrm.pack()

def createLoginGUI():

    loginFrm = tkinter.LabelFrame(innerFrm, text="Login")
    loginFrm.grid(row=0, column=0)

    lblUsername = tkinter.Label(loginFrm, text="Username: ")
    lblUsername.grid(row=0, column=0)

    lblPassword = tkinter.Label(loginFrm, text="Password: ")
    lblPassword.grid(row=1, column=0)

    entryUsername = tkinter.Entry(loginFrm)
    entryUsername.grid(row=0, column=1)

    entryPssw = tkinter.Entry(loginFrm, show='*')
    entryPssw.grid(row=1, column=1)

    bttnLogin = tkinter.Button(loginFrm, text="Login", command=lambda: DB.checkLogin(User.UserLoginDto(entryUsername.get(), entryPssw.get())))
    bttnLogin.grid(row=2, columnspan=2)

    for widget in loginFrm.winfo_children():
        if isinstance(widget, tkinter.Text):
            widget['font'] = ('Arial', 10)
            widget['height'] = 1
            widget['width'] = 20
        widget.grid_configure(padx=10, pady=10)
def createRegistrationGUI():

    registFrm = tkinter.LabelFrame(innerFrm, text="Registration")
    registFrm.grid(row=0, column=1)

    lblUsernameR = tkinter.Label(registFrm, text="Username: ")
    lblUsernameR.grid(row=0, column=0)

    lblPasswordR = tkinter.Label(registFrm, text="Password: ")
    lblPasswordR.grid(row=1, column=0)

    lblEmailR = tkinter.Label(registFrm, text="Email: ")
    lblEmailR.grid(row=2, column=0)

    lblAddressR = tkinter.Label(registFrm, text="Address: ")
    lblAddressR.grid(row=3, column=0)

    lblJobR = tkinter.Label(registFrm, text="Job: ")
    lblJobR.grid(row=4, column=0)

    lblPhoneNumberR = tkinter.Label(registFrm, text="Phone Number: ")
    lblPhoneNumberR.grid(row=5, column=0)

    entryUsernameR = tkinter.Entry(registFrm)
    entryUsernameR.grid(row=0, column=1)

    entryPsswR = tkinter.Entry(registFrm, show='*')
    entryPsswR.grid(row=1, column=1)

    entryEmailR = tkinter.Entry(registFrm)
    entryEmailR.grid(row=2, column=1)

    entryAddressR = tkinter.Entry(registFrm)
    entryAddressR.grid(row=3, column=1)

    entryJobR = tkinter.Entry(registFrm)
    entryJobR.grid(row=4, column=1)

    entryPhoneNumberR = tkinter.Entry(registFrm)
    entryPhoneNumberR.grid(row=5, column=1)

    bttnRegister = tkinter.Button(registFrm, text="Register",
                               command=lambda:  [DB.insertUserIntoDB(User.UserEntity(entryUsernameR.get(), entryPsswR.get(), entryEmailR.get(), entryAddressR.get(), entryJobR.get(), entryPhoneNumberR.get())),
                                                emptyComponents(entryEmailR, entryAddressR, entryJobR, entryUsernameR, entryPsswR, entryPhoneNumberR)
                                                ])
    bttnRegister.grid(row=6, column=0)

    bttnFakeData = tkinter.Button(registFrm, text="Generate",
                               command=lambda: generateFakeData(entryEmailR, entryAddressR, entryJobR, entryUsernameR,
                                                                entryPsswR, entryPhoneNumberR))
    bttnFakeData.grid(row=6, column=1)

    for widget in registFrm.winfo_children():
        if isinstance(widget, tkinter.Text):
            widget['font'] = ('Arial', 10)
            widget['height'] = 1
            widget['width'] = 20
        widget.grid_configure(padx=10, pady=10)
def generateFakeData(entryEmailR, entryAddressR, entryJobR, entryUsernameR, entryPsswR, entryPhoneNumberR):
    fake = Faker("hu_HU")
    entryEmailR.delete(0, "end")
    entryEmailR.insert(0, fake.ascii_free_email())
    entryAddressR.delete(0, "end")
    address = str(fake.street_address_with_county()).split("\n", 2)
    entryAddressR.insert(0, address[0] + ", " + address[1] + ", " + address[2])
    entryJobR.delete(0, "end")
    entryJobR.insert(0, fake.job())
    username = entryEmailR.get().split("@", 1)
    entryUsernameR.delete(0, "end")
    entryUsernameR.insert(0, username[0])
    entryPsswR.delete(0, "end")
    entryPhoneNumberR.delete(0, "end")
    entryPhoneNumberR.insert(0, fake.phone_number())
def emptyComponents(entryEmailR, entryAddressR, entryJobR, entryUsernameR, entryPsswR, entryPhoneNumberR):
    if entryEmailR.get() != "" and entryAddressR.get() != "" and entryJobR.get() != "" and entryUsernameR.get() != "" and entryPsswR.get() != "" and entryPhoneNumberR.get() != "":
        entryEmailR.delete(0, "end")
        entryAddressR.delete(0, "end")
        entryJobR.delete(0, "end")
        entryUsernameR.delete(0, "end")
        entryPsswR.delete(0, "end")
        entryPhoneNumberR.delete(0, "end")
def createDataOutputGUI():
    dOutputFrm = tkinter.LabelFrame(innerFrm, text="Registered Users")
    dOutputFrm.grid(row=1, columnspan=2)

    tv = Treeview(dOutputFrm)
    tv['columns'] = ('Username', 'Email')
    tv.heading('#0', text='')
    tv.column('#0', width=0)
    tv.heading('Username', text='Username')
    tv.column('Username', anchor='center', width=200)
    tv.heading('Email', text='Email')
    tv.column('Email', anchor='center', width=350)
    DB.getAllUsers()
    fillTreeView(tv)

    bttnRefresh = tkinter.Button(dOutputFrm, text="Refresh", command=lambda: fillTreeView(tv))
    bttnRefresh.grid(row=1, columnspan=1)

    bttnSave = tkinter.Button(dOutputFrm, text="Save to file", command=lambda: saveTreeView(tv))
    bttnSave.grid(row=2, columnspan=1)

    for widget in dOutputFrm.winfo_children():
        widget.grid_configure(padx=10, pady=10)

    mainFrm.mainloop()
def fillTreeView(tv):
    for row in tv.get_children():
        tv.delete(row)
    users = DB.getAllUsers()
    for user in users:
        tv.insert('', 'end', values=(user.username, user.email))
    tv.grid(sticky=("N", "S", "W", "E"))
    tv.grid_rowconfigure(0, weight=1)
    tv.grid_columnconfigure(0, weight=1)
def saveTreeView(tv):
    name = asksaveasfile(mode='w', defaultextension='.txt')
    userList = []
    for row in tv.get_children():
        userList.append(tv.item(row)['values'])
    for user in userList:
        name.write("Username: " + user.__getitem__(0) + " | Email: " + user.__getitem__(1) + "\n")
    name.close()


createLoginGUI()
createRegistrationGUI()
createDataOutputGUI()
