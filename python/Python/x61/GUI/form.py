from tkinter import *

root=Tk()
w=600
h=300
ws=root.winfo_screenwidth()
hs=root.winfo_screenheight()
x=(ws/2)-(w/2)
y=(hs/2)-(h/2)
root.geometry("%dx%d+%d+%d"%(w,h,x,y))
frame1=Frame(master=root,bg="#ffff00",width=650,height=150)
frame1.pack()
frame2=Frame(master=root,bg="#00ffff",width=650,height=150)
frame2.pack()

label1=Label(master=frame1,text="hismus")
label2=Label(master=frame2,text="kafizuq")
label1.place(x=100,y=30)
label2.place(x=250,y=100)
root.mainloop()