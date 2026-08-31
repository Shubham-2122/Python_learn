'''
    GUI : graphical user interface
    Tkinter desktop application create
    Tkinter : python inbuilt module che
    
'''
from tkinter import *
import mysql.connector
import tkinter.messagebox as msg

def create_conn():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="tkinter_demo"
)

print(create_conn())

#Tk : class che root ne name aapelu che
#Tk : init method bani hase ae j called 


# data have nakhva na che
def insert_data():
    print("insert data")
    if e_fname.get() == "" or e_lname.get()=="" or e_email.get()=="" or e_mobile.get()=="" :
        msg.showinfo("Insert Status","All Fields Are Mandatory")
    else:
        conn = create_conn()
        # aeni pase use kari python cursor my sql query lakhva
        cursor = conn.cursor()
        # sql in query lakho
        query = "insert into student(fname,lname,email,mobile) values(%s,%s,%s,%s)"
        # tuple banse
        argus = (e_fname.get(),e_lname.get(),e_email.get(),e_mobile.get())
        #query and argus nakhvanu
        cursor.execute(query,argus)
        # commit data sql change aave tyre use thay
        conn.commit()
        conn.close()
        #form data jaya pachi data remove thava joei ye
        e_fname.delete(0,'end')
        e_lname.delete(0,'end')
        e_email.delete(0,'end')
        e_mobile.delete(0,'end')
        msg.showinfo("Insert Status","Data Inserted succeessfully")

def search_data():
    print("serach data")
     #form data jaya pachi data remove thava joei ye
    e_fname.delete(0,'end')
    e_lname.delete(0,'end')
    e_email.delete(0,'end')
    e_mobile.delete(0,'end')
    if e_id.get()=="":
        msg.showinfo("Searcg Status","Id Is Mandatory")
    else:
        conn = create_conn()
        cursor = conn.cursor()
        query ="select * from student where id=%s"
        # tuple hoy , karvu padse
        argus =(e_id.get(),)
        cursor.execute(query,argus)
        row = cursor.fetchall()

        # list ma data aayo under type che
        # print(row)
        if row:
            e_fname.insert(0,row[0][1])
            e_lname.insert(0,row[0][2])
            e_email.insert(0,row[0][3])
            e_mobile.insert(0,row[0][4])
        else:
            msg.showinfo("Search Status","Id not Found")
        conn.close()


def update_data():
    print("update data")
    if e_fname.get() == "" or e_lname.get()=="" or e_email.get()=="" or e_mobile.get()=="" or e_id.get()=="" :
        msg.showinfo("Update Status","All Fields Are Mandatory")
    else:
        conn = create_conn()
        cursor = conn.cursor()
        query="update student set fname=%s,lname=%s,email=%s,mobile=%s where id=%s"
        argus=(e_fname.get(),e_lname.get(),e_email.get(),e_mobile.get(),e_id.get())
        cursor.execute(query,argus)
        conn.commit()
        conn.close()
         #form data jaya pachi data remove thava joei ye
        e_fname.delete(0,'end')
        e_lname.delete(0,'end')
        e_email.delete(0,'end')
        e_mobile.delete(0,'end')
        msg.showinfo("Update Status","Data updated successfully")

def delete_data():
    print("delete data")
    if  e_fname.get()=="" :
        msg.showinfo("Delete Status","ID is Mandatory")
    else:
        conn = create_conn()
        cursor = conn.cursor()
        query="delete from student where id=%s"
        argus=(e_id.get(),)
        cursor.execute(query,argus)
        conn.commit()
        conn.close()
         #form data jaya pachi data remove thava joei ye
        e_fname.delete(0,'end')
        e_lname.delete(0,'end')
        e_email.delete(0,'end')
        e_mobile.delete(0,'end')
        msg.showinfo("Delete Status","Data Delete successfully")

root = Tk()

#  size aape che application
root.geometry("390x390")

# application name 
root.title("my Tkinter CRUD Operation")

root.resizable(width=False,height=False)

# form banavu che
# l : lable che rule nthi khabr pade aetle
l_id = Label(root,text="ID")
l_id.place(x=50,y=50)

l_fname = Label(root,text="First Name")
l_fname.place(x=50,y=100)

l_lname = Label(root,text="Last Name")
l_lname.place(x=50,y=150)

l_email = Label(root,text="Email")
l_email.place(x=50,y=200)

l_mobile = Label(root,text="Mobile")
l_mobile.place(x=50,y=250)

# e rntery che but rule khabar pade aelte
e_id = Entry(root)
e_id.place(x=150,y=50)

e_fname = Entry(root)
e_fname.place(x=150,y=100)

e_lname = Entry(root)
e_lname.place(x=150,y=150)

e_email = Entry(root)
e_email.place(x=150,y=200)

e_mobile = Entry(root)
e_mobile.place(x=150,y=250)


# button joei ye 
insert = Button(root,text="INSERT",bg="black",fg="white",font=("Impact",15),command=insert_data)
insert.place(x=50,y=300)

search = Button(root,text="SEARCH",bg="black",fg="white",font=("Impact",15),command=search_data)
search.place(x=130,y=300)

update = Button(root,text="UPDATE",bg="black",fg="white",font=("Impact",15),command=update_data)
update.place(x=210,y=300)

delete = Button(root,text="DELETE",bg="black",fg="white",font=("Impact",15),command=delete_data)
delete.place(x=290,y=300)


# aa khali vs code ma mukvu pade to j run thase
root.mainloop()

