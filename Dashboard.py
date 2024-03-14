from tkinter import *
from PIL import ImageTk, Image  # type "Pip install pillow" in your terminal to install ImageTk and Image module
import pandas as pd
import os

class Person:
    def __init__(self, firstName, lastName, userId, password, department, mobileNo, birthDate):
        self.firstName=firstName
        self.lastName=lastName
        self.userId=userId
        self.password=password
        self.department=department
        self.mobileNo=mobileNo
        self.birthDate=birthDate

class Teacher(Person):
    def __init__(self, employeeId, firstName, lastName, userId, password, department, mobileNo, position, birthDate, yearOfJoining):
        Person.__init__(self, firstName, lastName, userId, password, department, mobileNo, birthDate)
        self.employeeId=employeeId
        self.position=position
        self.yearOfJoining=yearOfJoining

class Student(Person):
    def __init__(self, rollNo, firstName, lastName, userId, password, department, mobileNo, CGPA, birthDate):
        Person.__init__(self, firstName, lastName, userId, password, department, mobileNo, birthDate)
        self.rollNo=rollNo
        self.CGPA=CGPA

class UGStudent(Student):
    def __init__(self, rollNo, firstName, lastName, userId, password, department, mobileNo, CGPA, branch, birthDate):
        Student.__init__(self, rollNo, firstName, lastName, userId, password, department, mobileNo, CGPA, birthDate)
        self.branch=branch

class PGStudent(Student):
    def __init__(self, rollNo, firstName, lastName, userId, password, department, mobileNo, CGPA, branch, birthDate):
        Student.__init__(self, rollNo, firstName, lastName, userId, password, department, mobileNo, CGPA, birthDate)
        self.branch=branch

dataBase=list((pd.read_csv("Teacher.csv", index_col=[0]),pd.read_csv("UGStudent.csv", index_col=[0]),pd.read_csv("PGStudent.csv", index_col=[0])))

file2=open('temp.txt','r')

meth=file2.readline().strip()

uType=0
ind=0
uName=""
passWord=""
fname=""
lname=""
rollNo=""
mobileNo=""
userType=""
bd=""
bd_dd=1
bd_mm=1
bd_yyyy=2000
dep=""
branch=""
join_yyyy=1975
cgpa="0.00"



window=Tk()
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)
window.state('zoomed')
window.resizable(0, 0)
window.title('Dashboard')

icon = PhotoImage(file='images\\pic-icon.png')
window.iconphoto(True, icon)

DashboardPage=Frame(window, bg='black')
DeregisterationPage=Frame(window, bg='black')
ProfilePage=Frame(window)
ContactUs=Frame(window)

for frame in (DashboardPage, DeregisterationPage, ProfilePage, ContactUs):
    frame.grid(row=0, column=0, sticky='nsew')

def show_frame(frame):
    frame.tkraise()

def logOut():
    print(uType)
    print(uName)
    print(passWord)
    dataBase[0].to_csv("Teacher.csv", index=True, header=True)
    dataBase[1].to_csv("UGStudent.csv", index=True, header=True)
    dataBase[2].to_csv("PGStudent.csv", index=True, header=True)
    window.withdraw()
    os.system("python3 LoginAndRegistrationPage.py")
    window.destroy()

if meth=='L':
    uType=int(file2.readline().strip())
    ind=int(file2.readline().strip())
    file2.close()
    if uType==0:
        userType="Teacher"
        uName=dataBase[0]['UserId'][ind]
        passWord=dataBase[0]['Password'][ind]
        fname=dataBase[0]['FirstName'][ind]
        lname=dataBase[0]['LastName'][ind]
        rollNo=dataBase[0]['EmployeeId'][ind]
        mobileNo=dataBase[0]['MobileNo'][ind]
        dep=dataBase[0]['Department'][ind]
        bd=dataBase[0]['BirthDate'][ind].split('/')
        bd_dd=int(bd[0])
        bd_mm=int(bd[1])
        bd_yyyy=int(bd[2])
        branch=dataBase[0]['Position'][ind]
        join_yyyy=dataBase[0]['JoiningYear'][ind]
        teacher=Teacher(rollNo, fname, lname, uName, passWord, dep, mobileNo, branch, bd, join_yyyy)
    elif uType==1:
        userType="UG Student"
        uName=dataBase[1]['UserId'][ind]
        passWord=dataBase[1]['Password'][ind]
        fname=dataBase[1]['FirstName'][ind]
        lname=dataBase[1]['LastName'][ind]
        rollNo=dataBase[1]['RollNo'][ind]
        mobileNo=dataBase[1]['MobileNo'][ind]
        dep=dataBase[1]['Department'][ind]
        bd=dataBase[1]['BirthDate'][ind].split('/')
        bd_dd=int(bd[0])
        bd_mm=int(bd[1])
        bd_yyyy=int(bd[2])
        branch=dataBase[1]['Branch'][ind]
        cgpa=dataBase[1]['CGPA'][ind]
        ugstudent=UGStudent(rollNo, fname, lname, uName, passWord, dep, mobileNo, cgpa, branch, bd)
    else:
        userType="PG Student"
        uName=dataBase[2]['UserId'][ind]
        passWord=dataBase[2]['Password'][ind]
        fname=dataBase[2]['FirstName'][ind]
        lname=dataBase[2]['LastName'][ind]
        rollNo=dataBase[2]['RollNo'][ind]
        mobileNo=dataBase[2]['MobileNo'][ind]
        dep=dataBase[2]['Department'][ind]
        bd=dataBase[2]['BirthDate'][ind].split('/')
        bd_dd=int(bd[0])
        bd_mm=int(bd[1])
        bd_yyyy=int(bd[2])
        branch=dataBase[2]['Branch'][ind]
        cgpa=dataBase[2]['CGPA'][ind]
        pgstudent=PGStudent(rollNo, fname, lname, uName, passWord, dep, mobileNo, cgpa, branch, bd)
    show_frame(DashboardPage)
