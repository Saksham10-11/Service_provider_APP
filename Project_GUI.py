# Importing the required modules and packages
import Project as prj
from tkinter import *
from tkinter import ttk
import tkinter.messagebox as tmsg
import datetime
import traceback
import ctypes


# The basic app template is defined here
class App(Tk):
    def __init__(self):
        super().__init__()
        # Taking the dimensions of Users Screen
        self.scrwidth = self.winfo_screenwidth()
        self.scrheight = self.winfo_screenheight()

        # Calling the function to configure the main root
        self.root_configure()

    # Adding required configrations to the root
    def root_configure(self):

        if self.scrheight==768 and self.scrwidth==1366:
            # Setting the state of root to ZOOMED
            self.state("zoomed")
        else :
            ctypes.windll.shcore.SetProcessDpiAwareness(1)
            self.geometry("1366x768")

        
        self.photo_icon = PhotoImage(file='Images_icons\\Main_icon.png')
        self.iconphoto(False, self.photo_icon)
        self.title("Service2Door")
        # Creating the window that completely fits the screen except the taskbar
        self.state('zoomed')
        self.configure(bg="white")
        # Creation of status bar to provide the status of the program to the user
        statusstat = StringVar()
        statusstat.set("VIIT PE PBL    ~~version 1.23.0")
        sbarL = Label(self, textvariable=statusstat, bg='lightgrey',
                      width=80, border=0, anchor='w', padx=20, font="lucida 12 bold")
        sbarL.place(x=0, y=684)
        self.statusvar = StringVar()
        self.statusvar.set("Welcome...")
        self.sbarR = Label(self, textvariable=self.statusvar, bg="lightgrey", width=60,
                           relief=RAISED, border=0, anchor="e", padx=60, font="lucida 12 italic")
        self.sbarR.place(x=730, y=684)

    # Sets the current status of the program
    def setStatus(self, txt):
        self.statusvar.set(txt)
        self.sbarR.update()


# This is the main frame of the GUI
class MainFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        root.setStatus("Welcome ...")

        # Creates the main frame to navigate through pages
        self.main_frame = Frame(
            root, bg="white", width=root.scrwidth, height=root.scrheight-85)
        self.main_frame.place(x=0, y=0)
        self.label = Label(self.main_frame, text="Hello !").place(x=500, y=400)

        # Calling class function to insert images and other stuff in the frame
        self.insertImage()
        self.Other()

    # Opens the next Frame depending upon the type of user
    def nextFrame(self):
        if Type == "User":
            userLogin_frame = UserLoginFrame(root)
            self.main_frame.destroy()
        elif Type == "Worker":
            self.workerName = prj.ExtractName(Phone_num, Type)
            tmsg.showinfo(
                'Worker Login', f"Hey {self.workerName}, you are already registered ...\nYou may contact Admins for any Query !")
        elif Type == "Admin":
            adminLogin_frame = AdminLoginFrame(root)
            self.main_frame.destroy()
        else:
            # If user is not registerd the below Frame will help user to register
            ChoiceFrame = ChooseUser_worker(root)
            self.main_frame.destroy()

    # Activates when the arrow button is pressed ..
    def proceed(self):
        # Declaring PhoneNum as global variable as used many times in different classes
        global Phone_num
        Phone_num = self.Phone.get()
        Phone_num = Phone_num.strip()
        root.setStatus("Checking number...")
        # Adding delays to ensure smooth functioning of the program
        import time
        time.sleep(0.25)
        self.PhoneEntry.delete(0, END)
        result = prj.CheckPhoneNumber(Phone_num)
        root.setStatus("Ready...")
        if result == True:
            global Type
            Type = prj.CheckNumInDatabase(Phone_num)
            self.nextFrame()
        else:
            tmsg.showerror("Invalid number !",
                           "Please enter a valid Phone number")

    # Displays the messagebox
    def contact(self):
        tmsg.showinfo(
            'Contact Us', "You can contact us on any of our VIIT's official E-mail ID's")

    # Displays a messagebox
    def about(self):
        tmsg.showinfo(
            'About us', "This python program finds the nearest worker as per user's requirement .\nThis is created by Aditya , Anuj , Aarya , Sarvesh and Saksham .")

    # Inserting the images to the user login frame
    def insertImage(self):

        # importing the Pillow module
        from PIL import ImageTk, Image

        # Adding the Background image
        self.img = Image.open("Images_icons\\lightgreenLogin.png")
        self.resized_img = self.img.resize((1100, 683))
        self.photo1 = ImageTk.PhotoImage(self.resized_img)
        photo_label1 = Label(
            self.main_frame, image=self.photo1, anchor='ne', border=0)
        photo_label1.place(x=0, y=0)

        # Creating frames
        self.sub_frame = Frame(self.main_frame, height=565,
                               width=500, bg="white", borderwidth=5).place(x=710, y=60)
        frameT = Frame(self.main_frame, width=500, height=4,
                       bg="black").place(x=710, y=60)
        frameB = Frame(self.main_frame, width=504, height=4,
                       bg="black").place(x=710, y=625)
        frameL = Frame(self.main_frame, width=4, height=565,
                       bg='black').place(x=710, y=60)
        frameR = Frame(self.main_frame, width=4, height=565,
                       bg='black').place(x=1210, y=60)

        # Adding extra images and icons to the frame created
        self.icon = Image.open("Images_icons\\user_icon.png")
        self.resized_icon = self.icon.resize((110, 110))
        self.photo2 = ImageTk.PhotoImage(self.resized_icon)
        photo_label2 = Label(
            self.main_frame, image=self.photo2, border=0, bg="white")
        photo_label2.place(x=925, y=90)

        self.cartoon = Image.open("Images_icons\\man_icon.jpg")
        self.resized_cartoon = self.cartoon.resize((170, 360))
        self.photo3 = ImageTk.PhotoImage(self.resized_cartoon)
        photo_label3 = Label(
            self.main_frame, image=self.photo3, border=0, bg="white")
        photo_label3.place(x=725, y=220)

        self.mobile = Image.open("Images_icons\\phone-call.png")
        self.resized_mobile = self.mobile.resize((40, 45))
        self.photo4 = ImageTk.PhotoImage(self.resized_mobile)
        photo_label4 = Label(
            self.main_frame, image=self.photo4, border=0, bg="white")
        photo_label4.place(x=890, y=374)

        self.arrow = Image.open("Images_icons\\right-arrow.png")
        self.arrow_resized = self.arrow.resize((50, 40))
        self.photo5 = ImageTk.PhotoImage(self.arrow_resized)

    # Contains widgets to do user defined tasks
    def Other(self):

        # Creating a label to greet the user
        self.greet = Label(self.main_frame, text="WELCOME", bg="white", fg='black', font=(
            'Times New Roman', 32, 'bold')).place(x=870, y=210)
        self.frame1 = Frame(self.main_frame, bg="black",
                            height=4, width=230).place(x=878, y=258)

        # Taking input from the user
        self.txt = Label(self.main_frame, text="Enter your Phone number :", font=(
            "cosmicsansms", 16, "bold"), bg='white').place(x=880, y=320)
        self.Phone = StringVar()
        self.PhoneEntry = Entry(self.main_frame, textvariable=self.Phone, border=0,
                                width=15, bg='white', font=('Microsoft YaHei UI Light', 16, 'bold'))
        self.PhoneEntry.place(x=952, y=382)
        self.frame_line = Frame(
            self.main_frame, bg="black", width=160, height=3).place(x=945, y=412)

        # Creating button for user to proceed
        self.arrow_button = Button(self.main_frame, image=self.photo5,
                                   bg="white", border=0, cursor='hand2', command=self.proceed)
        self.arrow_button.place(x=1060, y=445)

        # Creating extra buttons ...(just for fun)
        self.contact_button = Button(self.main_frame, text='Contact us', fg='cyan2', bg="white",
                                     cursor='hand2', border=0, font='lucida 16 underline', command=self.contact)
        self.contact_button.place(x=925, y=535)
        Label(self.main_frame, text=u'\u24d8', bg='white', border=0,
              fg='cyan2', font="lucida 16 bold").place(x=937, y=577)
        self.about_button = Button(self.main_frame, text='about', bg="white", cursor='hand2',
                                   border=0, font='lucida 16 underline', fg='cyan2', command=self.about)
        self.about_button.place(x=960, y=570)


