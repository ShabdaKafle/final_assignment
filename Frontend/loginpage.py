from tkinter import *
from tkinter import messagebox
import Frontend.registerpage
import Backend.dbconnection
import Frontend.dashboard
import Frontend.profile

class Login_Page:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Page")
        self.root.geometry("800x450")

        self.db = Backend.dbconnection.DBConnect()

        self.root.config(bg="purple")


        self.F1 = Frame(self.root, bd=10, relief=RAISED)
        self.F1.place(x=184, y=44, width=400, height=350)


        self.title = Label(self.F1, text="Login to your account", font=("times new roman", 25, "bold"), fg="steelblue").place(x=14, y=10)


        self.lbusername = Label(self.F1, text="Username", font=("times new roman", 15, "bold")).place(x=10, y=95)
        self.txuser = Entry(self.F1, bd=5, relief=SUNKEN, width=25, font=("arial 13 bold"))
        self.txuser.place(x=110, y=95)

        self.lbpass = Label(self.F1, text="Password", font=("times new roman", 15, "bold")).place(x=10, y=170)
        self.txpass = Entry(self.F1, bd=5, relief=SUNKEN, width=25, font=("arial 13 bold"), show='*')
        self.txpass.place(x=110, y=170)

        btn_login = Button(self.F1, text="Login",font=('arial',16, 'bold'), bd=3,bg="steelblue",fg="white",\
                           command=self.btn_login_click)
        btn_login.place(x=100, y=250)

        btn_reset = Button(self.F1, text="Reset", font=('arial', 16, 'bold'), bd=3,bg="steelblue",\
                           fg="white", command=self.btn_reset_click)
        btn_reset.place(x=200, y=250)



        '''lbl_signup = Label(self.root, text='Create a new user.', fg='green', font=('arial', 16, 'italic'))
        lbl_signup.place(x=130, y=260)
        lbl_signup.bind('<Button-1>', self.lbl_signup_click)'''

    def btn_reset_click(self):
        self.txuser.delete(0, END)
        self.txuser.insert(0, "")

        self.txpass.delete(0, END)
        self.txpass.insert(0, "")


    def btn_login_click(self):
        uname = self.txuser.get()
        passw = self.txpass.get()

        if uname == '' or passw == '':
            messagebox.showerror('Error', 'Please fill the empty field')
        else:
            query = "select * from user_data where username=%s and password=%s"
            values = (uname, passw)
            rows = self.db.select(query, values)

            data = []

            if len(rows)!=0:
                for row in rows:
                    data.append(row[1])
                    data.append(row[5])
                print(data)
                if uname == data[0] and passw == data[1]:
                    self.btn_reset_click()
                    messagebox.showinfo('Success', 'Congratulations!! login successful')
                    query="select hostelname, address, contact from user_data where username=%s"
                    values=(data[0],)
                    row=self.db.select(query,values)
                    print(row)
                    self.root.destroy()
                    tk = Tk()
                    Frontend.dashboard.Dashboard(tk,data[0],row[0][0], row[0][1], row[0][2])



                else:
                    messagebox.showerror('Error', 'Invalid username and password')
            else:
                    messagebox.showinfo("Error", "User not registered !! Register first")


# wn = Tk()
# Login_Page(wn)
# wn.mainloop()