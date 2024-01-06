from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
def login():
    if usernameEntry.get() == "" or passwordEntry.get() == "":
        messagebox.showerror("error","please enter a valid username and password")
    elif usernameEntry.get() == "pavi" and passwordEntry.get() == "pavi":
        #messagebox.showinfo("success","very good")
        window.destroy()
        import sms


window = Tk()
window.geometry('1260x700+0+0')
window.configure(bg='white')

frame = Frame(window,bg="white")
frame.place(x=400, y=150)

image_path = 'graduation.png'
logo_image = Image.open(image_path)
logo_photo = ImageTk.PhotoImage(logo_image)

logo_label = Label(frame, image=logo_photo,bg="white")
logo_label.grid(row=0, column=0,columnspan=2,pady=10,padx=20)

username_image = PhotoImage(file='user.png')
user_label = Label(frame,image=username_image,text='User Name',compound=LEFT,font=('times new roman',20,'bold'),bg="white")
user_label.grid(row=1,column=0)

usernameEntry = Entry(frame,font=('times new roman',15),bd=3)
usernameEntry.grid(row=1,column=1,pady=10,padx=20)

password_image = PhotoImage(file='padlock.png')
password_label = Label(frame,image=password_image,text='Password',compound=LEFT,font=('times new roman',20,'bold'),bg="white")
password_label.grid(row=2,column=0)

passwordEntry = Entry(frame,font=('times new roman',15),bd=3)
passwordEntry.grid(row=2,column=1,padx=20,pady=10)

loginButton = Button(frame,text="Login",font=('times new roman',15,'bold'),fg='white',bg='black',cursor='hand2',command=login)
loginButton.grid(row=3,column=1,pady=20)
window.mainloop()