else:
    tmp1=file2.readline().strip()
    uType=int(tmp1)
    print(uType)
    uName=file2.readline().strip()
    print(uName,'*')
    passWord=file2.readline().strip()
    print(passWord,'**')
    if uType==0:
        userType="Teacher"
    elif uType==1:
        userType="UG Student"
    else:
        userType="PG Student"
    print(uType)
    print(uName)
    print(passWord)
    file2.close()
    show_frame(ProfilePage)

# Dashboard

design_frame1 = Listbox(DashboardPage, bg='black', width=window.winfo_screenwidth()-150, height=window.winfo_screenheight()-10, highlightthickness=0, borderwidth=0)
design_frame1.place(x=150, y=160)

# menu

minWidth=150
maxWidth=350
currentWidth=150
expanded=False

def menuExpand():
    global currentWidth
    global expanded
    currentWidth+=10
    rep=window.after(5,menuExpand)
    menu.config(width=currentWidth)
    if currentWidth>=maxWidth:
        expanded=True
        window.after_cancel(rep)
        getContents()

def menuCollapse():
    global currentWidth
    global expanded
    currentWidth-=20
    rep=window.after(5,menuCollapse)
    menu.config(width=currentWidth)
    if currentWidth<=minWidth:
        expanded=False
        window.after_cancel(rep)
        getContents()

def getContents():
    if expanded:
        home_button_label.config(text='Home')
        logout_button_label.config(text='Logout')
        deregister_button_label.config(text='Deregister')
        contact_button_label.config(text='Contact Us')
        love_label.config(image=love, text="Made with ", compound=RIGHT)
        by_label.config(text="By Ishaan Jain.")
    else:
        home_button_label.config(text='')
        logout_button_label.config(text='')
        deregister_button_label.config(text='')
        contact_button_label.config(text='')
        love_label.config(image='', text="")
        by_label.config(text="")
        

home=ImageTk.PhotoImage(Image.open('images\\homenew1.png'))
logout=ImageTk.PhotoImage(Image.open('images\\logoutnew1.png'))
deregister=ImageTk.PhotoImage(Image.open('images\\deregnew1.png'))
contact=ImageTk.PhotoImage(Image.open('images\\contactnew1.png'))
love=ImageTk.PhotoImage(Image.open('images\\love2.png'))

window.update()

menu=Frame(DashboardPage, bg='#49c5b6', width=minWidth, height=window.winfo_screenheight()-20)
menu.place(x=0, y=160)

home_button=Button(menu, image=home, bg='#49c5b6', command=lambda: show_frame(DashboardPage), relief='flat', cursor='hand2', activebackground='#1b87d2')
logout_button=Button(menu, image=logout, bg='#49c5b6', command=logOut, relief='flat', cursor='hand2', activebackground='#1b87d2')
deregister_button=Button(menu, image=deregister, bg='#49c5b6', command=lambda: show_frame(DeregisterationPage), relief='flat', cursor='hand2', activebackground='#1b87d2')
contact_button=Button(menu, image=contact, bg='#49c5b6', command=lambda: show_frame(ContactUs), relief='flat', cursor='hand2', activebackground='#1b87d2')

home_button_label=Label(menu, bg='#49c5b6', fg="white", font=('yu gothic ui', 21, 'bold'))
logout_button_label=Label(menu, bg='#49c5b6', font=('yu gothic ui', 21, 'bold'), fg="white")
deregister_button_label=Label(menu, bg='#49c5b6', font=('yu gothic ui', 21, 'bold'), fg="white")
contact_button_label=Label(menu, bg='#49c5b6', font=('yu gothic ui', 21, 'bold'), fg="white")
love_label=Label(menu, bg='#49c5b6', font=('yu gothic ui', 10, 'bold'))
by_label=Label(menu, bg='#49c5b6', font=('yu gothic ui', 10, 'bold'))

home_button.place(x=25, y=50)
logout_button.place(x=25, y=200)
deregister_button.place(x=25, y=350)
contact_button.place(x=25, y=500)
love_label.place(x=25, y=650)
by_label.place(x=25, y=675)


home_button_label.place(x=150, y=75)
logout_button_label.place(x=150, y=225)
deregister_button_label.place(x=150, y=375)
contact_button_label.place(x=150, y=525)



menu.bind('<Enter>', lambda event: menuExpand())
menu.bind('<Leave>', lambda event: menuCollapse())

# Header

design_frame2 = Listbox(DashboardPage, bg='black', width=window.winfo_screenwidth(), height=10, highlightthickness=0, borderwidth=0)
design_frame2.place(x=0, y=0)

logo=ImageTk.PhotoImage(Image.open('images\\dash3.png'))
hello_label=Label(design_frame2, text='IIT KGP', font=('Arial', 80, 'bold'), bg='black', fg='#49c5b6')

logo_image=Label(design_frame2, image=logo, bg='black')
logo_image.place(x=10, y=10)
hello_label.place(x=window.winfo_screenwidth()*0.4, y=10)

user_image=ImageTk.PhotoImage(Image.open('images\\user4.png'))
user_button=Button(design_frame2, image=user_image, bg='black', command=lambda: show_frame(ProfilePage), relief='flat', cursor='hand2', activebackground='#1f2833')
user_button.place(x=window.winfo_screenwidth()-100, y=17)

background=Label(design_frame1, bg='black', width=window.winfo_screenwidth()-150, height=window.winfo_screenheight()-5)
background.place(x=0, y=0)

home_label=Label(design_frame1, text='Welcome!!', bg='black', font=('bauhaus 93', 90, 'bold'), fg='#49c5b6')
home_label.place(x=design_frame1.winfo_screenwidth()*0.25, y=design_frame1.winfo_screenheight()*0.25)
name_label=Label(design_frame1, text=fname+" "+lname, bg='black', font=('yu gothic ui', 40, 'bold'), fg='white')
name_label.place(x=design_frame1.winfo_screenwidth()*0.35, y=design_frame1.winfo_screenheight()*0.4)

# Deregister

