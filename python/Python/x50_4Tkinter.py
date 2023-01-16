from tkinter import *
# def fun1(event):
#     print("funtion Actived")
def fun1(event):
    print("in")
def fun2(event):
    print("aut")
root=Tk()
w=600
h=300
ws=root.winfo_screenwidth()
hs=root.winfo_screenheight()
x=(ws/2)-(w/2)
y=(hs/2)-(h/2)
root.geometry("%dx%d+%d+%d"%(w,h,x,y))
button1=Button(master=root,text="ok",fg='green',width='20')
# button1.bind('<Button>',fun1)
# button1.bind('<Double-1>',fun1)
button1.bind('<Enter>',fun1)
button1.bind('<Leave>',fun2)
button1.pack()

root.mainloop()