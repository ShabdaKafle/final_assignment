from tkinter import *
from PIL import Image, ImageTk
import Frontend.records
import Frontend.profile
import Frontend.billing


class Dashboard:
    def __init__(self,root,username=None,hostelname=None):
        self.root=root
        self.username=username
        self.hostelname=hostelname

        self.root.title('dashboard')
        self.root.geometry('750x550')
        self.root.config(bg="white")


        self.F1 = Frame(self.root)
        self.F1.place(x=1, y=1, width=750, height=150)
        self.F1.config(bg="purple")


        # lb1 = Label(self.F1, text = "Welcome"+self.username,font=('arial',20,'bold'),fg='black', bg=\
        #          "purple").place(x=50, y=5)
        # lb2 = Label(self.F1, text=self.hostelname, font=('arial', 15, 'bold'), fg='black', bg=\
        # "purple").place(x=50, y=40)


        self.F2 = Frame(self.root,bd=5, relief=GROOVE)
        self.F2.place(x=1, y=150, width=750, height=400)
        self.F2.config(bg="white")
        btn_logout = Button(self.F2, text="Logout", justify="center", font=("times new roman", 16, "bold"), bg="purple", \
                            fg="white", bd=5, relief=RAISED).place(x=600, y=330, width=120)

        global dashboard
        dashboard = PhotoImage(file=r"C:\Users\ACER\Desktop\New folder\dash5.png")
        dash = Label(self.F2, image = dashboard)
        dash.place(x=190, y=20)

        global billing
        billing = PhotoImage(file=r"C:\Users\ACER\Desktop\New folder\bill3.png")
        bill = Label(self.F2, image=billing)
        bill.place(x=190, y=180)

        global records
        records = PhotoImage(file=r"C:\Users\ACER\Desktop\New folder\record4.png")
        rec = Label(self.F2, image=records)
        rec.place(x=370, y=20)

        global profile
        profile = PhotoImage(file=r"C:\Users\ACER\Desktop\New folder\profile1.png")
        prof = Label(self.F2, image=profile)
        prof.place(x= 370, y=180)

        btn_dash = Button(self.F2, image = dashboard, relief=RAISED, bd=9)
        btn_dash.place(x=190, y=20)

        btn_bill = Button(self.F2, image=billing, relief=RAISED, bd=9, command=self.btn_bill)
        btn_bill.place(x=190, y=180)

        btn_recn = Button(self.F2, image=records, relief=RAISED, bd=9, command=self.rec_btn)
        btn_recn.place(x=370, y=20)

        btn_prof = Button(self.F2, image=profile, relief=RAISED, bd=9,command=self.prof_btn)
        btn_prof.place(x= 370, y=180)

    def rec_btn(self):
        self.root.destroy()
        tk = Tk()
        Frontend.records.Record(tk)

    def prof_btn(self):
        self.root.destroy()
        tk = Tk()
        Frontend.profile.Profile(tk)

    def btn_bill(self):
        self.root.destroy()
        tk = Tk()
        Frontend.billing.Billing(tk)





# ac = Tk()
# Dashboard(ac)
# ac.mainloop()
        