design_frame3 = Listbox(DeregisterationPage, bg='black', width=window.winfo_screenwidth()-150, height=window.winfo_screenheight()-10, highlightthickness=0, borderwidth=0)
design_frame3.place(x=150, y=160)


minWidth1=150
maxWidth1=350
currentWidth1=150
expanded1=False

def menuExpand1():
    global currentWidth1
    global expanded1
    currentWidth1+=10
    rep1=window.after(5,menuExpand1)
    menu1.config(width=currentWidth1)
    if currentWidth1>=maxWidth1:
        expanded1=True
        window.after_cancel(rep1)
        getContents1()

def menuCollapse1():
    global currentWidth1
    global expanded1
    currentWidth1-=20
    rep1=window.after(5,menuCollapse1)
    menu1.config(width=currentWidth1)
    if currentWidth1<=minWidth1:
        expanded1=False
        window.after_cancel(rep1)
        getContents1()

def getContents1():
    if expanded1:
        home_button_label1.config(text='Home')
        logout_button_label1.config(text='Logout')
        deregister_button_label1.config(text='Deregister')
        contact_button_label1.config(text='Contact Us')
        love_label1.config(image=love, text="Made with ", compound=RIGHT)
        by_label1.config(text="By Ishaan Jain.")
    else:
        home_button_label1.config(text='')
        logout_button_label1.config(text='')
        deregister_button_label1.config(text='')
        contact_button_label1.config(text='')
        love_label1.config(image='', text="")
        by_label1.config(text="")


window.update()

menu1=Frame(DeregisterationPage, bg='#49c5b6', width=minWidth1, height=window.winfo_screenheight()-20)
menu1.place(x=0, y=160)

home_button1=Button(menu1, image=home, bg='#49c5b6', command=lambda: show_frame(DashboardPage), relief='flat', cursor='hand2', activebackground='#45a29e')
logout_button1=Button(menu1, image=logout, bg='#49c5b6', command=logOut, relief='flat', cursor='hand2', activebackground='#45a29e')
deregister_button1=Button(menu1, image=deregister, bg='#49c5b6', command=lambda: show_frame(DeregisterationPage), relief='flat', cursor='hand2', activebackground='#45a29e')
contact_button1=Button(menu1, image=contact, bg='#49c5b6', command=lambda: show_frame(ContactUs), relief='flat', cursor='hand2', activebackground='#45a29e')

home_button_label1=Label(menu1, bg='#49c5b6', font=('yu gothic ui', 21, 'bold'), fg="white")
logout_button_label1=Label(menu1, bg='#49c5b6', font=('yu gothic ui', 21, 'bold'), fg="white")
deregister_button_label1=Label(menu1, bg='#49c5b6', font=('yu gothic ui', 21, 'bold'), fg="white")
contact_button_label1=Label(menu1, bg='#49c5b6', font=('yu gothic ui', 21, 'bold'), fg="white")
love_label1=Label(menu1, bg='#49c5b6', font=('yu gothic ui', 10, 'bold'))
by_label1=Label(menu1, bg='#49c5b6', font=('yu gothic ui', 10, 'bold'))

home_button1.place(x=25, y=50)
logout_button1.place(x=25, y=200)
deregister_button1.place(x=25, y=350)
contact_button1.place(x=25, y=500)
love_label1.place(x=25, y=650)
by_label1.place(x=25, y=675)

home_button_label1.place(x=150, y=75)
logout_button_label1.place(x=150, y=225)
deregister_button_label1.place(x=150, y=375)
contact_button_label1.place(x=150, y=525)

menu1.bind('<Enter>', lambda event: menuExpand1())
menu1.bind('<Leave>', lambda event: menuCollapse1())

design_frame4 = Listbox(DeregisterationPage, bg='black', width=window.winfo_screenwidth(), height=10, highlightthickness=0, borderwidth=0)
design_frame4.place(x=0, y=0)

hello_label1=Label(design_frame4, text='IIT KGP', font=('Arial', 80, 'bold'), bg='black', fg='#49c5b6')
logo_image1=Label(design_frame4, image=logo, bg='black')
logo_image1.place(x=10, y=10)
hello_label1.place(x=window.winfo_screenwidth()*0.4, y=10)

user_button1=Button(design_frame4, image=user_image, bg='black', command=lambda: show_frame(ProfilePage), relief='flat', cursor='hand2', activebackground='#1f2833')
user_button1.place(x=window.winfo_screenwidth()-100, y=17)

background1=Label(design_frame3, bg='black', width=window.winfo_screenwidth()-150, height=window.winfo_screenheight()-5)
background1.place(x=0, y=0)

def dereg():
    win = Toplevel()
    window_width = 700
    window_height = 350
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    position_top = int(screen_height*0.5 - window_height / 4)
    position_right = int(screen_width*0.55 - window_width / 2)
    win.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')
    win.configure(background='black')
    win.overrideredirect(True)
    win.resizable(0, 0)
    global deregis

    def logIn():
        dataBase[0].to_csv("Teacher.csv", index=True, header=True)
        dataBase[1].to_csv("UGStudent.csv", index=True, header=True)
        dataBase[2].to_csv("PGStudent.csv", index=True, header=True)
        window.withdraw()
        win.withdraw()
        os.system("python3 LoginAndRegistrationPage.py")
        win.destroy()
        window.destroy()

    def yes():
        global deregis
        deregis=True
        dataBase[uType].drop([ind], inplace=True)
        dataBase[0].to_csv("Teacher.csv", index=True, header=True)
        dataBase[1].to_csv("UGStudent.csv", index=True, header=True)
        dataBase[2].to_csv("PGStudent.csv", index=True, header=True)
        sure.config(text='You have been succesfully deregistered', font=("yu gothic ui bold", 27))
        yes_button.config(text='Login Page', command=logIn)
        no_button.config(text='Exit', command=window.destroy)


    def no():
        global deregis
        deregis=False
        dataBase[0].to_csv("Teacher.csv", index=True, header=True)
        dataBase[1].to_csv("UGStudent.csv", index=True, header=True)
        dataBase[2].to_csv("PGStudent.csv", index=True, header=True)
        win.destroy()

    sure=Label(win, text='Are you sure you want to deregister?', fg='white', bg='black', font=("yu gothic ui bold", 30))
    sure.place(x=win.winfo_screenwidth()*0.01, y=win.winfo_screenheight()*0.1)
    yes_button=Button(win, text='YES', bg='#49c5b6', fg='white', activebackground='#45a29e', activeforeground="black", font=('yu gothic ui semibold', 20, 'bold'), command=yes, width=8)
    yes_button.place(x=win.winfo_screenwidth()*0.1, y=win.winfo_screenheight()*0.2)
    no_button=Button(win, text='NO', bg='#49c5b6', fg='white', activebackground='#45a29e', activeforeground="black", font=('yu gothic ui semibold', 20, 'bold'), command=no, width=8)
    no_button.place(x=win.winfo_screenwidth()*0.3, y=win.winfo_screenheight()*0.2)


