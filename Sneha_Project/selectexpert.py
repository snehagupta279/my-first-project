from tkinter import *
from tkinter import messagebox
from subprocess import call
import os
import database as t


def Ok():

    expertid = e1.get()
    tktno = e2.get()

    data=t.retrieve_Data_For_Select_Expert(expertid)

    if(len(data)==0):
        messagebox.showinfo("","Invalid Expert ID or TicketNo.")

    else :
        Role=data[0][5]

        if(Role==0):
            messagebox.showinfo("","Invalid Expert ID or TicketNo.")
 
        elif(Role==1):
            t.update_expert(expertid,tktno)
            messagebox.showinfo("","Updated successfully")
            root.destroy()
            call(["python","admin.py"])
        
        else :
            messagebox.showinfo("","Invalid Expert ID or TicketNo.")
        


def Update():
    c=Ok()

def Back():
    root.destroy()
    call(["python","admin.py"])



os.system("mode con cols=50")
os.system("mode con lines=20")
root = Tk()
root.title("Assign Expert")

root.geometry("900x600+100+50")
C = Canvas(root, bg="sky blue", height=1000, width=1500)

filename = PhotoImage(file = "images//expert1.png")
background_label = Label(root, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

global e1
global e2

 
Label(root, text="Expert ID").place(x=10, y=10)
Label(root, text="TicketID").place(x=10, y=40)
 
e1 = Entry(root)
e1.place(x=140, y=10)
 
e2 = Entry(root)
e2.place(x=140, y=40)


Button(root, text="Update", command=Update ,height = 1, width = 8).place(x=100, y=100)
Button(root, text="Back", command=Back ,height = 1, width = 8).place(x=100, y=140)
C.pack()

root.mainloop()