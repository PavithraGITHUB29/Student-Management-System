from tkinter import *
import time
import ttkthemes
from tkinter import ttk,messagebox,filedialog
import pymysql
import pandas

#localhost,root,Pavithra@2004
global mycursor,con

def top_data(button_text,command):
   global idEntry,nameEntry,mobEntry,mailEntry,genderEntry,birthEntry,deptEntry,yearEntry,screen
   screen = Toplevel()
   screen.grab_set()
   screen.resizable(False, False)
   idLabel = Label(screen, text='Id', font=('times new roman', 15, 'bold'))
   idLabel.grid(row=0, column=0, padx=20, pady=20)
   idEntry = Entry(screen, font=('times new roman', 15, 'bold'))
   idEntry.grid(row=0, column=1, padx=20, pady=20)

   nameLabel = Label(screen, text='Name', font=('times new roman', 15, 'bold'))
   nameLabel.grid(row=1, column=0, padx=20, pady=20)
   nameEntry = Entry(screen, font=('times new roman', 15, 'bold'))
   nameEntry.grid(row=1, column=1, padx=20, pady=20)

   mobLabel = Label(screen, text='Mobile', font=('times new roman', 15, 'bold'))
   mobLabel.grid(row=3, column=0, padx=20, pady=20)
   mobEntry = Entry(screen, font=('times new roman', 15, 'bold'))
   mobEntry.grid(row=3, column=1, padx=20, pady=20)

   mailLabel = Label(screen, text='Email', font=('times new roman', 15, 'bold'))
   mailLabel.grid(row=4, column=0, padx=20, pady=20)
   mailEntry = Entry(screen, font=('times new roman', 15, 'bold'))
   mailEntry.grid(row=4, column=1, padx=20, pady=20)

   genderLabel = Label(screen, text='Gender', font=('times new roman', 15, 'bold'))
   genderLabel.grid(row=5, column=0, padx=20, pady=20)
   genderEntry = Entry(screen, font=('times new roman', 15, 'bold'))
   genderEntry.grid(row=5, column=1, padx=20, pady=20)

   birthLabel = Label(screen, text='D.O.B', font=('times new roman', 15, 'bold'))
   birthLabel.grid(row=6, column=0, padx=20, pady=20)
   birthEntry = Entry(screen, font=('times new roman', 15, 'bold'))
   birthEntry.grid(row=6, column=1, padx=20, pady=20)

   deptLabel = Label(screen, text='Department', font=('times new roman', 15, 'bold'))
   deptLabel.grid(row=7, column=0, padx=20, pady=20)
   deptEntry = Entry(screen, font=('times new roman', 15, 'bold'))
   deptEntry.grid(row=7, column=1, padx=20, pady=20)

   yearLabel = Label(screen, text='Year Of Study', font=('times new roman', 15, 'bold'))
   yearLabel.grid(row=8, column=0, padx=20, pady=20)
   yearEntry = Entry(screen, font=('times new roman', 15, 'bold'))
   yearEntry.grid(row=8, column=1, padx=20, pady=20)

   updatestudent = ttk.Button(screen, text=button_text, command=command)
   updatestudent.grid(row=9, column=1)
   if button_text == 'Update Student':
      indexing = studentTable.focus()
      content = studentTable.item(indexing)
      listdata = content['values']
      idEntry.insert(0, listdata[0])
      nameEntry.insert(0, listdata[1])
      mobEntry.insert(0, listdata[2])
      mailEntry.insert(0, listdata[3])
      genderEntry.insert(0, listdata[4])
      birthEntry.insert(0, listdata[5])
      deptEntry.insert(0, listdata[6])
      yearEntry.insert(0, listdata[7])

def connect_database():
   def connect():
      global mycursor,con
      try:
         con = pymysql.connect(host=hostname_entry.get(),user=username_entry.get(),password=password_entry.get())
         mycursor = con.cursor()
         messagebox.showinfo('successs','connection successful',parent=connect_window)
      except:
         messagebox.showerror('error','Invalid Details',parent=connect_window)
      query = 'use studentmanagement'
      mycursor.execute(query)
      addStudentButton.config(state=NORMAL)
      searchStudentButton.config(state=NORMAL)
      updateStudentButton.config(state=NORMAL)
      deleteStudentButton.config(state=NORMAL)
      showStudentButton.config(state=NORMAL)
      exportStudentButton.config(state=NORMAL)
      exitButton.config(state=NORMAL)
      connect_window.destroy()



   connect_window = Toplevel()
   connect_window.grab_set()
   connect_window.geometry('470x250+730+230')
   connect_window.title('database connection')

   hostname_label = Label(connect_window,text='Host Name',font=('arial',15,'bold'))
   hostname_label.grid(row=0,column=0,padx=10,pady=20)
   hostname_entry = Entry(connect_window,font=('roman',15,'bold'),bd=2)
   hostname_entry.grid(row=0,column=1,padx=30,pady=20)

   username_label = Label(connect_window, text='User Name', font=('arial', 15, 'bold'))
   username_label.grid(row=1, column=0, padx=10,pady=20)
   username_entry = Entry(connect_window, font=('roman', 15, 'bold'), bd=2)
   username_entry.grid(row=1, column=1, padx=30,pady=20)

   password_label = Label(connect_window, text='Password', font=('arial', 15, 'bold'))
   password_label.grid(row=2, column=0, padx=10, pady=20)
   password_entry = Entry(connect_window, font=('roman', 15, 'bold'), bd=2)
   password_entry.grid(row=2, column=1, padx=30, pady=20)

   connect_button = ttk.Button(connect_window,text='Connect',command=connect)
   connect_button.grid(row=3,column=1)