dereg_title=Label(design_frame3, text='Deregistration Request', bg='black', font=('bauhaus 93', 60, 'bold'), fg='#49c5b6')
dereg_title.place(x=design_frame3.winfo_screenwidth()*0.15, y=design_frame3.winfo_screenheight()*0.075)
dereg_label=Label(design_frame3, bg='Black', text='Are You Sure You Want to Deregister?', font=('yu gothic ui', 30, 'bold'), fg='white')
dereg_label.place(x=design_frame3.winfo_screenwidth()*0.2, y=design_frame3.winfo_screenheight()*0.225)
dereg_button=Button(design_frame3, text='Submit Deregistration Request', bg='#49c5b6', fg='white', font=("yu gothic ui bold", 25), cursor='hand2', activebackground='#45A29E', activeforeground="black", command=dereg)
dereg_button.place(x=design_frame3.winfo_screenwidth()*0.275, y=design_frame3.winfo_screenheight()*0.325)

# Profile Page

design_frame5 = Listbox(ProfilePage, bg='black', width=window.winfo_screenwidth()-150, height=window.winfo_screenheight()-10, highlightthickness=0, borderwidth=0)
design_frame5.place(x=150, y=160)

minWidth2=150
maxWidth2=350
currentWidth2=150
expanded2=False

def menuExpand2():
    global currentWidth2
    global expanded2
    currentWidth2+=10
    rep2=window.after(5,menuExpand2)
    menu2.config(width=currentWidth2)
    if currentWidth2>=maxWidth2:
        expanded2=True
        window.after_cancel(rep2)
        getContents2()

def menuCollapse2():
    global currentWidth2
    global expanded2
    currentWidth2-=20
    rep2=window.after(5,menuCollapse2)
    menu2.config(width=currentWidth2)
    if currentWidth2<=minWidth2:
        expanded2=False
        window.after_cancel(rep2)
        getContents2()

def getContents2():
    if expanded2:
        home_button_label2.config(text='Home')
        logout_button_label2.config(text='Logout')
        deregister_button_label2.config(text='Deregister')
        contact_button_label2.config(text='Contact Us')
        love_label2.config(image=love, text="Made with ", compound=RIGHT)
        by_label2.config(text="By Ishaan Jain.")
    else:
        home_button_label2.config(text='')
        logout_button_label2.config(text='')
        deregister_button_label2.config(text='')
        contact_button_label2.config(text='')
        love_label2.config(image='', text="")
        by_label2.config(text="")


window.update()

menu2=Frame(ProfilePage, bg='#49c5b6', width=minWidth2, height=window.winfo_screenheight()-20)
menu2.place(x=0, y=160)

home_button2=Button(menu2, image=home, bg='#49c5b6', command=lambda: show_frame(DashboardPage), relief='flat', cursor='hand2', activebackground='#45a29e')
logout_button2=Button(menu2, image=logout, bg='#49c5b6', command=logOut, relief='flat', cursor='hand2', activebackground='#45a29e')
deregister_button2=Button(menu2, image=deregister, bg='#49c5b6', command=lambda: show_frame(DeregisterationPage), relief='flat', cursor='hand2', activebackground='#45a29e')
contact_button2=Button(menu2, image=contact, bg='#49c5b6', command=lambda: show_frame(ContactUs), relief='flat', cursor='hand2', activebackground='#45a29e')

home_button_label2=Label(menu2, bg='#49c5b6', font=('yu gothic ui', 21, 'bold'), fg="white")
logout_button_label2=Label(menu2, bg='#49c5b6', font=('yu gothic ui', 21, 'bold'), fg="white")
deregister_button_label2=Label(menu2, bg='#49c5b6', font=('yu gothic ui', 21, 'bold'), fg="white")
contact_button_label2=Label(menu2, bg='#49c5b6', font=('yu gothic ui', 21, 'bold'), fg="white")
love_label2=Label(menu2, bg='#49c5b6', font=('yu gothic ui', 10, 'bold'))
by_label2=Label(menu2, bg='#49c5b6', font=('yu gothic ui', 10, 'bold'))

home_button2.place(x=25, y=50)
logout_button2.place(x=25, y=200)
deregister_button2.place(x=25, y=350)
contact_button2.place(x=25, y=500)

home_button_label2.place(x=150, y=75)
logout_button_label2.place(x=150, y=225)
deregister_button_label2.place(x=150, y=375)
contact_button_label2.place(x=150, y=525)
love_label2.place(x=25, y=650)
by_label2.place(x=25, y=675)

menu2.bind('<Enter>', lambda event: menuExpand2())
menu2.bind('<Leave>', lambda event: menuCollapse2())

design_frame6 = Listbox(ProfilePage, bg='black', width=window.winfo_screenwidth(), height=10, highlightthickness=0, borderwidth=0)
design_frame6.place(x=0, y=0)

hello_label2=Label(design_frame6, text='IIT KGP', font=('Arial', 80, 'bold'), bg='black', fg='#49c5b6')
logo_image2=Label(design_frame6, image=logo, bg='black')
logo_image2.place(x=10, y=10)
hello_label2.place(x=window.winfo_screenwidth()*0.4, y=10)

