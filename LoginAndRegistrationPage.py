from tkinter import *
from PIL import ImageTk, Image  # type "Pip install pillow" in your terminal to install ImageTk and Image module
import re
import pandas as pd
import os

dataBase=list((pd.read_csv("Teacher.csv", index_col=[0]),pd.read_csv("UGStudent.csv", index_col=[0]),pd.read_csv("PGStudent.csv", index_col=[0])))



userName=""
passWord=""
uType=0

#==================================

window = Tk()
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)
window.state('zoomed')
window.resizable(0, 0)
window.title('Login and Registration Page')

# Window Icon Photo
icon = PhotoImage(file='images\\pic-icon.png')
window.iconphoto(True, icon)

LoginPage = Frame(window)
RegistrationPage = Frame(window)

for frame in (LoginPage, RegistrationPage):
    frame.grid(row=0, column=0, sticky='nsew')


def show_frame(frame):
    frame.tkraise()


show_frame(LoginPage)


# LOGIN PAGE

design_frame1 = Listbox(LoginPage, bg='black', width=window.winfo_screenwidth(), height=window.winfo_screenheight(), highlightthickness=0, borderwidth=0)
design_frame1.place(x=0, y=0)

design_frame3 = Listbox(LoginPage, bg='#1f2833', width=100, height=33, highlightthickness=2, borderwidth=0, highlightbackground='#49c5b6', highlightcolor="#49c5b6")
design_frame3.place(x=75, y=106)

design_frame4 = Listbox(LoginPage, bg='black', width=100, height=33, highlightthickness=2, borderwidth=0, highlightbackground='#49c5b6', highlightcolor="#49c5b6")
design_frame4.place(x=676, y=106)

# Email
email_entry0 = Entry(design_frame4, fg="#49c5b6", font=("yu gothic ui semibold", 12), highlightthickness=2, bg="#1f2833")
email_entry0.place(x=134, y=170, width=256, height=34)
email_entry0.config(highlightbackground="black", highlightcolor="#49c5b6")
email_label = Label(design_frame4, text='• Email Id', fg="#49c5b6", bg='black', font=("yu gothic ui", 11, 'bold'))
email_label.place(x=130, y=140)


# Password
password_entry1 = Entry(design_frame4, fg="#49c5b6", font=("yu gothic ui semibold", 12), show='•', highlightthickness=2, bg="#1f2833")
password_entry1.place(x=134, y=250, width=256, height=34)
password_entry1.config(highlightbackground="black", highlightcolor="#49c5b6")
password_label = Label(design_frame4, text='• Password', fg="#49c5b6", bg='black', font=("yu gothic ui", 11, 'bold'))
password_label.place(x=130, y=220)


# Incorrect Password
password_incorrect_label = Label(design_frame4, text='', fg="red", bg='black', font=("yu gothic ui", 11, 'bold'))
password_incorrect_label.place(x=130, y=310)

# function for show and hide password
def password_command():
    if password_entry1.cget('show') == '•':
        password_entry1.config(show='')
    else:
        password_entry1.config(show='•')


# Show password checkbutton 
checkButton = Checkbutton(design_frame4, bg='black', command=password_command, text='show password', fg="#49c5b6", activebackground="#1f2833", activeforeground="#45a29e", selectcolor="#1f2833")
checkButton.place(x=140, y=288)

# Sign Up Buttons
SignUp_button = Button(LoginPage, text='Sign up', font=("yu gothic ui bold", 12), bg='black', fg="#49c5b6", activeforeground="#45a29e",
                       command=lambda: show_frame(RegistrationPage), borderwidth=0, activebackground='#1f2833', cursor='hand2')
SignUp_button.place(x=1100, y=175)

# Welcome Label
welcome_label = Label(design_frame4, text='Welcome', font=('Arial', 20, 'bold'), bg='black', fg="#49c5b6")
welcome_label.place(x=130, y=15)

