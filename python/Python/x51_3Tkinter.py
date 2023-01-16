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
frame1=Frame(master=root,bg='red')
frame1.pack(side=TOP,fill=BOTH,expand=True)
label1=Label(master=frame1,text='sharmita',bg="#a1a1a1")
label1.place(x=100,y=20)

root.geometry("%dx%d+%d+%d" % (w, h, x, y))
frame2=Frame(master=root,bg='green',width=325,height=100)
frame2.pack(side=LEFT)
label2=Label(master=frame2,text='sharmita',bg="#a1a1a1")
label2.place(x=100,y=20)

root.geometry("%dx%d+%d+%d" % (w, h, x, y))
frame3=Frame(master=root,bg='blue',width=325,height=100)
frame3.pack(side=RIGHT)
label3=Label(master=frame3,text='sharmita',bg="#a1a1a1")
label3.place(x=100,y=20)


root.mainloop()
