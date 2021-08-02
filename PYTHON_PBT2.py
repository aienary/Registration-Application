import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from tkinter import *

def Delete(event):
	e_id.delete(0,END)
	e_name.delete(0,END)
	e_birthdate.delete(0,END)
	e_addressone.delete(0,END)
	e_addresstwo.delete(0,END)
	e_code.delete(0,END)
	e_city.delete(0,END)
	e_phonenum.delete(0,END)
	row_name = listBox.selection()[0]
	select = listBox.set(row_name)
	e_id.insert(0,select['ID'])
	e_name.insert(0,select['Name'])
	e_birthdate.insert(0,select['Birthdate'])
	e_addressone.insert(0,select['Addressone'])
	e_addresstwo.insert(0,select['Addresstwo'])
	e_code.insert(0,select['Code'])
	e_city.insert(0,select['City'])
	e_phonenum.insert(0,select['Phonenum'])

def Add():
	ID = e_id.get()
	name = e_name.get()
	birthdate = e_birthdate.get()
	age = options.get()
	gender = valRadio.get()
	addressone = e_addressone.get()
	addresstwo = e_addresstwo.get()
	code = e_code.get()
	city = e_city.get()
	state = statemenu.get()
	phonenum = e_phonenum.get()

	mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="registrationbooks")
	mycursor=mysqldb.cursor()

	try:
		sql = "INSERT INTO studentforms (ID,name,birthdate,age,gender,addressone,addresstwo,code,city,state,phonenum) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
		val = (ID,name,birthdate,age,gender,addressone,addresstwo,code,city,state,phonenum)
		mycursor.execute(sql, val)
		mysqldb.commit()
		lastid = mycursor.lastrowid
		messagebox.showinfo("information", "Record inserted successfully")
		e_id.delete(0,END)
		e_name.delete(0,END)
		e_birthdate.delete(0,END)
		e_addressone.delete(0,END)
		e_addresstwo.delete(0,END)
		e_code.delete(0,END)
		e_city.delete(0,END)
		e_phonenum.delete(0,END)
	except Exception as e:
		print(e)
		mysqldb.rollback()
		mysqldb.close()


def update():
	ID = e_id.get()
	name = e_name.get()
	birthdate = e_birthdate.get()
	age = options.get()
	gender = valRadio.get()
	addressone = e_addressone.get()
	addresstwo = e_addresstwo.get()
	code = e_code.get()
	city = e_city.get()
	state = statemenu.get()
	phonenum = e_phonenum.get()
	mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="registrationbooks")
	mycursor=mysqldb.cursor()

	try:
		sql = "Update studentforms set name= %s,birthdate= %s,age= %s,gender= %s, addressone= %s, addresstwo= %s, code= %s, city= %s, state= %s, phonenum= %s where id= %s"
		val = (name,birthdate,age,gender,addressone,addresstwo,code,city,state,phonenum,ID)
		mycursor.execute(sql, val)
		mysqldb.commit()
		lastid = mycursor.lastrowid
		messagebox.showinfo("information", "Record Updated Successfully")

		e_id.delete(0,END)
		e_name.delete(0,END)
		e_birthdate.delete(0,END)
		e_addressone.delete(0,END)
		e_addresstwo.delete(0,END)
		e_code.delete(0,END)
		e_city.delete(0,END)
		e_phonenum.delete(0,END)
		e_id.focus_set()

	except Exception as e:

		print(e)
		mysqldb.rollback()
		mysqldb.close()

def show():
	mysqldb = mysql.connector.connect(host="localhost",user="root",password="",database="registrationbooks")
	mycursor = mysqldb.cursor()
	mycursor.execute("SELECT ID,name,birthdate,age,gender,addressone,addresstwo,code,city,state,phonenum FROM studentforms")
	records = mycursor.fetchall()
	print(records)

	for i, (ID,Name,Birthdate,Age,Gender,Addressone,Addresstwo,Code,City,State,Phonenum) in enumerate(records, start=1):
		listBox.insert("", "end", values=(ID, Name, Birthdate, Age, Gender, Addressone, Addresstwo, Code, City, State, Phonenum))
		mysqldb.close()