user_button2=Button(design_frame6, image=user_image, bg='black', command=lambda: show_frame(ProfilePage), relief='flat', cursor='hand2', activebackground='#1f2833')
user_button2.place(x=window.winfo_screenwidth()-100, y=17)

background2=Label(design_frame5, bg='black', width=window.winfo_screenwidth()-150, height=window.winfo_screenheight()-5)
background2.place(x=0, y=0)

# general



profile_title=Label(design_frame5, text='Your Profile', bg='black', font=('bauhaus 93', 60, 'bold'), fg='#49c5b6')
profile_title.place(x=design_frame5.winfo_screenwidth()*0.285, y=design_frame5.winfo_screenheight()*0.075)

first_name_label=Label(design_frame5, text='• First Name', fg="#49c5b6", bg='black', font=("yu gothic ui", 11, 'bold'))
first_name_entry=Entry(design_frame5, fg="#49c5b6", bg='#1f2833', font=("yu gothic ui semibold", 12), highlightthickness=2, disabledbackground="black", disabledforeground="#45a29e", highlightbackground="#1f2833", highlightcolor="#49c5b6")
first_name_entry.insert(0, fname)
first_name_entry.config(state="disabled")
first_name_label.place(x=design_frame5.winfo_screenwidth()*0.25, y=design_frame5.winfo_screenheight()*0.2)
first_name_entry.place(x=design_frame5.winfo_screenwidth()*0.25, y=design_frame5.winfo_screenheight()*0.225)

last_name_label=Label(design_frame5, text='• Last Name', fg="#49c5b6", bg='black', font=("yu gothic ui", 11, 'bold'))
last_name_entry=Entry(design_frame5, fg="#49c5b6", bg='#1f2833', font=("yu gothic ui semibold", 12), highlightthickness=2, disabledbackground="black", disabledforeground="#45a29e", highlightbackground="#1f2833", highlightcolor="#49c5b6")
last_name_entry.insert(0, lname)
last_name_entry.config(state='disabled')
last_name_label.place(x=design_frame5.winfo_screenwidth()*0.50, y=design_frame5.winfo_screenheight()*0.2)
last_name_entry.place(x=design_frame5.winfo_screenwidth()*0.50, y=design_frame5.winfo_screenheight()*0.225)

# Employee Id for teacher, roll no for student
no_label=Label(design_frame5, text='• Roll No.', fg="#49c5b6", bg='black', font=("yu gothic ui", 11, 'bold'))
no_entry=Entry(design_frame5, fg="#49c5b6", bg='#1f2833', font=("yu gothic ui semibold", 12), highlightthickness=2, disabledbackground="black", disabledforeground="#45a29e", highlightbackground="#1f2833", highlightcolor="#49c5b6")
no_entry.insert(0, rollNo)
no_entry.config(state="disabled")
no_label.place(x=design_frame5.winfo_screenwidth()*0.25, y=design_frame5.winfo_screenheight()*0.3)
no_entry.place(x=design_frame5.winfo_screenwidth()*0.25, y=design_frame5.winfo_screenheight()*0.325)

mobile_label=Label(design_frame5, text='• Mobile No.', fg="#49c5b6", bg='black', font=("yu gothic ui", 11, 'bold'))
mobile_entry=Entry(design_frame5, fg="#49c5b6", bg='#1f2833', font=("yu gothic ui semibold", 12), highlightthickness=2, disabledbackground="black", disabledforeground="#45a29e", highlightbackground="#1f2833", highlightcolor="#49c5b6")
mobile_entry.insert(0, mobileNo)
mobile_entry.config(state="disabled")
mobile_label.place(x=design_frame5.winfo_screenwidth()*0.50, y=design_frame5.winfo_screenheight()*0.3)
mobile_entry.place(x=design_frame5.winfo_screenwidth()*0.50, y=design_frame5.winfo_screenheight()*0.325)


bd_d=IntVar(value=bd_dd)
bd_m=IntVar(value=bd_mm)
bd_y=IntVar(value=bd_yyyy)
birthdate_label=Label(design_frame5, text='• Birthdate (DD MM YYYY)', fg="#49c5b6", bg='black', font=("yu gothic ui", 11, 'bold'))
birthdate_dd=Spinbox(design_frame5, from_=1, to=31, fg='#49c5b6', bg='#1f2833', font=("yu gothic ui semibold", 12), highlightthickness=2, width=3, textvariable=bd_d, disabledbackground="black", disabledforeground="#45a29e", highlightbackground="#1f2833", highlightcolor="#49c5b6")
birthdate_mm=Spinbox(design_frame5, from_=1, to=12, fg='#49c5b6', bg='#1f2833', font=("yu gothic ui semibold", 12), highlightthickness=2, width=3, textvariable=bd_m, disabledbackground="black", disabledforeground="#45a29e", highlightbackground="#1f2833", highlightcolor="#49c5b6")
birthdate_yyyy=Spinbox(design_frame5, from_=1900, to=2024, fg='#49c5b6', bg='#1f2833', font=("yu gothic ui semibold", 12), highlightthickness=2, width=5, textvariable=bd_y, disabledbackground="black", disabledforeground="#45a29e", highlightbackground="#1f2833", highlightcolor="#49c5b6")
birthdate_dd.config(state="disabled")
birthdate_mm.config(state="disabled")
birthdate_yyyy.config(state="disabled")
birthdate_label.place(x=design_frame5.winfo_screenwidth()*0.25, y=design_frame5.winfo_screenheight()*0.4)
birthdate_dd.place(x=design_frame5.winfo_screenwidth()*0.25, y=design_frame5.winfo_screenheight()*0.425)
birthdate_mm.place(x=design_frame5.winfo_screenwidth()*0.29, y=design_frame5.winfo_screenheight()*0.425)
birthdate_yyyy.place(x=design_frame5.winfo_screenwidth()*0.33, y=design_frame5.winfo_screenheight()*0.425)

