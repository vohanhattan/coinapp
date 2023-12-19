from tkinter import *
from PIL import ImageTk

def signup_page():
    login_window.destroy()
    import signup

def user_enter(event):
    if usernameEntry.get()=='  Username':
        usernameEntry.delete(0,END)

def password_enter(event):
    if passwordEntry.get()=='  Password':
        passwordEntry.delete(0,END)
        hide()

def hide():
    closeeye.config(file="Image/login/closeye.png")
    passwordEntry.config(show='*')
    eyeButton.config(command=show)

def show():
    closeeye.config(file="Image/login/openeye.png")
    passwordEntry.config(show='')
    eyeButton.config(command=hide)

login_window=Tk()
login_window.geometry('990x660+50+50')
login_window.resizable(0,0)
login_window.title('Login Page')
bgImage=ImageTk.PhotoImage(file="Image/login/bg.jpg")

bgLabel=Label(login_window, image=bgImage)
bgLabel.place (x=0,y=0)

heading=Label(login_window, text='USER LOGIN',font=('Microsoft Yahei UI Light', 23,'bold'), bg='white', fg='black')
heading.place(x=605,y=120)

usernameEntry=Entry(login_window, width=25, font=('Microsoft Yahei UI Light', 11,'bold'), bd=0,fg='black')
usernameEntry.place(x=580,y=200)
usernameEntry.insert(0,'  Username')
usernameEntry.bind('<FocusIn>',user_enter)

frame1=Frame(login_window,width=250,height=2,bg='black')
frame1.place(x=580,y=222)

passwordEntry=Entry(login_window, width=25, font=('Microsoft Yahei UI Light', 11,'bold'), bd=0,fg='black')
passwordEntry.place(x=580,y=260)
passwordEntry.insert(0,'  Password')
passwordEntry.bind('<FocusIn>',password_enter)

frame2=Frame(login_window,width=250,height=2,bg='black')
frame2.place(x=580,y=282)


closeeye=PhotoImage(file="Image/login/openeye.png")
eyeButton=Button(login_window,image=closeeye,bd=0,bg='white',activebackground='white',cursor='hand2',command=hide)
eyeButton.place(x=800,y=255)

forgetButton=Button(login_window,text='Forgot Password',bd=0,bg='white',activebackground='white',
                    cursor='hand2',font=('Microsoft Yahei UI Light', 9,'bold'),
                    fg='black', activeforeground='black')
forgetButton.place(x=715,y=295)

loginButton=Button(login_window,text='Login', font=('Open Sans', 16,'bold'),
                    fg='white', bg='#03a9f4' ,activeforeground='white',
                    activebackground='#03a9f4', cursor='hand2', bd=0,width=19)
loginButton.place(x=578,y=350)

orLabel=Label(login_window,text='-------------- OR --------------',font=('Open Sans',16),fg='black',bg='white')
orLabel.place(x=583,y=400)

facebook_logo=PhotoImage(file='Image/login/facebook.png')
fbLable=Label(login_window,image=facebook_logo,bg='white')
fbLable.place(x=660, y=440)

google_logo=PhotoImage(file='Image/login/google.png')
fbLable=Label(login_window,image=google_logo,bg='white')
fbLable.place(x=710, y=440)

signupLabel=Label(login_window,text="Don't have an account?",font=('Open Sans',9,'bold'),fg='black',bg='white')
signupLabel.place(x=590,y=500)

newaccountButton=Button(login_window,text='Create new one', font=('Open Sans', 9,'bold underline'),
                    fg='blue', bg='white' ,activeforeground='white',
                    activebackground='white', cursor='hand2', bd=0, command=signup_page)
newaccountButton.place(x=727,y=500)

login_window.mainloop()
