from tkinter import *
flag = FALSE


def btnOk_Click(event):
    global flag
    if flag == False:
        lable1.config(text="Hello")
        button1.config(bg='red', fg='#ffffff')
        flag = True
    else:
        lable1.config(text='hello')
        button1.config(bg='green', fg='#000000')
        flag = False


root = Tk()
w = 600
h = 300
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = (ws/2)-(w/2)
y = (hs/2)-(h/2)
root.geometry("%dx%d+%d+%d" % (w, h, x, y))
lable1 = Label(master=root, text="hello", width=30)
lable1.pack()
button1 = Button(master=root, text="ok", bg="green", width=30)
button1.pack()
button1.bind("<Button>", btnOk_Click)
root.mainloop()
