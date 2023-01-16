from tkinter import *
flag = FALSE

root = Tk()
w = 650
h = 300
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = (ws/2)-(w/2)
y = (hs/2)-(h/2)
root.geometry("%dx%d+%d+%d" % (w, h, x, y))
root.config(bg="#00aa80")
label1=Label(master=root,text="sharfix",bg='#a1a1a1',width=20)
label1.grid(row=0,column=0)
button1=Button(master=root,text="ok",bg="#990080",width=20)
button1.grid(row=0,column=1,padx=5,pady=5)

root.geometry("%dx%d+%d+%d" % (w, h, x, y))
label2=Label(master=root,text="sharfix",bg='#a1a1a1',width=20)
label2.grid(row=1,column=0,pady=5)
button2=Button(master=root,text="ok",bg="#990080",width=20)
button2.grid(row=1,column=1,padx=5)


root.mainloop()
