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

txtBxName = tkinter.Text(inputFrm)
txtBxName.grid(row=0, column=1)

txtBxAge = tkinter.Text(inputFrm)
txtBxAge.grid(row=1, column=1)

cmbBxGender = ttk.Combobox(inputFrm, height=1, font=('Arial', 10), width=17, values=["Male", "Female"])
cmbBxGender.grid(row=2, column=1)

txtBxSalary = tkinter.Text(inputFrm)
txtBxSalary.grid(row=3, column=1)

txtBxEmail = tkinter.Text(inputFrm)
txtBxEmail.grid(row=4, column=1)

for widget in inputFrm.winfo_children():
    if isinstance(widget, tkinter.Text):
        widget['font'] = ('Arial', 10)
        widget['height'] = 1
        widget['width'] = 20
    widget.grid_configure(padx=10, pady=10)



mainFrm.mainloop()