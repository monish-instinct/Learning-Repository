#import tkinter and mysql connector module
import tkinter as tk #imported tkinter in the name of tk
import mysql.connector
#message box box was separately imported from tkinter  
from tkinter import messagebox
from PIL import Image,ImageTk
from tkinter.ttk import *
# This below module is used to convert interger data into string and represent in (_strftime_)
from time import strftime
window=tk.Tk()
#To resize tkinter screen size to monitor size and background color if needed
window.configure(width=1100,height=window.winfo_screenheight())
window.title('School Management')
#This few lines of code is added to fix an image in the first tkinter window
fname=Image.open('test_1.jpg')
ans=ImageTk.PhotoImage(fname)
imglbl=tk.Label(window,image=ans)
imglbl.place(x=0,y=0)
# This define function is used to add a digital clock over the window with  HH/MM/SS/P
def time():
    string=strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)

label=Label(window,font=('Arial',25),background='black',foreground='cyan')
label.place(x=910,y=5)
# Calling function
time()


# This whole define function is for the data entry section and the database is also connected to MySql
def click_insert():
    window=tk.Tk()
    #To resize tkinter screen size to monitor size and background color if needed
    window.configure(width=1100,height=window.winfo_screenheight(),bg='azure2')
    # Title for the window
    window.title('RD International School')

    # This function is defined for database connection with MySql_
    def db_connection():
        roll_no=int(rnotb.get())
        name=nametb.get()
        english=int(engtb.get())
        maths=int(mathtb.get())
        physics=int(phytb.get())
        chemistry=int(chetb.get())
        tamil=int(tamtb.get())
        # Below function gives the total of the marks which is provided
        total=english+maths+physics+chemistry+tamil
        # This line gives the average of all 5 marks
        average=total/5
        connector=mysql.connector.connect(host='localhost',user='root',password='12345',database='studentdetails')
        cursor=connector.cursor()
        cursor.execute("insert into sdetails values(%d,'%s',%d,%d,%d,%d,%d,%d,%f)"%(roll_no,name,english,maths,physics,chemistry,tamil,total,average))
        connector.commit()
        clearbox()
        messagebox.showinfo('Insert','Successfully Inserted')
       
    def clearbox(): #To clear the data after saving it to mysql in tkinter screen
        rnotb.delete(0,'end')
        nametb.delete(0,'end')
        englishtb=(0,'end')
        mathstb=(0,'end')
        physicstb=(0,'end')
        chemistrytb=(0,'end')
        tamiltb=(0,'end')

    # This line is used to give multiple commands
    command = lambda: [db_connection(), window.destroy()]
  
    namelbl=tk.Label(window,text='DATA ENTRY',height=2,font='Algerian 20',width=24,borderwidth=5,relief='solid')
    namelbl.place(x=362,y=50)

    #Student roll number label and tab
    rnolbl=tk.Label(window,text='Enter student roll number',height=2,font='Algerian 20',width=24,borderwidth=5,relief='solid')
    rnolbl.place(x=100,y=150)

    rnotb=tk.Entry(window,width=10,font='Times 40',borderwidth=5,relief='solid')
    rnotb.place(x=700,y=150)

    #Student name label and tab
    namelbl=tk.Label(window,text='Enter student name',height=2,font='Algerian 20',width=24,borderwidth=5,relief='solid')
    namelbl.place(x=100,y=250)

    nametb=tk.Entry(window,width=10,font='Times 40',borderwidth=5,relief='solid')
    nametb.place(x=700,y=250)

    #Student english mark and tab
    englbl=tk.Label(window,text='Enter English mark',height=2,font='Algerian 20',width=24,borderwidth=5,relief='solid')
    englbl.place(x=100,y=350)

    engtb=tk.Entry(window,width=10,font='Times 40',borderwidth=5,relief='solid')
    engtb.place(x=700,y=350)

    #Student maths mark label and tab
    mathlbl=tk.Label(window,text='Enter Maths mark',height=2,font='Algerian 20',width=24,borderwidth=5,relief='solid')
    mathlbl.place(x=100,y=450)

    mathtb=tk.Entry(window,width=10,font='Times 40',borderwidth=5,relief='solid')
    mathtb.place(x=700,y=450)

    #Student physics mark label and tab
    phylbl=tk.Label(window,text='Enter Physics mark',height=2,font='Algerian 20',width=24,borderwidth=5,relief='solid')
    phylbl.place(x=100,y=550)

    phytb=tk.Entry(window,width=10,font='Times 40',borderwidth=5,relief='solid')
    phytb.place(x=700,y=550)

    #Student chemistry mark label and tab
    chelbl=tk.Label(window,text='Enter Chemistry mark',height=2,font='Algerian 20',width=24,borderwidth=5,relief='solid')
    chelbl.place(x=100,y=650)

    chetb=tk.Entry(window,width=10,font='Times 40',borderwidth=5,relief='solid')
    chetb.place(x=700,y=650)

    #Student name label and tab
    tamlbl=tk.Label(window,text='Enter Tamil mark',height=2,font='Algerian 20',width=24,borderwidth=5,relief='solid')
    tamlbl.place(x=100,y=750)

    tamtb=tk.Entry(window,width=10,font='Times 40',borderwidth=5,relief='solid')
    tamtb.place(x=700,y=750)

    #This is for button
    button=tk.Button(window,text='Submit',height=2,borderwidth=5,relief='solid',width=10,activebackground='azure2',command=command,cursor='hand2')
    button.place(x=550,y=850)

    #This is for button
    button=tk.Button(window,text='<<<',height=1,borderwidth=2,relief='solid',width=5,activebackground='azure2',command=window.destroy,cursor='hand2')
    button.place(x=100,y=50)
        

