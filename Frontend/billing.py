from tkinter import *
from tkinter import ttk
import Frontend.dashboard
import Frontend.records
import Frontend.profile

class Billing:
    def __init__(self, root):
        self.root = root
        self.root.title("billing")
        self.root.geometry('1050x600')
        self.root.config(bg="white")

        self.frame = Frame(self.root, bg="purple", bd=5, relief=FLAT)
        self.frame.place(x=1, y=1, width=200, height=600)

        btn_dash = Button(self.frame, text="Dashboard", font=("arial", 20, "bold"), width=9, \
                          relief=FLAT, bg="purple", fg="navy", command=self.btn_dash)
        btn_dash.place(x=20, y=30)

        global dash3
        dash3 = PhotoImage(file=r"C:\Users\ACER\Desktop\New folder\dashboard4.png")
        dash_icon = Label(self.frame, image=dash3)
        dash_icon.place(x=1, y=45)

        btn_bill = Button(self.frame, text="Billing", font=("arial", 20, "bold"), width=8, \
                          relief=FLAT, bg="purple", fg="navy")
        btn_bill.place(x=5, y=230)

        global bill3
        bill3 = PhotoImage(file=r"C:\Users\ACER\Desktop\New folder\billing6.png")
        bill_icon = Label(self.frame, image=bill3)
        bill_icon.place(x=1, y=245)

        btn_recn = Button(self.frame, text="Records", font=("arial", 20, "bold"), width=9, \
                          relief=FLAT, bg="purple", fg="navy",command=self.rec_btn)
        btn_recn.place(x=5, y=130)

        global rec3
        rec3 = PhotoImage(file=r"C:\Users\ACER\Desktop\New folder\record5.png")
        rec_icon = Label(self.frame, image=rec3)
        rec_icon.place(x=1, y=145)

        btn_prof = Button(self.frame, text="Profile", font=("arial", 20, "bold"), width=8, \
                          relief=FLAT, bg="purple", fg="navy", command=self.prof_btn)
        btn_prof.place(x=5, y=330)

        global prof3
        prof3 = PhotoImage(file=r"C:\Users\ACER\Desktop\New folder\profile7.png")
        prof_icon = Label(self.frame, image=prof3)
        prof_icon.place(x=1, y=345)


        self.f1 = Frame(self.root, bg="white", bd=5, relief=GROOVE)
        self.f1.place(x=200, y=1, width=450, height=600)

        quote2 = Label(self.f1, text="Billing details", font=("arial 18 bold"), fg="royalblue", \
                       bg="white").place(x=5, y=10)


        self.bill = Label(self.f1, text="Bill number", font=("cambria 14 bold"), bg="white", fg="navy").place(x=10,y=70)
        self.num = Entry(self.f1, bd=5, relief=GROOVE, width=25, font=("arial 13 bold"))
        self.num.place(x=130, y=70)

        self.date = Label(self.f1, text="Date", font=("cambria 14 bold"), bg="white", fg="navy").place(x=10,y=130)
        self.da = Entry(self.f1, bd=5, relief=GROOVE, width=25, font=("arial 13 bold"))
        self.da.place(x=130, y=130)

        self.name = Label(self.f1, text="Name", font=("cambria 14 bold"), bg="white", fg="navy").place(x=10, y=190)
        self.nm = Entry(self.f1, bd=5, relief=GROOVE, width=25, font=("arial 13 bold"))
        self.nm.place(x=130, y=190)

        self.type = Label(self.f1, text="Room type", font=("cambria 14 bold"), bg="white", fg="navy").place(x=10,y=250)
        self.rtype = ttk.Combobox(self.f1, values=("2-seater", "3-seater", "4-seater"), state='readonly')
        self.rtype.place(x=130, y=255)

        self.month = Label(self.f1, text="For month of", font=("cambria 14 bold"), bg="white", fg="navy").place(x=10, y=310)
        self.mn = Entry(self.f1, bd=5, relief=GROOVE, width=25, font=("arial 13 bold"))
        self.mn.place(x=130, y=310)

        self.total = Label(self.f1, text="Total", font=("cambria 14 bold"), bg="white", fg="navy").place(x=10, y=370)
        self.fee = Entry(self.f1, bd=5, relief=GROOVE, width=25, font=("arial 13 bold"))
        self.fee.place(x=130, y=370)

        btn_bills = Button(self.f1, text="Generate Bill", font=("arial", 16, "bold"), width=12, relief=GROOVE, \
                         bd=5, bg="steelblue", fg="white")
        btn_bills.place(x=50, y=470)

        btn_clear = Button(self.f1, text="Clear", font=("arial", 16, "bold"), width=7, \
                            relief=GROOVE, bd=5, bg="steelblue", fg="white")
        btn_clear.place(x=240, y=470)

        self.frame1 = Frame(self.root, bg="white", bd=5, relief=GROOVE)
        self.frame1.place(x=650, y=1, width=400, height=600)

        







    def btn_dash(self):
        self.root.destroy()
        tk = Tk()
        Frontend.dashboard.Dashboard(tk)

    def prof_btn(self):
        self.root.destroy()
        tk = Tk()
        Frontend.profile.Profile(tk)

    def rec_btn(self):
        self.root.destroy()
        tk = Tk()
        Frontend.records.Record(tk)


at = Tk()
Billing(at)
at.mainloop()