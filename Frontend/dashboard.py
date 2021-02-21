from tkinter import *
from PIL import Image, ImageTk


class Dashboard:
    def __init__(self,root):
        self.root=root
        self.root.title('dashboard')
        self.root.geometry('750x550')
        self.root.config(bg="white")

        '''lb=Label(self.root,text='Welcome to dashboard',font=('arial',20,'bold'),fg='white', bg=
                 "purple")
        lb.pack(fill=X)'''

        self.F1 = Frame(self.root)
        self.F1.place(x=1, y=1, width=750, height=150)
        self.F1.config(bg="purple")

        '''btn_logout = Button(self.F1, text="Logout", justify="center", font=("times new roman", 20, "bold"), bg="white",\
                             fg="brown", bd=5, relief=GROOVE).place(x=510, y=10, width=150)'''

        lb1 = Label(self.F1, text = "Welcome username",font=('arial',20,'bold'),fg='black', bg=\
                 "purple").place(x=50, y=5)
        lb2 = Label(self.F1, text="Hostelname", font=('arial', 15, 'bold'), fg='black', bg=\
        "purple").place(x=50, y=40)


        self.F2 = Frame(self.root,bd=5, relief=GROOVE)
        self.F2.place(x=1, y=190, width=750, height=360)
        self.F2.config(bg="white")
        btn_logout = Button(self.F2, text="Logout", justify="center", font=("times new roman", 16, "bold"), bg="white", \
                            fg="blue", bd=5, relief=GROOVE).place(x=590, y=290, width=120)

        global dashboard
        dashboard = PhotoImage(file="dash.png")
        dash = Label(self.F2, image = dashboard)
        dash.place(x=190, y=20)

        global billing
        billing = PhotoImage(file="bill.png")
        bill = Label(self.F2, image=billing)
        bill.place(x=190, y=160)

        global records
        records = PhotoImage(file="record.png")
        rec = Label(self.F2, image=records)
        rec.place(x=370, y=20)

        global profile
        profile = PhotoImage(file="profile.png")
        prof = Label(self.F2, image=profile)
        prof.place(x= 370, y=160)

        btn_dash = Button(self.F2, image = dashboard, relief=RAISED, bd=3)
        btn_dash.place(x=190, y=20)

        btn_bill = Button(self.F2, image=billing, relief=RAISED, bd=3)
        btn_bill.place(x=190, y=160)

        btn_recn = Button(self.F2, image=records, relief=RAISED, bd=3)
        btn_recn.place(x=370, y=20)

        btn_prof = Button(self.F2, image=profile, relief=RAISED, bd=3)
        btn_prof.place(x= 370, y=160)


a = Tk()
Dashboard(a)
a.mainloop()
        