# top Login Button
login_button = Button(LoginPage, text='Login', font=("yu gothic ui bold", 12), bg='black', fg="#49c5b6", activeforeground="#45a29e",
                      borderwidth=0, activebackground='#1f2833', cursor='hand2')
login_button.place(x=845, y=175)

login_line = Canvas(LoginPage, width=60, height=5, bg='#49c5b6', highlightthickness=0)
login_line.place(x=840, y=203)

# On pressing Login
def loginUser():
    file1=open('temp.txt','w')
    email=email_entry0.get()
    password=password_entry1.get()
    global validUser
    global userType
    validUser=False
    for i in range(3):
        idx=dataBase[i][dataBase[i]['UserId'] == email]
        if len(idx)>0:
            
            validUser=True
            global ind
            ind=idx.index[0]
            userType=i
            if password==dataBase[i]['Password'][ind]:
                if(dataBase[i]['Attempts'][ind]>0):
                    dataBase[i].at[ind, 'Attempts']=3
                    password_incorrect_label.config(text='')
                    dataBase[0].to_csv("Teacher.csv", index=True, header=True)
                    dataBase[1].to_csv("UGStudent.csv", index=True, header=True)
                    dataBase[2].to_csv("PGStudent.csv", index=True, header=True)
                    file1.write(f"L\n{userType}\n{ind}")
                    file1.close()
                    window.withdraw()
                    os.system("python3 Dashboard.py")
                    window.destroy()
                    break
                else:
                    password_incorrect_label.config(text="Your account is deactivated. Contact Tech Support.")
                    email_entry0.delete(0, END)
                    password_entry1.delete(0, END)  
                    break
            else:
                if(dataBase[i]['Attempts'][ind]>0):
                    dataBase[i].at[ind, 'Attempts']-= 1
                    dataBase[0].to_csv("Teacher.csv", index=True, header=True)
                    dataBase[1].to_csv("UGStudent.csv", index=True, header=True)
                    dataBase[2].to_csv("PGStudent.csv", index=True, header=True)
                    password_incorrect_label.config(text='Incorrect Email Id or Password. You have only '+str(dataBase[i].at[ind, 'Attempts'])+' attempts remaining.')
                    email_entry0.delete(0, END)
                    password_entry1.delete(0, END)  
                    break
                else:
                    password_incorrect_label.config(text="Your account is deactivated. Contact Tech Support.")
                    email_entry0.delete(0, END)
                    password_entry1.delete(0, END)
                    break
        else:
            pass

    if validUser==False:
        password_incorrect_label.config(text='No Acount linked with given Email Id. Please Sign Up.')
        email_entry0.delete(0, END)
        password_entry1.delete(0, END)





# LOGIN  down button
loginBtn1 = Button(design_frame4, command=loginUser, fg='white', text='Login', bg='#49c5b6', font=("yu gothic ui bold", 15),
                   cursor='hand2', activebackground='#45a29e', activeforeground="#1f2833")
loginBtn1.place(x=133, y=340, width=256, height=50)


# ICONS 

# Email icon
email_icon = Image.open('images\\email2.png')
photo = ImageTk.PhotoImage(email_icon)
emailIcon_label = Label(design_frame4, image=photo, bg='black')
emailIcon_label.image = photo
emailIcon_label.place(x=100, y=170)

# password icon
password_icon = Image.open('images\\password2.png')
photo = ImageTk.PhotoImage(password_icon)
password_icon_label = Label(design_frame4, image=photo, bg='black')
password_icon_label.image = photo
password_icon_label.place(x=100, y=250)

# picture icon 
picture_icon = Image.open('images\\user3.png')
photo = ImageTk.PhotoImage(picture_icon)
picture_icon_label = Label(design_frame4, image=photo, bg='black')
picture_icon_label.image = photo
picture_icon_label.place(x=280, y=5)

