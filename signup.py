from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import pymysql
import re

def clear():
    emailEntry.delete(0,END)
    usernameEntry.delete(0,END)
    passwordEntry.delete(0,END)
    confirmEntry.delete(0,END)

def validate_username(username):
    if not username.strip():
        return False
    special_characters = re.compile(r'[!@#$%^&*(),.?":{}|<>]')
    if special_characters.search(username):
        return False
    if len(username) < 3 or len(username) > 20:
        return False
    return True

def validate_email(email):
    if not email.strip():
        return False
    email_regex = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    return bool(email_regex.match(email))

def validate_password(password):
    # Check password length (at least 8 characters)
    if len(password) < 8:
        return False

    # Check that the password has at least one lowercase letter
    if not any(char.islower() for char in password):
        return False

    # Check that the password has at least one uppercase letter
    if not any(char.isupper() for char in password):
        return False

    # Check that the password has at least one digit
    if not any(char.isdigit() for char in password):
        return False

    # Check that the password has at least one special character
    special_characters = re.compile(r'[!@#$%^&*(),.?":{}|<>]')
    if not special_characters.search(password):
        return False

    return True

def validate_confirmpassword(confirmpassword):
    password = passwordEntry.get()

    if password != confirmpassword:
        return False
    if not validate_password(password):
        return False
    return True

def connect_database():
    host = "localhost"
    user = "root"
    password_db = "123456"
    database = ""

    email = emailEntry.get()
    username = usernameEntry.get()
    password = passwordEntry.get()
    confirmpassword = confirmEntry.get()
    if validate_email(email) == False:
    #or usernameEntry.get()=='' or passwordEntry.get()=='' or confirmEntry.get()=='':
        messagebox.showerror('Error','Invalid email.')
    
    elif validate_username(username) == False:
        messagebox.showerror('Error','Invalid username.')
   
    elif validate_password(password) == False:
        messagebox.showerror('Error','Invalid password. Kindly please check:\n' 
                             ' Check password length (at least 8 characters).\n'
                             ' Check that the password has at least one lowercase letter.\n'
                             ' Check that the password has at least one capital letter.\n'
                             ' Check that the password has at least one digit.\n'
                             ' Check that the password has at least one special character.\n')
    elif validate_confirmpassword(confirmpassword) == False:
        messagebox.showerror("Error", "Passwords do not match.")
    elif check.get()==0:
        messagebox.showerror("Error", "Please accept terms and Conditions.")
    
    else:
        try:
            connection = pymysql.connect(
                host=host,
                user=user,
                password=password_db)
                
            mycursor = connection.cursor()  
        except:
            messagebox.showerror("Error", "Database connectivity Issue, Please try again.")
            return
        try:
            query='CREATE DATABASE IF NOT EXISTS coinapp'
            mycursor.execute(query)
            query='USE coinapp'
            mycursor.execute(query)
            query='CREATE TABLE IF NOT EXISTS userpf (id BIGINT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(50) NOT NULL, password VARCHAR(50) NOT NULL, role VARCHAR(20) NOT NULL)'
            mycursor.execute(query)
        except:
            mycursor.execute('USE coinapp')
        
        query = 'INSERT INTO userpf (email, username, password, role) VALUES (%s,%s,%s,%s)'
        mycursor.execute(query,(emailEntry.get(),usernameEntry.get(),passwordEntry.get(),'User'))
        connection.commit()
        connection.close()
        messagebox.showinfo("Success", "Register is successful.")
        clear()





def login_page():
    signup_window.destroy()
    import signin


signup_window=Tk()
signup_window.title('Signup Page')
signup_window.resizable(False,False)
background=ImageTk.PhotoImage(file='Image/login/bg.jpg')

bgLable=Label(signup_window,image=background)
bgLable.grid()

frame = Frame(signup_window,bg='white')
frame.place(x=554,y=100)

heading=Label(frame, text='CREATE AN ACCOUNT',font=('Microsoft Yahei UI Light', 18,'bold'), 
              bg='white', fg='black')
heading.grid(row=0,column=0,padx=10,pady=10)



emailLable=Label(frame,text='Email',font=('Microsoft Yahei UI Light', 10,'bold'),
                 bg='white', fg='black')
emailLable.grid(row=1,column=0,sticky='w',padx=25,pady=(2,0))
emailEntry=Entry(frame,width=30,font=('Microsoft Yahei UI Light', 10,'bold'),
                 bg='white', fg='black')
emailEntry.grid(row=2,column=0,sticky='w',padx=25)


usernameLable=Label(frame,text='Username',font=('Microsoft Yahei UI Light', 10,'bold'),
                 bg='white', fg='black')
usernameLable.grid(row=3,column=0,sticky='w',padx=25,pady=(2,0))
usernameEntry=Entry(frame,width=30,font=('Microsoft Yahei UI Light', 10,'bold'),
                 bg='white', fg='black')
usernameEntry.grid(row=4,column=0,sticky='w',padx=25)


passwordLable=Label(frame,text='Password',font=('Microsoft Yahei UI Light', 10,'bold'),
                 bg='white', fg='black')
passwordLable.grid(row=5,column=0,sticky='w',padx=25,pady=(2,0))
passwordEntry=Entry(frame,width=30,font=('Microsoft Yahei UI Light', 10,'bold'),
                 bg='white', fg='black')
passwordEntry.grid(row=6,column=0,sticky='w',padx=25)
passwordEntry.config(show='*')

confirmLable=Label(frame,text='Confirm Password',font=('Microsoft Yahei UI Light', 10,'bold'),
                 bg='white', fg='black')
confirmLable.grid(row=7,column=0,sticky='w',padx=25,pady=(2,0))
confirmEntry=Entry(frame,width=30,font=('Microsoft Yahei UI Light', 10,'bold'),
                 bg='white', fg='black')
confirmEntry.grid(row=8,column=0,sticky='w',padx=25)
confirmEntry.config(show='*')
check = IntVar()
termsandconditions=Checkbutton(frame,text='I agree to the Term & Conditions',
                               font=('Microsoft Yahei UI Light', 9,'bold'),fg='black',
                               bg='white',activebackground='white',activeforeground='black',
                               cursor='hand2',variable=check)
termsandconditions.grid(row=9,column=0,padx=10,pady=15)

signupButton=Button(frame,text='Signup', font=('Open Sans', 16,'bold'), bd=0,
                    fg='white', bg='#03a9f4' ,activeforeground='white',
                    activebackground='#03a9f4',width=17,cursor='hand2', command=connect_database)
signupButton.grid(row=10,column=0,pady=10)

alreadyaccount=Label(frame,text="Already have an account?",font=('Open Sans',9,'bold'),
                     fg='black',bg='white')
alreadyaccount.grid(row=11,column=0,sticky='w',padx=25,pady=10)

loginButton=Button(frame,text='Log in', font=('Open Sans', 9,'bold underline'), 
                     bg='white', fg='blue', bd=0,cursor='hand2',
                     activebackground='white',activeforeground='blue',command=login_page)
loginButton.place(x=180,y=381)

signup_window.mainloop()