depOptions=["Aerospace Engineering", "Agricultural and Food Engineering", "Architecture and Regional Planning", "Bioscience and Biotechnology", "Chemical Engineering", "Chemistry", "Civil Engineering", "Computer Science and Engineering", "Electrical Engineering", "Electronics and Electrical Communication Engg.", "Geology and Geophysics", "Humanities and Social Sciences", "Industrial and Systems Engineering", "Mathematics", "Mechanical Engineering", "Metallurgical and Materials Engineering", "Mining Engineering", "Ocean Engg and Naval Architecture", "Physics"]

branchOptions=["B.Tech (4yrs)", "B.Tech + M.Tech (5yrs)"]

if userType=="PG Student":
    branchOptions=["M.Tech (2yrs)", "Research Scholar", "PhD"]
elif userType=="Teacher":
    branchOptions=["Professor", "Assistant Professor", "Associate Professor"]


depSelection = StringVar(value=dep)
department_label=Label(design_frame5, text='• Department', fg="#49c5b6", bg='black', font=("yu gothic ui", 11, 'bold'))
department_menu=OptionMenu(design_frame5, depSelection, *depOptions)
department_menu.config(fg="#49c5b6", bg='#1f2833', font=("yu gothic ui semibold", 12), highlightthickness=2, disabledforeground="#45a29e", highlightbackground="#1f2833", highlightcolor="#49c5b6", activebackground="#1f2833", activeforeground="#45a29e")
dep_menu=design_frame5.nametowidget(department_menu.menuname)
dep_menu.config(bg='#1f2833', fg='#49c5b6', font=("yu gothic ui semibold", 12), activebackground="black", activeforeground="#45a29e")
department_menu.config(state="disabled")
department_label.place(x=design_frame5.winfo_screenwidth()*0.50, y=design_frame5.winfo_screenheight()*0.4)
department_menu.place(x=design_frame5.winfo_screenwidth()*0.50, y=design_frame5.winfo_screenheight()*0.425)

branchSelection = StringVar(value=branch)
branch_label=Label(design_frame5, text='• Branch', fg="#49c5b6", bg='black', font=("yu gothic ui", 11, 'bold'))
branch_menu=OptionMenu(design_frame5, branchSelection, *branchOptions)
branch_menu.config(fg="#49c5b6", bg='#1f2833', font=("yu gothic ui semibold", 12), highlightthickness=2, disabledforeground="#45a29e", highlightbackground="#1f2833", highlightcolor="#49c5b6", activebackground="#1f2833", activeforeground="#45a29e")
bra_menu=design_frame5.nametowidget(branch_menu.menuname)
bra_menu.config(bg='#1f2833', fg='#49c5b6', font=("yu gothic ui semibold", 12), activebackground="black", activeforeground="#45a29e")
branch_menu.config(state="disabled")
branch_label.place(x=design_frame5.winfo_screenwidth()*0.25, y=design_frame5.winfo_screenheight()*0.5)
branch_menu.place(x=design_frame5.winfo_screenwidth()*0.25, y=design_frame5.winfo_screenheight()*0.525)

if userType=="Teacher":
    join_y=IntVar(value=join_yyyy)
    branch_label.config(text="• Position")
    join_year_label=Label(design_frame5, text="• Year of Joining", fg="#49c5b6", bg='black', font=("yu gothic ui", 11, 'bold'))
    join_year=Spinbox(design_frame5, from_=1950, to=2024, fg='#49c5b6', bg='#1f2833', font=("yu gothic ui semibold", 12), highlightthickness=2, width=5, textvariable=join_y, disabledbackground="black", disabledforeground="#45a29e", highlightbackground="#1f2833", highlightcolor="#49c5b6")
    join_year.config(state="disabled")
    join_year_label.place(x=design_frame5.winfo_screenwidth()*0.50, y=design_frame5.winfo_screenheight()*0.5)
    join_year.place(x=design_frame5.winfo_screenwidth()*0.50, y=design_frame5.winfo_screenheight()*0.525)
else:
    cgpa_label=Label(design_frame5, text="• CGPA", fg="#49c5b6", bg='black', font=("yu gothic ui", 11, 'bold'))
    cgpa_entry=Entry(design_frame5, fg="#49c5b6", bg='#1f2833', font=("yu gothic ui semibold", 12), highlightthickness=2, disabledbackground="black", disabledforeground="#45a29e", highlightbackground="#1f2833", highlightcolor="#49c5b6")
    cgpa_entry.insert(0, cgpa)
    cgpa_entry.config(state="disabled")
    cgpa_label.place(x=design_frame5.winfo_screenwidth()*0.50, y=design_frame5.winfo_screenheight()*0.5)
    cgpa_entry.place(x=design_frame5.winfo_screenwidth()*0.50, y=design_frame5.winfo_screenheight()*0.525)

editAccess=False