# This is the forget pass page 
class ForgetPasswordPage(ttk.Frame):
    def __init__(self,container):
        super().__init__(container)
        root.setStatus("Forgot Password ...")

        # Creates the main frame to navigate through pages
        self.main_frame = Frame(
            root, bg="white", width=root.scrwidth, height=root.scrheight-85)
        self.main_frame.place(x=0, y=0)

        # Calling class function to insert images and other attributes in the frame
        self.insertImage()
        self.Other()

    # Returns to the previous page
    def Back_page(self):
        Main_frame = UserLoginFrame(root)
        self.main_frame.destroy()

    # Check the otp Entered and Redirect the user
    def CheckOTP(self):
        Entered_otp = self.OTP.get()
        if Entered_otp == OTP:
            self.OTPEntry.delete(0, END)
            reset_page = ResetPassPage(root)
            self.main_frame.destroy()
        else:
            tmsg.showerror("Incorrect OTP", "Please Enter the valid OTP !")
            self.OTPEntry.delete(0, END)

    # Inserting images to make the GUI attractive
    def insertImage(self):

        # importing the Pillow module
        from PIL import ImageTk, Image

        # Adding the Background image
        self.img1 = Image.open("Images_icons\\OTP_Entry.jpg")
        self.resized_img1 = self.img1.resize((880, 683))
        self.photo1 = ImageTk.PhotoImage(self.resized_img1)
        self.photo_label1 = Label(
            self.main_frame, image=self.photo1, anchor='ne', border=0)
        self.photo_label1.place(x=0, y=0)

        # Creating frames
        self.sub_frame = Frame(self.main_frame, height=565,
                               width=400, bg="white", borderwidth=5).place(x=900, y=60)
        frameT = Frame(self.main_frame, width=400, height=4,
                       bg="black").place(x=900, y=60)
        frameB = Frame(self.main_frame, width=404, height=4,
                       bg="black").place(x=900, y=625)
        frameL = Frame(self.main_frame, width=4, height=565,
                       bg='black').place(x=900, y=60)
        frameR = Frame(self.main_frame, width=4, height=565,
                       bg='black').place(x=1300, y=60)

        # Adding extra images and icons to the frame created
        self.Pass_icon = Image.open('Images_icons\\LockIcon.png')
        self.resized_Pass_icon = self.Pass_icon.resize((40, 40))
        self.photo2 = ImageTk.PhotoImage(self.resized_Pass_icon)
        photo_label2 = Label(
            self.main_frame, image=self.photo2, border=0, bg="white")
        photo_label2.place(x=965, y=500)

        # User Icon
        self.icon = Image.open("Images_icons\\user_icon.png")
        self.resized_icon = self.icon.resize((130, 130))
        self.photo3 = ImageTk.PhotoImage(self.resized_icon)
        photo_label3 = Label(
            self.main_frame, image=self.photo3, border=0, bg="white")
        photo_label3.place(x=1030, y=90)

        # Proceed icon image
        self.arrow = Image.open("Images_icons\\right-arrow.png")
        self.arrow_resized = self.arrow.resize((50, 40))
        self.photo1 = ImageTk.PhotoImage(self.arrow_resized)

        # Back Button Icon
        self.back_icon = Image.open("Images_icons\\BackArrow.png")
        self.back_resized = self.back_icon.resize((50, 40))
        self.photo_icon2 = ImageTk.PhotoImage(self.back_resized)

    # Adding the other attributes to the current frame
    def Other(self):

        # Creating a label to greet the user
        self.First_name = prj.ExtractName(Phone_num, Type)  # <-- change
        self.greet_label = Label(self.main_frame, text=f"Hey {self.First_name.title()} ,", bg="white", fg='black', font=(
            'Times New Roman', 32, 'bold')).place(x=910, y=225)
        self.info_label = Label(self.main_frame, text="                 OTP has been sent\nsucessfully  ,  enter it below to\nproceed to the reset Password\npage .                                     ", anchor='nw',
                                bg="white", fg='black', font=('Times New Roman', 24, 'italic'))
        self.info_label.place(x=910, y=280)

        # Taking Password as input from the user
        self.txt = Label(self.main_frame, text="Enter the 4-digit OTP :", font=(
            "cosmicsansms", 18, "bold"), bg='white').place(x=970, y=455)
        self.OTP = StringVar()
        self.OTPEntry = Entry(self.main_frame, textvariable=self.OTP, border=0,
                              width=16, bg='white', font=('Microsoft YaHei UI Light', 16, 'bold'))
        self.OTPEntry.place(x=1025, y=500)
        self.frame_line = Frame(
            self.main_frame, bg="black", width=200, height=3).place(x=1017, y=535)

        # Creating the login button
        self.proceed_button = Button(self.main_frame, bg='white', image=self.photo1,
                                     border=0, cursor='hand2', command=self.CheckOTP)
        self.proceed_button.place(x=1180, y=560)

        # Creating the back button
        self.back_button = Button(self.main_frame, bg='white', cursor='hand2',
                                  image=self.photo_icon2, border=0, command=self.Back_page)
        self.back_button.place(x=910, y=80)


# This is the login frame for the user
class UserLoginFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        root.setStatus("User Login ...")

        # Creates the main frame to navigate through pages
        self.main_frame = Frame(
            root, bg="white", width=root.scrwidth, height=root.scrheight-85)
        self.main_frame.place(x=0, y=0)

        # Calling class function to insert images and other attributes in the frame
        self.insertImage()
        self.Other()

    # Logs in  the user if correct pass is entered
    def Login_user(self):
        # Checking if the password entered matches the one stored in the Database
        self.Entered_Password = self.Password.get()
        self.Real_Password = prj.ExtractUserPass(Phone_num)
        root.setStatus("Checking Password...")
        import time
        time.sleep(0.25)
        self.PassEntry.delete(0, END)
        root.setStatus("Ready...")

        # If the passwords matches the open the user interface
        if self.Real_Password == self.Entered_Password:
            MainUI_Page = MainUI(root)
            self.main_frame.destroy()
        else:
            tmsg.showerror("Incorrect Password !",
                           "Re-entre your Password....")

    # Returns to the previous page
    def Back_page(self):
        Main_frame = MainFrame(root)
        self.main_frame.destroy()

    # Executes forget pass functions
    def Forget_pass(self):
        global OTP
        # OTP = prj.SendOTP()
        OTP = '2022'
        forget_pass = ForgetPasswordPage(root)
        self.main_frame.destroy()

    # Inserting images to make the GUI attractive
    def insertImage(self):

        # importing the Pillow module
        from PIL import ImageTk, Image

        # Adding the Background image
        self.img = Image.open("Images_icons\\greenUserLogin.jpg")
        self.resized_img = self.img.resize((750, 683))
        self.photo1 = ImageTk.PhotoImage(self.resized_img)
        photo_label1 = Label(
            self.main_frame, image=self.photo1, anchor='ne', border=0)
        photo_label1.place(x=0, y=0)

        # Creating frames
        self.sub_frame = Frame(self.main_frame, height=565,
                               width=500, bg="white", borderwidth=5).place(x=750, y=60)
        frameT = Frame(self.main_frame, width=500, height=4,
                       bg="black").place(x=750, y=60)
        frameB = Frame(self.main_frame, width=504, height=4,
                       bg="black").place(x=750, y=625)
        frameL = Frame(self.main_frame, width=4, height=565,
                       bg='black').place(x=750, y=60)
        frameR = Frame(self.main_frame, width=4, height=565,
                       bg='black').place(x=1250, y=60)

        # Adding extra images and icons to the frame created
        self.Pass_icon = Image.open('Images_icons\\LockIcon.png')
        self.resized_Pass_icon = self.Pass_icon.resize((40, 40))
        self.photo2 = ImageTk.PhotoImage(self.resized_Pass_icon)
        photo_label2 = Label(
            self.main_frame, image=self.photo2, border=0, bg="white")
        photo_label2.place(x=820, y=400)

        # User Icon
        self.icon = Image.open("Images_icons\\user_icon.png")
        self.resized_icon = self.icon.resize((130, 130))
        self.photo3 = ImageTk.PhotoImage(self.resized_icon)
        photo_label3 = Label(
            self.main_frame, image=self.photo3, border=0, bg="white")
        photo_label3.place(x=925, y=90)

        # Forget Password Button Icon
        self.ForgetPass_icon = Image.open('Images_icons\\ForgetPass.jpg')
        self.resized_ForgetPass_icon = self.ForgetPass_icon.resize((150, 350))
        self.photo = ImageTk.PhotoImage(self.resized_ForgetPass_icon)
        photo_label = Label(
            self.main_frame, image=self.photo, border=0, bg="white")
        photo_label.place(x=1100, y=270)

        # Login Button Icon
        self.login_icon = Image.open("Images_icons\\Login_icon.png")
        self.login_resized = self.login_icon.resize((125, 50))
        self.photo_icon1 = ImageTk.PhotoImage(self.login_resized)

        # Back Button Icon
        self.back_icon = Image.open("Images_icons\\BackArrow.png")
        self.back_resized = self.back_icon.resize((50, 40))
        self.photo_icon2 = ImageTk.PhotoImage(self.back_resized)

    # Contains widgets to do user defined tasks
    def Other(self):

        # Creating a label to greet the user
        self.First_name = prj.ExtractName(Phone_num, Type)  # <-- change
        self.greet_label = Label(self.main_frame, text="WELCOME BACK,", bg="white", fg='black', font=(
            'Times New Roman', 32, 'bold')).place(x=800, y=225)
        self.name_label = Label(self.main_frame, text=f"{self.First_name.upper()}", anchor=CENTER,
                                bg="white", width=10, fg='black', font=('Times New Roman', 32, 'bold'))
        self.name_label.place(x=860, y=280)

        # Taking Password as input from the user
        self.txt = Label(self.main_frame, text="Enter your Password :", font=(
            "cosmicsansms", 18, "bold"), bg='white').place(x=820, y=360)
        self.Password = StringVar()
        self.PassEntry = Entry(self.main_frame, textvariable=self.Password, border=0,
                               width=16, show='*', bg='white', font=('Microsoft YaHei UI Light', 16, 'bold'))
        self.PassEntry.place(x=880, y=400)
        self.frame_line = Frame(
            self.main_frame, bg="black", width=200, height=3).place(x=875, y=430)

        # Creating the login button
        self.login_button = Button(self.main_frame, bg='white', image=self.photo_icon1,
                                   border=0, cursor='hand2', command=self.Login_user)
        self.login_button.place(x=955, y=450)

        # Creating the back button
        self.back_button = Button(self.main_frame, bg='white', cursor='hand2',
                                  image=self.photo_icon2, border=0, command=self.Back_page)
        self.back_button.place(x=770, y=80)

        # Creating Forget Password Button
        self.forget_button = Button(self.main_frame, text="forget password ?", border=0, bg="white",
                                    fg='cyan2', font='lucida 16 underline', cursor="hand2", command=self.Forget_pass)
        self.forget_button.place(x=900, y=550)


