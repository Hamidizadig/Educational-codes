from tkinter import *
def fun1():
    print("hello")
root=Tk()
w=600
h=300
ws=root.winfo_screenwidth()
hs=root.winfo_screenheight()
x=(ws/2)-(w/2)
y=(hs/2)-(h/2)
root.geometry("%dx%d+%d+%d"%(w,h,x,y))
label1=Label(root,font=('tahoma',20),text='kasifiaz')
label1.pack()

message1=Message(root,relief=RAISED,text="fghbnjkml,kjhgfcgvhbjnkmlkltvgbhnjmk,lkmjnhgfkm")
message1.pack()
label1.config(text='confisus',fg="red")
label1.after(5000,fun1)
label1.config(text='xlux',fg='red')

root.mainloop()