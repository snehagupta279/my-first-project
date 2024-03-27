# Import the required libraries
from tkinter import *
from tkinter import ttk
from subprocess import call
import database as t

# Create an instance of tkinter frame
root = Tk()
root.title("ADMIN")
# Set the size of the tkinter window
root.geometry("1000x500")

def back():
    root.destroy()
    call(["python","signin.py"])

def Assign():
    root.destroy()
    call(["python","selectexpert.py"])

# Create an object of Style widget
style = ttk.Style()
style.theme_use('clam')

# Add a Treeview widget
tree = ttk.Treeview(root, column=("TicketID", "Description", "Expert_Name", "Reportee_Name", "Status"), show='headings', height=20)
tree.column("# 1", anchor=CENTER)
tree.heading("# 1", text="TicketID")
tree.column("# 2", anchor=CENTER)
tree.heading("# 2", text="Description")
tree.column("# 3", anchor=CENTER)
tree.heading("# 3", text="Expert_Name")
tree.column("# 4", anchor=CENTER)
tree.heading("# 4", text="Reportee_Name")
tree.column("# 5", anchor=CENTER)
tree.heading("# 5", text="Status")


l= t.display_tickets_for_admin()
l2= t.display_tickets_for_admin_NULL()
data=l[0]
data1=l[1]
print(l2)

j=0
for i in data:
    ticketno="Tk-{}".format(i[0])
    tree.insert('', 'end', text="1", values=(ticketno, i[1], i[2], data1[j][1], i[3]))
    j=j+1

Button(root, text="Back", command=back ,height = 1, width = 10).place(x=1000, y=500)
Button(root, text="Assign Expert", command=Assign ,height = 1, width = 15).place(x=800, y=500)
tree.pack()

root.state('zoomed')
root.mainloop()