# Left Side Picture
side_image = Image.open('images\\dash4.png')
photo = ImageTk.PhotoImage(side_image)
side_image_label = Label(design_frame3, image=photo, bg='#1f2833')
side_image_label.image = photo
side_image_label.place(x=50, y=10)


# FORGOT PASSWORD  PAGE 

def forgot_password():
    win = Toplevel()
    window_width = 350
    window_height = 350
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    position_top = int(screen_height / 4 - window_height / 4)
    position_right = int(screen_width / 2 - window_width / 2)
    win.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')
    win.title('Forgot Password')
    win.iconbitmap('images\\aa.ico')
    win.configure(background='black')
    win.resizable(0, 0)

    # ====== Email ====================
    email_entry2 = Entry(win, fg="#49c5b6", bg="#1f2833", font=("yu gothic ui semibold", 12), highlightthickness=2)
    email_entry2.place(x=40, y=30, width=256, height=34)
    email_entry2.config(highlightbackground="#1f2833", highlightcolor="#49c5b6")
    email_label2 = Label(win, text='• Email account', fg="#49c5b6", bg='black',
                         font=("yu gothic ui", 11, 'bold'))
    email_label2.place(x=40, y=0)

    # ====  New Password ==================
    new_password_entry = Entry(win, fg="#49c5b6", bg="#1f2833", font=("yu gothic ui semibold", 12), show='•', highlightthickness=2)
    new_password_entry.place(x=40, y=110, width=256, height=34)
    new_password_entry.config(highlightbackground="#1f2833", highlightcolor="#49c5b6")
    new_password_label = Label(win, text='• New Password', fg="#49c5b6", bg='black', font=("yu gothic ui", 11, 'bold'))
    new_password_label.place(x=40, y=80)

    # ====  Confirm Password ==================
    confirm_password_entry = Entry(win, fg="#49c5b6", bg="#1f2833", font=("yu gothic ui semibold", 12), show='•', highlightthickness=2)
    confirm_password_entry.place(x=40, y=190, width=256, height=34)
    confirm_password_entry.config(highlightbackground="#1f2833", highlightcolor="#49c5b6")
    confirm_password_label = Label(win, text='• Confirm Password', fg="#49c5b6", bg='black',
                                   font=("yu gothic ui", 11, 'bold'))
    confirm_password_label.place(x=40, y=160)

    # ======= Update password Button ============
    update_pass = Button(win, fg='white', text='Update Password', bg='#49c5b6', font=("yu gothic ui bold", 14),
                         cursor='hand2', activebackground='#45a29e', activeforeground="#1f2833")
    update_pass.place(x=40, y=240, width=256, height=50)


forgotPassword = Button(design_frame4, text='Forgot password', font=("yu gothic ui", 8, "bold underline"), bg='black', fg="#49c5b6",
                        borderwidth=0, activebackground='black', command=lambda: forgot_password(), cursor="hand2")
forgotPassword.place(x=290, y=290)


# REGISTRATION PAGE 

design_frame5 = Listbox(RegistrationPage, bg='black', width=window.winfo_screenwidth(), height=window.winfo_screenheight(), highlightthickness=0, borderwidth=0)
design_frame5.place(x=0, y=0)

design_frame7 = Listbox(RegistrationPage, bg='#1f2833', width=100, height=33, highlightthickness=2, borderwidth=0, highlightbackground="#49c5b6", highlightcolor="#49c5b6")
design_frame7.place(x=75, y=106)

design_frame8 = Listbox(RegistrationPage, bg='black', width=100, height=33, highlightthickness=2, borderwidth=0, highlightbackground="#49c5b6", highlightcolor="#49c5b6")
design_frame8.place(x=676, y=106)

