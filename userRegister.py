from cProfile import label
from email import message
from email.mime import image
from sqlite3 import Cursor
from tkinter import *
from tkinter import ttk
from turtle import bgcolor
from PIL import ImageTk
from click import command
import customtkinter



class userRegister():
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x600+150+50")
        self.root.resizable(0,0)
        self.root.title("Registration")

        frame1=Frame(self.root,background="darkblue",width="400",height="600")
        frame1.place(x="0",y="0")

        

        
        frame2=Frame(self.root,background="white",width="700",height="600")
        frame2.place(x="400",y="0")

       

        

#REGISTRATION FORM in frame 2
        heading2=Label(frame2,text="REGISTRATION",font="bold 25",background="white",foreground="darkblue")
        heading2.place(x="50",y="20")
        
        self.fname = Label(frame2,text="FIRST NAME",font=("times new roman",15),background="white",foreground="black")
        self.fname.place(x="50",y="100")
        self.efname=Entry(frame2,font=("times new roman",12),border="2",background="lightgrey",foreground="black")
        self.efname.place(x="50",y="130",width="250")

        self.lname = Label(frame2,text="LAST NAME",font=("times new roman",15),background="white",foreground="black")
        self.lname.place(x="400",y="100")
        self.efname=Entry(frame2,font=("times new roman",12),border="2",background="lightgrey",foreground="black")
        self.efname.place(x="400",y="130",width="250")

        self.email = Label(frame2,text="EMAIL",font=("times new roman",15),background="white",foreground="black")
        self.email.place(x="50",y="170")
        self.eemail=Entry(frame2,font=("times new roman",12),border="2",background="lightgrey",foreground="black")
        self.eemail.place(x="50",y="200",width="250")

        self.contact = Label(frame2,text="CONTACT",font=("times new roman",15),background="white",foreground="black")
        self.contact.place(x="400",y="170")
        self.econtact=Entry(frame2,font=("times new roman",12),border="2",background="lightgrey",foreground="black")
        self.econtact.place(x="400",y="200",width="250")

        self.address = Label(frame2,text="ADDRESS",font=("times new roman",15),background="white",foreground="black")
        self.address.place(x="50",y="240")
        self.eaddress=Entry(frame2,font=("times new roman",12) ,border="2",background="lightgrey",foreground="black")
        self.eaddress.place(x="50",y="270",width="250")

        self.gender = Label(frame2,text="GENDER ",font=("times new roman",15),background="white",foreground="black")
        self.gender.place(x="400",y="240")
        self.egender=ttk.Combobox(frame2,font=("times new roman",12),state="readonly",background="lightgrey",foreground="black")
        self.egender['values']=("Male","Female")
        self.egender.place(x="400",y="270",width="250")
        self.egender.current(0)

        self.password = Label(frame2,text="PASSWORD",font=("times new roman",15),background="white",foreground="black")
        self.password.place(x="50",y="310")
        self.epassword=Entry(frame2,font=("times new roman",12),border="2",background="lightgrey",foreground="black")
        self.epassword.place(x="50",y="340",width="250")

        self.confirmpassword = Label(frame2,text="CONFIRM PASSWORD",font=("times new roman",15),background="white",foreground="black")
        self.confirmpassword.place(x="400",y="310")
        self.epassword=Entry(frame2,font=("times new roman",12) ,border="2",background="lightgrey",foreground="black")
        self.epassword.place(x="400",y="340",width="250")

        self.securityQuestion = Label(frame2,text="SECURITY QUESTION",font=("times new roman",15),background="white",foreground="black")
        self.securityQuestion.place(x="50",y="380")
        self.eSecurityQuestion=ttk.Combobox(frame2,font=("times new roman",12),state="readonly",background="lightgrey",foreground="black")
        self.eSecurityQuestion['values']=("Place Of Birth","Favourite Country","First Salary")
        self.eSecurityQuestion.place(x="50",y="410",width="250")
        self.eSecurityQuestion.current(0)

        self.answere = Label(frame2,text="ANSWERE",font=("times new roman",15),background="white",foreground="black")
        self.answere.place(x="400",y="380")
        self.eAnswere=Entry(frame2,font=("times new roman",12) ,border="2",background="lightgrey",foreground="black")
        self.eAnswere.place(x="400",y="410",width="250")

        def click():
                print("btn working")

        self.regBtn =customtkinter.CTkButton(frame2,text="REGISTER",cursor="hand2",command=click,text_font=("times new roman",16,"bold"),fg_color=("darkblue"),text_color=("white"),hover_color=("blue"))
        self.regBtn.place(width="180",height="40",x="250",y="500")

        
        
#registration form end

#frame1 content 


        
        self.heading=Label(frame1,text="HOME",font="bold 25",background="#1d0790",foreground="white")
        self.heading.place(x="10",y="20")
        self.subheading=Label(frame1,text="SECURITY",font="bold 25",background="#1d0790",foreground="white")
        self.subheading.place(x="10",y="60")

        self.content=Label(frame1,text="Provide Full Proof ",background="#1d0790",foreground="white",font=("times new roman",18))
        self.content.place(x="10",y="230")
        self.subcontent=Label(frame1,text="Security To House ",background="#1d0790",foreground="white",font=("times new roman",18))
        self.subcontent.place(x="10",y="270")

        self.haveAccount = Label(frame1,text="Already Have An Account",font=("times new roman",12),background="#1d0790",foreground="white")
        self.haveAccount.place(x="25",y="450")

        def loginWindow():
                root.destroy()
                import userLogin
                
        self.loginBtn = Button(frame1,text="LOGIN",font=("times new roman",12),command=loginWindow,cursor="hand2",background="white",foreground="darkblue")
        self.loginBtn.place(x="50",y="500",width="110",height="35")

     
        

root = Tk()
ob = userRegister(root)
root.mainloop()
