from tkinter import *
from tkinter import ttk 
from tkinter import messagebox
import mysql.connector

db = mysql.connector.connect(host="localhost",user="root",passwd="",database="student")
cur = db.cursor()


root = Tk()
root.geometry("1250x350+100+100")
root.title("Student Form")

def delete_r():
    try:

        rollno = roll_e.get()

        sql = "DELETE FROM info WHERE rollno=%s"
        cur.execute(sql,(rollno,))
        db.commit()
        messagebox.showinfo("Message","Record Deleted")
        roll_e.delete(0,END)
        name_e.delete(0,END)
        div_e.delete(0,END)
        year_e.delete(0,END)
    except:
        messagebox.showinfo("Message","Error Occured")

def update():
    try:
        l = list()
        l.clear()


        name = name_e.get()
        rollno = roll_e.get()
        divi = div_e.get()
        year = year_e.get()

        l.append(name)
        l.append(divi.upper())
        l.append(year)
        l.append(rollno)

        sql = "UPDATE info SET sname=%s,sdiv=%s,syear=%s WHERE rollno=%s"

        cur.execute(sql,l)
        db.commit()
        messagebox.showinfo("Message","Record Updated")

        roll_e.delete(0,END)
        name_e.delete(0,END)
        div_e.delete(0,END)
        year_e.delete(0,END)
    except:
        messagebox.showinfo("Error","Error")


def View():
    for i in tree.get_children():
        tree.delete(i)

    cur.execute("SELECT * FROM info")
    rows = cur.fetchall()

    for row in rows:
        tree.insert("", END, values=row)


def sear():
    try:
        cur.execute('select count(*) from info where rollno=%s',(roll_e.get(),))
        co=cur.fetchone()
        if(co[0]>0):
            cur.execute('select sname,sdiv,syear from info where rollno=%s',(roll_e.get(),))
            
            name_e.delete(0,END)
            div_e.delete(0,END)
            year_e.delete(0,END)
            for r in cur.fetchall():
                name_e.insert(0,r[0])
                div_e.insert(0,r[1])
                year_e.insert(0,r[2])
           
        else:
            messagebox.showinfo("Message","No Record Exist Check Roll NO")
            roll_e.delete(0,END)
            name_e.delete(0,END)
            div_e.delete(0,END)
            year_e.delete(0,END)

    except:
        messagebox.showinfo("Error","No data found")

def reg():
    try:
        l = list()
        l.clear()

        name = name_e.get()
        rollno = roll_e.get()
        divi = div_e.get()
        year = year_e.get()
        

        l.append(rollno)
        l.append(name)
        l.append(divi.upper())
        l.append(year)
        

        sql = "INSERT INTO info VALUES (%s,%s,%s,%s)"

        cur.execute(sql,l)
        db.commit()
        messagebox.showinfo("Status", "Student Records Inserted")

        roll_e.delete(0,END)
        name_e.delete(0,END)
        div_e.delete(0,END)
        year_e.delete(0,END)
    except:
        messagebox.showinfo("Error", "Check Roll No")

la=Label(root,text="Student Details Entry Form")
name_l = Label(root,text="Name")
name_e = Entry(root,width=25)
roll_l = Label(root,text="Roll No")
roll_e = Entry(root,width=25)
div_l = Label(root,text="Division")
div_e = Entry(root,width=25)
year_l = Label(root,text="Year")
year_e = Entry(root,width=25)


la.place(x=50,y=5)
name_l.place(x=10,y=40)
name_e.place(x=100,y=40)
roll_l.place(x=10,y=80)
roll_e.place(x=100,y=80)
div_l.place(x=10,y=120)
div_e.place(x=100,y=120)
year_l.place(x=10,y=160)
year_e.place(x=100,y=160)

b1=Button(root,text="Register",command=reg)
b1.place(x=20,y=200)
b2=Button(root,text="Quit",command=root.destroy)
b2.place(x=260,y=200)
b3=Button(root,text="Search",command=sear)
b3.place(x=200,y=200)
b4 = Button(root,text="Update",command=update)
b4.place(x=80,y=200)
b5 = Button(root,text="Delete",command=delete_r)
b5.place(x=140,y=200)


tree= ttk.Treeview(root, column=("column1", "column2", "column3", "column4"), show='headings',height=12)
tree.heading("#1", text="Student Id")
tree.heading("#2", text="Student Name")
tree.heading("#3", text="Division")
tree.heading("#4", text="Year")
tree.place(x=350,y=20)

b2 = Button(text="view data", command=View)
b2.place(x=700,y=300)


root.mainloop()
