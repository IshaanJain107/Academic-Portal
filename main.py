from tkinter import *
from tkinter import ttk
from tkinter.ttk import Progressbar
import os

root = Tk()
image = PhotoImage(file='images//dash5.png')

height = 430
width = 530
x = (root.winfo_screenwidth()//2)-(width//2)
y = (root.winfo_screenheight()//2)-(height//2)
root.geometry('{}x{}+{}+{}'.format(width, height, x, y))
root.overrideredirect(True)

root.config(background="black")

welcome_label=Label(root, text='IIT KGP', bg='black', font=("Arial", 30, "bold"), fg='#49c5b6')
welcome_label.place(x=185, y=20)

bg_label=Label(root, image=image, bg='black')
bg_label.place(x=130, y=65)

progress_label = Label(root, text="Loading...", font=("Trebuchet Ms", 15, "bold"), fg='#49c5b6', bg='black')
progress_label.place(x=190, y=330)
progress=ttk.Style()
progress.theme_use("clam")
progress.configure("red.Horizontal.TProgressbar", background="#49c5b6")

progress=Progressbar(root, orient=HORIZONTAL, length=400, mode='determinate', style="red.Horizontal.TProgressbar")
progress.place(x=60, y=370)

def top():
    root.withdraw()
    os.system("python3 LoginAndRegistrationPage.py")
    root.destroy()

i=0

def load():
    global i
    if i<=10:
        txt='Loading...'+str(10*i)+'%'
        progress_label.config(text=txt)
        progress_label.after(600, load)
        progress['value']=10*i
        i+=1
    else:
        top()

load()
root.resizable(False, False)
root.mainloop()
