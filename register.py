from cProfile import label
from email import message
from email.mime import image
from sqlite3 import Cursor
from tkinter import*
from tkinter import ttk
import tkinter
from turtle import width
import customtkinter
from PIL import Image,ImageTk
import re
from tkinter import messagebox
from click import command
import customtkinter
from numpy import equal, number
from tkinter import messagebox
import pymysql


class Register:
    def __init__(self,root):
        self.root = root
        self.root.title("HSS Registration Form")
        self.root.geometry("1650x900+150+70")
        self.root.resizable(width=FALSE,height=FALSE)
        self.root.config(bg="grey60")
        #customtkinter.set_appearance_mode("grey")
        
        
        # BG Image
        
        # self.bg = ImageTk.PhotoImage(file="/home/syed/Desktop/FYP-Project/FYP_HSS_9_12_2021/Practice-GUI/images/b6.jpg")
        # bg = Label(self.root, image=self.bg).place(x=0,y=0, relheight=1, relwidth=1)
        #title=customtkinter.CTkLabel(self.root, text="Home Security System ", text_font=("Helvetica", 25, "bold"),fg_color="grey68")
        #title.place(x=80,y=30, width=450, height=50)
        
        mainLabel = customtkinter.CTkLabel(master=self.root, text="Home Security System", width=850, height=120, corner_radius=18, text_font=("Helvetica", 20, "bold"),fg_color="grey71")
        mainLabel.place(x=770, y=75, anchor=tkinter.CENTER)
        
        # # LEFT Image
        self.left = ImageTk.PhotoImage(file="/home/syed/Desktop/FYP-Project/FYP_HSS_9_12_2021/Practice-GUI/images/reg2.png")
        leftImg = customtkinter.CTkLabel(self.root, image=self.left, corner_radius=20, fg_color="grey60")
        leftImg.place(x=80,y=280, height=480, width=520)
        
        # REGISTRATION Frame
        regFrame = customtkinter.CTkFrame(self.root, fg_color="grey70", corner_radius=18)
        regFrame.place(x=650, y=180, width=900, height=680)
        title=customtkinter.CTkLabel(regFrame, text="Registration Here", text_font=("Helvetica", 25, "bold"), fg_color="grey71")
        title.place(x=50,y=30, width=300, height=50)
        
        #-------------------ROW-1------------------------#
        
        firstName=Label(regFrame, text="First Name : ", font=("Helvetica", 12, "bold"),bg="grey71", fg="black").place(x=50,y=160)
        self.txt_firstName = customtkinter.CTkEntry(regFrame, text_font=("Helvetica", 12),fg_color="grey85")
        self.txt_firstName.place(x=150,y=155, width=250, height=30)
        
        
        
        lastName=Label(regFrame, text="Last Name : ", font=("Helvetica", 12, "bold"),bg="grey71", fg="black").place(x=510,y=160)
        self.txt_lastName = customtkinter.CTkEntry(regFrame,text_font=("Helvetica", 12),fg_color="grey85")
        self.txt_lastName.place(x=610,y=155, width=250, height=30)  
        
        
        #--------------------ROW-2-------------------------#
        
        contactNumber=Label(regFrame, text="Contact : ", font=("Helvetica", 12, "bold"),bg="grey71", fg="black").place(x=70,y=220)
        self.txt_contactNumber = customtkinter.CTkEntry(regFrame, text_font=("Helvetica", 12),fg_color="grey85")
        self.txt_contactNumber.place(x=150,y=215, width=250, height=30)
        
        email=Label(regFrame, text="Email : ", font=("Helvetica", 12, "bold"),bg="grey71", fg="black").place(x=545,y=220)
        self.txt_email = customtkinter.CTkEntry(regFrame, text_font=("Helvetica", 12),fg_color="grey85")
        self.txt_email.place(x=610,y=215, width=250, height=30)
        
        #--------------------ROW-2.1-------------------------#
        
        cnicNumber=Label(regFrame, text="CNIC : ", font=("Helvetica", 12, "bold"),bg="grey71", fg="black").place(x=90,y=280)
        self.txt_cnicNumber = customtkinter.CTkEntry(regFrame, text_font=("Helvetica", 12),fg_color="grey85")
        self.txt_cnicNumber.place(x=150,y=275, width=250, height=30)
        
        country=Label(regFrame, text="Country : ", font=("Helvetica", 12, "bold"),bg="grey71", fg="black").place(x=525,y=280)
        self.txt_country = customtkinter.CTkEntry(regFrame, text_font=("Helvetica", 12),fg_color="grey85")
        self.txt_country.place(x=610,y=275, width=250, height=30)
        
        #--------------------ROW-2.2-------------------------#
        
        state=Label(regFrame, text="State : ", font=("Helvetica", 12, "bold"),bg="grey71", fg="black").place(x=90,y=330)
        self.txt_state = customtkinter.CTkEntry(regFrame, text_font=("Helvetica", 12),fg_color="grey85")
        self.txt_state.place(x=150,y=325, width=250, height=30)
        
        city=Label(regFrame, text="City : ", font=("Helvetica", 12, "bold"),bg="grey71", fg="black").place(x=560,y=340)
        self.txt_city = customtkinter.CTkEntry(regFrame, text_font=("Helvetica", 12),fg_color="grey85")
        self.txt_city.place(x=610,y=335, width=250, height=30)
        
        
         #--------------------ROW-2.3-------------------------#
        
        address=Label(regFrame, text="Address : ", font=("Helvetica", 12, "bold"),bg="grey71", fg="black").place(x=65,y=390)
        self.txt_address = customtkinter.CTkEntry(regFrame, text_font=("Helvetica", 12),fg_color="grey85")
        self.txt_address.place(x=150,y=385, width=250, height=30)
        
        cmb_gender=Label(regFrame, text="Gender : ", font=("Helvetica", 12, "bold"),bg="grey71", fg="black").place(x=530,y=390)
        #txt_gender = customtkinter.CTkEntry(regFrame, text_font=("Helvetica", 12),fg_color="grey85").place(x=610,y=275, width=250, height=30)
        self.cmb_gender = ttk.Combobox(regFrame, font=("Helvetica", 12), state='readonly',justify=CENTER)
        self.cmb_gender['values']=("Select","Male","Female","Prefer not to say")
        self.cmb_gender.place(x=610,y=385, width=250, height=30)
        self.cmb_gender.current(0)
        
        
        #--------------------ROW-3-------------------------#
        
        secQuestion=Label(regFrame, text="Security : ", font=("Helvetica", 12, "bold"),bg="grey71", fg="black").place(x=65,y=440)
        
        self.cmb_secQuestion = ttk.Combobox(regFrame, font=("Helvetica", 12), state='readonly',justify=CENTER)
        #cmb_secQuestion = customtkinter.CTkFrame(regFrame, text_font=("Helvetica", 12), state='readonly',justify=CENTER)
        self.cmb_secQuestion['values']=("Select","Your First Pet Name","Your Grand Father Name","Your Grand Mother Name","Your Favourite Hobby","Your Favourite Color","Your Birth Place","Your Best Friend Name")
        self.cmb_secQuestion.place(x=150,y=435, width=250, height=30)
        self.cmb_secQuestion.current(0)
        
        
        answer=Label(regFrame, text="Answer : ", font=("Helvetica", 12, "bold"),bg="grey71", fg="black").place(x=530,y=440)
        self.txt_answer = customtkinter.CTkEntry(regFrame, text_font=("Helvetica", 12),fg_color="grey85")
        self.txt_answer.place(x=610,y=435, width=250, height=30)
        
        #--------------------ROW-4-------------------------#
        
        password=Label(regFrame, text="Password : ", font=("Helvetica", 12, "bold"),bg="grey71", fg="black").place(x=55,y=490)
        self.txt_password = customtkinter.CTkEntry(regFrame, text_font=("Helvetica", 12),fg_color="grey85", show="*")
        self.txt_password.place(x=150,y=485, width=250, height=30)
        
        
        confirmPassword=Label(regFrame, text="Confirm Password : ", font=("Helvetica", 12, "bold"),bg="grey71", fg="black").place(x=450,y=490)
        self.txt_confirmPassword = customtkinter.CTkEntry(regFrame, text_font=("Helvetica", 12),fg_color="grey85", show="*")
        self.txt_confirmPassword.place(x=610,y=485, width=250, height=30)
        
        
        def openLogin():
            root.destroy()
            import userLogin        
        
        
        def clearTextBox():
                self.txt_firstName.delete(0,END)
                self.txt_lastName.delete(0,END)
                self.txt_contactNumber.delete(0,END)
                self.txt_email.delete(0,END)
                self.txt_cnicNumber.delete(0,END)
                self.txt_country.delete(0,END)
                self.txt_state.delete(0,END)
                self.txt_city.delete(0,END)
                self.txt_address.delete(0,END)
                self.cmb_gender.current(0)
                self.cmb_secQuestion.current(0)
                self.txt_answer.delete(0,END)
                self.txt_password.delete(0,END)
                self.txt_confirmPassword.delete(0,END)


        def onClick():
                self.regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

                if self.txt_firstName.get() == "" or self.txt_lastName.get()=="" or self.txt_address.get()=="" or self.txt_contactNumber.get()=="" or self.txt_email.get()=="" or self.txt_cnicNumber.get()=="" or  self.txt_country.get()=="" or  self.txt_state.get()=="" or self.txt_city.get()=="" or self.txt_answer.get()=="" or self.txt_password.get()=="" or self.txt_confirmPassword.get()=="" or self.cmb_gender.get()=="Select" or self.cmb_secQuestion.get()=="Select":
                    messagebox.showerror("Error","All Fields Are Required")
                elif self.txt_password.get() != self.txt_confirmPassword.get():
                    messagebox.showerror("Error","Password Must Be Same")
                elif re.fullmatch(self.regex,self.txt_email.get()) == None:
                    messagebox.showerror("Error","Email Not Valid")   
                elif self.txt_contactNumber.get().isnumeric()== False :
                    messagebox.showerror("Error","Contact Must Be A Number")
                elif self.txt_cnicNumber.get().isnumeric()== False :
                    messagebox.showerror("Error","CNIC Must Be A Number")                       
                else:
                    try:
                                con = pymysql.connect(host="localhost",user="root",password="",database="HSS")
                                cur = con.cursor()
                                
                                #check email already exist
                                cur.execute("select * from User where Email=%s",self.txt_email.get())
                                row=cur.fetchone()

                                #if email already exist
                                if row != None:
                                        messagebox.showerror("Error","This Email Already Exist")
                                
                                #email dont exist
                                else:
                                        cur.execute("insert into User (firstName,lastName,contact,email, cnic, country , state , city ,address,gender,security,answer,password) values(%s,%s,%s, %s, %s, %s, %s, %s,%s,%s,%s,%s,%s)",
                                        
                                        (

                                                self.txt_firstName.get(),
                                                self.txt_lastName.get(),
                                                self.txt_contactNumber.get(),
                                                self.txt_email.get(),
                                                self.txt_cnicNumber.get(),
                                                self.txt_country.get(),
                                                self.txt_state.get(),
                                                self.txt_city.get(),
                                                self.txt_address.get(),
                                                self.cmb_gender.get(),
                                                self.cmb_secQuestion.get(),
                                                self.txt_answer.get(),
                                                self.txt_password.get()
                                        ))
                                        messagebox.showinfo("SuccessfullY","Registration Completed")
                                        clearTextBox()
                                        openLogin()

                                con.commit()
                                con.close()
                                        
                                
                    except Exception as es:
                            messagebox.showerror("Error",str(es))
                
        
        
        
        
        submitButton=customtkinter.CTkButton(regFrame,text="Registration Here", text_font=("bold"), command=onClick ,fg_color="grey60", hover="grey70")
        submitButton.place(x=680,y=620, width=180)
        
        def BackToLogin():
            root.destroy()
            import userLogin
            
        backToLoginButton=customtkinter.CTkButton(regFrame,text="Back To Login",text_font=("bold"), command=BackToLogin,fg_color="grey80", hover="grey70")
        backToLoginButton.place(x=500,y=620, width=150)
        

        
        
    
root =Tk()
obj = Register(root)
root.mainloop()