root = Tk()
valRadio = StringVar()
root.title("Registration Application")
root.geometry("500x500")
global e_id
global e_name
global e_birthdate
global e_addressone
global e_addresstwo
global e_code
global e_city
global e_phonenum

tk.Label(root, text="ABC Kindergarden Permatang Pauh", width=33, fg= 'dark blue',font=("Britannic Bold", 23)).place(x=73, y=34)

tk.Label(root, text='STUDENT ID :', font=('Century Gothic', 10)).place(x=70, y=100)
Label(root, text='STUDENT NAME :', font=('Century Gothic', 10)).place(x=70, y=130)
Label(root, text='BIRTH DATE :', font=('Century Gothic', 10)).place(x=70, y=160)

Label(root, text='AGE :', font=('Century Gothic', 10)).place(x=70, y=190)
options=StringVar(root)
options.set("please select the age")
menu=OptionMenu(root,options, "3 years","4 years","5 years", "6 years")
menu.place(x=240, y=190)

Label(root, text='GENDER :', font=('Century Gothic', 10)).place(x=70, y=220)

r1 = Radiobutton(root, text="Male",
      variable=valRadio, value='Male').place(x=235, y=220)
r2 = Radiobutton(root, text="Female",
      variable=valRadio, value='Female').place(x=290, y=220)

Label(root, text='ADDRESS 1 :', font=('Century Gothic', 10)).place(x=70, y=250)
Label(root, text='ADDRESS 2 :', font=('Century Gothic', 10)).place(x=70, y=280)
Label(root, text='CODE :', font=('Century Gothic', 10)).place(x=70, y=310)
Label(root, text='CITY :', font=('Century Gothic', 10)).place(x=70, y=340)

Label(root, text='STATE :', font=('Century Gothic', 10)).place(x=70, y=370)
statemenu=StringVar(root)
statemenu.set("select the state")
menu=OptionMenu(root,statemenu, "Perak","Pahang","Johor", "Penang", "Kedah", "Sabah", 
	"Sarawak", "Selangor", "Kelantan", "Perlis", "Kelantan")
menu.place(x=240, y=370)

Label(root, text='PARENTS TEL. NUM :', font=('Century Gothic', 10)).place(x=70, y=400)

e_id = Entry(root)
e_id.place(x=240, y=100)

e_name = Entry(root)
e_name.place(x=240, y=130)

e_birthdate = Entry(root)
e_birthdate.place(x=240, y=160)

e_addressone = Entry(root)
e_addressone.place(x=240, y=250)

e_addresstwo = Entry(root)
e_addresstwo.place(x=240, y=280)

e_code = Entry(root)
e_code.place(x=240, y=310)

e_city = Entry(root)
e_city.place(x=240, y=340)

e_phonenum = Entry(root)
e_phonenum.place(x=240, y=400)

Button(root, text="Update", width=20, bg='purple', fg='white', command=update).place(x=30, y=430)
Button(root, text="Add", width=20, bg='purple', fg='white', command=Add).place(x=210, y=430)

cols = ['ID','Name', 'Birthdate', 'Age', 'Gender', 'Addressone', 'Addresstwo', 'Code', 'City', 'State', 'Phonenum']
treeScroll = ttk.Scrollbar(root)
treeScroll.pack(side=RIGHT, fill=Y)
listBox = ttk.Treeview(root, height=10, columns=cols, show='headings', yscrollcommand = treeScroll.set)

listBox.pack(side=LEFT, fill=BOTH)
treeScroll.config(command=listBox.yview)

for col in cols:
	listBox.heading(col, text=col)
	listBox.column(col, width=120, anchor=tk.CENTER)
	listBox.place(x=5, y=460)

show()
listBox.bind('<Double-Button-1>',Delete)
root.mainloop()
