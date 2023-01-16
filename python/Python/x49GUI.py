from tkinter import * 
root=Tk()
root.title("Python GUI")
# root.iconbitmap('icons/p')
root.geometry('%dx%d+%d+%d'%(600,120,500,200))
label1=Label(master=root,text="shapex",bg="#FF00FF",fg="yellow",width="30",
             height="3",font=('arial'),cursor='heart',anchor='nw',relief=RAISED)
label1.pack()

label2=Label(root,text="xsman.com")
label2.pack()
root.mainloop()