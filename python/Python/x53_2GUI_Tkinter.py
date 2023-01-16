from tkinter import *
from tkinter import messagebox
from tkinter import font


def move(event):
    print(event.x, event.y)


root = Tk()
w = 200
h = 200
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = (ws/2)-(w/2)
y = (hs/2)-(h/2)
root.geometry("%dx%d+%d+%d" % (w, h, x, y))
root.resizable(width=0, height=0)
message = Message(
    master=root, text='sdfghyjukiolpedrftgyhutyguhijihgftr6tyguhj')
message.config(bg="#f07", font=('tahoma', 15))
message.pack(ipadx=3, ipady=3)
message.bind("<Enter>", move)
root.mainloop()
