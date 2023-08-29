from email.mime import image
from fileinput import close
from sqlite3 import Cursor
from tkinter import *
import tkinter
from tkinter.font import BOLD
from turtle import heading
import customtkinter
from PIL import Image, ImageTk
from cv2 import destroyWindow
from tkinter import ttk
from tkinter import messagebox
import pymysql


class admin():
    def __init__(self,root):
        self.root=root
        self.root.geometry("1200x750+100+0")
        self.root.title("HSS Admin Login")
        self.root.resizable(0,0)
        self.root.configure(background="grey67")
        
        #Admin Login Heading
        mainLabel = customtkinter.CTkLabel(master=self.root, text="Welcome to Admin Login", width=850, height=120, corner_radius=18, text_font=("Helvetica", 20, "bold"),fg_color="grey60")
        mainLabel.place(x=530, y=75, anchor=tkinter.CENTER)

        #left frame for image and other content

        leftFrame = customtkinter.CTkFrame(self.root,fg_color="white", corner_radius=20)
        leftFrame.place(width=600,height=550,x=20,y=160)

        mainHeading = customtkinter.CTkLabel(leftFrame,text="ＡＤＭＩＮ ＰＡＮＥＬ",text_font=("",24,"bold"))
        mainHeading.place(x=100,y=40,width=400)

        cctvImg = ImageTk.PhotoImage(Image.open("/home/syed/Desktop/FYP-Project/FYP_HSS_9_12_2021/Practice-GUI/button_images/cctv1.png").resize((350, 350))) 
        ImgBtn=customtkinter.CTkButton(leftFrame,image=cctvImg,text="",fg_color="white",hover_color="white",)
        ImgBtn.place(x=100,y=100)

        # LINE seperate
        seperateLine = customtkinter.CTkFrame(leftFrame,fg_color="black")
        seperateLine.place(width=470,height=1,x=70,y=450)

        heading = customtkinter.CTkLabel(leftFrame,text="𝘍𝘶𝘵𝘶𝘳𝘦 𝘰𝘧 𝘚𝘢𝘧𝘦 𝘚𝘦𝘤𝘶𝘳𝘪𝘵𝘺",text_font=("",16, "bold"),fg_color="white")
        heading.place(x=100,y=480,width=400)

        #right frame for admin login

        rightFrame=customtkinter.CTkFrame(self.root,fg_color="grey78",corner_radius=18)
        rightFrame.place(width=500,height=450,x=650,y=200)

        keyImg = ImageTk.PhotoImage(Image.open("/home/syed/Desktop/FYP-Project/FYP_HSS_9_12_2021/Practice-GUI/button_images/adminLoginImg.png").resize((100, 80))) 
        photoBtn = customtkinter.CTkButton(rightFrame,text="",image=keyImg,fg_color="grey78",hover_color="grey67")
        photoBtn.place(x=160,y=10, width=200, height=140)


        email=customtkinter.CTkLabel(rightFrame,text="Email : ",text_font=("helvetica",16,"bold"),fg_color="grey78")
        email.place(x=30,y=175)

        self.eEmail = customtkinter.CTkEntry(rightFrame,text_font=("helvetica",14),fg_color="white")
        self.eEmail.place(x=140,y=170,width=300)

        password=customtkinter.CTkLabel(rightFrame,text="Password : ",text_font=("helvetica",16,"bold"),fg_color="grey78")
        password.place(x=0,y=250,width=150)

        self.ePassword = customtkinter.CTkEntry(rightFrame,text_font=("helvetica",14),fg_color="white", show="*")
        self.ePassword.place(x=140,y=250,width=300)    
        
        #clear text box after login
        def clear():
            self.eEmail.delete(0,END)
            self.ePassword.delete(0,END)

        #login dataset 
        def adminLogin():
            if self.eEmail.get()=="" or self.ePassword.get()=="":
                messagebox.showerror("Error","Please Enter Email and Password")
            else:
                try:
                    con=pymysql.connect(host="localhost",user="root",password="",database="HSS")
                    cur=con.cursor()

                    cur.execute("select * from Admin where email=%s and password=%s",(self.eEmail.get(),self.ePassword.get() ) )
                    row=cur.fetchone()
                    
                    if row ==None:
                        messagebox.showerror("Error","Email or Password is incorrect")
                    
                    else:
                        messagebox.showinfo("Login","Login Successfull")
                        clear()
                    con.close()
                except Exception as es:
                    messagebox.showerror("Error",str(es))    

        img = ImageTk.PhotoImage(Image.open("/home/syed/Desktop/FYP-Project/FYP_HSS_9_12_2021/Practice-GUI/button_images/loginbtn.png").resize((30, 30))) 
        loginBtn=customtkinter.CTkButton(rightFrame,image=img,text="Login",cursor="hand2",text_font=("helvetica",12),fg_color="grey60",hover_color="grey70",text_color="white", command=adminLogin)
        loginBtn.place(x=290,y=320,width=150)

root=customtkinter.CTk()
obj=admin(root)
root.mainloop()