# This is the login frame for the Admin
class AdminLoginFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        root.setStatus("Admin Login ...")

        # Creates the main frame to navigate through pages
        self.main_frame = Frame(
            root, bg="white", width=root.scrwidth, height=root.scrheight-85)
        self.main_frame.place(x=0, y=0)

        # To add images and make changes here ..
        # importing the Pillow module
        from PIL import ImageTk, Image

        # Adding the Background image
        self.img = Image.open("Images_icons\\OOPS_icon.png")
        self.resized_img = self.img.resize((700, 660))
        self.photo1 = ImageTk.PhotoImage(self.resized_img)
        photo_label1 = Label(self.main_frame, image=self.photo1,
                             bg='white', anchor='ne', border=0)
        photo_label1.place(x=10, y=0)

        # Creating frames
        self.sub_frame = Frame(self.main_frame, height=565,
                               width=500, bg="white", borderwidth=5).place(x=750, y=60)
        frameT = Frame(self.main_frame, width=500, height=4,
                       bg="black").place(x=750, y=60)
        frameB = Frame(self.main_frame, width=504, height=4,
                       bg="black").place(x=750, y=625)
        frameL = Frame(self.main_frame, width=4, height=565,
                       bg='black').place(x=750, y=60)
        frameR = Frame(self.main_frame, width=4, height=565,
                       bg='black').place(x=1250, y=60)

        # Displaying the information
        self.Admin_Name = prj.ExtractName(Phone_num, Type)
        Label(self.main_frame, text=f'Hey {self.Admin_Name},', bg='white', font=(
            'Times new roman', 34, 'bold')).place(x=780, y=150)
        Label(self.main_frame, text='               This page is currently \nunder the development process.',
              bg='white', font='cosmicsansms 24 italic').place(x=780, y=220)

        # Creating button to navigate through the pages
        self.previous_button = Button(self.main_frame, fg='cyan2', border=0, font='lucida 24 underline',
                                      bg='white', cursor='hand2', text="<<< Go back to the \nlogin page ......", command=self.PreviousPage)
        self.previous_button.place(x=850, y=450)

    # To go back to the main Frame
    def PreviousPage(self):
        Main_frame = MainFrame(root)
        root.setStatus('Welcome....')
        self.main_frame.destroy()