""" ADD STUDENT FUNCTION """

def add_data():
   global mycursor, con
   try:
      try:
         if (
                 idEntry.get() == ""
                 or nameEntry.get() == ""
                 or mobEntry.get() == ""
                 or mailEntry.get() == ""
                 or genderEntry.get() == ""
                 or birthEntry.get() == ""
                 or yearEntry.get() == ""
         ):
            error_message = messagebox.showerror(
               "Error", message="All Fields are required", parent=screen
            )
         else:
            currentdate = time.strftime("%d-%m-%Y")
            currenttime = time.strftime("%H:%H:%S")
            query = "insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            values = (
               idEntry.get(),
               nameEntry.get(),
               mobEntry.get(),
               mailEntry.get(),
               genderEntry.get(),
               birthEntry.get(),
               deptEntry.get(),
               yearEntry.get(),
               currentdate,
               currenttime,
            )
            mycursor.execute(query, values)
            con.commit()
            result = messagebox.askyesno('success','Data added successfully, Do you want to clear the form ?')
            if(result):
               idEntry.delete(0,END)
               nameEntry.delete(0, END)
               mobEntry.delete(0, END)
               mailEntry.delete(0, END)
               birthEntry.delete(0, END)
               deptEntry.delete(0, END)
               yearEntry.delete(0, END)
               genderEntry.delete(0, END)
            else:
               pass
            query = 'select * from student'
            mycursor.execute(query)
            fetched = mycursor.fetchall()
            studentTable.delete(*studentTable.get_children())
            for data in fetched:
               datalist = list(data)
               studentTable.insert('',END,values=datalist)

      except Exception as e:
            messagebox.showerror("Error", message=f"Error in add_data: {str(e)}", parent=screen)
            print(f"Error in add_data: {str(e)}")
            con.rollback()
   except:
      msg = messagebox.showerror('error','id cannot be repeated',parent=screen)
      return



"""SEARCH STUDENT FUNCTION"""


def search_data():
   query='select * from student where id=%s or name=%s or mobile=%s or email=%s or gender=%s or department=%s or year_of_study=%s'
   mycursor.execute(query,(idEntry.get(),nameEntry.get(),mobEntry.get(),mailEntry.get(),genderEntry.get(),deptEntry.get(),yearEntry.get()))

   fetched = mycursor.fetchall()
   studentTable.delete(*studentTable.get_children())
   for data in fetched:
      listdata = list(data)
      studentTable.insert('',END,values=listdata)


""" DELETE STUDENT FUNCTION """

def delete_student():
   indexing=studentTable.focus()    #gives complete content or row
   content=studentTable.item(indexing)
   content_id = content['values'][0]
   query='delete from student where id=%s'
   mycursor.execute(query,(content_id))
   con.commit()
   messagebox.showinfo('success',message=f'successfully deleted id number {content_id}')
   query='select * from student'
   mycursor.execute(query)
   fetched = mycursor.fetchall()
   studentTable.delete(*studentTable.get_children())
   for data in fetched:
      studentTable.insert('',END,values=data)


""" SHOW STUDENT FUNCTION """

def show_student():
   query = 'select * from student'
   mycursor.execute(query)
   fetched = mycursor.fetchall()
   studentTable.delete(*studentTable.get_children())
   for data in fetched:
      studentTable.insert('', END, values=data)


""" UPDATE STUDENT FUNCTION """
def update_data():
   current_date = time.strftime("%d-%m-%Y")
   current_time = time.strftime("%H:%H:%S")
   query='update student set name=%s,mobile=%s,email=%s,gender=%s,dob=%s,department=%s,year_of_study=%s,date=%s,time=%s where id=%s'
   mycursor.execute(query,(nameEntry.get(),mobEntry.get(),mailEntry.get(),genderEntry.get(),birthEntry.get(),deptEntry.get(),yearEntry.get(),current_date,current_time,idEntry.get()))
   con.commit()
   messagebox.showinfo('success','update successful')
   screen.destroy()
   show_student()


""" EXPORT STUDENT FUNCTION """


def export_student():
   url = filedialog.asksaveasfilename(defaultextension='.csv')
   indexing = studentTable.get_children()
   newlist = []
   for index in indexing:
      content = studentTable.item(index)
      datalist = content['values']
      newlist.append(datalist)
   table=pandas.DataFrame(newlist,columns=['Id','Name','Mobile','Email','Gender','dob','Department','Year of Study','added date','added time'])
   table.to_csv(url,index=False)
   messagebox.showinfo('success','Data stored successfully')


