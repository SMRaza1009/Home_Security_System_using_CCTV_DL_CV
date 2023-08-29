from decimal import ROUND_CEILING
from email.mime import image
from fileinput import close
from lib2to3.pgen2.token import LEFTSHIFT
from logging import root
from sqlite3 import Cursor
from tkinter import *
import tkinter
from tkinter.font import BOLD
from turtle import heading
from webbrowser import BackgroundBrowser
import customtkinter
from PIL import Image, ImageTk
from cv2 import destroyWindow, resize
from tkinter import messagebox
import pymysql



class userDashboard():
    
    
     def __init__(self,root):
        self.root = root 
        #self.root = Tk()
        #dashboard.withdraw()
        self.root.title("User Dashboard")
        root.geometry("1650x930+140+50")
        root.resizable(width=FALSE,height=FALSE)
        #customtkinter.set_appearance_mode("grey")
        self.root.config(bg="grey60")
        
        # lbl=Label(dashboard,text=emailEntry.get())
        # lbl.place(x=50,y=50)
        # lbl=customtkinter.CTkLabel(dashboard,text=emailEntry.get(),text_font=("Helvetica", 13, "bold"),fg_color="white",text_color="black")
        # lbl.place(x=10,y=10, width=250)
        
        # LEFT FRAME
        
        leftFrame = customtkinter.CTkFrame(self.root, fg_color="grey60", corner_radius=30)
        leftFrame.place(x=5, y=5, width=420, height=860)
        
        # LEFT Main Heading
        leftMainLabel = customtkinter.CTkLabel(master=self.root, text="ʜᴏᴍᴇ ꜱᴇᴄᴜʀɪᴛʏ ꜱʏꜱᴛᴇᴍ", width=400, height=95,corner_radius=0, text_font=("Helvetica", 27, "bold"),fg_color="grey60")
        leftMainLabel.place(x=215, y=75, anchor=tkinter.CENTER)
        
        
        
       
        
        
        
        
        #CCTV Image
        userCamImg = ImageTk.PhotoImage(Image.open('/home/syed/Desktop/FYP-Project/FYP_HSS_9_12_2021/Practice-GUI/images/cam.png').resize((140,80)))
        userCamImg = customtkinter.CTkButton(leftFrame,image=userCamImg,text="",hover_color=None,fg_color="grey60")
        userCamImg.place(x=5,y=100, width=120, height=100)
        
        #User Image
        userImg=ImageTk.PhotoImage(Image.open('/home/syed/Desktop/FYP-Project/FYP_HSS_9_12_2021/Practice-GUI/images/usr.png').resize((250, 250)))
        userImgBtn = customtkinter.CTkButton(leftFrame,image=userImg,text="",hover_color=None,fg_color="grey60")
        userImgBtn.place(x=90,y=180, height=250)
        
        # TAG line
        tagline = customtkinter.CTkLabel(leftFrame,text="We Protect | We Secure",text_font=("Helvetica", 16, "bold"),fg_color="grey60")
        tagline.place(width=250, height=50, x=80,y=820)
        
        #-------------------------------------------------------#
        
        # RIGHT FRAME
        
        rightFrame = customtkinter.CTkFrame(self.root, fg_color="grey80", corner_radius=20)
        rightFrame.place(x=430, y=1, width=1415, height=930)
        
        #RIGHT Main Heading
        LeftMainLabel = customtkinter.CTkLabel(rightFrame, text="ᴜꜱᴇʀ ᴅᴀꜱʜʙᴏᴀʀᴅ", width=850, height=120,corner_radius=0, text_font=("Helvetica", 25, "bold"),fg_color="grey80")
        LeftMainLabel.place(x=540, y=75, anchor=tkinter.CENTER)
       
       
        #-------------------------------------------------------#
        #Single CCTV Image
        singleCCTVImg=ImageTk.PhotoImage(Image.open('/home/syed/Desktop/FYP-Project/FYP_HSS_9_12_2021/Practice-GUI/images/s1.png').resize((100, 100)))
        singleCCTVImgBtn = customtkinter.CTkButton(rightFrame,image=singleCCTVImg,text="",hover_color=NONE,fg_color="grey80")
        singleCCTVImgBtn.place(x=210,y=280, height=130)
        
        
        #Single Camera Button
        singleCCTVButton=customtkinter.CTkButton(rightFrame,text="Single Mode CCTV", text_font=("bold"), fg_color="grey75", hover_color="grey70")
        singleCCTVButton.place(x=170,y=420, width=200)
        
        
        #-------------------------------------------------------#
        #double CCTV Image
        doubleCCTVImg=ImageTk.PhotoImage(Image.open('/home/syed/Desktop/FYP-Project/FYP_HSS_9_12_2021/Practice-GUI/images/d2.png').resize((120, 120)))
        doubleCCTVImgBtn = customtkinter.CTkButton(rightFrame,image=doubleCCTVImg,text="",hover_color=NONE,fg_color="grey80")
        doubleCCTVImgBtn.place(x=750,y=280, height=130)
        
        
        #double Camera Button
        doubleCCTVButton=customtkinter.CTkButton(rightFrame,text="Double Mode CCTV", text_font=("bold"), fg_color="grey75", hover_color="grey70")
        doubleCCTVButton.place(x=710,y=420, width=200)
        
        
        #-------------------------------------------------------#
        #VIDEO CCTV Image
        videoCCTVImg=ImageTk.PhotoImage(Image.open('/home/syed/Desktop/FYP-Project/FYP_HSS_9_12_2021/Practice-GUI/images/v2.png').resize((150, 80)))
        videoCCTVImgBtn = customtkinter.CTkButton(rightFrame,image=videoCCTVImg,text="",hover_color=NONE,fg_color="grey80")
        videoCCTVImgBtn.place(x=450,y=280, height=100)
        
        
        #video Camera Button
        videoCCTVButton=customtkinter.CTkButton(rightFrame,text="Video Mode CCTV", text_font=("bold"), fg_color="grey75", hover_color="grey70")
        videoCCTVButton.place(x=430,y=420, width=200)
        
        
        #-------------------------------------------------------#
        #VIEW Save CCTV Image
        viewSaveImg=ImageTk.PhotoImage(Image.open('/home/syed/Desktop/FYP-Project/FYP_HSS_9_12_2021/Practice-GUI/images/vI.png').resize((100, 100)))
        viewSaveImgBtn = customtkinter.CTkButton(rightFrame,image=viewSaveImg,text="",hover_color=NONE,fg_color="grey80")
        viewSaveImgBtn.place(x=210,y=540, height=130)
        
        
        #VIEW Save CCTV Image Button
        viewSaveImgButton=customtkinter.CTkButton(rightFrame,text="View Saved Images", text_font=("bold"), fg_color="grey75", hover_color="grey70")
        viewSaveImgButton.place(x=170,y=680, width=200)
        
        #-------------------------------------------------------#
        #VIEW Save CCTV Recording
        viewSaveRec=ImageTk.PhotoImage(Image.open('/home/syed/Desktop/FYP-Project/FYP_HSS_9_12_2021/Practice-GUI/images/vR.png').resize((100, 100)))
        viewSaveRecBtn = customtkinter.CTkButton(rightFrame,image=viewSaveRec,text="",hover_color=NONE,fg_color="grey80")
        viewSaveRecBtn.place(x=750,y=540, height=130)
        
        
        #VIEW Save CCTV Recording Button
        viewSaveRecButton=customtkinter.CTkButton(rightFrame,text="View Saved Recording", text_font=("bold"), fg_color="grey75", hover_color="grey70")
        viewSaveRecButton.place(x=710,y=680, width=200)
        
        
        #-------------------------------------------------------#
        #Edit Profile
        editProfileImg=ImageTk.PhotoImage(Image.open('/home/syed/Desktop/FYP-Project/FYP_HSS_9_12_2021/Practice-GUI/images/eP.png').resize((160, 160)))
        editProfileImgBtn = customtkinter.CTkButton(rightFrame,image=editProfileImg,text="",hover_color=NONE,fg_color="grey80")
        editProfileImgBtn.place(x=450,y=500, height=180)
        
        
        #edit Profile Button
        editProfileButton=customtkinter.CTkButton(rightFrame,text="Edit Profile", text_font=("bold"), fg_color="grey75", hover_color="grey70")
        editProfileButton.place(x=430,y=680, width=200)
        
        
        
        #-------------------------------------------------------#
        # Right Sub Frame in RIGHT FRAME
        rightSubFrame = customtkinter.CTkFrame(rightFrame, fg_color="grey60", corner_radius=30)
        rightSubFrame.place(x=1010, y=105, width=420, height=800)
        
        #Right Sub Frame Heading
        rightSubFrameLabel = customtkinter.CTkLabel(rightSubFrame, text="ꜱᴇᴛ ᴛʜʀᴇꜱʜᴏʟᴅ", width=230, height=100,corner_radius=0, text_font=("Helvetica", 18, "bold"),fg_color="grey60")
        rightSubFrameLabel.place(x=100, y=50, anchor=tkinter.CENTER)
        
        # #-------------------------------------------------------#
        # #Threshold Frame
        #thresholdFrame = customtkinter.CTkFrame(rightSubFrame, fg_color="grey60", corner_radius=30)
        #thresholdFrame.place(x=5, y=5, width=10, height=10)
        
        # #0.1 Threshold Radio Button
        v = StringVar(root,"0.1")
 
        # Dictionary to create multiple buttons
        # values = {
        # "Threshold 0.1" : "0.1",
        # "Threshold 0.2" : "0.2",
        # "Threshold 0.3" : "0.3",
        # "Threshold 0.4" : "0.4",
        # "Threshold 0.5" : "0.5"
        #   }
        
        # for (text, value) in values.items():
        radioButtonOne = Radiobutton(rightSubFrame, text = "Threshold 0.1", variable = v, value = 0.1, bg="grey60", font=("bold"))
        radioButtonOne.pack(anchor=W, padx=15, pady=10, ipady=1 )
        radioButtonOne.place(x= 35, y=100)
        
        radioButtonTwo = Radiobutton(rightSubFrame, text = "Threshold 0.2", variable = v, value = 0.2, bg="grey60", font=("bold"))
        radioButtonTwo.pack(anchor=W, padx=15, pady=10, ipady=1 )
        radioButtonTwo.place(x= 35, y=150)
        
        radioButtonThree = Radiobutton(rightSubFrame, text = "Threshold 0.3", variable = v, value = 0.3, bg="grey60", font=("bold"))
        radioButtonThree.pack(anchor=W, padx=15, pady=10, ipady=1 )
        radioButtonThree.place(x= 35, y=200)
        
        radioButtonFour = Radiobutton(rightSubFrame, text = "Threshold 0.4", variable = v, value = 0.4, bg="grey60", font=("bold"))
        radioButtonFour.pack(anchor=W, padx=15, pady=10, ipady=1 )
        radioButtonFour.place(x= 35, y=250)
        
        radioButtonFifth = Radiobutton(rightSubFrame, text = "Threshold 0.45", variable = v, value = 0.45, bg="grey60", font=("bold"))
        radioButtonFifth.pack(anchor=W, padx=15, pady=10, ipady=1 )
        radioButtonFifth.place(x= 35, y=300)
                #Radiobutton(rightSubFrame, text = text, variable = v, value = value[1]).pack(anchor=W, padx=3, pady=20)
                #Radiobutton(rightSubFrame, text = text, variable = v, value = value[2]).pack(anchor=W, padx=3, pady=30)
                #Radiobutton(rightSubFrame, text = text, variable = v, value = value[3]).pack(anchor=W, padx=3, pady=40) 
                #Radiobutton(rightSubFrame, text = text, variable = v, value = value[4]).pack(anchor=W, padx=3, pady=40)      
                
                 
        #-------------------------------------------------------#
        #Right Sub Frame Heading Two
        rightSubFrameLabelTwo = customtkinter.CTkLabel(rightSubFrame, text="ʀᴀɪꜱᴇ ᴀʟᴀʀᴍ", width=230, height=100,corner_radius=0, text_font=("Helvetica", 18, "bold"),fg_color="grey60")
        rightSubFrameLabelTwo.place(x=100, y=400, anchor=tkinter.CENTER)
        
        j = StringVar(root,"Yes")
        
        radioButtonSix = Radiobutton(rightSubFrame, text = "Yes", variable = j, value = 1, bg="grey60", font=("bold"))
        radioButtonSix.pack(anchor=W, padx=15, pady=10, ipady=1 )
        radioButtonSix.place(x= 35, y=450)
        
        radioButtonSeven = Radiobutton(rightSubFrame, text = "No", variable = j, value = 2, bg="grey60", font=("bold"))
        radioButtonSeven.pack(anchor=W, padx=15, pady=10, ipady=1 )
        radioButtonSeven.place(x= 35, y=500)
        
        
        
        
        
        
        
        
        
        
        
        
        
root =customtkinter.CTk()
ob = userDashboard(root)
root.mainloop()        