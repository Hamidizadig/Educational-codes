from tkinter import *
from tkinter import messagebox

root = Tk()
w = 650
h = 300
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = (ws/2)-(w/2)
y = (hs/2)-(h/2)
root.geometry("%dx%d+%d+%d" % (w, h, x, y))
root.resizable(width=0, height=1)
root.columnconfigure(1, weight=0)
root.columnconfigure(2, weight=1)
root.columnconfigure(2, weight=3)
root.columnconfigure(3, weight=2)

label = Label(master=root, text="Hello1")
label.grid(row=0, column=0, pady=5, padx=5)

label2 = Label(master=root, text="hello2")
label2.grid(row=0, column=1, pady=5, padx=5)

label3 = Label(master=root, text="hello3")
label3.grid(row=1, column=0, pady=5, padx=5)

label4 = Label(master=root, text="hello4")
label4.grid(row=1, column=1, pady=5, padx=5)

label5 = Label(master=root, text="hello5", width=20, bg="red")
label5.grid(row=2, column=0, pady=5, padx=5)

label6 = Label(master=root, text="hello5", width=20, bg="blue")
label6.grid(row=1, column=3, pady=5, padx=5)

root.mainloop()
