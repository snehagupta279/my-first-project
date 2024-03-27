# Import module
from tkinter import *
from tkinter import messagebox
from subprocess import call
import database as t

# Create object
root = Tk()
root.title('Update Status')
root.geometry("1000x650+100+30")

def show():
    status = clicked.get()
    tktno = e2.get()
    t.update_status(status,tktno)
    messagebox.showinfo("","Updated successfully")
    root.destroy()
    call(["python","expert.py"])

def Back():
    root.destroy()
    call(["python","expert.py"])

# Dropdown menu options
options = [
    "WIP",
    "Cancel",
    "Refuse",
    "Approve"
]
  
# datatype of menu text
clicked = StringVar()

# initial menu text
clicked.set( "Select Status" )

# Add Background Image
filename = PhotoImage(file = "images//status.png")
background_label = Label(root, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create Dropdown menu
drop = OptionMenu( root , clicked , *options ).place(x=100, y=55)

Label(root, text="Status").place(x=20, y=60)
Label(root, text="TicketID").place(x=20, y=100)

e2 = Entry(root)
e2.place(x=100, y=100)

# Create button, it will change label text
button = Button( root , text = "Update" , command = show, height = 1, width = 10 ).place(x=50, y=150)   #x=240, y=57
Button(root, text="Back", command=Back ,height = 1, width = 10).place(x=50, y=190)
# Create Label
label = Label( root , text = " " )
label.pack()

#root.state('zoomed')

# Execute tkinter
root.mainloop()
