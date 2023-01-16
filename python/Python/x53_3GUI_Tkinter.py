from tkinter import *
c = 10000


def counter(label1):
    def count():
        global c

        label1.config(text=str(c))
        if c == 0:
            return
        c -= 1
        label1.after(1, count)
    count()


root = Tk()
w = 200
h = 200
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = (ws/2)-(w/2)
y = (hs/2)-(h/2)
root.geometry("%dx%d+%d+%d" % (w, h, x, y))
root.resizable(width=0, height=0)
label1 = Label(master=root, text="0", font=('tahoma', 30))
label1.pack()
counter(label1)
button1 = Button(master=root, text="Stop", width=20, command=root.destroy)
button1.pack()
root.mainloop()
