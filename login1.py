from tkinter import *
from tkinter import messagebox
import mysql.connector as msl

def newPage():
    win = Tk()

    def verify():
        n1 = n_entry.get()
        p1 = p_entry.get()
        obj = msl.connect(host='localhost',user='root',password='qwerty@1234', database='android')
        print("Connected to android database")
        c = obj.cursor()
        c.execute("SELECT * FROM registration where name = %s and mob = %s",(n1,p1))
        result = c.fetchone()
        print(result)
        if result:
            messagebox.showinfo("Success", "Login successful")
        else:
            messagebox.showerror("Failed", "Invalid credentials")
            n_entry.delete(0,END)
            p_entry.delete(0,END)


    win.geometry("450x300")
    win.title("Login")

    heading = Label(win, text="SIGN-IN-PAGE",font=('arial',30,'bold')).pack()

    name = Label(win, text="Name: ", font=('arial', 20,'italic')).place(x=20,y=100)
    n_entry = Entry(win,width =15, font=('arial', 20,'italic'),fg = "blue")
    n_entry.place(x=170,y=100)

    pwd = Label(win, text="Password: ", font=('arial',20, 'italic')).place(x=20,y=160)
    p_entry = Entry(win,width =15, font=('arial', 20,'italic'),fg='red')
    p_entry.place(x=170,y=160)

    loginBtn = Button(win,text='Login',font=('arial', 20,'italic'),command=verify).pack(side='bottom')

    info = Label(win,text="**use your mob no. as password",bg='yellow',font=('arial',10,'italic')).pack(side='bottom',pady=10)

    win.mainloop()