def edit():
    global editAccess, uName, passWord, meth, ind, fname, lname, rollNo, mobileNo, dep, bd_dd, bd_mm, bd_yyyy, branch, join_yyyy, cgpa
    if editAccess:
        #update values
        if meth=='S':
            fname=first_name_entry.get()
            lname=last_name_entry.get()
            rollNo=no_entry.get()
            mobileNo=mobile_entry.get()
            dep=depSelection.get()
            bd_dd=bd_d.get() 
            bd_mm=bd_m.get()
            bd_yyyy=bd_y.get()
            branch=branchSelection.get()
            if uType==0:
                join_yyyy=join_y.get()
            else:
                cgpa=cgpa_entry.get()
            if uType==0:
                global teacher
                teacher=Teacher(rollNo, fname, lname, uName, passWord, dep, mobileNo, branch, bd, join_yyyy)
                dataBase[0]=pd.concat([dataBase[0], pd.Series({'UserId': uName, 'Password': passWord, 'FirstName': fname, 'LastName': lname, 'EmployeeId': rollNo, 'MobileNo': mobileNo, 'Department': dep, 'BirthDate': f"{bd_dd}/{bd_mm}/{bd_yyyy}", 'Position': branch, 'JoiningYear': join_yyyy, 'Attempts': 3}).to_frame().T], ignore_index=True)
            else:
                if uType==1:
                    global ugstudent
                    ugstudent=UGStudent(rollNo, fname, lname, uName, passWord, dep, mobileNo, cgpa, branch, bd)
                else:
                    global pgstudent
                    pgstudent=PGStudent(rollNo, fname, lname, uName, passWord, dep, mobileNo, cgpa, branch, bd)
                dataBase[uType]=pd.concat([dataBase[uType], pd.Series({'UserId': uName, 'Password': passWord, 'FirstName': fname, 'LastName': lname, 'RollNo': rollNo, 'MobileNo': mobileNo, 'Department': dep, 'BirthDate': f"{bd_dd}/{bd_mm}/{bd_yyyy}", 'Branch': branch, 'CGPA': cgpa, 'Attempts': 3}).to_frame().T], ignore_index=True)
            idx=(dataBase[uType]['UserId']==uName)
            ind=idx.index[0]
            meth='L'
            dataBase[0].to_csv("Teacher.csv", index=True, header=True)
            dataBase[1].to_csv("UGStudent.csv", index=True, header=True)
            dataBase[2].to_csv("PGStudent.csv", index=True, header=True)
        else:
            fname=first_name_entry.get()
            lname=last_name_entry.get()
            rollNo=no_entry.get()
            mobileNo=mobile_entry.get()
            dep=depSelection.get()
            bd_dd=bd_d.get()
            bd_mm=bd_m.get()
            bd_yyyy=bd_y.get()
            branch=branchSelection.get()
            if uType==0:
                join_yyyy=join_y.get()
            else:
                cgpa=cgpa_entry.get()
            if uType==0:
                dataBase[uType].at[ind, 'FirstName']=fname
                dataBase[uType].at[ind, 'LastName']=lname
                dataBase[uType].at[ind, 'MobileNo']=mobileNo
                dataBase[uType].at[ind, 'Department']=dep
                dataBase[uType].at[ind, 'BirthDate']=f"{bd_dd}/{bd_mm}/{bd_yyyy}"
                dataBase[uType].at[ind, 'Position']=branch
                dataBase[uType].at[ind, 'EmployeeId']=rollNo
                dataBase[uType].at[ind, 'JoiningYear']=join_yyyy
            else:
                dataBase[uType].at[ind, 'FirstName']=fname
                dataBase[uType].at[ind, 'LastName']=lname
                dataBase[uType].at[ind, 'MobileNo']=mobileNo
                dataBase[uType].at[ind, 'Department']=dep
                dataBase[uType].at[ind, 'BirthDate']=f"{bd_dd}/{bd_mm}/{bd_yyyy}"
                dataBase[uType].at[ind, 'Branch']=branch
                dataBase[uType].at[ind, 'RollNo']=rollNo
                dataBase[uType].at[ind, 'CGPA']=cgpa
        dataBase[0].to_csv("Teacher.csv", index=True, header=True)
        dataBase[1].to_csv("UGStudent.csv", index=True, header=True)
        dataBase[2].to_csv("PGStudent.csv", index=True, header=True)
        edit_button.config(text="Edit", width=125)
        first_name_entry.config(state="disabled")
        last_name_entry.config(state='disabled')
        no_entry.config(state="disabled")
        mobile_entry.config(state="disabled")
        birthdate_dd.config(state="disabled")
        birthdate_mm.config(state="disabled")
        birthdate_yyyy.config(state="disabled")
        department_menu.config(state="disabled")
        branch_menu.config(state="disabled")
        if userType=="Teacher":
            join_year.config(state="disabled")
        else:
            cgpa_entry.config(state="disabled")
        editAccess=False
    else:
        edit_button.config(text="Update", width=150)
        first_name_entry.config(state="normal")
        last_name_entry.config(state="normal")
        no_entry.config(state="normal")
        mobile_entry.config(state="normal")
        birthdate_dd.config(state="normal")
        birthdate_mm.config(state="normal")
        birthdate_yyyy.config(state="normal")
        department_menu.config(state="normal")
        branch_menu.config(state="normal")
        if userType=="Teacher":
            join_year.config(state="normal")
        else:
            cgpa_entry.config(state="normal")
        editAccess=True


edit_image=ImageTk.PhotoImage(Image.open('images\\edit3.png'))

edit_button=Button(design_frame5, image=edit_image, text="Edit", command=edit, bg='#49c5b6', relief='flat', cursor='hand2', activebackground='#45a29e', activeforeground="black", compound=LEFT, fg='white', font=("yu gothic ui", 30, "bold"), height=40, width=125)
edit_button.place(x=design_frame5.winfo_screenwidth()*0.39, y=design_frame5.winfo_screenheight()*0.65)


# Contact page


design_frame7 = Listbox(ContactUs, bg='black', width=window.winfo_screenwidth()-150, height=window.winfo_screenheight()-10, highlightthickness=0, borderwidth=0)
design_frame7.place(x=150, y=160)

minWidth3=150
maxWidth3=350
currentWidth3=150
expanded3=False

def menuExpand3():
    global currentWidth3
    global expanded3
    currentWidth3+=10
    rep3=window.after(5,menuExpand3)
    menu3.config(width=currentWidth3)
    if currentWidth3>=maxWidth3:
        expanded3=True
        window.after_cancel(rep3)
        getContents3()

def menuCollapse3():
    global currentWidth3
    global expanded3
    currentWidth3-=20
    rep3=window.after(5,menuCollapse3)
    menu3.config(width=currentWidth3)
    if currentWidth3<=minWidth3:
        expanded3=False
        window.after_cancel(rep3)
        getContents3()

