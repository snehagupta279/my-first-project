import mysql.connector


def insertion_tickets(Description,ExpertID,ReporteeID,Status):
    con=mysql.connector.connect(host="localhost",user="springstudent",password="springstudent",database="ticketing_system")
    cur = con.cursor()
    
    cur.execute("SHOW TABLES")
    flag=0
    for x in cur:
        if x=="tickets":
            flag=1
            break

    if (flag==0):
        cur.execute("CREATE TABLE IF NOT EXISTS tickets (TicketID INT AUTO_INCREMENT PRIMARY KEY, Description VARCHAR(500), ExpertID INT, ReporteeID INT, Status VARCHAR(20), datePublished TIMESTAMP DEFAULT CURRENT_TIMESTAMP)")

    query="Insert into tickets(Description,ExpertID,ReporteeID,Status) VALUES ('{}', {}, {}, '{}')".format(Description,ExpertID,ReporteeID,Status)
    cur.execute(query)
    con.commit()


def display_tickets_for_user(id):
    con=mysql.connector.connect(host="localhost",user="springstudent",password="springstudent",database="ticketing_system")
    cur = con.cursor()
    
    query = "select tickets.TicketID, tickets.Description, concat(user.First_Name, ' ' ,user.Last_Name) as Expert_Name, tickets.Status FROM ticketing_system.tickets INNER JOIN ticketing_system.user where(ExpertID=ID and ReporteeID={})".format(id)
    cur.execute(query)
    data=cur.fetchall()
    return data
    
def display_tickets_for_admin():
    con=mysql.connector.connect(host="localhost",user="springstudent",password="springstudent",database="ticketing_system")
    cur = con.cursor()
    
    query = "SELECT tickets.TicketID, tickets.Description, concat(user.First_Name, ' ' ,user.Last_Name) as Expert_Name, tickets.Status FROM ticketing_system.tickets INNER JOIN ticketing_system.user  ON  tickets.ExpertID is NOT NULL AND tickets.ExpertID = user.ID"
    query1 = "SELECT tickets.TicketID, concat(user.First_Name, ' ' ,user.Last_Name) as Reportee_Name FROM ticketing_system.tickets INNER JOIN ticketing_system.user ON tickets.ReporteeID = user.ID"
    cur.execute(query)
    data=cur.fetchall()
    cur.execute(query1)
    data1=cur.fetchall()
    l=[data,data1]
    return l
    

def display_tickets_for_expert(id):
    con=mysql.connector.connect(host="localhost",user="springstudent",password="springstudent",database="ticketing_system")
    cur = con.cursor()
    
    query = "SELECT tickets.TicketID, tickets.Description, concat(user.First_Name, ' ' ,user.Last_Name) as Reportee_Name, tickets.Status FROM ticketing_system.tickets INNER JOIN ticketing_system.user where(ExpertID={} and ReporteeID=ID )".format(id)
    cur.execute(query)
    data=cur.fetchall()

    return data

def insert_problem_statement(Description,ReporteeID):
    con=mysql.connector.connect(host="localhost",user="springstudent",password="springstudent",database="ticketing_system")
    cur = con.cursor()
    query="Insert into tickets(Description,ReporteeID) VALUES ('{}', {})".format(Description,ReporteeID)
    query1="Update tickets set ExpertID=7 where ExpertID is NULL"
    cur.execute(query)
    cur.execute(query1)
    con.commit()

def display_tickets_for_admin_NULL():
    con=mysql.connector.connect(host="localhost",user="springstudent",password="springstudent",database="ticketing_system")
    cur = con.cursor()
    
    query = "SELECT tickets.TicketID, tickets.Description, concat(user.First_Name, ' ' ,user.Last_Name) as Reportee_Name FROM ticketing_system.tickets, ticketing_system.user where tickets.ExpertID is NULL"

    cur.execute(query)
    data=cur.fetchall()
   
    return data

def update_expert(expertid,tktno):
    con=mysql.connector.connect(host="localhost",user="springstudent",password="springstudent",database="ticketing_system")
    cur = con.cursor()
    
    query = "update tickets set tickets.ExpertID={} where tickets.TicketID={}".format(expertid,tktno)
    cur.execute(query)
    con.commit()

def update_status(status,tktno):
    con=mysql.connector.connect(host="localhost",user="springstudent",password="springstudent",database="ticketing_system")
    cur = con.cursor()
    
    query = "update tickets set tickets.Status='{}' where tickets.TicketID={}".format(status,tktno)
    cur.execute(query)
    con.commit()

def retrieve_ID(username,password):
    con=mysql.connector.connect(host="localhost",user="springstudent",password="springstudent",database="ticketing_system")
    cur = con.cursor()

    query = "select ID from user where Username='{}' and Password='{}'".format(username,password)
    cur.execute(query)
    data=cur.fetchall()
    return data

def insert_ID(ID):
    con=mysql.connector.connect(host="localhost",user="springstudent",password="springstudent",database="ticketing_system")
    cur = con.cursor()
    
    cur.execute("SHOW TABLES")
    flag=0
    for x in cur:
        if x=="temp":
            flag=1
            break

    if (flag==0):
        cur.execute("CREATE TABLE IF NOT EXISTS temp (userID INT)")

    query="Insert into temp(userID) VALUES ({})".format(ID)
    cur.execute(query)
    con.commit()

def retrieve_ID2():
    con=mysql.connector.connect(host="localhost",user="springstudent",password="springstudent",database="ticketing_system")
    cur = con.cursor()
    
    query = "select userID from temp"
    cur.execute(query)
    data=cur.fetchall()

    return data

def truncate_temp():
    con=mysql.connector.connect(host="localhost",user="springstudent",password="springstudent",database="ticketing_system")
    cur = con.cursor()
    
    query1 = "truncate table temp"
    cur.execute(query1)
    con.commit()
    

def retrieve_Role(Id):
    con=mysql.connector.connect(host="localhost",user="springstudent",password="springstudent",database="ticketing_system")
    cur = con.cursor()
    
    query = "select Role from user where ID={}".format(Id)
    cur.execute(query)
    data=cur.fetchall()
    return data

def retrieve_Data_For_Select_Expert(expertid):

    con=mysql.connector.connect(host="localhost",user="springstudent",password="springstudent",database="ticketing_system")
    cur = con.cursor()
    
    query = "select * from user where ID={}".format(expertid)
    cur.execute(query)
    data=cur.fetchall()
    return data
