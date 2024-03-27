# Import the required libraries
from tkinter import *
from tkinter import ttk
from subprocess import call
import database as t

# Create an instance of tkinter frame
root = Tk()
root.title("TICKET VIEW")
# Set the size of the tkinter window
root.geometry("1000x500")

def back():
    root.destroy()
    call(["python","user.py"])


# Create an object of Style widget
style = ttk.Style()
style.theme_use('clam')

# Add a Treeview widget
tree = ttk.Treeview(root, column=("TicketID", "Description", "Expert_Name", "Status"), show='headings', height=20)
tree.column("# 1", anchor=CENTER)
tree.heading("# 1", text="TicketID")
tree.column("# 2", anchor=CENTER)
tree.heading("# 2", text="Description")
tree.column("# 3", anchor=CENTER)
tree.heading("# 3", text="Expert_Name")
tree.column("# 4", anchor=CENTER)
tree.heading("# 4", text="Status")

data=t.retrieve_ID2()
id=data[0][0]

data = t.display_tickets_for_user(id)
print(data)

for i in data:
    ticketno="Tk-{}".format(i[0])
    tree.insert('', 'end', text="1", values=(ticketno, i[1], i[2], i[3]))

Button(root, text="Back", command=back ,height = 1, width = 10).place(x=950, y=500)

tree.pack()

root.state('zoomed')
root.mainloop()
