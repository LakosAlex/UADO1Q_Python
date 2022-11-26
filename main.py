import tkinter
import DB
from faker import *

import User

loginFrm = tkinter.Tk()
loginFrm.title("Login App")
loginFrm.configure(bg='lightblue')
innerFrm = tkinter.Frame(loginFrm)
innerFrm.pack()


def createLoginGUI():

    inputFrm = tkinter.LabelFrame(innerFrm, text="Login")
    inputFrm.grid(row=0, column=0)

    lblUsername = tkinter.Label(inputFrm, text="Username: ")
    lblUsername.grid(row=0, column=0)

    lblPassword = tkinter.Label(inputFrm, text="Password: ")
    lblPassword.grid(row=1, column=0)

    entryUsername = tkinter.Entry(inputFrm)
    entryUsername.grid(row=0, column=1)

    entryPssw = tkinter.Entry(inputFrm, show='*')
    entryPssw.grid(row=1, column=1)

    bttnLogin = tkinter.Button(inputFrm, text="Login", command=lambda: DB.checkLogin(User.UserLoginDto(entryUsername.get(), entryPssw.get())))
    bttnLogin.grid(row=2, columnspan=2)

    for widget in inputFrm.winfo_children():
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

    lblJobR = tkinter.Label(registFrm, text="Address: ")
    lblJobR.grid(row=4, column=0)

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
                               command=lambda: [DB.registerUser(entryUsernameR.get(), entryPsswR.get()),
                                                DB.insertUserIntoDB(User.UserEntity(entryUsernameR.get(), entryPsswR.get(),
                                                entryEmailR.get(), entryAddressR.get(), entryJobR.get(), entryPhoneNumberR.get())),
                                                emptyComponents(entryEmailR, entryAddressR, entryJobR, entryUsernameR, entryPsswR,entryPhoneNumberR),
                                                ])
    bttnRegister.grid(row=6, column=0)

    bttnFakeData = tkinter.Button(registFrm, text="Generate fake personal data",
                               command=lambda: generateFakeData(entryEmailR, entryAddressR, entryJobR, entryUsernameR,
                                                                entryPsswR, entryPhoneNumberR))
    bttnFakeData.grid(row=6, column=1)

    for widget in registFrm.winfo_children():
        if isinstance(widget, tkinter.Text):
            widget['font'] = ('Arial', 10)
            widget['height'] = 1
            widget['width'] = 20
        widget.grid_configure(padx=10, pady=10)
    loginFrm.mainloop()
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
    entryEmailR.delete(0, "end")
    entryAddressR.delete(0, "end")
    entryJobR.delete(0, "end")
    entryUsernameR.delete(0, "end")
    entryPsswR.delete(0, "end")
    entryPhoneNumberR.delete(0, "end")

DB.readDBFile()
loginGUI = createLoginGUI()
registrationGUI = createRegistrationGUI()