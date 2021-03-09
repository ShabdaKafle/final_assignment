from tkinter import *
from tkinter import ttk
from tkinter import messagebox

import model.user
import Backend.dbconnection
import Frontend.loginpage
import Frontend.welcomepage


class Register_Page:
    def __init__(self, register):
        self.register = register
        self.register.title('User registration')
        self.register.geometry('800x750')
        self.register.config(bg="purple")

        self.db= Backend.dbconnection.DBConnect()

        self.fr1 = Frame(self.register, bd=5, relief=RIDGE)
        self.fr1.place(x=95, y=20, width=600, height=700)
        quote2 = Label(self.fr1, text="REGISTER HERE", font=("arial 20 bold"), fg="steelblue").place(x=10, y=10)

        # creating register
        self.username = Label(self.fr1, text="Username", font=("cambria 14"), fg="black").place(x=10, y=70)
        self.uname = Entry(self.fr1, bd=5, relief=GROOVE, width=27, font=("arial 13 bold"))
        self.uname.place(x=120, y=70)

        self.hostelname = Label(self.fr1, text="Hostel name", font=("cambria 14"), fg="black").place(x=10, y=120)
        self.hname = Entry(self.fr1, bd=5, relief=GROOVE, width=32, font=("arial 13 bold"))
        self.hname.place(x=120, y=120)

        self.address = Label(self.fr1, text="Address", font=("cambria"), fg="black").place(x=10, y=170)
        self.add = Entry(self.fr1, bd=5, relief=GROOVE, width=27, font=("arial 13 bold"))
        self.add.place(x=105, y=170)

        self.type = Label(self.fr1, text="Hostel Type", font=("cambria"), fg="black").place(x=10, y=220)
        self.htype = ttk.Combobox(self.fr1, values=("Girls", "Boys"), state='readonly')
        self.htype.place(x=120, y=225)

        self.con = Label(self.fr1, text="Conatct number", font=("cambria"), fg="black").place(x=10, y=270)
        self.cont = Entry(self.fr1, bd=5, relief=GROOVE, width=25, font=("arial 13 bold"))
        self.cont.place(x=160, y=270)

        self.password1 = Label(self.fr1, text="Password", font=("cambria"), fg="black").place(x=10, y=320)
        self.pw1 = Entry(self.fr1, bd=5, relief=GROOVE, width=25, font=("arial 13 bold"), show='*')
        self.pw1.place(x=110, y=320)

        self.confirm_pass = Label(self.fr1, text="Confirm Password", font=("cambria"), fg="black").place(x=10, y=370)
        self.conpw = Entry(self.fr1, bd=5, relief=GROOVE, width=25, font=("arial 13 bold"), show='*')
        self.conpw.place(x=180, y=370)

        self.var_chk = IntVar()
        chk = Checkbutton(self.fr1, text="I agree to the terms and conditions", variable=self.var_chk, onvalue=1, offvalue=0,\
                          font=("arial 12 bold")).place(x=100, y=450)


        btn_register = Button(self.fr1, text='Register', font=('arial', 15, 'bold'), width=8, bd=5, bg="steelblue", fg="white",\
                              relief=RAISED,command=self.add_click, padx=5)
        btn_register.place(x=70, y=520)

        btn_reset = Button(self.fr1, text='Reset', font=('arial', 15, 'bold'), width=8, bd=5,bg="steelblue",fg="white",\
                           relief=RAISED,command=self.reset_click, padx=5)
        btn_reset.place(x=200, y=520)

        btn_back = Button(self.fr1, text='Back', font=('arial', 15, 'bold'), width=8, bd=5, bg="steelblue",
                           fg="white", \
                           relief=RAISED, command=self.back_click, padx=5)
        btn_back.place(x=330, y=520)




    def reset_click(self):
        self.uname.delete(0, END)
        self.hname.delete(0, END)
        self.add.delete(0, END)
        self.cont.delete(0, END)
        self.pw1.delete(0, END)
        self.conpw.delete(0, END)
        self.uname.insert(0, '')
        self.hname.insert(0, '')
        self.add.insert(0, '')
        self.cont.insert(0, '')
        self.pw1.insert(0, '')
        self.conpw.insert(0, '')

    def back_click(self):
        self.register.destroy()
        tk = Tk()
        Frontend.welcomepage.Welcome(tk)


    def add_click(self):
        username = self.uname.get()
        hostelname = self.hname.get()
        add = self.add.get()
        contact = self.cont.get()
        password = self.pw1.get()
        con_password = self.conpw.get()
        hostel_type = self.htype.get()


        if username == '' or hostelname == '' or add == '' or contact == '' or password == '' or con_password == '' or hostel_type == '':
            messagebox.showerror('Error', 'Please fill the empty field')
            return

        if password!= con_password:
            messagebox.showerror("Error", "Passwords do not match with each other")
            return

        if self.var_chk.get() == 0:
            messagebox.showerror("Error", "Please agree to the terms and condtions")
            return



        u = model.user.User(username, hostelname, add, contact, password)


        query = "insert into user_data(username,hostelname,address,contact, password) values(%s,%s,%s,%s,%s)"
        values=(u.get_username(),u.get_hostelname(),u.get_address(),u.get_contact(), u.get_password())

        self.db.insert(query,values)

        messagebox.showinfo('Success', 'User Registration successful')
        self.register.destroy()
        tk = Toplevel()
        Frontend.loginpage.Login_Page(tk)

# a = Tk()
# Register_Page(a)
# a.mainloop()



