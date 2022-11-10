import tkinter
from tkinter import ttk

mainFrm = tkinter.Tk()
mainFrm.title("Employee Manager App")
mainFrm.configure(bg='lightblue')

innerFrm = tkinter.Frame(mainFrm)
innerFrm.pack()

# Personal Information Input
inputFrm = tkinter.LabelFrame(innerFrm, text="Personal Information Input")
inputFrm.grid(row=0, column=0)

lblName = tkinter.Label(inputFrm, text="Name: ")
lblName.grid(row=0, column=0)

lblAge = tkinter.Label(inputFrm, text="Age: ")
lblAge.grid(row=1, column=0)

lblGender = tkinter.Label(inputFrm, text="Gender: ")
lblGender.grid(row=2, column=0)

lblSalary = tkinter.Label(inputFrm, text="Salary (HUF): ")
lblSalary.grid(row=3, column=0)

lblEmail = tkinter.Label(inputFrm, text="Email: ")
lblEmail.grid(row=4, column=0)

txtBxName = tkinter.Text(inputFrm, height=1, font=('Arial', 10), width=20)
txtBxName.grid(row=0, column=1, pady=10, padx=10)

txtBxAge = tkinter.Text(inputFrm, height=1, font=('Arial', 10), width=20)
txtBxAge.grid(row=1, column=1, pady=10)

cmbBxGender = ttk.Combobox(inputFrm, height=1, font=('Arial', 10), width=17, values=["Male", "Female"])
cmbBxGender.grid(row=2, column=1, pady=10)

txtBxSalary = tkinter.Text(inputFrm, height=1, font=('Arial', 10), width=20)
txtBxSalary.grid(row=3, column=1, pady=10)

txtBxEmail = tkinter.Text(inputFrm, height=1, font=('Arial', 10), width=20)
txtBxEmail.grid(row=4, column=1, pady=10)

mainFrm.mainloop()