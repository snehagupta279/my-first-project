from tkinter import *
from tkinter import messagebox
from subprocess import call
import os
import database as t


def clear():
    my_text.delete(1.0, END)

def get_text():
    text=my_text.get(1.0,21.0)
    data=t.retrieve_ID2()

    id=data[0][0]
    t.insert_problem_statement(text,id)
    messagebox.showinfo("","Problem Submitted!")
    root.destroy()
    call(["python","user.py"])

def Exit():
    messagebox.showinfo("","Exiting")
    root.destroy()

def back():
    root.destroy()
    call(["python","user.py"])


os.system("mode con cols=50")
os.system("mode con lines=20")
root = Tk()
root.title('Problem Form')
root.geometry("1000x650+100+30")


filename = PhotoImage(file = "images//desk.png")
background_label = Label(root, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

my_text = Text(root, width=80, height=20, font=("Helvetica", 15))
my_text.pack(pady=20)

button_frame = Frame(root)
button_frame.pack()


Button(root, text="Clear Screen", command=clear,height = 1, width = 10).place(x=600, y=510) 


Button(root, text="Submit here", command=get_text,height = 1, width = 10).place(x=700, y=510)


Button(root, text="Back", command=back ,height = 1, width = 10).place(x=640, y=570) 

root.state('zoomed')
root.mainloop()