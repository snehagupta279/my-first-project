from tkinter import *
from tkinter import messagebox
from subprocess import call
import os
import database as t

def query():
    root.destroy()
    call(["python","feedback.py"])

def view():
    root.destroy()
    call(["python","usertable.py"])

def logout():
    t.truncate_temp()
    root.destroy()
    call(["python","signin.py"])


os.system("mode con cols=50")
os.system("mode con lines=20")
root = Tk()
root.title("Want to")
root.geometry("500x400+100+50")
C = Canvas(root, bg="sky blue", height=1000, width=1500)

filename = PhotoImage(file = "images//tkt.png")
background_label = Label(root, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

Button(root, text="Raise a Ticket", command=query ,height = 1, width = 10).place(x=300, y=50)
Button(root, text="View Tickets", command=view ,height = 1, width = 10).place(x=300, y=100)
Button(root, text="Logout", command=logout ,height = 1, width = 10).place(x=300, y=150)
C.pack()
root.mainloop()