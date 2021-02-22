from tkinter import *
from PIL import Image, ImageTk


class Dashboard:
    def __init__(self,root):
        self.root=root
        self.root.title('dashboard')
        self.root.geometry('750x550')
        self.root.config(bg="white")


        self.F1 = Frame(self.root)
        self.F1.place(x=1, y=1, width=750, height=150)
        self.F1.config(bg="purple")


        lb1 = Label(self.F1, text = "Welcome username",font=('arial',20,'bold'),fg='black', bg=\
                 "purple").place(x=50, y=5)
        lb2 = Label(self.F1, text="Hostelname", font=('arial', 15, 'bold'), fg='black', bg=\
        "purple").place(x=50, y=40)


        self.F2 = Frame(self.root,bd=5, relief=GROOVE)
        self.F2.place(x=1, y=150, width=750, height=400)
        self.F2.config(bg="white")
        btn_logout = Button(self.F2, text="Logout", justify="center", font=("times new roman", 16, "bold"), bg="purple", \
                            fg="white", bd=5, relief=RAISED).place(x=600, y=330, width=120)

        global dashboard
        dashboard = PhotoImage(file=r"dash.png")
        dash = Label(self.F2, image = dashboard)
        dash.place(x=190, y=20)

        global billing
        billing = PhotoImage(file=r"bill.png")
        bill = Label(self.F2, image=billing)
        bill.place(x=190, y=180)

        global records
        records = PhotoImage(file=r"record.png")
        rec = Label(self.F2, image=records)
        rec.place(x=370, y=20)

        global profile
        profile = PhotoImage(file=r"profile.png")
        prof = Label(self.F2, image=profile)
        prof.place(x= 370, y=180)

        btn_dash = Button(self.F2, image = dashboard, relief=RAISED, bd=9)
        btn_dash.place(x=190, y=20)

        btn_bill = Button(self.F2, image=billing, relief=RAISED, bd=9)
        btn_bill.place(x=190, y=180)

        btn_recn = Button(self.F2, image=records, relief=RAISED, bd=9)
        btn_recn.place(x=370, y=20)

        btn_prof = Button(self.F2, image=profile, relief=RAISED, bd=9)
        btn_prof.place(x= 370, y=180)

'''ac = Tk()
Dashboard(ac)
ac.mainloop()'''
        