"""" EXIT FUNCTION """
def iexit():
   result = messagebox.askyesno('comfirm','want to exit')
   if result:
      root.destroy()
   else:
      pass


"""FUNCTION TO GET CURRENT DATE AND TIME """


def clock():
   date =  time.strftime('%d-%m-%Y')
   currenttime = time.strftime('%H:%H:%S')
   datetimeLabel.config(text=f'    Date: {date}\n Time: {currenttime}')
   datetimeLabel.after(1000,clock)


""" BASIC GUI """

root = ttkthemes.ThemedTk()
root.get_themes()
root.set_theme('radiance')
root.geometry('1274x680+0+0')
datetimeLabel = Label(root,text='',font=('times new roman',18,'bold'))
datetimeLabel.place(x=5,y=5)
clock()

s = "Student Management System"
sliderLabel = Label(root,text=s,font=('times new roman',20,'italic bold'))
sliderLabel.place(x=500,y=10)

connectButton = ttk.Button(root,text='Connect Database',command=connect_database)
connectButton.place(x=980,y=10)

leftFrame = Frame(root)
leftFrame.place(x=20,y=80,width=280,height=600)

logo_image = PhotoImage(file='student.png')
logo_label = Label(leftFrame,image=logo_image)
logo_label.grid(row=0,column=1)
addStudentButton = ttk.Button(leftFrame,text='Add Student',width=20,state=DISABLED,command=lambda :top_data('Add Student',add_data))
addStudentButton.grid(row=1,column=1,pady=20,padx=40)

searchStudentButton = ttk.Button(leftFrame,text='Search Student',width=20,state=DISABLED,command=lambda: top_data('Search Student',search_data))
searchStudentButton.grid(row=2,column=1,pady=20,padx=40)

updateStudentButton = ttk.Button(leftFrame,text='Update Student',width=20,state=DISABLED,command=lambda: top_data('Update Student',update_data))
updateStudentButton.grid(row=3,column=1,pady=20,padx=40)

deleteStudentButton = ttk.Button(leftFrame,text='Delete Student',width=20,state=DISABLED,command=delete_student)
deleteStudentButton.grid(row=4,column=1,pady=20,padx=40)

showStudentButton = ttk.Button(leftFrame,text='Show Student',width=20,state=DISABLED,command=show_student)
showStudentButton.grid(row=5,column=1,pady=20,padx=40)

exportStudentButton = ttk.Button(leftFrame,text='Export Student',width=20,state=DISABLED,command=export_student)
exportStudentButton.grid(row=6,column=1,pady=20,padx=40)

exitButton = ttk.Button(leftFrame,text='Exit',width=20,command=iexit)
exitButton.grid(row=7,column=1,pady=20,padx=40)
rightFrame = Frame(root)
rightFrame.place(x=350,y=80,width=820,height=600)

scrollbarX = Scrollbar(rightFrame,orient=HORIZONTAL)
scrollbarY = Scrollbar(rightFrame,orient=VERTICAL)

scrollbarX.pack(side=BOTTOM,fill=X)
scrollbarY.pack(side=RIGHT,fill=Y)

""" CREATING TREEVIEW FOR STORING THE DATA """


studentTable = ttk.Treeview(rightFrame,columns=('id','name','mobile','email','gender','dob','department','yos','added_date','added_time'),xscrollcommand=scrollbarX.set,yscrollcommand=scrollbarY.set)
studentTable.pack(fill=BOTH,expand=1)

scrollbarX.config(command=studentTable.xview)
scrollbarY.config(command=studentTable.yview)

studentTable.heading('id',text='Id')
studentTable.heading('name',text='Name')
studentTable.heading('mobile',text='Mobile')
studentTable.heading('email',text='Email')
studentTable.heading('gender',text='Gender')
studentTable.heading('dob',text='DOB')
studentTable.heading('department',text='Department')
studentTable.heading('yos',text='Year Of Study')
studentTable.heading('added_date',text='added date')
studentTable.heading('added_time',text='added time')

studentTable.column('id',width=50,anchor=CENTER)
studentTable.column('name',width=200,anchor=CENTER)
studentTable.column('mobile',width=200,anchor=CENTER)
studentTable.column('email',width=300,anchor=CENTER)
studentTable.column('gender',width=100,anchor=CENTER)
studentTable.column('department',width=150,anchor=CENTER)
studentTable.column('yos',width=150,anchor=CENTER)
studentTable.column('dob',width=100,anchor=CENTER)
studentTable.column('added_date',width=200,anchor=CENTER)
studentTable.column('added_time',width=200,anchor=CENTER)
style = ttk.Style()
style.configure('Treeview',font=('arial',12,'bold'),foreground='black')
style.configure('Treeview.Heading',font=('arial',15,'bold'),foreground='black')
studentTable.config(show='headings')

root.mainloop()