# This Frame allows the users to choose between User and Worker
class ChooseUser_worker(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        root.setStatus("Choose User/Worker ...")

        # Creates the main frame to navigate through pages
        self.main_frame = Frame(
            root, bg="white", width=root.scrwidth, height=root.scrheight-85)
        self.main_frame.place(x=0, y=0)

        # Calling class function to insert images in the frame
        self.insertImage()
        self.Other()

    # Opens the previous and destroys the current one
    def BackPage(self):
        Main_frame = MainFrame(root)
        self.main_frame.destroy()

    # Opens user registration page
    def registerUserPage(self):
        register_User = registerUser(root)
        self.main_frame.destroy()

    # Opens worker registration page
    def registerWorkerPage(self):
        register_Worker = registerWorker(root)
        self.main_frame.destroy()

    # Inserting the images in the GUI
    def insertImage(self):

        # importing the Pillow module
        from PIL import ImageTk, Image

        # Adding the Background image
        self.img = Image.open("Images_icons\\ChooseRegister.jpg")
        self.resized_img = self.img.resize((750, 683))
        self.photo1 = ImageTk.PhotoImage(self.resized_img)
        photo_label1 = Label(
            self.main_frame, image=self.photo1, anchor='ne', border=0)
        photo_label1.place(x=0, y=0)

        # Creating frames
        self.sub_frame = Frame(self.main_frame, height=565,
                               width=500, bg="white", borderwidth=5).place(x=750, y=60)
        frameT = Frame(self.main_frame, width=500, height=4,
                       bg="black").place(x=750, y=60)
        frameB = Frame(self.main_frame, width=504, height=4,
                       bg="black").place(x=750, y=625)
        frameL = Frame(self.main_frame, width=4, height=565,
                       bg='black').place(x=750, y=60)
        frameR = Frame(self.main_frame, width=4, height=565,
                       bg='black').place(x=1250, y=60)

        # Register User Button Icon
        self.registerUser = Image.open("Images_icons\\oval_user.png")
        self.registerUser_resized = self.registerUser.resize((450, 350))
        self.photo_icon1 = ImageTk.PhotoImage(self.registerUser_resized)

        # Register Worker Button Icon
        self.registerWorker = Image.open("Images_icons\\oval_worker.png")
        self.registerWorker_resized = self.registerWorker.resize((450, 350))
        self.photo_icon2 = ImageTk.PhotoImage(self.registerWorker_resized)

        # Back Button Icon
        self.back_icon = Image.open("Images_icons\\BackArrow.png")
        self.back_resized = self.back_icon.resize((70, 60))
        self.photo_icon3 = ImageTk.PhotoImage(self.back_resized)

    # Inserting the other required functions
    def Other(self):
        # Add text
        txt = Label(self.main_frame, text="Choose one of the \noptions below....",
                    bg='white', font=('Times new roman', 36, 'bold'))
        txt.place(x=850, y=80)

        # User register button
        self.User_button = Button(self.main_frame, image=self.photo_icon1, bg='white',
                                  border=0, width=350, height=170, cursor='hand2', command=self.registerUserPage)
        self.User_button.place(x=830, y=250)

        # Worker register button
        self.Worker_button = Button(self.main_frame, image=self.photo_icon2, border=0,
                                    width=350, height=170, bg='white', cursor='hand2', command=self.registerWorkerPage)
        self.Worker_button.place(x=830, y=430)

        # Creating the back button
        self.back_button = Button(self.main_frame, image=self.photo_icon3,
                                  bg='white', cursor='hand2', border=0, command=self.BackPage)
        self.back_button.place(x=770, y=80)


# This frame registers the user
class registerUser(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        root.setStatus("User Registeration ...")

        # Creates the main frame to navigate through pages
        self.main_frame = Frame(
            root, bg="white", width=root.scrwidth, height=root.scrheight-85)
        self.main_frame.place(x=0, y=0)

        # Golbalising Type variable and assigning it the value
        global Type
        Type = 'User'

        # Calling class function to insert images and other attributes in the frame
        self.insertImage()
        self.Other()
        self.Inputdata()

    # Procceds the user icon the next page after making few checks
    def Proceed(self):
        # Extracting data from input
        self.Firstname = self.First_name.get()
        self.Firstname.strip()
        self.Firstname.lower()
        self.Firstname.title()
        self.Lastname = self.Last_name.get()
        self.Lastname.strip()
        self.Lastname.lower()
        self.Lastname.title()
        self.Email = self.mail.get()
        self.Email.strip()

        # Pausing and setting the Status
        import time
        root.setStatus("Checking input...")
        time.sleep(0.25)
        root.setStatus('Ready ...')

        # Using Exception handling to handle the UnboundLocalVariable Error
        try:
            # Checking the input data
            check1 = prj.CheckName(self.Firstname, self.Lastname)
            check2 = prj.CheckEmail(self.Email)
            # Performing the tasks based on the conditions
            if check1 == True and check2 == True:
                # declaring Global Variables
                global User_FName
                global User_LName
                global User_Email

                User_FName = self.Firstname
                User_LName = self.Lastname
                User_Email = self.Email

                # Moving user to next page and destroy the current one
                CreatePass_Page = CreatePassPage(root)
                self.main_frame.destroy()

            elif check1 == True and check2 == False:
                tmsg.showerror('Invalid input !',
                               'Please re-enter the valid E-mail addres.')
                self.mailEntry.delete(0, END)

            elif check1 == False and check2 == True:
                tmsg.showerror('Invalid input !',
                               'Please re-enter the valid Name.')
                self.FnameEntry.delete(0, END)
                self.LnameEntry.delete(0, END)

            elif check1 == False and check2 == False:
                tmsg.showerror('Invalid input !',
                               'Please re-enter the valid Name and Email.')
                self.FnameEntry.delete(0, END)
                self.LnameEntry.delete(0, END)
                self.mailEntry.delete(0, END)
        except UnboundLocalError:
            tmsg.showerror(
                'Error !', 'Please fill all the blanks before proceeding...')

    # Returns to the previous page
    def Back_page(self):
        Main_frame = MainFrame(root)
        self.main_frame.destroy()

    # Inserting Images and Creating Frames
    def insertImage(self):

        # importing the Pillow module
        from PIL import ImageTk, Image

        # Adding the Background image
        self.img = Image.open("Images_icons\\UserRegister.jpg")
        self.resized_img = self.img.resize((750, 683))
        self.photo1 = ImageTk.PhotoImage(self.resized_img)
        photo_label1 = Label(
            self.main_frame, image=self.photo1, anchor='ne', border=0)
        photo_label1.place(x=0, y=0)

        # Creating frames
        self.sub_frame = Frame(self.main_frame, height=565,
                               width=500, bg="white", borderwidth=5).place(x=750, y=60)
        frameT = Frame(self.main_frame, width=500, height=4,
                       bg="black").place(x=750, y=60)
        frameB = Frame(self.main_frame, width=504, height=4,
                       bg="black").place(x=750, y=625)
        frameL = Frame(self.main_frame, width=4, height=565,
                       bg='black').place(x=750, y=60)
        frameR = Frame(self.main_frame, width=4, height=565,
                       bg='black').place(x=1250, y=60)

        # Adding extra images and icons to the frame created
        self.icon = Image.open("Images_icons\\user.png")
        self.resized_icon = self.icon.resize((150, 150))
        self.photo3 = ImageTk.PhotoImage(self.resized_icon)

        # Back Button Icon
        self.back_icon = Image.open("Images_icons\\BackArrow.png")
        self.back_resized = self.back_icon.resize((50, 40))
        self.photo_icon2 = ImageTk.PhotoImage(self.back_resized)

        # arrow icon for procced button
        self.arrow = Image.open("Images_icons\\right-arrow.png")
        self.arrow_resized = self.arrow.resize((50, 40))
        self.photo5 = ImageTk.PhotoImage(self.arrow_resized)

    # Adding the other attributes to the Frame
    def Other(self):

        # Display the text to the user
        txt_greet = Label(self.main_frame, text='Hey User,', bg='white',
                          anchor='w', font=('Times new roman', 30, 'bold'))
        txt = Label(self.main_frame, text='         Please fill the details below to \nregister with us...                             ',
                    bg='white', font=('Times new roman', 22, 'bold'))
        txt_greet.place(x=790, y=210)
        txt.place(x=790, y=260)

        # Placing the icon here just to overlap it on the previous label
        self.photo_label3 = Label(
            self.main_frame, image=self.photo3, border=0, bg="white")
        self.photo_label3.place(x=925, y=80)

        # Creating the back button
        self.back_button = Button(self.main_frame, bg='white', cursor='hand2',
                                  image=self.photo_icon2, border=0, command=self.Back_page)
        self.back_button.place(x=760, y=70)

        # Creating button for user to proceed
        self.arrow_button = Button(self.main_frame, image=self.photo5,
                                   bg="white", border=0, cursor='hand2', command=self.Proceed)
        self.arrow_button.place(x=1120, y=550)

    # Taking the data as an Input from the User
    def Inputdata(self):
        # Taking First Name as input from the user
        self.txt1 = Label(self.main_frame, text="First Name :",
                          font=("cosmicsansms", 18, "bold"), bg='white')
        self.txt1.place(x=810, y=370)
        self.First_name = StringVar()
        self.FnameEntry = Entry(self.main_frame, textvariable=self.First_name, border=0,
                                width=16, bg='white', font=('Microsoft YaHei UI Light', 16, 'bold'))
        self.FnameEntry.place(x=970, y=370)
        self.frame_line1 = Frame(
            self.main_frame, bg="black", width=200, height=3).place(x=960, y=400)

        # Taking Last Name as input from the user
        self.txt2 = Label(self.main_frame, text="Last Name :",
                          font=("cosmicsansms", 18, "bold"), bg='white')
        self.txt2.place(x=810, y=430)
        self.Last_name = StringVar()
        self.LnameEntry = Entry(self.main_frame, textvariable=self.Last_name, border=0,
                                width=16, bg='white', font=('Microsoft YaHei UI Light', 16, 'bold'))
        self.LnameEntry.place(x=970, y=430)
        self.frame_line2 = Frame(
            self.main_frame, bg="black", width=200, height=3).place(x=960, y=460)

        # Taking E-mail as input from the user
        self.txt3 = Label(self.main_frame, text="   E-mail     :",
                          font=("cosmicsansms", 18, "bold"), bg='white')
        self.txt3.place(x=810, y=490)
        self.mail = StringVar()
        self.mailEntry = Entry(self.main_frame, textvariable=self.mail, border=0,
                               width=16, bg='white', font=('Microsoft YaHei UI Light', 16, 'bold'))
        self.mailEntry.place(x=970, y=490)
        self.frame_line3 = Frame(
            self.main_frame, bg="black", width=200, height=3).place(x=960, y=517)


# This Frame registers the worker
class registerWorker(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        root.setStatus("Worker Registration ...")

        # Creates the main frame to navigate through pages
        self.main_frame = Frame(
            root, bg="white", width=root.scrwidth, height=root.scrheight-85)
        self.main_frame.place(x=0, y=0)

        # Globalising the Type variable and assigning the value to it
        global Type
        Type = "Worker"

        # Calling class function to insert images and other attributes in the frame
        self.insertImage()
        self.Other()
        self.Inputdata()

    # Procceds the worker to the next page after making few checks
    def Proceed(self):
        # Extracting data from input
        self.Firstname = self.First_name.get()
        self.Firstname.strip()
        self.Firstname.title()
        self.Lastname = self.Last_name.get()
        self.Lastname.strip()
        self.Lastname.title()
        self.Email = self.mail.get()
        self.Email.strip()
        self.landmark = self.Landmark.get()
        self.profession = self.Profession.get()
        self.weblink = self.Weblink.get()
        self.distance = self.Distance.get()

        # Pausing and setting the Status
        import time
        root.setStatus("Checking input...")
        time.sleep(0.25)
        root.setStatus('Ready ...')

        # Checking the input data
        check1 = prj.CheckName(self.Firstname, self.Lastname)
        check2 = prj.CheckEmail(self.Email)
        check3 = prj.CheckLandmark(self.landmark)
        check4 = prj.CheckType(self.profession)

        # Creating list of all inputs
        L = [self.Firstname, self.Lastname, self.Email, self.landmark,
             self.profession, self.distance, self.weblink]

        # Performing the tasks based on the conditions
        mainCheck1 = False
        mainCheck2 = False
        mainCheck3 = False

        # Checks for Blanks
        for i in L:
            if i == '':
                mainCheck3 = True
                break
            else:
                pass

        # Makes various checks on Name and Email
        if check1 == True and check2 == True:
            mainCheck1 = True
        elif check1 == True and check2 == False:
            tmsg.showerror('Invalid input !',
                           'Please re-enter the valid E-mail addres.')
            self.mailEntry.delete(0, END)
        elif check1 == False and check2 == True:
            tmsg.showerror('Invalid input !',
                           'Please re-enter the valid Name.')
            self.FnameEntry.delete(0, END)
            self.LnameEntry.delete(0, END)
        elif check1 == False and check2 == False:
            tmsg.showerror('Invalid input !',
                           'Please re-enter the valid Name and Email.')
            self.FnameEntry.delete(0, END)
            self.LnameEntry.delete(0, END)
            self.mailEntry.delete(0, END)
        else:
            pass

        # Makes Checks for the Combobox and returns errors to user (if any)
        if check3 == True and check4 == True:
            mainCheck2 = True
        elif check3 == False or check4 == False:
            self.Landmark_box.delete(0, END)
            self.Profession_box.delete(0, END)
            tmsg.showerror(
                'Invalid Input !', 'Please choose one of the options from \nthe dropbox of profession and Landmark')
        else:
            pass

        # Executes if any blank is left empty
        if mainCheck3 == True:
            tmsg.showerror(
                'error', 'Please fill all the blanks spaces before proceeding')

        # If all the checks are done then the below code will execute
        if mainCheck3 == False and mainCheck1 == True and mainCheck2 == True:

            # Declaring Global variablaes
            global Worker_FName
            global Worker_LName
            global Worker_Email
            global Worker_Landmark
            global Worker_Distance
            global Worker_Weblink
            global Worker_Profession

            Worker_FName = self.Firstname
            Worker_LName = self.Lastname
            Worker_Email = self.Email
            Worker_Landmark = self.landmark
            Worker_Distance = self.distance
            Worker_Weblink = self.weblink
            Worker_Profession = self.profession

            # Definig the object and creating the next frame
            CreatePass_Page = CreatePassPage(root)
            self.main_frame.destroy()

    # Returns to the previous page
    def Back_page(self):
        Main_frame = MainFrame(root)
        self.main_frame.destroy()

    # Inserting images and creating sub frames
    def insertImage(self):

        # importing the Pillow module
        from PIL import ImageTk, Image

        # Adding the Background image
        self.img = Image.open("Images_icons\\WorkerRegister.jpg")
        self.resized_img = self.img.resize((750, 683))
        self.photo1 = ImageTk.PhotoImage(self.resized_img)
        photo_label1 = Label(
            self.main_frame, image=self.photo1, anchor='ne', border=0)
        photo_label1.place(x=0, y=0)

        # Creating frames
        self.sub_frame = Frame(self.main_frame, height=640,
                               width=500, bg="white", borderwidth=5).place(x=750, y=60)
        frameT = Frame(self.main_frame, width=500, height=4,
                       bg="black").place(x=750, y=60)
        frameB = Frame(self.main_frame, width=504, height=4,
                       bg="black").place(x=750, y=680)
        frameL = Frame(self.main_frame, width=4, height=640,
                       bg='black').place(x=750, y=60)
        frameR = Frame(self.main_frame, width=4, height=640,
                       bg='black').place(x=1250, y=60)

        # Adding extra images and icons to the frame created
        self.icon = Image.open("Images_icons\\user.png")
        self.resized_icon = self.icon.resize((140, 140))
        self.photo3 = ImageTk.PhotoImage(self.resized_icon)
        photo_label3 = Label(
            self.main_frame, image=self.photo3, border=0, bg="white")
        photo_label3.place(x=780, y=100)

        # Back Button Icon
        self.back_icon = Image.open("Images_icons\\BackArrow.png")
        self.back_resized = self.back_icon.resize((50, 40))
        self.photo_icon2 = ImageTk.PhotoImage(self.back_resized)

        # arrow icon for procced button
        self.arrow = Image.open("Images_icons\\right-arrow.png")
        self.arrow_resized = self.arrow.resize((50, 40))
        self.photo5 = ImageTk.PhotoImage(self.arrow_resized)

    # Setting other attributes of the Frame
    def Other(self):
        # Display the text to the user
        txt_greet = Label(self.main_frame, text='Hey Worker,', bg='white',
                          anchor='w', font=('Times new roman', 30, 'bold'))
        txt = Label(self.main_frame, text='         Please fill the details \nbelow to register with us...',
                    bg='white', font=('Times new roman', 22, 'bold'))
        txt_greet.place(x=920, y=110)
        txt.place(x=920, y=160)

        # Creating the back button
        self.back_button = Button(self.main_frame, bg='white', cursor='hand2',
                                  image=self.photo_icon2, border=0, command=self.Back_page)
        self.back_button.place(x=760, y=70)

        # Creating button for user to proceed
        self.arrow_button = Button(self.main_frame, image=self.photo5,
                                   bg="white", border=0, cursor='hand2', command=self.Proceed)
        self.arrow_button.place(x=1120, y=625)

    # Taking Data as an input from the user
    def Inputdata(self):
        # Taking First Name as input from the user
        self.txt1 = Label(self.main_frame, text="First Name :",
                          font=("cosmicsansms", 18, "bold"), bg='white')
        self.txt1.place(x=810, y=270)
        self.First_name = StringVar()
        self.FnameEntry = Entry(self.main_frame, textvariable=self.First_name, border=0,
                                width=16, bg='white', font=('Microsoft YaHei UI Light', 16, 'bold'))
        self.FnameEntry.place(x=970, y=270)
        self.frame_line1 = Frame(
            self.main_frame, bg="black", width=200, height=3).place(x=960, y=300)

        # Taking Last Name as input from the user
        self.txt2 = Label(self.main_frame, text="Last Name :",
                          font=("cosmicsansms", 18, "bold"), bg='white')
        self.txt2.place(x=810, y=320)
        self.Last_name = StringVar()
        self.LnameEntry = Entry(self.main_frame, textvariable=self.Last_name, border=0,
                                width=16, bg='white', font=('Microsoft YaHei UI Light', 16, 'bold'))
        self.LnameEntry.place(x=970, y=320)
        self.frame_line2 = Frame(
            self.main_frame, bg="black", width=200, height=3).place(x=960, y=350)

        # Taking E-mail as input from the user
        self.txt3 = Label(self.main_frame, text="   E-mail     :",
                          font=("cosmicsansms", 18, "bold"), bg='white')
        self.txt3.place(x=810, y=370)
        self.mail = StringVar()
        self.mailEntry = Entry(self.main_frame, textvariable=self.mail, border=0,
                               width=16, bg='white', font=('Microsoft YaHei UI Light', 16, 'bold'))
        self.mailEntry.place(x=970, y=370)
        self.frame_line3 = Frame(
            self.main_frame, bg="black", width=200, height=3).place(x=960, y=400)

        # Taking worker's Profession as input from the user
        self.txt4 = Label(self.main_frame, text="Proffesion :",
                          font=("cosmicsansms", 18, "bold"), bg='white')
        self.txt4.place(x=810, y=520)
        self.Profession = StringVar()
        self.Profession_box = ttk.Combobox(root, width=14, font=(
            'Microsoft YaHei UI Light', 16, 'bold'), textvariable=self.Profession)
        self.Profession_box['values'] = (
            'Electrician', 'Plumber', 'Laundry', 'Mechanic')
        self.Profession_box.place(x=960, y=520)
        self.frame_line4 = Frame(
            self.main_frame, bg="black", width=200, height=3).place(x=960, y=550)

        # Taking Landmark as input from the user
        self.txt5 = Label(self.main_frame, text="Landmark  :",
                          font=("cosmicsansms", 18, "bold"), bg='white')
        self.txt5.place(x=810, y=570)
        self.Landmark = StringVar()
        self.Landmark_box = ttk.Combobox(root, width=14, font=(
            'Microsoft YaHei UI Light', 16, 'bold'), textvariable=self.Landmark)
        self.Landmark_box['values'] = ('VIITMainGate')
        self.Landmark_box.place(x=960, y=570)
        self.frame_line5 = Frame(
            self.main_frame, bg="black", width=200, height=3).place(x=960, y=600)

        # Taking Distance as input from the user
        self.txt6 = Label(self.main_frame, text="  Distance   :", font=(
            "cosmicsansms", 18, "bold"), bg='white')
        self.txt6.place(x=810, y=420)
        self.Distance = StringVar()
        self.DistanceEntry = Entry(self.main_frame, textvariable=self.Distance, border=0,
                                   width=16, bg='white', font=('Microsoft YaHei UI Light', 16, 'bold'))
        self.DistanceEntry.place(x=970, y=420)
        self.frame_line6 = Frame(
            self.main_frame, bg="black", width=200, height=3).place(x=960, y=450)

        # Taking Weblink as input from the user
        self.txt7 = Label(self.main_frame, text="  Weblink   :", font=(
            "cosmicsansms", 18, "bold"), bg='white')
        self.txt7.place(x=810, y=470)
        self.Weblink = StringVar()
        self.WeblinkEntry = Entry(self.main_frame, textvariable=self.Weblink, border=0,
                                  width=16, bg='white', font=('Microsoft YaHei UI Light', 16, 'bold'))
        self.WeblinkEntry.place(x=970, y=470)
        self.frame_line7 = Frame(
            self.main_frame, bg="black", width=200, height=3).place(x=960, y=500)


# This is the reset password page
class ResetPassPage(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        root.setStatus("Reset password ...")

        # Creates the main frame to navigate through pages
        self.main_frame = Frame(
            root, bg="white", width=root.scrwidth, height=root.scrheight-85)
        self.main_frame.place(x=0, y=0)

        # Calling the class functions
        self.insertImage()
        self.Other()

    # Returns to the previous Page depending upon the type
    def Backpage(self):
        Userlogin = UserLoginFrame(root)
        self.main_frame.destroy()

    # Makes checks on the input
    def Register(self):

        # Extreacting the input
        self.Pass1 = self.CreatePassword.get()
        self.Pass2 = self.ConfirmPassword.get()

        # Displaying the status of the program to the User
        import time
        root.setStatus("Checking Passwords ...")
        time.sleep(0.25)

        # Checks if any of the passwords entered is empty
        if self.Pass1 == '' or self.Pass2 == '':
            tmsg.showerror(
                'Error !', 'Please fill all the blanks before proceeding !')
        else:
            # If passwords entered matched the User gets registered Sucessfully
            if self.Pass1 == self.Pass2:
                prj.ChangeUserPass(Phone_num, self.Pass1)
                tmsg.showinfo('Password Reset Sucessfully',
                              'Please Log in to use the app ...')
                Main_frame = MainFrame(root)
                self.main_frame.destroy()
            else:
                self.CreatePassEntry.delete(0, END)
                self.ConfirmPassEntry.delete(0, END)
                tmsg.showerror(
                    'Error', 'The entered Passwords have not matched !\nPlease re-enter...')

    # Inserting images to the Frame
    def insertImage(self):

        # importing the Pillow module
        from PIL import ImageTk, Image

        # Adding the Background image
        self.img = Image.open("Images_icons\\Createpass.jpg")
        self.resized_img = self.img.resize((750, 683))
        self.photo1 = ImageTk.PhotoImage(self.resized_img)
        photo_label1 = Label(
            self.main_frame, image=self.photo1, anchor='ne', border=0)
        photo_label1.place(x=0, y=0)

        # Creating frames
        self.sub_frame = Frame(self.main_frame, height=565,
                               width=500, bg="white", borderwidth=5).place(x=750, y=60)
        frameT = Frame(self.main_frame, width=500, height=4,
                       bg="black").place(x=750, y=60)
        frameB = Frame(self.main_frame, width=504, height=4,
                       bg="black").place(x=750, y=625)
        frameL = Frame(self.main_frame, width=4, height=565,
                       bg='black').place(x=750, y=60)
        frameR = Frame(self.main_frame, width=4, height=565,
                       bg='black').place(x=1250, y=60)

        # Adding extra images and icons to the frame created
        self.icon = Image.open("Images_icons\\user_icon.png")
        self.resized_icon = self.icon.resize((150, 150))
        self.photo3 = ImageTk.PhotoImage(self.resized_icon)

        # Back Button Icon
        self.back_icon = Image.open("Images_icons\\BackArrow.png")
        self.back_resized = self.back_icon.resize((60, 50))
        self.photo_icon2 = ImageTk.PhotoImage(self.back_resized)

        # SignUp icon for procced button
        self.Sign_up = Image.open("Images_icons\\right-arrow.png")
        self.Sign_up_resized = self.Sign_up.resize((100, 75))
        self.photo5 = ImageTk.PhotoImage(self.Sign_up_resized)

    # Adding other attributes to the Frame
    def Other(self):
        # Display the text depending upon the user type
        self.Name = prj.ExtractName(Phone_num, Type)
        txt_greet = Label(self.main_frame, text=f'Hey {self.Name},', bg='white', anchor='w', font=(
            'Times new roman', 30, 'bold'))
        txt = Label(self.main_frame, text='        Please reset your Password to \ncontinue ...                                    ',
                    bg='white', font=('Times new roman', 22, 'bold'))
        txt_greet.place(x=790, y=240)
        txt.place(x=790, y=290)

        # Placing the icon here just to overlap it on the previous label
        self.photo_label3 = Label(
            self.main_frame, image=self.photo3, border=0, bg="white")
        self.photo_label3.place(x=925, y=80)

        # Creating the back button
        self.back_button = Button(self.main_frame, bg='white', cursor='hand2',
                                  image=self.photo_icon2, border=0, command=self.Backpage)
        self.back_button.place(x=770, y=80)

        # Creating Entry Widgets for Password Entry
        self.txt1 = Label(self.main_frame, text=" Create Password  :",
                          font=("cosmicsansms", 18, "bold"), bg='white')
        self.txt1.place(x=790, y=400)
        self.CreatePassword = StringVar()
        self.CreatePassEntry = Entry(self.main_frame, textvariable=self.CreatePassword, border=0,
                                     width=16, bg='white', show='*', font=('Microsoft YaHei UI Light', 16, 'bold'))
        self.CreatePassEntry.place(x=1040, y=400)
        self.frame_line1 = Frame(
            self.main_frame, bg="black", width=170, height=3).place(x=1035, y=430)

        self.txt2 = Label(self.main_frame, text="Confirm Password :",
                          font=("cosmicsansms", 18, "bold"), bg='white')
        self.txt2.place(x=790, y=460)
        self.ConfirmPassword = StringVar()
        self.ConfirmPassEntry = Entry(self.main_frame, textvariable=self.ConfirmPassword, border=0,
                                      width=16, bg='white', show='*', font=('Microsoft YaHei UI Light', 16, 'bold'))
        self.ConfirmPassEntry.place(x=1040, y=460)
        self.frame_line1 = Frame(
            self.main_frame, bg="black", width=170, height=3).place(x=1035, y=490)

        # Creating button for user to proceed
        self.Signup_button = Button(self.main_frame, image=self.photo5,
                                    bg="white", border=0, cursor='hand2', command=self.Register)
        self.Signup_button.place(x=1050, y=540)


# Creates the password and registers the user
class CreatePassPage(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        root.setStatus("Create password ...")

        # Creates the main frame to navigate through pages
        self.main_frame = Frame(
            root, bg="white", width=root.scrwidth, height=root.scrheight-85)
        self.main_frame.place(x=0, y=0)

        # Calling the class functions
        self.insertImage()
        self.Other()

    # Returns to the previous Page depending upon the type
    def Backpage(self):
        # For worker
        if Type == 'Worker':
            registerWorker_Page = registerWorker(root)
            self.main_frame
        # For User
        elif Type == 'User':
            registerUser_page = registerUser(root)
            self.main_frame
        else:
            tmsg.showwarning('Warnning !', 'Sorry , Something went wrong !')
            exit()

    # Registers by adding the data to CSV files
    def AddData_tocsv(self):
        if Type == 'User':
            prj.CreateUserAccount(Phone_num, User_FName,
                                  User_LName, User_Email, self.Pass1)
        elif Type == 'Worker':
            prj.CreateWorkerAccount(Phone_num, Worker_Profession, Worker_FName, Worker_LName,
                                    Worker_Email, Worker_Landmark, Worker_Distance, Worker_Weblink)
        else:
            tmsg.showerror('Error', "Sorry , Something went wrong !")
            exit()

    # Makes checks on the input
    def Register(self):

        # Extreacting the input
        self.Pass1 = self.CreatePassword.get()
        self.Pass2 = self.ConfirmPassword.get()

        # Displaying the status of the program to the User
        import time
        root.setStatus("Checking Passwords ...")
        time.sleep(0.25)

        # Checks if any of the passwords entered is empty
        if self.Pass1 == '' or self.Pass2 == '':
            tmsg.showerror(
                'Error !', 'Please fill all the blanks before proceeding !')
        else:
            # If passwords entered matched the User gets registered Sucessfully
            if self.Pass1 == self.Pass2:
                self.AddData_tocsv()
                root.setStatus("Registered Sucessfully ...")
                tmsg.showinfo('Registered Sucessfully',
                              'Please Log in to use the app ...')
                Main_frame = MainFrame(root)
                self.main_frame.destroy()
            else:
                self.CreatePassEntry.delete(0, END)
                self.ConfirmPassEntry.delete(0, END)
                tmsg.showerror(
                    'Error', 'The entered Passwords have not matched !\nPlease re-enter...')

    # Inserting images to the Frame
    def insertImage(self):

        # importing the Pillow module
        from PIL import ImageTk, Image

        # Adding the Background image
        self.img = Image.open("Images_icons\\Createpass.jpg")
        self.resized_img = self.img.resize((750, 683))
        self.photo1 = ImageTk.PhotoImage(self.resized_img)
        photo_label1 = Label(
            self.main_frame, image=self.photo1, anchor='ne', border=0)
        photo_label1.place(x=0, y=0)

        # Creating frames
        self.sub_frame = Frame(self.main_frame, height=565,
                               width=500, bg="white", borderwidth=5).place(x=750, y=60)
        frameT = Frame(self.main_frame, width=500, height=4,
                       bg="black").place(x=750, y=60)
        frameB = Frame(self.main_frame, width=504, height=4,
                       bg="black").place(x=750, y=625)
        frameL = Frame(self.main_frame, width=4, height=565,
                       bg='black').place(x=750, y=60)
        frameR = Frame(self.main_frame, width=4, height=565,
                       bg='black').place(x=1250, y=60)

        # Adding extra images and icons to the frame created
        self.icon = Image.open("Images_icons\\user_icon.png")
        self.resized_icon = self.icon.resize((150, 150))
        self.photo3 = ImageTk.PhotoImage(self.resized_icon)

        # Back Button Icon
        self.back_icon = Image.open("Images_icons\\BackArrow.png")
        self.back_resized = self.back_icon.resize((60, 50))
        self.photo_icon2 = ImageTk.PhotoImage(self.back_resized)

        # SignUp icon for procced button
        self.Sign_up = Image.open("Images_icons\\Signup_button.png")
        self.Sign_up_resized = self.Sign_up.resize((125, 75))
        self.photo5 = ImageTk.PhotoImage(self.Sign_up_resized)

    # Adding other attributes to the Frame
    def Other(self):
        # Display the text depending upon the user type
        if Type == 'User':
            txt_greet = Label(self.main_frame, text=f'Hey {User_FName.title()},', bg='white', anchor='w', font=(
                'Times new roman', 30, 'bold'))
            txt = Label(self.main_frame, text='          Please set your Password to \nregister with us...                             ',
                        bg='white', font=('Times new roman', 22, 'bold'))
            txt_greet.place(x=790, y=240)
            txt.place(x=790, y=290)
        elif Type == 'Worker':
            txt_greet = Label(self.main_frame, text=f'Hey {Worker_FName.title()},', bg='white', anchor='w', font=(
                'Times new roman', 30, 'bold'))
            txt = Label(self.main_frame, text='          Please set your Password to \nregister with us...                             ',
                        bg='white', font=('Times new roman', 22, 'bold'))
            txt_greet.place(x=790, y=240)
            txt.place(x=790, y=290)
        else:
            pass

        # Placing the icon here just to overlap it on the previous label
        self.photo_label3 = Label(
            self.main_frame, image=self.photo3, border=0, bg="white")
        self.photo_label3.place(x=925, y=80)

        # Creating the back button
        self.back_button = Button(self.main_frame, bg='white', cursor='hand2',
                                  image=self.photo_icon2, border=0, command=self.Backpage)
        self.back_button.place(x=770, y=80)

        # Creating Entry Widgets for Password Entry
        self.txt1 = Label(self.main_frame, text=" Create Password  :",
                          font=("cosmicsansms", 18, "bold"), bg='white')
        self.txt1.place(x=790, y=400)
        self.CreatePassword = StringVar()
        self.CreatePassEntry = Entry(self.main_frame, textvariable=self.CreatePassword, border=0,
                                     width=16, bg='white', show='*', font=('Microsoft YaHei UI Light', 16, 'bold'))
        self.CreatePassEntry.place(x=1040, y=400)
        self.frame_line1 = Frame(
            self.main_frame, bg="black", width=170, height=3).place(x=1035, y=430)

        self.txt2 = Label(self.main_frame, text="Confirm Password :",
                          font=("cosmicsansms", 18, "bold"), bg='white')
        self.txt2.place(x=790, y=460)
        self.ConfirmPassword = StringVar()
        self.ConfirmPassEntry = Entry(self.main_frame, textvariable=self.ConfirmPassword, border=0,
                                      width=16, bg='white', show='*', font=('Microsoft YaHei UI Light', 16, 'bold'))
        self.ConfirmPassEntry.place(x=1040, y=460)
        self.frame_line1 = Frame(
            self.main_frame, bg="black", width=170, height=3).place(x=1035, y=490)

        # Creating button for user to proceed
        self.Signup_button = Button(self.main_frame, image=self.photo5,
                                    bg="white", border=0, cursor='hand2', command=self.Register)
        self.Signup_button.place(x=1050, y=540)


# Main UI of the app
class MainUI(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        root.setStatus("Welcome ...")
        Home_page = HomePage(root)

        # Ctreaing the static sub-frames of the UI
        self.main_subframe_left = Frame(
            root, width=300, bg='white', height=root.scrheight-85)
        self.main_subframe_left.place(x=0, y=0)
        Frame(root, width=5, bg='green',
              height=root.scrheight-85).place(x=300, y=0)

        self.main_subframe_top = Frame(
            root, width=root.scrwidth-305, height=40, bg='lightyellow')
        self.main_subframe_top.place(x=305, y=0)
        Frame(root, height=5, width=root.scrwidth -
              305, bg='yellow').place(x=305, y=40)

        # self.getConfiguredName()
        self.configure_leftFrame()
        self.configure_topFrame()

    # Returns to the home page when HOME Button is clicked
    def ToHomePage(self):
        # Overlaps the current farme
        Home_page = HomePage(root)

    def ViewProfile(self):
        pass

    def configure_leftFrame(self):
        # Adding the images
        from PIL import Image, ImageTk

        # Adding the User Icon
        self.icon = Image.open("Images_icons\\user_icon.png")
        self.resized_icon = self.icon.resize((140, 140))
        self.photo1 = ImageTk.PhotoImage(self.resized_icon)
        self.photo_label1 = Label(
            self.main_subframe_left, image=self.photo1, border=0, bg="white")
        self.photo_label1.place(x=75, y=40)

        # Creating the label for all buttons
        self.arrow_label1 = Label(
            self.main_subframe_left, text='>>', bg='white', fg='black', border=0, font='lucida 20')
        self.arrow_label2 = Label(
            self.main_subframe_left, text='>>', bg='white', fg='black', border=0, font='lucida 20')
        self.arrow_label3 = Label(
            self.main_subframe_left, text='>>', bg='white', fg='black', border=0, font='lucida 20')
        self.arrow_label4 = Label(
            self.main_subframe_left, text='>>', bg='white', fg='black', border=0, font='lucida 20')
        self.arrow_label5 = Label(
            self.main_subframe_left, text='>>', bg='white', fg='black', border=0, font='lucida 20')
        self.arrow_label6 = Label(
            self.main_subframe_left, text='>>', bg='white', fg='black', border=0, font='lucida 20')
        self.arrow_label7 = Label(
            self.main_subframe_left, text='>>', bg='white', fg='black', border=0, font='lucida 20')

        '''****Adding the buttons****'''
        # Adding home buttton to navigate through the pages
        self.Home_button = Button(self.main_subframe_left, fg='cyan2', border=0, font='lucida 24 underline',
                                  bg='white', cursor='hand2', text="Home", command=self.ToHomePage)
        self.Home_button.place(x=60, y=236)
        self.arrow_label1.place(x=25, y=250)

        # Adding Profile buttton to view user profile
        self.Profile_button = Button(self.main_subframe_left, fg='cyan2', border=0, font='lucida 24 underline',
                                     bg='white', cursor='hand2', text="My Profile", command=self.ViewProfile)
        self.Profile_button.place(x=60, y=281)
        self.arrow_label2.place(x=25, y=295)

        # Adding ContactUs buttton
        self.Home_button = Button(self.main_subframe_left, fg='cyan2', border=0, font='lucida 24 underline',
                                  bg='white', cursor='hand2', text="Contact Us")
        self.Home_button.place(x=60, y=326)
        self.arrow_label3.place(x=25, y=340)

        # Adding Report a bug Button
        self.Home_button = Button(self.main_subframe_left, fg='cyan2', border=0, font='lucida 24 underline',
                                  bg='white', cursor='hand2', text="Report a bug")
        self.Home_button.place(x=60, y=371)
        self.arrow_label4.place(x=25, y=385)

        # Adding Give Feedback Button
        self.Home_button = Button(self.main_subframe_left, fg='cyan2', border=0, font='lucida 24 underline',
                                  bg='white', cursor='hand2', text="Give Feedback")
        self.Home_button.place(x=60, y=416)
        self.arrow_label5.place(x=25, y=430)

        # Adding Settings Button to change the GUI setting and some on screen parameters
        self.Home_button = Button(self.main_subframe_left, fg='cyan2', border=0, font='lucida 24 underline',
                                  bg='white', cursor='hand2', text="Settings")
        self.Home_button.place(x=60, y=461)
        self.arrow_label6.place(x=25, y=475)

        # Adding View History Button to get the login as well as search history
        self.Home_button = Button(self.main_subframe_left, fg='cyan2', border=0, font='lucida 24 underline',
                                  bg='white', cursor='hand2', text="View History")
        self.Home_button.place(x=60, y=509)
        self.arrow_label7.place(x=25, y=525)

    def configure_topFrame(self):
        # Adding time to GUI Window
        from time import strftime
        # Gets current time and configure the label

        def time():
            self.str1 = strftime(' %H : %M ')
            self.time_label.config(text=self.str1)
            self.time_label.after(1000, time)

        self.time_label = Label(self.main_subframe_top,
                                font='calibri 26 bold', bg='white')
        self.time_label.place(x=920, y=0)
        time()

        date = datetime.datetime.now()
        date_text = f"{date:%A, %B %d, %Y}"
        Label(text=date_text, font='calibri 20 bold',
              bg='white').place(x=800, y=0)


# Home page of the app
class HomePage(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        # Creating the variable sub-frame of the UI
        self.main_frame = Frame(
            root, width=root.scrwidth-305, height=root.scrheight-130, bg='white')
        self.main_frame.place(x=305, y=45)

        # Calling class functions
        self.insertImages()
        self.Other()

    # This function proceeds the user to next page
    def Proceed(self):
        self.UserRequiredLandmark = self.Landmark.get()
        self.UserRequiredWorkerType = self.Profession.get()
        import time
        root.setStatus('Checking Input ...')
        time.sleep(0.25)
        root.setStatus('Ready')
        if self.UserRequiredLandmark == 'None' or self.UserRequiredWorkerType == 'None':
            tmsg.showerror(
                'Error !', 'Please select the radiobutton before proceeding ...')
        else:
            # Creating the global variables
            global UserREQLandmark
            global UserREQProfession

            UserREQLandmark = self.UserRequiredLandmark
            UserREQProfession = self.UserRequiredWorkerType

            # Calling next class
            DisplayName_Page = DisplayPage(root)
            self.main_frame.destroy()

    # Inserting Images to the GUI
    def insertImages(self):
        # importing the Pillow module
        from PIL import ImageTk, Image

        # Adding the Background image
        self.img = Image.open("Images_icons\\search.jpg")
        self.resized_img = self.img.resize((650, 623))
        self.photo1 = ImageTk.PhotoImage(self.resized_img)
        photo_label1 = Label(
            self.main_frame, image=self.photo1, anchor='ne', border=0)
        photo_label1.place(x=10, y=5)

        # Adding image to the proceed button
        self.arrow = Image.open("Images_icons\\right-arrow.png")
        self.arrow_resized = self.arrow.resize((60, 50))
        self.photo5 = ImageTk.PhotoImage(self.arrow_resized)

    # Adding other required attributes to the GUI
    def Other(self):

        # Displaying texts on the frame
        self.Instruct_label = Label(self.main_frame, text="Choose from the options below \nto get the desired worker ...\n", font=(
            'Times new Roman', 28, 'bold'), bg='white')
        self.Instruct_label.place(x=560, y=30)

        # Taking required profession as input
        self.Profession_label = Label(
            self.main_frame, text='Profession :', bg='white', font=('Times new Roman', 26, 'bold'))
        self.Profession_label.place(x=680, y=160)

        # Creating RadioButtons
        self.Profession = StringVar()
        self.option1 = Radiobutton(self.main_frame, text='Electrician', cursor='hand2', variable=self.Profession,
                                   value='Electrician', bg='white', font=('Lucida', 20, 'bold'))
        self.option1.place(x=740, y=210)
        self.option1.deselect()

        self.option2 = Radiobutton(self.main_frame, text='Plumber', cursor='hand2', variable=self.Profession,
                                   value='Plumber', bg='white', font=('Lucida', 20, 'bold'))
        self.option2.place(x=740, y=250)
        self.option2.deselect()

        self.option3 = Radiobutton(self.main_frame, text='Laundry', cursor='hand2', variable=self.Profession,
                                   value='Laundry', bg='white', font=('Lucida', 20, 'bold'))
        self.option3.place(x=740, y=290)
        self.option3.deselect()

        self.option4 = Radiobutton(self.main_frame, text='Mechanic', cursor='hand2', variable=self.Profession,
                                   value='Mechanic', bg='white', font=('Lucida', 20, 'bold'))
        self.option4.place(x=740, y=330)
        self.option4.deselect()

        # Setting the initial value of the Profession variable
        self.Profession.set(None)

        # Taking required Landmark as input
        self.Landmark_label = Label(self.main_frame, text='Landmark :', bg='white', font=(
            'Times new Roman', 26, 'bold'))
        self.Landmark_label.place(x=680, y=400)

        # Creating RadioButtons
        self.Landmark = StringVar()
        self.option1 = Radiobutton(self.main_frame, text='VIIT Main Gate', variable=self.Landmark,
                                   value='VIITMainGate', cursor='hand2', bg='white', font=('Lucida', 20, 'bold'))
        self.option1.place(x=740, y=450)
        self.option1.deselect()

        # Setting the initial value of the Landmark variable
        self.Landmark.set(None)

        # Creating button for user to proceed
        self.arrow_button = Button(self.main_frame, image=self.photo5,
                                   bg="white", border=0, cursor='hand2', command=self.Proceed)
        self.arrow_button.place(x=900, y=530)


# Page which Displays the names and distances of required workers
class DisplayPage(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        # Creating the variable sub-frame of the UI
        self.main_frame = Frame(
            root, width=root.scrwidth-305, height=root.scrheight-130, bg='white')
        self.main_frame.place(x=305, y=45)

        # Calling class functions
        self.insertImages()
        self.getAvailableWorkers()
        self.Other()

    # Get the available workers as per the user's requirement
    def getAvailableWorkers(self):

        # Calling project file's function
        self.AvailableWorkers, self.RequiredIndexes, self.Name, self.raw_Distance = prj.DisplayAvailabeWorkers(
            UserREQLandmark, UserREQProfession)
        self.NumOfWorkers = len(self.AvailableWorkers)

    # Inserting images to the GUI to make it interesting
    def insertImages(self):

        # importing the Pillow module
        from PIL import ImageTk, Image

        # Adding the Background image
        self.img = Image.open("Images_icons\\Display_names.jpg")
        self.resized_img = self.img.resize((650, 623))
        self.photo1 = ImageTk.PhotoImage(self.resized_img)
        photo_label1 = Label(
            self.main_frame, image=self.photo1, anchor='ne', border=0)
        photo_label1.place(x=10, y=5)

        # Creating frames
        self.sub_frame = Frame(self.main_frame, height=510,
                               width=400, bg="blue", borderwidth=5).place(x=650, y=85)

        """******************************Adding the Scrollbar*******************************"""

        self.my_canvas = Canvas(self.main_frame, bg='white')
        self.my_canvas.place(in_=self.main_frame,
                             height=510, width=400, x=650, y=85)

        self.my_scrollbar = Scrollbar(
            self.main_frame, orient=VERTICAL, command=self.my_canvas.yview)
        self.my_scrollbar.place(in_=self.main_frame, x=1033, y=85, height=510)

        self.my_canvas.configure(yscrollcommand=self.my_scrollbar.set)
        self.my_canvas.configure(scrollregion=(0, 0, 400, 1100))

        self.frame = Frame(self.my_canvas, width=400, height=510, bg='white')
        self.frame.pack()

        self.my_canvas.create_window((0, 0), window=self.frame, anchor='nw')

        # Creating the outline of the main frame
        frameT = Frame(self.main_frame, width=400, height=4,
                       bg="black").place(x=650, y=85)
        frameB = Frame(self.main_frame, width=404, height=4,
                       bg="black").place(x=650, y=595)
        frameL = Frame(self.main_frame, width=4, height=510,
                       bg='black').place(x=650, y=85)
        frameR = Frame(self.main_frame, width=4, height=510,
                       bg='black').place(x=1050, y=85)

        # Adding the sort button
        self.sort_icon = Image.open("Images_icons\\sort.png")
        self.sort_resized = self.sort_icon.resize((50, 40))
        self.photo_icon2 = ImageTk.PhotoImage(self.sort_resized)

    # Sorts the availabe workers by Distance from VIIT Main gate
    def sort_byDistance(self):
        import time
        # Processing the raw distance to make it usable
        self.Distance = []
        for i in self.raw_Distance:
            self.dist = ''
            for j in i:
                if j in [f'{i}' for i in range(10)]:
                    self.dist += j
                else:
                    pass
            self.Distance.append(int(self.dist))

        # Creating the dictionary for sorting purpose
        self.indices = [i for i in range(len(self.AvailableWorkers))]
        Worker_info_dict = {}
        for i, j in zip(self.indices, self.Distance):
            Worker_info_dict[i] = j

        # Sorting the dict by values
        Worker_info_dict = sorted(Worker_info_dict.items(), key=lambda x: x[1])

        # Displaying the status of the program to the user
        root.setStatus("Sorting by Distance ...")
        time.sleep(0.25)
        # Clearing the contents of the main frame
        for widget in self.frame.winfo_children():
            widget.destroy()

        # Adding the sorted workers in the canvas widget
        for idx, i in enumerate(Worker_info_dict):
            def func(x=i[0]):
                return self.DisplayDetailed(x)
            Button(self.frame, text=f'{idx+1}. {self.AvailableWorkers[i[0]]}', border=0, font='lucida 19 bold',
                   cursor='hand2', bg='white', command=func).pack(side=TOP, anchor='w', pady=10)

        root.setStatus("Ready ...")

    # Sorts the available workers by Name
    def sort_byName(self):
        import time

        self.indices = [i for i in range(len(self.AvailableWorkers))]
        Worker_info_dict = {}
        for i, j in zip(self.indices, self.Name):
            Worker_info_dict[i] = j

        # Sorting the dict by values
        Worker_info_dict = sorted(Worker_info_dict.items(), key=lambda x: x[1])

        # Displaying the status of the program to the user
        root.setStatus("Sorting by Name ...")
        time.sleep(0.25)

        # Clearing the contents of the main frame
        for widget in self.frame.winfo_children():
            widget.destroy()

        # Adding the sorted workers in the canvas widget
        for idx, i in enumerate(Worker_info_dict):
            def func(x=i[0]):
                return self.DisplayDetailed(x)
            Button(self.frame, text=f'{idx+1}. {self.AvailableWorkers[i[0]]}', border=0, font='lucida 19 bold',
                   cursor='hand2', bg='white', command=func).pack(side=TOP, anchor='w', pady=10)

        root.setStatus("Ready ...")

    # Placing the available workers Frames
    def PlaceAvailableWorkers(self):
        for idx, i in enumerate(self.AvailableWorkers):
            def func(x=idx):
                return self.DisplayDetailed(x)

            Button(self.frame, text=f'{idx+1}. {i}', border=0, font='lucida 19 bold',
                   cursor='hand2', bg='white', command=func).pack(side=TOP, anchor='w', pady=10)

    # Display detailed info of the worker
    def DisplayDetailed(self, value):
        self.index = self.RequiredIndexes[value]
        Workerdata = prj.DisplayDetailedInfo(self.index)

        # Declaring the global Variable
        global REQ_WorkerDatalist
        REQ_WorkerDatalist = Workerdata

        # Calling the next Page
        DisplayDetails_Page = DisplayDetailsPage(root)
        self.main_frame.destroy()

    # Displaying other attributes of this GUI class
    def Other(self):

        # Displaying the text to the user
        txt = Label(self.main_frame, text="Available Workers",
                    bg='white', font=('Times new roman', 30, 'bold'))
        txt.place(x=645, y=25)
        Frame(self.main_frame, bg='black',
              width=335, height=3).place(x=643, y=70)

        # Adding the sort button
        self.sort_button = Menubutton(
            self.main_frame, image=self.photo_icon2, cursor="hand2", border=0, bg='white')
        self.sort_button.place(x=990, y=35)
        self.sort_button.menu = Menu(self.sort_button, tearoff=0)
        self.sort_button["menu"] = self.sort_button.menu

        self.sort_button.menu.add_command(
            label="By Distance", command=self.sort_byDistance)
        self.sort_button.menu.add_command(
            label="By Name", command=self.sort_byName)

        # Calling the place function to place the workers in the GUI
        self.PlaceAvailableWorkers()


# Page which display the details of the required worker
class DisplayDetailsPage(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        # Creating the variable sub-frame of the UI
        self.main_frame = Frame(
            root, width=root.scrwidth-305, height=root.scrheight-130, bg='white')
        self.main_frame.place(x=305, y=45)

        # Calling class functions
        self.insertImages()
        self.Other()

    # Taking the user to the previous page
    def Back_page(self):
        DisplayName_Page = DisplayPage(root)
        self.main_frame.destroy()

    # Redirect the user to maps on google chrome
    def Redirect(self):
        self.Weblink = REQ_WorkerDatalist[7]
        tmsg.showinfo('Redirecting !',
                      "You will be redirected to chrome window...")
        root.setStatus("Redirecting ...")
        import time
        prj.getDirections(self.Weblink)
        time.sleep(0.5)
        root.setStatus('Ready')

    # Inserting images to the GUI to make it interesting
    def insertImages(self):

        # importing the Pillow module
        from PIL import ImageTk, Image

        # Adding the Background image
        self.img = Image.open("Images_icons\\Get_Location.jpg")
        self.resized_img = self.img.resize((650, 623))
        self.photo1 = ImageTk.PhotoImage(self.resized_img)
        photo_label1 = Label(
            self.main_frame, image=self.photo1, anchor='ne', border=0)
        photo_label1.place(x=10, y=5)

        # Creating frames
        self.sub_frame = Frame(self.main_frame, height=580,
                               width=400, bg="white", borderwidth=5).place(x=650, y=30)
        frameT = Frame(self.main_frame, width=400, height=4,
                       bg="black").place(x=650, y=30)
        frameB = Frame(self.main_frame, width=404, height=4,
                       bg="black").place(x=650, y=610)
        frameL = Frame(self.main_frame, width=4, height=580,
                       bg='black').place(x=650, y=30)
        frameR = Frame(self.main_frame, width=4, height=580,
                       bg='black').place(x=1050, y=30)

        # Worker Icon
        self.icon = Image.open("Images_icons\\user_icon.png")
        self.resized_icon = self.icon.resize((120, 120))
        self.photo3 = ImageTk.PhotoImage(self.resized_icon)
        photo_label3 = Label(
            self.main_frame, image=self.photo3, border=0, bg="white")
        photo_label3.place(x=795, y=45)

        # Back Button Icon
        self.back_icon = Image.open("Images_icons\\BackArrow.png")
        self.back_resized = self.back_icon.resize((50, 40))
        self.photo_icon2 = ImageTk.PhotoImage(self.back_resized)

    # Declare other required attributes of the GUI class
    def Other(self):

        # Creating the back button
        self.back_button = Button(self.main_frame, bg='white', cursor='hand2',
                                  image=self.photo_icon2, border=0, command=self.Back_page)
        self.back_button.place(x=670, y=40)

        # Displaying First Name to the user
        self.txt1 = Label(self.main_frame, text="First Name :",
                          font=("Times new roman", 20, "bold"), bg='white')
        self.txt1.place(x=690, y=200)
        self.ans1 = Label(self.main_frame, text=REQ_WorkerDatalist[0],
                          font=("cosmicsansms", 20, "italic"), bg='white')
        self.ans1.place(x=845, y=200)

        # Displaying Last Name to the user
        self.txt2 = Label(self.main_frame, text="Last Name  :",
                          font=("Times new roman", 20, "bold"), bg='white')
        self.txt2.place(x=690, y=235)
        self.ans2 = Label(self.main_frame, text=REQ_WorkerDatalist[1],
                          font=("cosmicsansms", 20, "italic"), bg='white')
        self.ans2.place(x=845, y=235)

        # Displaying Profession to the user
        self.txt3 = Label(self.main_frame, text="Profession  :",
                          font=("Times new roman", 20, "bold"), bg='white')
        self.txt3.place(x=690, y=270)
        self.ans3 = Label(self.main_frame, text=REQ_WorkerDatalist[2],
                          font=("cosmicsansms", 20, "italic"), bg='white')
        self.ans3.place(x=845, y=270)

        # Displaying Contact to the user
        self.txt4 = Label(self.main_frame, text="Contact      :",
                          font=("Times new roman", 20, "bold"), bg='white')
        self.txt4.place(x=690, y=305)
        self.ans4 = Label(self.main_frame, text=REQ_WorkerDatalist[3],
                          font=("cosmicsansms", 20, "italic"), bg='white')
        self.ans4.place(x=845, y=305)

        # Displaying Landmark to the user
        self.txt5 = Label(self.main_frame, text="Landmark  :",
                          font=("Times new roman", 20, "bold"), bg='white')
        self.txt5.place(x=690, y=340)
        self.ans5 = Label(self.main_frame, text=REQ_WorkerDatalist[5],
                          font=("cosmicsansms", 20, "italic"), bg='white')
        self.ans5.place(x=845, y=340)

        # Displaying Distance to the user
        self.txt6 = Label(self.main_frame, text="Distance     :",
                          font=("Times new roman", 20, "bold"), bg='white')
        self.txt6.place(x=690, y=375)
        self.ans6 = Label(self.main_frame, text=REQ_WorkerDatalist[6],
                          font=("cosmicsansms", 20, "italic"), bg='white')
        self.ans6.place(x=845, y=375)

        # Displaying Email to the user
        self.txt7 = Label(self.main_frame, text="E-mail  :",
                          font=("Times new roman", 20, "bold"), bg='white')
        self.txt7.place(x=690, y=410)
        self.ans7 = Label(self.main_frame, text=REQ_WorkerDatalist[4],
                          font=("cosmicsansms", 16, "italic"), bg='white')
        self.ans7.place(x=800, y=415)

        self.getDirection_button = Button(self.main_frame, text='Get Direction >>>', border=0,
                                          cursor='hand2', fg='cyan', bg='white', font=('lucida', 24, 'bold'), command=self.Redirect)
        self.getDirection_button.place(x=720, y=530)
        Frame(self.main_frame, bg='cyan', width=300,
              height=5).place(x=715, y=580)


# The execution of the file
if __name__ == "__main__":
    try:
        root = App()
        Main_frame = MainFrame(root)
        root.mainloop()
    except Exception as E:

        # Gets the current time
        CurrentTime = datetime.datetime.now()

        # Append the error info in the file and exits the program
        with open("GUI_errors.txt", 'a') as f:
            f.write(f"Time : {str(CurrentTime)}\n")
            f.write(f"Exception : {str(E)}\n")
            f.write(f"{traceback.format_exc()}\n")
            f.close()
        print("Sorry , something went wrong !")
        exit()