# Type
options=["Teacher", "UG Student", "PG Student"]
variable = StringVar()
variable.set(options[0])
type_menu = OptionMenu(design_frame8, variable, *options)
type_menu.config(highlightbackground="#1f2833", highlightcolor="#49c5b6", font=("yu gothic ui semibold", 12), fg="#49c5b6", bg='#1f2833', activebackground="#1f2833", activeforeground="#45a29e")
menu=design_frame8.nametowidget(type_menu.menuname)
menu.config(bg='#1f2833', font=("yu gothic ui semibold", 12), fg="#49c5b6", activebackground="black", activeforeground="#45a29e")
type_menu.place(x=284, y=150, width=286, height=34)
type_label = Label(design_frame8, text='• Type of Account', fg="#49c5b6", bg='black', font=("yu gothic ui", 11, 'bold'))
type_label.place(x=280, y=120)



head=Label(design_frame8, text='', fg="#49c5b6", bg='black', font=("yu gothic ui", 11, 'bold'))
head.place(x=10, y=140)
condition1=Label(design_frame8, text='', fg="red", bg='black', font=("yu gothic ui", 11, 'bold'))
condition1.place(x=10, y=160)
condition2=Label(design_frame8, text='', fg="red", bg='black', font=("yu gothic ui", 11, 'bold'))
condition2.place(x=10, y=180)
condition3=Label(design_frame8, text='', fg="red", bg='black', font=("yu gothic ui", 11, 'bold'))
condition3.place(x=10, y=200)
condition4=Label(design_frame8, text='', fg="red", bg='black', font=("yu gothic ui", 11, 'bold'))
condition4.place(x=10, y=220)
condition5=Label(design_frame8, text='', fg="red", bg='black', font=("yu gothic ui", 11, 'bold'))
condition5.place(x=10, y=240)


# ======= Email ===========
em=StringVar()

email_entry = Entry(design_frame8, text=(em), fg="#49c5b6", bg="#1f2833", font=("yu gothic ui semibold", 12), highlightthickness=2)
email_entry.place(x=284, y=220, width=286, height=34)
email_entry.config(highlightbackground="#1f2883", highlightcolor="#49c5b6")
email_label = Label(design_frame8, text='• Email Id', fg="#49c5b6", bg='black', font=("yu gothic ui", 11, 'bold'))
email_label.place(x=280, y=190)

# UserIdChecker

def userIdCheck(*args):
    str2=em.get()
    condition1.config(text='')
    global userIdValid
    if re.match(r"^[a-zA-Z0-9_\-.]+@[a-zA-Z0-9_\-.]+\.[a-zA-Z]{2,}$", str2):
        userIdValid=True
    else:
        condition1.config(text='Invalid Email Id', fg="red")
        userIdValid=False
    if userIdValid:
        for i in range(3):
            if str2 in dataBase[i]['UserId']:
                condition1.config(text='Email Id Already Exists', fg="red")
                userIdValid=False
                break
            else:
                condition1.config(text='')


def userIdActive():
    em.trace('w', userIdCheck)

def userIdInactive():
    condition1.config(text='')
    


email_entry.bind('<Enter>', lambda event: userIdActive())
email_entry.bind('<Leave>', lambda event: userIdInactive())


# ====== Password =========
pw=StringVar()

password_entry = Entry(design_frame8, text=(pw), fg="#49c5b6", bg="#1f2833", font=("yu gothic ui semibold", 12), show='•', highlightthickness=2)
password_entry.place(x=284, y=295, width=286, height=34)
password_entry.config(highlightbackground="#1f2833", highlightcolor="#49c5b6")
password_label = Label(design_frame8, text='• Password', fg="#49c5b6", bg='black',
                       font=("yu gothic ui", 11, 'bold'))
password_label.place(x=280, y=265)

# Password Checker

req=list((False, False, False, False, False, True))

