from tkinter import *

class Record:
    def __init__(self, root):
        self.root = root
        self.root.title("records")
        self.root.geometry('850x500')
        self.root.config(bg="white")

        btn_add = Button(self.root, text="Add", font=("arial", 16, "bold"),width=7, relief=GROOVE,\
                         bd=5,bg="steelblue", fg="white")
        btn_add.place(x=620, y=10)

        btn_search = Button(self.root, text="Search", font=("arial", 16, "bold"), width=7,\
                            relief=GROOVE, bd=5,bg="steelblue", fg="white")
        btn_search.place(x=740, y=10)

        global icon
        icon = PhotoImage(file=r"record_icon.png")
        rec_icon = Label(self.root, image=icon)
        rec_icon.place(x=30, y=5)

        self.frame = Frame(self.root, bg="purple", bd=5, relief=FLAT)
        self.frame.place(x=1, y=70, width=200, height=430)

        btn_dash = Button(self.frame, text="Dashboard",font=("arial", 20, "bold"), width=9,\
                          relief=FLAT, bg="purple", fg="navy")
        btn_dash.place(x=20, y=30)

        global dash1
        dash1 = PhotoImage(file=r"dashboard4.png")
        dash_icon = Label(self.frame, image=dash1)
        dash_icon.place(x=1, y=45)

        btn_bill = Button(self.frame, text="Billing", font=("arial", 20, "bold"), width=8,\
                          relief=FLAT, bg="purple", fg="navy")
        btn_bill.place(x=5, y=230)

        global bill1
        bill1 = PhotoImage(file=r"billing6.png")
        bill_icon = Label(self.frame, image=bill1)
        bill_icon.place(x=1, y=245)


        btn_recn = Button(self.frame, text="Records", font=("arial", 20, "bold"),width=9,\
                          relief=FLAT, bg="purple", fg="navy")
        btn_recn.place(x=5, y=130)

        global rec1
        rec1 = PhotoImage(file=r"record5.png")
        rec_icon = Label(self.frame, image=rec1)
        rec_icon.place(x=1, y=145)

        btn_prof = Button(self.frame, text="Profile", font=("arial", 20, "bold"),width=8,\
                          relief=FLAT, bg="purple", fg="navy")
        btn_prof.place(x=5, y=330)

        global prof1
        prof1 = PhotoImage(file=r"profile7.png")
        prof_icon = Label(self.frame, image=prof1)
        prof_icon.place(x=1, y=345)


        self.fram = Frame(self.root, bg= "white", bd=5, relief=GROOVE)
        self.fram.place(x=230, y=70, width= 620, height=430)


        self.fr = Frame(self.fram, bg="purple")
        self.fr.place(x=1, y=1, width=608, height=40)

        quote1 = Label(self.fr, text="Student records", font=("arial 16 bold"), fg="royalblue", \
                       bg="purple").place(x=1, y=1)



'''bc = Tk()
Record(bc)
bc.mainloop()'''
