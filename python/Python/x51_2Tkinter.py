from tkinter import *
flag = FALSE

root = Tk()
w = 600
h = 300
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = (ws/2)-(w/2)
y = (hs/2)-(h/2)
root.geometry("%dx%d+%d+%d" % (w, h, x, y))

root.mainloop()