def passwordCheck(*args):
    str1=pw.get()
    head.config(text='• Password must contain:')
    condition1.config(text='• 8-12 characters')
    condition4.config(text='• At least one number')
    condition3.config(text='• At least one lowercase letter')
    condition2.config(text='• At least one uppercase letter')
    condition5.config(text='• At least one special character')
    condition1.config(fg='red')
    condition2.config(fg='red')
    condition3.config(fg='red')
    condition4.config(fg='red')
    condition5.config(fg='red')
    specialCharacter=list(('!','@','#','$','%','&','*'))
    for i in range(len(str1)):
        if(i>=7):
            condition1.config(fg='green')
            
            req[0]=True
        if(i>11):
            condition1.config(fg='red')

            req[0]=False
        if(str1[i]>='0' and str1[i]<='9'):
            condition4.config(fg='green')
            
            req[3]=True
        elif(str1[i]>='a' and str1[i]<='z'):
            condition3.config(fg='green')
            
            req[2]=True
        elif(str1[i]>='A' and str1[i]<='Z'):
            condition2.config(fg='green')
            
            req[1]=True
        elif str1[i] in specialCharacter:
            condition5.config(fg='green')
            
            req[4]=True
        req[5]=True
        for j in range(5):
            if(req[j]==False):
                req[j]=False
                break

    

def passwordActive():
    pw.trace('w', passwordCheck)

def passwordInactive():
    head.config(text='')
    condition1.config(text='')
    condition4.config(text='')
    condition3.config(text='')
    condition2.config(text='')
    condition5.config(text='')
    


password_entry.bind('<Enter>', lambda event: passwordActive())
password_entry.bind('<Leave>', lambda event: passwordInactive())



def password_command2():
    if password_entry.cget('show') == '•':
        password_entry.config(show='')
    else:
        password_entry.config(show='•')


checkButton = Checkbutton(design_frame8, bg='black', command=password_command2, text='show password', fg="#49c5b6", selectcolor="#1f2833", activebackground="#1f2833", activeforeground="#45a29e")
checkButton.place(x=290, y=330)



# ====== Confirm Password =============
cpw=StringVar()
confirmPassword_entry = Entry(design_frame8, text=(cpw), fg="#49c5b6", bg="#1f2833", font=("yu gothic ui semibold", 12), show='•', highlightthickness=2)
confirmPassword_entry.place(x=284, y=385, width=286, height=34)
confirmPassword_entry.config(highlightbackground="#1f2833", highlightcolor="#49c5b6")
confirmPassword_label = Label(design_frame8, text='• Confirm Password', fg="#49c5b6", bg='black',
                              font=("yu gothic ui", 11, 'bold'))
confirmPassword_label.place(x=280, y=355)


def confirmPasswordCheck(*args):
    condition1.config(text='Confirm Password must be \nsame as Password')
    condition1.config(fg='red')
    str3=cpw.get()
    global pEqual
    if(str3==password1):
        condition1.config(fg='green')
        pEqual=True
    else:
        condition1.config(fg='red')
        pEqual=False

def confirmPasswordActive():
    global password1
    password1=pw.get()
    cpw.trace('w', confirmPasswordCheck)

def confirmPasswordInactive():
    head.config(text='')
    condition1.config(text='')
    condition4.config(text='')
    condition3.config(text='')
    condition2.config(text='')
    condition5.config(text='')
    


confirmPassword_entry.bind('<Enter>', lambda event: confirmPasswordActive())
confirmPassword_entry.bind('<Leave>', lambda event: confirmPasswordInactive())


def password_command3():
    if confirmPassword_entry.cget('show') == '•':
        confirmPassword_entry.config(show='')
    else:
        confirmPassword_entry.config(show='•')


checkButton = Checkbutton(design_frame8, bg='black', command=password_command3, text='show password', fg="#49c5b6", selectcolor="#1f2833", activebackground="#1f2833", activeforeground="#45a29e")
checkButton.place(x=290, y=420)

