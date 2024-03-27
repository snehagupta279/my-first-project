from tkinter import *
from tkinter import messagebox
from subprocess import call
import os
import database as t


def Ok():

    t.truncate_temp()
    uname = e1.get()
    password = e2.get()

    data=t.retrieve_ID(uname,password)
    if(len(data)==0):
        messagebox.showinfo("","Invalid username or password")

    else :
        Id=data[0][0]
        t.insert_ID(Id)
        data=t.retrieve_Role(Id)
        Role=data[0][0]

        if(Role==0):
            root.destroy()
            call(["python","admin.py"])
 
        elif(Role==1):
            root.destroy()
            call(["python","expert.py"])
        
        else :
            root.destroy()
            call(["python","user.py"])


def signin():
    c=Ok()

def Exit():
    x=messagebox.askquestion("Quit","Are you sure want to Exit")
    if(x=='yes'):
        root.destroy()



os.system("mode con cols=50")
os.system("mode con lines=20")
root = Tk()
root.title("Login")

root.geometry("900x600+100+50")
C = Canvas(root, bg="sky blue", height=1000, width=1500)

filename = PhotoImage(file = "images//signin.png")
background_label = Label(root, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

global e1
global e2

Label(root, text="UserName").place(x=10, y=10)
Label(root, text="Password").place(x=10, y=40)
 
e1 = Entry(root)
e1.place(x=140, y=10)
 
e2 = Entry(root)
e2.place(x=140, y=40)
e2.config(show="*")


Button(root, text="Login", command=signin ,height = 1, width = 8).place(x=100, y=100)
Button(root, text="Exit", command=Exit ,height = 1, width = 8).place(x=100, y=140)
C.pack()
root.mainloop()
