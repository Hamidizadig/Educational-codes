from tkinter import *
from tkinter import messagebox
flag = FALSE


def calcSum(event):
    num1 = int(entry1.get())
    num2 = int(entry2.get())
    messagebox.showinfo("hello", str(num1+num2))


root = Tk()
w = 650
h = 300
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = (ws/2)-(w/2)
y = (hs/2)-(h/2)
root.geometry("%dx%d+%d+%d" % (w, h, x, y))
# root.config(bg="#009ab0")
label1 = Label(master=root, text="sharfix n1", width=10)
label1.grid(row=0, column=0, pady=4)
entry1 = Entry(master=root)
entry1.grid(row=0, column=1, pady=4)

label2 = Label(master=root, text="sharfix n2", width=10)
label2.grid(row=1, column=0, pady=5)
entry2 = Entry(master=root, text="123")
entry2.grid(row=1, column=1, pady=4)

button1 = Button(master=root, text='+', width=30)
button1.grid(row=2, column=0, columnspan=2)
button1.bind("<Button>", calcSum)
root.mainloop()
