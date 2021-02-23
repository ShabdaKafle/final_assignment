from tkinter import *
import Frontend.dashboard
import Frontend.records
import Frontend.profile

class Billing:
    def __init__(self, root):
        self.root = root
        self.root.title("billing")
        self.root.geometry('850x500')
        self.root.config(bg="white")



        self.frame = Frame(self.root, bg="purple", bd=5, relief=FLAT)
        self.frame.place(x=1, y=70, width=200, height=430)

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
                          relief=FLAT, bg="purple", fg="navy")
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


# at = Tk()
# Billing(at)
# at.mainloop()