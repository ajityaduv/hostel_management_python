from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import messagebox
from click import command
import mysql.connector as msl

root = Tk()
root.title("Hostel Management System")
root.geometry("700x720+400+50")
root.iconbitmap(r'D:\python codes\day14_gui\icon.ico')

def add():
    name1 = n_entry.get()
    address1 = a_entry.get()
    phone1 = p_entry.get()
    branch1 = b_entry.get()
    pname1 = pn_entry.get()
    room1 = r_entry.get()


    obj = msl.connect(host='localhost', user='root', password='qwerty@1234')
    print("connsction successful")
    cursor = obj.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS hostel1")
    obj = msl.connect(host='localhost', user='root', password='qwerty@1234',database='hostel1')
    cursor = obj.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS details(name varchar(30), room varchar(10),address varchar(30), phone varchar(20), branch varchar(20), parent varchar(30))")
    print("table created successfully")
    cursor.execute("INSERT INTO details VALUES(%s,%s,%s,%s,%s,%s)",(name1,room1,address1,phone1,branch1,pname1))
    print("Values inserted successfully")
    obj.commit()
    str = "hostel room booked successfully! room id: " + room1
    messagebox.showinfo("success", str)

def view():
    win = Toplevel(root)
    obj = msl.connect(host='localhost', user='root', password='qwerty@1234',database='hostel1')
    print("connection successful")
    cursor = obj.cursor()
    cursor.execute("SELECT * FROM details")
    tree = ttk.Treeview(win)
    tree['show'] = 'headings'
    tree['columns'] = ("1","2","3","4","5","6")

    tree.column('1', width=130,minwidth=50,anchor=CENTER)
    tree.column('2', width=130,minwidth=50,anchor=CENTER)
    tree.column('3', width=130,minwidth=50,anchor=CENTER)
    tree.column('4', width=130,minwidth=50,anchor=CENTER)
    tree.column('5', width=130,minwidth=50,anchor=CENTER)
    tree.column('6', width=130,minwidth=50,anchor=CENTER)


    tree.heading("1", text = "NAME", anchor=CENTER)
    tree.heading("2", text = "ROOM ID", anchor=CENTER)
    tree.heading("3", text = "ADDRESS", anchor=CENTER)
    tree.heading("4", text = "PHONE", anchor=CENTER)
    tree.heading("5", text = "BRANCH", anchor=CENTER)
    tree.heading("6", text = "PARENT'S NAME", anchor=CENTER)

    i=0
    for row in cursor:
        tree.insert('',i,text='',values=(row[0],row[1],row[2],row[3],row[4],row[5]))
        i+=1

    # tree.place(x=0,y=0)
    tree.pack()
    win.mainloop()


global img
img = ImageTk.PhotoImage(Image.open(r'D:\python codes\day14_gui\wallpaperflare.com_wallpaper.jpg'))
img_lbl = Label(root,image=img).pack()

heading = Label(root, text = "WELCOME TO HOSTEL MANAGEMENT SYSTEM", font=('ariel',20,'bold')).place(x=30,y=20)

name = Label(root, text = "Name:", font = ('ariel', 20, 'bold')).place(x=50,y=120)
n_entry = Entry(root,width =15, font = ('ariel', 20, 'italic'),fg='blue')
n_entry.place(x=210,y=120)

roomid = Label(root, text = "RoomID:", font = ('ariel', 20, 'bold')).place(x=50,y=180)
r_entry = Entry(root,width =15, font = ('ariel', 20, 'italic'),fg='blue')
r_entry.place(x=210,y=180)

address = Label(root, text = "Adress:", font = ('ariel', 20, 'bold')).place(x=50,y=240)
a_entry = Entry(root,width =15, font = ('ariel', 20, 'italic'),fg='blue')
a_entry.place(x=210,y=240)

phone = Label(root, text = "Phone:", font = ('ariel', 20, 'bold')).place(x=50,y=300)
p_entry = Entry(root,width =15, font = ('ariel', 20, 'italic'),fg='blue')
p_entry.place(x=210,y=300)

branch = Label(root, text = "Branch: ", font = ('ariel', 20, 'bold')).place(x=50,y=360)
b_entry = Entry(root,width =15, font = ('ariel', 20, 'italic'),fg='blue')
b_entry.place(x=210,y=360)

#Parents Name
pname = Label(root,text = "Parent's Name: ", font=('ariel', 20, 'bold'))
pname.place(x=50,y=480)

pn_entry = Entry(root,width =15, font = ('ariel', 20, 'italic'),fg='blue')
pn_entry.place(x=290,y=480)

#submitbtn
submitBtn = Button(root,text="Add Data",font=('arial',20), command=add)
submitBtn.place(x=130,y=600)

#viewbtn
viewbtn = Button(root,text="View Data",font=('arial',20), command=view)
viewbtn.place(x=400,y=600)

root.mainloop()