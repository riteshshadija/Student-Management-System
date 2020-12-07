from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
# import cx_Oracle

root=Tk()
root.title("student management system")
root.geometry("300x300+400+200")

adst=Toplevel(root)
adst.title("add student")
adst.geometry("300x300+400+200")
adst.withdraw()

lblRnoadd=Label(adst,text='rollno')
entRnoadd=Entry(adst,bd=5)
lblNameadd=Label(adst,text='Name')
entNameadd=Entry(adst,bd=5)


def f1():
	con=None
	try:
		con=cx_Oracle.connect("system/abc123")
		cursor=con.cursor()
		s1=entRnoadd.get()
		if(s1==''):
			messagebox.showerror("incomplete",'RollNo is Empty')
			entRnoadd.focus()
			return
		s2=entNameadd.get()
		if(s2==''):
			messagebox.showerror('incomplete','Name is Empty')
			entNameadd.focus()
			return
		if(not s1.isdigit()):
			messagebox.showerror('incomplte','invalid rollno')
			entRnoadd.delete(0,END)
			entRnoadd.focus()
			return
		if(s2.isdigit()):
			messagebox.showerror('incomplte','invalid name')
			entNameadd.delete(0,END)
			entNameadd.focus()
			return
		rno=int(entRnoadd.get())
		name=entNameadd.get()
		sql="insert into student1 values('%d','%s')"
		args=(rno,name)
		cursor.execute(sql % args)
		con.commit()
		msg=str(cursor.rowcount)+" rows inserted"
		messagebox.showinfo("success",msg)
	except cx_Oracle.DatabaseError as e:
		msg='issue'+str(e)
		messagebox.showerror('issue',msg)
		con.rollback()
	finally:
		cursor.close()
		if con is not None:
			con.close()
	entRnoadd.delete(0,END)
	entNameadd.delete(0,END)
	entRnoadd.focus()

btnsaveadd=Button(adst,text='Save',command=f1,width=10)

def f2():
	root.deiconify()
	adst.withdraw()

btnbackadd=Button(adst,text='Back',command=f2,width=10)
lblRnoadd.pack(pady=8)
entRnoadd.pack(pady=5)
lblNameadd.pack(pady=5)
entNameadd.pack(pady=5)
btnsaveadd.pack(pady=10)
btnbackadd.pack(pady=5)

def f3():
	adst.deiconify()
	root.withdraw()
	entRnoadd.focus()


btnaddroot=Button(root,text='Add',width=10,command=f3)

vist=Toplevel(root)
vist.title("view student")
vist.geometry("300x300+400+200")
vist.withdraw()
stdata=scrolledtext.ScrolledText(vist,width=30,height=15)

def f4():
	root.deiconify()
	vist.withdraw()
	stdata.delete("1.0",END)
btnBackView=Button(vist,text="back",command=f4,width=10)
stdata.pack()
btnBackView.pack()

def f5():
	vist.deiconify()
	root.withdraw()
	con=None
	try:
		con=cx_Oracle.connect("system/abc123")
		cursor=con.cursor()
		sql="select * from student1"
		cursor.execute(sql)
		rows=cursor.fetchall()
		data=""
		for r in rows:
			rno=r[0]
			name=r[1]
			data=data+'RollNo:'+str(rno)+'Name:'+name+'\n'
		stdata.insert(INSERT,data)
	except cx_Oracle.DatabaseError as e:
		msg="issue"+str(e)
		messagebox.showerror("error",msg)
	finally:
		cursor.close()
		if con is not None:
			con.close()
btnviewroot=Button(root,text='View',width=10,command=f5)

delst=Toplevel(root)
delst.title("Delete Student")
delst.geometry("300x300+400+200")
delst.withdraw()

lblRnodelst=Label(delst,text="RollNo:",width=10)
entRnodelst=Entry(delst,bd=5)

