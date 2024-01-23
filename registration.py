from tkinter import *
from tkinter import messagebox
import mysql.connector as msl
import login1
from PIL import ImageTk, Image

root = Tk()
root.title("Registration Window")
root.geometry("600x400")

def submit():
    name1 = n_entry.get()
    city1 = c_entry.get()
    mob1 = m_entry.get()
    sub1 = s_entry.get()

    print("your name is : ", name1)
    print("Your city is : ", city1)
    print("Your Mobile number is : ", mob1)
    print("Your subject is : ", sub1)

    

    obj = msl.connect(host='localhost',user='root',password='qwerty@1234', database='android')
    print("Connected to android database")
    c = obj.cursor()
    c.execute("create table if not exists registration(name varchar(30), city varchar(30), mob varchar(30), sub varchar(30))")
    print("table created successfully")
    c.execute("insert into registration values(%s,%s,%s,%s)",(name1,city1,mob1,sub1))
    obj.commit()
    print("values inserted successfully")

    messagebox.showinfo("SUCCESS"," Your form is Successfully submitted")


def login(): 
    login1.newPage()


heading = Label(root, text="SIGNUP-PAGE",font=('arial',30,'bold')).pack()


name = Label(root, text="Name: ", font=('arial', 22,'bold')).place(x=40,y=80)
n_entry = Entry(root,width =15, font=('arial', 20,'italic'),fg = "blue")
n_entry.place(x=160,y=80)

city = Label(root, text="City: ", font=('arial',22, 'bold')).place(x=40,y=135)
c_entry = Entry(root,width =15, font=('arial', 20,'italic'),fg='red')
c_entry.place(x=160,y=135)

mob = Label(root, text="Mobile: ", font=('arial',22, 'bold')).place(x=40,y=190)
m_entry = Entry(root,width =15, font=('arial', 20,'italic'),fg='green')
m_entry.place(x=160,y=190)

sub = Label(root, text="Subject: ", font=('arial',22, 'bold')).place(x=40,y=245)
s_entry = Entry(root,width =15, font=('arial', 20,'italic'),fg='purple')
s_entry.place(x=160,y=245)


submitBtn = Button(root, text="Submit",font=('arial',20,'bold'),bg="grey", command=submit).pack(side='bottom')
loginBtn = Button(root,text="Login", font=('arial',20,'bold'),bg='green',fg='white',command=login).pack(side='bottom')
root.mainloop()