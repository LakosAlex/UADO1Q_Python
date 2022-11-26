import tkinter
import DB
def createLoginGUI():
    loginFrm = tkinter.Tk()
    loginFrm.title("Login App")
    loginFrm.configure(bg='lightblue')

    innerFrm = tkinter.Frame(loginFrm)
    innerFrm.pack()

    inputFrm = tkinter.LabelFrame(innerFrm, text="Login")
    inputFrm.grid(row=0, column=0)

    lblName = tkinter.Label(inputFrm, text="Username: ")
    lblName.grid(row=0, column=0)

    lblAge = tkinter.Label(inputFrm, text="Password: ")
    lblAge.grid(row=1, column=0)

    entryUsername = tkinter.Entry(inputFrm)
    entryUsername.grid(row=0, column=1)

    entryPssw = tkinter.Entry(inputFrm, show='*')
    entryPssw.grid(row=1, column=1)

    bttnLogin = tkinter.Button(inputFrm, text="Login", command=lambda: DB.checkLogin(entryUsername.get(), entryPssw.get()))
    bttnLogin.grid(row=2, columnspan=2)

    for widget in inputFrm.winfo_children():
        if isinstance(widget, tkinter.Text):
            widget['font'] = ('Arial', 10)
            widget['height'] = 1
            widget['width'] = 20
        widget.grid_configure(padx=10, pady=10)

    loginFrm.mainloop()

DB.readDBFile()

loginGUI = createLoginGUI()