def click_delete():
    window=tk.Tk()
    #To resize tkinter screen size to monitor size and background color if needed
    window.configure(width=1100,height=window.winfo_screenheight(),bg='cornflower blue')
    window.title('RD International School')
    def db_connection():
        roll_no=int(rnotb.get())
        con=mysql.connector.connect(host='localhost',user='root',password='12345',database='studentdetails')
        cur=con.cursor()
        cur.execute("select * from sdetails where roll_no=%d"%roll_no)
        alldata=cur.fetchall()
        clearbox()
        # This line is to fetch all the data's from MySql
        if len(alldata)>0:
            for i in alldata:
                messagebox.showinfo('----Name----','Name : '+i[1])
                cur.execute("delete from sdetails where roll_no=%d"%roll_no)
                con.commit()
                clearbox()
                messagebox.showinfo('Delete','Successfully Deleted')
        else:
             messagebox.showwarning('Search result','Not found in database')

    def clearbox(): #To clear the data after saving it to mysql in tkinter screen
        rnotb.delete(0,'end')

    command = lambda: [db_connection(), window.destroy()]

    namelbl=tk.Label(window,text='STUDENT NAME DELETE',height=2,font='Algerian 20',width=24,borderwidth=5,relief='solid')
    namelbl.place(x=362,y=50)

    #Student roll number label and tab
    rnolbl=tk.Label(window,text='Enter student roll number',height=2,font='Algerian 20',width=24,borderwidth=5,relief='solid')
    rnolbl.place(x=100,y=250)

    rnotb=tk.Entry(window,width=10,font='Times 40',borderwidth=5,relief='solid')
    rnotb.place(x=700,y=250)


    #This is for button
    button=tk.Button(window,text='Submit',height=2,borderwidth=5,relief='solid',width=10,activebackground='azure2',command=command,cursor='hand2')
    button.place(x=550,y=450)

    
    # Exit Button
    button=tk.Button(window,text='<<<',height=1,borderwidth=2,relief='solid',width=5,activebackground='azure2',command=window.destroy,cursor='hand2')
    button.place(x=100,y=50)
    
        

def click_edit():
    window=tk.Tk()
    #To resize tkinter screen size to monitor size and background color if needed
    window.configure(width=1100,height=window.winfo_screenheight(),bg='cornflower blue')
    window.title('RD International School')

    def db_connection():
        roll_no=int(rnotb.get())
        name=nametb.get()
        con=mysql.connector.connect(host='localhost',user='root',password='12345',database='studentdetails')
        cur=con.cursor()
        cur.execute("select * from sdetails where roll_no=%d"%roll_no)
        alldata=cur.fetchall()
        clearbox()
        if len(alldata)>0:
            for i in alldata:
                messagebox.showinfo('----Name----','Name : '+i[1])
                cur.execute("UPDATE sdetails SET name='%s' WHERE roll_no=%d"%(name,roll_no))
                con.commit()
                clearbox()
                messagebox.showinfo('Edit','Successfully Edited')
        else:
            messagebox.showwarning('Search rcesult','Not found in database')

    def clearbox(): #To clear the data after saving it to mysql in tkinter screen
        rnotb.delete(0,'end')
        nametb.delete(0,'end')

    command = lambda: [db_connection(), window.destroy()]

    namelbl=tk.Label(window,text='STUDENT NAME EDIT',height=2,font='Algerian 20',width=24,borderwidth=5,relief='solid')
    namelbl.place(x=362,y=50)

    #Student roll number label and tab
    rnolbl=tk.Label(window,text='Enter student roll number',height=2,font='Algerian 20',width=24,borderwidth=5,relief='solid')
    rnolbl.place(x=100,y=200)

    rnotb=tk.Entry(window,width=10,font='Times 40',borderwidth=5,relief='solid')
    rnotb.place(x=600,y=200)

    #Student name label and tab
    namelbl=tk.Label(window,text='Enter student name',height=2,font='Algerian 20',width=24,borderwidth=5,relief='solid')
    namelbl.place(x=100,y=300)

    nametb=tk.Entry(window,width=10,font='Times 40',borderwidth=5,relief='solid')
    nametb.place(x=600,y=300)

    #This is for button
    button=tk.Button(window,text='Submit',height=2,borderwidth=5,relief='solid',width=10,activebackground='azure2',command=command,cursor='hand2')
    button.place(x=550,y=450)


    #This is for button
    button=tk.Button(window,text='<<<',height=1,borderwidth=2,relief='solid',width=5,activebackground='azure2',command=window.destroy,cursor='hand2')
    button.place(x=100,y=50)
      