def f6():
	con=None
	try:
		con=cx_Oracle.connect("system/abc123")
		cursor=con.cursor()
		s1=entRnodelst.get()
		if(s1==''):
			messagebox.showerror("incomplete",'RollNo is Empty')
			entRnodelst.focus()
			return
		if(not s1.isdigit()):
			messagebox.showerror('incomplte','invalid rollno')
			entRnodelst.delete(0,END)
			entRnodelst.focus()
			return

		rno=int(entRnodelst.get())
		sql="delete from student1 where rno='%d'"
		args=(rno)
		cursor.execute(sql % args)
		con.commit()
		msg=str(cursor.rowcount)+" rows deleted"
		messagebox.showinfo("success",msg)
	except cx_Oracle.DatabaseError as e:
		msg='issue'+str(e)
		messagebox.showerror('issue',msg)
	finally:
		cursor.close()
		if con is not None:
			con.close()
	entRnodelst.delete(0,END)
	entRnodelst.focus()
btndeletedelst=Button(delst,text='Delete',width=10,command=f6)
def f7():
	root.deiconify()
	delst.withdraw()

btnbackdel=Button(delst,text='Back',width=10,command=f7)

def f8():
	delst.deiconify()
	root.withdraw()
	entRnodelst.focus()

btndeleteroot=Button(root,text='Delete',width=10,command=f8)
lblRnodelst.pack(pady=5)
entRnodelst.pack(pady=5)
btndeletedelst.pack(pady=5)
btnbackdel.pack(pady=5)

upst=Toplevel(root)
upst.title("Update Student")
upst.geometry("300x300+400+200")
upst.withdraw()

lblRnoupst=Label(upst,text="RollNo:",width=10)
entRnoupst=Entry(upst,bd=5)
lblnameupst=Label(upst,text="Name:",width=10)
entnameupst=Entry(upst,bd=5)

def f9():
	con=None
	try:
		con=cx_Oracle.connect("system/abc123")
		cursor=con.cursor()
		s1=entRnoupst.get()
		if(s1==''):
			messagebox.showerror("incomplete",'RollNo is Empty')
			entRnoupst.focus()
			return
		s2=entnameupst.get()
		if(s2==''):
			messagebox.showerror("incomplete",'Name is Empty')
			entRnoupst.focus()
			return
		if(not s1.isdigit()):
			messagebox.showerror('incomplte','invalid rollno')
			entRnoupst.delete(0,END)
			entRnoupst.focus()
			return
		if(s2.isdigit()):
			messagebox.showerror('incomplte','invalid name')
			entnameupst.delete(0,END)
			entnameupst.focus()
			return

		rno=int(entRnoupst.get())
		name=entnameupst.get()
		sql="update student1 set name='%s' where rno='%d'"
		args=(name,rno)
		cursor.execute(sql % args)
		con.commit()
		msg=str(cursor.rowcount)+" rows updated"
		messagebox.showinfo("success",msg)
	except cx_Oracle.DatabaseError as e:
		msg='issue'+str(e)
		messagebox.showerror('issue',msg)
	finally:
		cursor.close()
		if con is not None:
			con.close()
	entRnoupst.delete(0,END)
	entRnoupst.focus()
	entnameupst.delete(0,END)
	entRnoupst.focus()
btnupst=Button(upst,text='Update',width=10,command=f9)

def f10():
	root.deiconify()
	upst.withdraw()

btnbackupst=Button(upst,text='Back',command=f10,width=10)

def f11():
	upst.deiconify()
	root.withdraw()
	entRnoupst.focus()

btnupdateroot=Button(root,text='update',width=10,command=f11)
lblRnoupst.pack(pady=10)
entRnoupst.pack(pady=10)
lblnameupst.pack(pady=10)
entnameupst.pack(pady=10)
btnupst.pack(pady=10)
btnbackupst.pack(pady=10)

btnaddroot.pack(pady=10)
btnviewroot.pack(pady=10)
btnupdateroot.pack(pady=10)
btndeleteroot.pack(pady=10)

def f12():
	 ans= messagebox.askyesno("Exit","Are you sure?")
	 if ans:
	 	import sys
	 	sys.exit()

root.protocol("WM_DELETE_WINDOW",f12)

root.mainloop()