def getContents3():
    if expanded3:
        home_button_label3.config(text='Home')
        logout_button_label3.config(text='Logout')
        deregister_button_label3.config(text='Deregister')
        contact_button_label3.config(text='Contact Us')
        love_label3.config(image=love, text="Made with ", compound=RIGHT)
        by_label3.config(text="By Ishaan Jain.")
    else:
        home_button_label3.config(text='')
        logout_button_label3.config(text='')
        deregister_button_label3.config(text='')
        contact_button_label3.config(text='')
        love_label3.config(image='', text="")
        by_label3.config(text="")


window.update()

menu3=Frame(ContactUs, bg='#49c5b6', width=minWidth3, height=window.winfo_screenheight()-20)
menu3.place(x=0, y=160)

home_button3=Button(menu3, image=home, bg='#49c5b6', command=lambda: show_frame(DashboardPage), relief='flat', cursor='hand2', activebackground='#45a29e')
logout_button3=Button(menu3, image=logout, bg='#49c5b6', command=logOut, relief='flat', cursor='hand2', activebackground='#45a29e')
deregister_button3=Button(menu3, image=deregister, bg='#49c5b6', command=lambda: show_frame(DeregisterationPage), relief='flat', cursor='hand2', activebackground='#45a29e')
contact_button3=Button(menu3, image=contact, bg='#49c5b6', command=lambda: show_frame(ContactUs), relief='flat', cursor='hand2', activebackground='#45a29e')

home_button_label3=Label(menu3, bg='#49c5b6', font=('yu gothic ui', 21, 'bold'), fg="white")
logout_button_label3=Label(menu3, bg='#49c5b6', font=('yu gothic ui', 21, 'bold'), fg="white")
deregister_button_label3=Label(menu3, bg='#49c5b6', font=('yu gothic ui', 21, 'bold'), fg="white")
contact_button_label3=Label(menu3, bg='#49c5b6', font=('yu gothic ui', 21, 'bold'), fg="white")
love_label3=Label(menu3, bg='#49c5b6', font=('yu gothic ui', 10, 'bold'))
by_label3=Label(menu3, bg='#49c5b6', font=('yu gothic ui', 10, 'bold'))

home_button3.place(x=25, y=50)
logout_button3.place(x=25, y=200)
deregister_button3.place(x=25, y=350)
contact_button3.place(x=25, y=500)
love_label3.place(x=25, y=650)
by_label3.place(x=25, y=675)

home_button_label3.place(x=150, y=75)
logout_button_label3.place(x=150, y=225)
deregister_button_label3.place(x=150, y=375)
contact_button_label3.place(x=150, y=525)

menu3.bind('<Enter>', lambda event: menuExpand3())
menu3.bind('<Leave>', lambda event: menuCollapse3())

design_frame8 = Listbox(ContactUs, bg='black', width=window.winfo_screenwidth(), height=10, highlightthickness=0, borderwidth=0)
design_frame8.place(x=0, y=0)

hello_label3=Label(design_frame8, text='IIT KGP', font=('Arial', 80, 'bold'), bg='black', fg='#49c5b6')
logo_image3=Label(design_frame8, image=logo, bg='black')
logo_image3.place(x=10, y=10)
hello_label3.place(x=window.winfo_screenwidth()*0.4, y=10)

user_button3=Button(design_frame8, image=user_image, bg='black', command=lambda: show_frame(ProfilePage), relief='flat', cursor='hand2', activebackground='#1f2833')
user_button3.place(x=window.winfo_screenwidth()-100, y=17)

background3=Label(design_frame7, bg='black', width=window.winfo_screenwidth()-150, height=window.winfo_screenheight()-5)
background3.place(x=0, y=0)

contact_title=Label(design_frame7, text='Contact Us', bg='black', font=('bauhaus 93', 60, 'bold'), fg='#49c5b6')
contact_title.place(x=design_frame7.winfo_screenwidth()*0.285, y=design_frame7.winfo_screenheight()*0.075)

text_label=Label(design_frame7, text="If you having any complain/feedback, reach out to us at:", bg='black', fg='white', font=('yu gothic ui', 20, 'bold'))
text_label.place(x=design_frame7.winfo_screenwidth()*0.2, y=design_frame7.winfo_screenheight()*0.25)

call_image=ImageTk.PhotoImage(Image.open('images\\call2.png'))
email__image=ImageTk.PhotoImage(Image.open('images\\email2.png'))
insta__image=ImageTk.PhotoImage(Image.open('images\\insta2.png'))
fb_image=ImageTk.PhotoImage(Image.open('images\\fb2.png'))
x_image=ImageTk.PhotoImage(Image.open('images\\x2.png'))

call_label=Label(design_frame7, image=call_image, text="+91 85913 95627", font=("yu gothic ui", 30, "bold"), fg="#49c5b6", bg="black", compound=LEFT)
email_label=Label(design_frame7, image=email__image, text="jainishaan107@gmail.com", font=("yu gothic ui", 30, "bold"), fg="#49c5b6", bg="black", compound=LEFT)
insta_label=Label(design_frame7, image=insta__image, text="ft_ish107", font=("yu gothic ui", 30, "bold"), fg="#49c5b6", bg="black", compound=LEFT)
fb_label=Label(design_frame7, image=fb_image, text="Ishaan Jain", font=("yu gothic ui", 30, "bold"), fg="#49c5b6", bg="black", compound=LEFT)
x_label=Label(design_frame7, image=x_image, text="Ishaan Jain", font=("yu gothic ui", 30, "bold"), fg="#49c5b6", bg="black", compound=LEFT)

call_label.place(x=design_frame7.winfo_screenwidth()*0.3, y=design_frame7.winfo_screenheight()*0.3)
email_label.place(x=design_frame7.winfo_screenwidth()*0.3, y=design_frame7.winfo_screenheight()*0.375)
insta_label.place(x=design_frame7.winfo_screenwidth()*0.3, y=design_frame7.winfo_screenheight()*0.45)
fb_label.place(x=design_frame7.winfo_screenwidth()*0.3, y=design_frame7.winfo_screenheight()*0.525)
x_label.place(x=design_frame7.winfo_screenwidth()*0.3, y=design_frame7.winfo_screenheight()*0.6)

window.mainloop()
