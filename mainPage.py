from tkinter import*
from tkinter import ttk
import tkinter
from turtle import width
from customtkinter import *
import customtkinter
from PIL import Image,ImageTk 
import tensorflow as tf

    


class mainPage:
    def __init__(self,root):
        self.root = root
        self.root.title("Home Security System ")
        self.root.geometry("1250x750+250+50")
        self.root.resizable(width=FALSE,height=FALSE)
        #self.root.config(bg="grey67")
        customtkinter.set_appearance_mode("grey")
       
        
        
        # BG Image
        
        mainLabel = customtkinter.CTkLabel(master=self.root, text="Welcome to Home Security System", width=850, height=120, corner_radius=18, text_font=("Helvetica", 25, "bold"),fg_color="grey60")
        mainLabel.place(x=600, y=120, anchor=tkinter.CENTER)
        
        #self.bg = ImageTk.PhotoImage(file="/home/syed/Desktop/FYP-Project/FYP_HSS_9_12_2021/Practice-GUI/images/b6.jpg")
        #bg = Label(self.root, image=self.bg).place(x=350,y=0, relheight=1, relwidth=1)
        #title=Label(self.root, text="Welcome to Home Security System ", font=("Helvetica", 25, "bold"),bg="grey68", fg="black").place(x=80,y=30)
        
        # Main Frame
        loginFrame = customtkinter.CTkFrame(self.root,  corner_radius=18, fg_color="grey66")
        loginFrame.place(x=100, y=200, width=1000, height=490)
        
        # USER FRAME
        userFrame = customtkinter.CTkFrame(loginFrame, fg_color="grey66")
        userFrame.place(x=50, y=50, width=420, height=380)
        userCamImg = ImageTk.PhotoImage(Image.open('/home/syed/Desktop/FYP-Project/FYP_HSS_9_12_2021/Practice-GUI/images/cam.png').resize((140,80)))
        userCamImg = customtkinter.CTkButton(userFrame,image=userCamImg,text="",hover_color=None,fg_color="grey66")
        userCamImg.place(x=0,y=0)
        
        def userWindow():
            root.destroy()
            import userLogin
            
        userImg=ImageTk.PhotoImage(Image.open('/home/syed/Desktop/FYP-Project/FYP_HSS_9_12_2021/Practice-GUI/images/usr.png').resize((250, 250)))
        userImgBtn = customtkinter.CTkButton(userFrame,image=userImg,text="",hover_color=None,fg_color="grey66")
        userImgBtn.place(x=90,y=50)
        userLoginButton=customtkinter.CTkButton(userFrame, command=userWindow,text="User Login",corner_radius=30, width=140, height=40, text_font=("Helvetica", 13, "bold"), fg_color="grey60",hover_color="grey76")
        userLoginButton.place(x=150,y=300)
        
        #Seperater Frame
        sepFrame = customtkinter.CTkFrame(loginFrame, fg_color="black")
        sepFrame.place(x=520, y=100, width=3, height=280)
        
        
        
        # ADMIN FRAME
        adminFrame = customtkinter.CTkFrame(loginFrame, fg_color="grey66")
        adminFrame.place(x=530, y=50, width=420, height=380)
        def userWindow():
            root.destroy()
            import adminLogin
        adminImg=ImageTk.PhotoImage(Image.open('/home/syed/Desktop/FYP-Project/FYP_HSS_9_12_2021/Practice-GUI/images/admin.png').resize((180, 180)))
        adminImgBtn = customtkinter.CTkButton(adminFrame,image=adminImg,text="",hover_color=None,fg_color="grey66")
        adminImgBtn.place(x=140,y=80)
        adminLoginButton=customtkinter.CTkButton(adminFrame, command=userWindow, text="Admin Login",corner_radius=30, width=140, height=40, text_font=("Helvetica", 13, "bold"), fg_color="grey60",hover_color="grey76")
        adminLoginButton.place(x=150,y=300)
        
        
       
        
        
        
 
    
root =Tk()
obj = mainPage(root)
root.mainloop()        