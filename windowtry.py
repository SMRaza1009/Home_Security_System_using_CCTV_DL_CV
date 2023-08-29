from tkinter import *
import customtkinter

class user():
    def third():
        thr=Tk()
        thr.geometry("600x600")
        lab3=Label(thr,text="search window")
        lab3.pack()        

    def second(name1):
        sec=Tk()
        sec.geometry("400x400")
        lab2=Label(sec,text="user dashboard")
        lab2.pack()
        btn2=Button(sec,text=name1,command=user.third)
        btn2.pack()
           
    def d():
        user.second()
        root.destroy()
    
    def __init__(self,root):
        self.root=root
        self.root.geometry("200x200")
        lab1=Label(root,text="login window")
        lab1.pack()
        name1 ="Raza"
        btn1= Button(self.root,text="open second window",command=user.d(name1))
        btn1.pack()
        
        

    

root=Tk()
obj = user(root)
root.mainloop()