def signUp():
    file1=open('temp.txt','w')
    head.config(text="")
    condition1.config(text="")
    condition2.config(text="")
    condition3.config(text="")
    global passWord, userName, uType, first
    if not userIdValid:
        head.config(text="Error")
        condition1.config(text="• Invalid Email Id.", fg="red")
    if not req[5]:
        head.config(text="Error")
        condition2.config(text="• Password not satisfying\n all conditions.", fg="red")
    if not pEqual:
        head.config(text="Error")
        condition3.config(text="• Confirm password not \nsame as Password.", fg="red")
    if userIdValid and req[5] and pEqual:
        passWord=pw.get()
        userName=em.get()
        first=True
        typeUser=variable.get()
        if typeUser=="Teacher":
            uType=0
        elif typeUser=="UG Student":
            uType=1
        elif typeUser=="PG Student":
            uType=2
        file1.write("S\n{}\n{}\n{}".format(uType,userName,passWord))
        file1.close()
        file2=open('temp.txt', 'r')
        print(file2.read())
        file2.close()
        window.withdraw()
        os.system("python3 Dashboard.py")
        window.destroy()

# ========= Buttons ====================
SignUp_button = Button(RegistrationPage, text='Sign up', font=("yu gothic ui bold", 12), bg='black', fg="#49c5b6",
                       command=lambda: show_frame(LoginPage), borderwidth=0, activebackground='#1f2833', cursor='hand2')
SignUp_button.place(x=1100, y=175)

SignUp_line = Canvas(RegistrationPage, width=60, height=5, bg='#49c5b6', highlightthickness=0)
SignUp_line.place(x=1100, y=203)

# ===== Welcome Label ==================
welcome_label = Label(design_frame8, text='Welcome', font=('Arial', 20, 'bold'), bg='black', fg="#49c5b6")
welcome_label.place(x=130, y=15)

# ========= Login Button =========
login_button = Button(RegistrationPage, text='Login', font=("yu gothic ui bold", 12), bg='black', fg="#49c5b6",
                      borderwidth=0, activebackground='#1f2833', activeforeground="#45a29e", command=lambda: show_frame(LoginPage), cursor='hand2')
login_button.place(x=845, y=175)

# SIGN UP down button
signUp2 = Button(design_frame8, fg='white', text='Sign Up', bg='#49c5b6', font=("yu gothic ui bold", 15), command= signUp,
                 cursor='hand2', activebackground='#1f2833', activeforeground="#45a29e")
signUp2.place(x=285, y=450, width=286, height=50)

# password icon
password_icon = Image.open('images\\password2.png')
photo = ImageTk.PhotoImage(password_icon)
password_icon_label = Label(design_frame8, image=photo, bg='black')
password_icon_label.image = photo
password_icon_label.place(x=250, y=295)

# confirm password icon
confirmPassword_icon = Image.open('images\\password2.png')
photo = ImageTk.PhotoImage(confirmPassword_icon)
confirmPassword_icon_label = Label(design_frame8, image=photo, bg='black')
confirmPassword_icon_label.image = photo
confirmPassword_icon_label.place(x=250, y=385)

# Email icon 
email_icon = Image.open('images\\email2.png')
photo = ImageTk.PhotoImage(email_icon)
emailIcon_label = Label(design_frame8, image=photo, bg='black')
emailIcon_label.image = photo
emailIcon_label.place(x=250, y=220)

# Full Name icon
name_icon = Image.open('images\\user5.png')
photo = ImageTk.PhotoImage(name_icon)
nameIcon_label = Label(design_frame8, image=photo, bg='black')
nameIcon_label.image = photo
nameIcon_label.place(x=247, y=148)

# picture icon 
picture_icon = Image.open('images\\user3.png')
photo = ImageTk.PhotoImage(picture_icon)
picture_icon_label = Label(design_frame8, image=photo, bg='black')
picture_icon_label.image = photo
picture_icon_label.place(x=280, y=5)

# Left Side Picture 
side_image = Image.open('images\\dash4.png')
photo = ImageTk.PhotoImage(side_image)
side_image_label = Label(design_frame7, image=photo, bg='#1f2833')
side_image_label.image = photo
side_image_label.place(x=50, y=10)

window.mainloop()