from email.mime import image
from fileinput import close
from sqlite3 import Cursor
from tkinter import *
import tkinter
from tkinter.font import BOLD
from turtle import heading
import customtkinter
from PIL import Image, ImageTk
from cv2 import BORDER_DEFAULT, BORDER_WRAP, destroyWindow
from tkinter import ttk
from tkinter import messagebox
import pymysql



class forget():
    def __init__(self,root):
        self.root=root
        self.root.geometry("500x800+650+150")
        self.root.title("HSS Forget Password")
        #customtkinter.set_appearance_mode("grey")
        self.root.resizable(0,0)
        self.root.config(bg="grey80")

        #background frame white
        backFrame = customtkinter.CTkFrame(self.root,fg_color="white",corner_radius=30)
        backFrame.place(width=500,height=630,x=0,y=200)

        #image frame
        imgFrame=customtkinter.CTkFrame(self.root,fg_color="grey65",bg_color="grey65",corner_radius=0)
        imgFrame.place(width=100,height=100,x=200,y=150)

        forgetImage = ImageTk.PhotoImage(Image.open("/home/syed/Desktop/FYP-Project/FYP_HSS_9_12_2021/Practice-GUI/button_images/forget.png").resize((130, 140)))        

        button_1 = customtkinter.CTkButton(imgFrame,image=forgetImage,text="",text_font=("Helvetica",16,"bold") ,width=100, height=120, fg_color="grey65", corner_radius=12,hover_color=None)
        button_1.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        
        #backFrame Content
        email = customtkinter.CTkLabel(backFrame, text="Email", text_font=("Helvetica",16, "bold"))
        email.place(x=190, y=110)
        
        self.eEmail = customtkinter.CTkEntry(backFrame,text_font=("Helvetica",14), bg_color="white", fg_color="lightgrey", corner_radius=10)
        self.eEmail.place(x=100, y= 140,width=300)
               
        securityQuestion = customtkinter.CTkLabel(backFrame,text="Security Question",text_font=("Helvetica",16, "bold"))
        securityQuestion.place(width=200,x=150,y=190)

        self.eSecurityQuestion=ttk.Combobox(backFrame ,font=("Helvetica",12),state="readonly",background="lightgrey",foreground="black",justify=CENTER)
        self.eSecurityQuestion['values']=("Select","Your First Pet Name","Your Grand Father Name","Your Grand Mother Name","Your Favourite Hobby","Your Favourite Color","Your Birth Place","Your Best Friend Name")
        self.eSecurityQuestion.place(x=100,y="225",width="300", height=30)
        self.eSecurityQuestion.current(0)

        answere = customtkinter.CTkLabel(backFrame,text="Answer",text_font=("Helvetica",16, "bold"))
        answere.place(x=180,y=270)

        self.eAnswer=customtkinter.CTkEntry(backFrame,text_font=("Helvetica",12) ,bg_color="white",fg_color="lightgrey",corner_radius=10)
        self.eAnswer.place(x=100,y="300",width="300")

        newPassword = customtkinter.CTkLabel(backFrame,text="New Password",text_font=("Helvetica",16, "bold") )
        newPassword.place(x=180,y=345,width=150)

        self.eNewPassword=customtkinter.CTkEntry(backFrame,text_font=("Helvetica",12, "bold") ,bg_color="white",fg_color="lightgrey",corner_radius=10, show="*")
        self.eNewPassword.place(x=100,y="375",width="300")

        confirmPassword = customtkinter.CTkLabel(backFrame,text="Confirm Password",text_font=("Helvetica",16, "bold"))
        confirmPassword.place(x=150,y=430,width=200)

        self.eConfirmPassword=customtkinter.CTkEntry(backFrame,text_font=("Helvetica",12, "bold") ,bg_color="white",fg_color="lightgrey",corner_radius=10, show="*")
        self.eConfirmPassword.place(x=100,y="460",width="300")

        seperateLine=customtkinter.CTkFrame(backFrame,fg_color="darkblue")
        seperateLine.place(width=230,height=1.25,x=140,y=510)
        
         #clear text box 
        def clear():
            self.eEmail.delete(0,END)
            self.eNewPassword.delete(0,END)
            self.eAnswer.delete(0,END)
            self.eConfirmPassword.delete(0,END)

        #forget pass
        def forgetPassword():
            if self.eEmail.get()=="" or self.eNewPassword.get()=="" or self.eSecurityQuestion.get()=="Select" or self.eNewPassword.get()=="" or self.eConfirmPassword.get()=="":
                messagebox.showerror("Error","All fields are required")
            elif self.eNewPassword.get() != self.eConfirmPassword.get():
                    messagebox.showerror("Error","Password Must Be Same")    
            else:
                try:
                    con=pymysql.connect(host="localhost",user="root",password="",database="HSS")
                    cur=con.cursor()

                    
                    cur.execute("select * from User where email=%s and security =%s and answer =%s",
                                (
                                    self.eEmail.get(),
                                    self.eSecurityQuestion.get(),
                                    self.eAnswer.get()
                                ))
                    row=cur.fetchone()
                    
                    if row != None:
                        cur.execute("update User set password = %s where email=%s",(self.eNewPassword.get(),self.eEmail.get() ) )
                        con.commit()
                        messagebox.showinfo("Success","Password Updated Successfull")
                        clear()
                        root.destroy()
                        import userLogin

                    else:
                        messagebox.showerror("Error","Wrong Email or Security Answer")
                    
                    
                    
                    con.close()
                    
                except Exception as es:
                    messagebox.showerror("Error",str(es))
        
        resetImage = ImageTk.PhotoImage(Image.open("/home/syed/Desktop/FYP-Project/FYP_HSS_9_12_2021/Practice-GUI/button_images/reset.png").resize((30, 30)))
        resetBtn = customtkinter.CTkButton(backFrame,text="Reset",image=resetImage,cursor="hand2",fg_color="lightgrey",hover_color="grey60",text_font=("Helvetica",16,"bold"),command=forgetPassword)
        resetBtn.place(width=150,x=180,y=530, height=35)




root=customtkinter.CTk()
obj = forget(root)
root.mainloop()