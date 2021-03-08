from tkinter import *

import Frontend.dashboard
import Frontend.records
import Frontend.billing
import model.user
import Backend.dbconnection

class Profile:
    def __init__(self, root):
        self.root = root
        self.root.title("profile")
        self.root.geometry('700x430')
        self.root.config(bg="white")

        self.db = Backend.dbconnection.DBConnect()



        self.fr = Frame(self.root, bg="purple", bd=5, relief=FLAT)
        self.fr.place(x=1, y=1, width=200, height=430)

        btn_dash = Button(self.fr, text="Dashboard", font=("arial", 20, "bold"), width=9, \
                          relief=FLAT, bg="purple", fg="navy", command=self.btn_dash)
        btn_dash.place(x=20, y=30)

        global dash2
        dash2 = PhotoImage(file=r"C:\Users\ACER\Desktop\New folder\dashboard4.png")
        dash_icon = Label(self.fr, image=dash2)
        dash_icon.place(x=1, y=45)

        btn_bill = Button(self.fr, text="Billing", font=("arial", 20, "bold"), width=8, \
                          relief=FLAT, bg="purple", fg="navy", command=self.btn_bill)
        btn_bill.place(x=5, y=230)

        global bill2
        bill2 = PhotoImage(file=r"C:\Users\ACER\Desktop\New folder\billing6.png")
        bill_icon = Label(self.fr, image=bill2)
        bill_icon.place(x=1, y=245)

        btn_recn = Button(self.fr, text="Records", font=("arial", 20, "bold"), width=9, \
                          relief=FLAT, bg="purple", fg="navy", command=self.rec_btn)
        btn_recn.place(x=5, y=130)

        global rec2
        rec2 = PhotoImage(file=r"C:\Users\ACER\Desktop\New folder\record5.png")
        rec_icon = Label(self.fr, image=rec2)
        rec_icon.place(x=1, y=145)

        btn_prof = Button(self.fr, text="Profile", font=("arial", 20, "bold"), width=8, \
                          relief=FLAT, bg="purple", fg="navy")
        btn_prof.place(x=5, y=330)

        global prof2
        prof2 = PhotoImage(file=r"C:\Users\ACER\Desktop\New folder\profile7.png")
        prof_icon = Label(self.fr, image=prof2)
        prof_icon.place(x=1, y=345)

        self.fra = Frame(self.root, bg="white", bd=5, relief=GROOVE)
        self.fra.place(x=200, y=1, width=500, height=430)

        quote = Label(self.fra, text="About the user", font=("arial 18 bold"), fg="royalblue", \
                    bg="white").place(x=120, y=40)

        global prof
        prof = PhotoImage(file=r"C:\Users\ACER\Desktop\New folder\profile.png")
        rec_icon = Label(self.root, image=prof)
        rec_icon.place(x=210, y=10)

        self.name = Label(self.fra, text="Name", font=("cambria 20 bold"), bg="white", fg="navy").place(x=10, y=125)

        self.contact = Label(self.fra, text="Contact", font=("cambria 20 bold"), bg="white", fg="navy").place(x=10,y=185)

        self.hostel = Label(self.fra, text="Hostel name", font=("cambria 20 bold"), bg="white", fg="navy").place(x=10,y=245)

        self.address = Label(self.fra, text="Address", font=("cambria 20 bold"), bg="white", fg="navy").place(x=10, y=305)


    # def profile_details(self):
    #     query = "select username, hostelname, address, contact from user_data where username = '%s'"
    #     values = ('', '', '', '')
    #
    #     rows = self.db.select(query, values)
    #     Label(self.root, text=rows[1], font=("times new roman", 20, "bold"), bg="white", fg="navy").place(x=100, y=125)

    def btn_dash(self):
        self.root.destroy()
        tk = Tk()
        Frontend.dashboard.Dashboard(tk)

    def rec_btn(self):
        self.root.destroy()
        tk = Tk()
        Frontend.records.Record(tk)

    def btn_bill(self):
        self.root.destroy()
        tk = Tk()
        Frontend.billing.Billing(tk)


# ag = Tk()
# Profile(ag)
# ag.mainloop()