def click_search():
    window=tk.Tk()
    #To resize tkinter screen size to monitor size and background color if needed
    window.configure(width=1100,height=window.winfo_screenheight(),bg='cornflower blue')
    window.title('RD International School')

    def db_connection():
        roll_no=int(rnotb.get())
        con=mysql.connector.connect(host='localhost',user='root',password='12345',database='studentdetails')
        cur=con.cursor()
        cur.execute("select * from sdetails where roll_no=%d"%roll_no)
        alldata=cur.fetchall()
        con.commit()
        clearbox()
        if len(alldata)>0:
            for i in alldata:
                messagebox.showinfo('----Name----','Name : '+i[1])
        else:
            messagebox.showwarning('Search result','Not found in database')
   
    def clearbox(): #To clear the data after saving it to mysql in tkinter screen
        rnotb.delete(0,'end')

    command = lambda: [db_connection(), window.destroy()]


    namelbl=tk.Label(window,text='STUDENT NAME SEARCH',height=2,font='Algerian 20',width=24,borderwidth=5,relief='solid')
    namelbl.place(x=362,y=50)

    #Student roll number label and tab
    rnolbl=tk.Label(window,text='Enter student roll number',height=2,font='Algerian 20',width=24,borderwidth=5,relief='solid')
    rnolbl.place(x=100,y=250)

    rnotb=tk.Entry(window,width=10,font='Times 40',borderwidth=5,relief='solid')
    rnotb.place(x=700,y=250)
    
    #This is for button
    button=tk.Button(window,text='Submit',height=2,borderwidth=5,relief='solid',width=10,activebackground='azure2',command=command,cursor='hand2')
    button.place(x=550,y=450)
    
    #This is for button
    button=tk.Button(window,text='<<<',height=1,borderwidth=2,relief='solid',width=5,activebackground='azure2',command=window.destroy,cursor='hand2')
    button.place(x=100,y=50)
        
   
    
class school():
    def __init__(self):
        namelbl=tk.Label(window,text='------- MAIN MENU -------',height=2,font='Algerian 20',width=24,borderwidth=5,relief='solid')
        namelbl.place(x=362,y=50)

        button=tk.Button(window,text='1.Student Data Entry',height=1,borderwidth=5,relief='solid',width=25,font='Algerian 20',command=click_insert,activebackground='azure2',cursor='hand2')
        button.place(x=350,y=200)

        button=tk.Button(window,text='2.Delete Student Name',height=1,borderwidth=5,relief='solid',width=25,font='Algerian 20',command=click_delete,activebackground='azure2',cursor='hand2')
        button.place(x=350,y=300)

        button=tk.Button(window,text='3.Search Student Name',height=1,borderwidth=5,relief='solid',width=25,font='Algerian 20',command=click_search,activebackground='azure2',cursor='hand2')
        button.place(x=350,y=400)

        button=tk.Button(window,text='4.Edit Student Name',height=1,borderwidth=5,relief='solid',width=25,font='Algerian 20',command=click_edit,activebackground='azure2',cursor='hand2')
        button.place(x=350,y=500)

        button=tk.Button(window,text='5.Exit',height=1,borderwidth=5,relief='solid',width=25,font='Algerian 20',command=window.destroy,activebackground='azure2',cursor='hand2')
        button.place(x=350,y=600)

        

a=school()














