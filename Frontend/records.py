from tkinter import *
from tkinter import ttk
import Frontend.add_students
import Frontend.dashboard
import Frontend.profile
import Frontend.billing
import Frontend.search_students
import Backend.dbconnection
import Frontend.update_students
class Record:
    def __init__(self, root, username=None,hostelname=None, contact=None, address=None):
        self.db = Backend.dbconnection.DBConnect()
        self.root = root
        self.root.title("records")
        self.root.geometry('1050x700')
        self.root.config(bg="white")
        self.username = username
        self.hostelname = hostelname
        self.contact = contact
        self.address = address
        self.selected_index = -1
        btn_add = Button(self.root, text="Add", font=("arial", 16, "bold"),width=7, relief=GROOVE,\
                         bd=5,bg="steelblue", fg="white", command=self.add_btn)
        btn_add.place(x=380, y=10)


        btn_search = Button(self.root, text="Search", font=("arial", 16, "bold"), width=7,\
                            relief=GROOVE, bd=5,bg="steelblue", fg="white", command=self.btn_search)
        btn_search.place(x=500, y=10)


        btn_delete = Button(self.root, text="Delete", font=("arial", 16, "bold"), width=7, \
                            relief=GROOVE, bd=5, bg="steelblue", fg="white", command=self.btn_delete)
        btn_delete.place(x=860, y=10)


        btn_sort = Button(self.root, text="Sort", font=("arial", 16, "bold"), width=7, \
                            relief=GROOVE, bd=5, bg="steelblue", fg="white")
        btn_sort.place(x=740, y=10)

        btn_update = Button(self.root, text="Update", font=("arial", 16, "bold"), width=7, \
                          relief=GROOVE, bd=5, bg="steelblue", fg="white", command=self.update_btn)
        btn_update.place(x=620, y=10)



        global icon
        icon = PhotoImage(file=r"C:\Users\ACER\Desktop\New folder\rec_icon2.png")
        rec_icon = Label(self.root, image=icon)
        rec_icon.place(x=30, y=5)

        self.frame = Frame(self.root, bg="purple", bd=5, relief=FLAT)
        self.frame.place(x=1, y=70, width=200, height=430)

        btn_dash = Button(self.frame, text="Dashboard",font=("arial", 20, "bold"), width=9,\
                          relief=FLAT, bg="purple", fg="navy", command=self.btn_dash)
        btn_dash.place(x=20, y=30)

        global dash1
        dash1 = PhotoImage(file=r"C:\Users\ACER\Desktop\New folder\dashboard4.png")
        dash_icon = Label(self.frame, image=dash1)
        dash_icon.place(x=1, y=45)

        btn_bill = Button(self.frame, text="Billing", font=("arial", 20, "bold"), width=8,\
                          relief=FLAT, bg="purple", fg="navy", command=self.btn_bill)
        btn_bill.place(x=5, y=230)

        global bill1
        bill1 = PhotoImage(file=r"C:\Users\ACER\Desktop\New folder\billing6.png")
        bill_icon = Label(self.frame, image=bill1)
        bill_icon.place(x=1, y=245)


        btn_recn = Button(self.frame, text="Records", font=("arial", 20, "bold"),width=9,\
                          relief=FLAT, bg="purple", fg="navy")
        btn_recn.place(x=5, y=130)

        global rec1
        rec1 = PhotoImage(file=r"C:\Users\ACER\Desktop\New folder\record5.png")
        rec_icon = Label(self.frame, image=rec1)
        rec_icon.place(x=1, y=145)

        btn_prof = Button(self.frame, text="Profile", font=("arial", 20, "bold"),width=8,\
                          relief=FLAT, bg="purple", fg="navy", command=self.prof_btn)
        btn_prof.place(x=5, y=330)

        global prof1
        prof1 = PhotoImage(file=r"C:\Users\ACER\Desktop\New folder\profile7.png")
        prof_icon = Label(self.frame, image=prof1)
        prof_icon.place(x=1, y=345)


        self.fram = Frame(self.root, bg= "white", bd=5, relief=GROOVE)
        self.fram.place(x=230, y=70, width= 820, height=630)


        self.fr = Frame(self.fram, bg="purple")
        self.fr.place(x=1, y=1, width=806, height=40)

        quote1 = Label(self.fr, text="Student records", font=("arial 16 bold"), fg="royalblue", \
                       bg="purple").place(x=1, y=1)

        scroll_x=Scrollbar(self.fram, orient=HORIZONTAL)
        scroll_y=Scrollbar(self.fram, orient=VERTICAL)
        self.student_record = ttk.Treeview(self.fram, columns=("id", "name", "address", "contact", "profession","parentsnum", "localnum", "roomnum", "roomtype"),\
                                      xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        self.student_record.bind('<<TreeviewSelect>>', self.on_select)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_record.xview)
        scroll_y.config(command=self.student_record.yview)

        self.student_record.heading("id", text="ID")
        self.student_record.heading("name", text="Name")
        self.student_record.heading("address", text="Address")
        self.student_record.heading("contact", text="Contact")
        self.student_record.heading("profession", text="Profession")
        self.student_record.heading("parentsnum", text="Parents number")
        self.student_record.heading("localnum", text="Local guardians number")
        self.student_record.heading("roomnum", text="Room number")
        self.student_record.heading("roomtype", text="Room type")

        self.student_record['show']='headings'

        self.student_record.column("id",width=60)
        self.student_record.column("roomnum", width=120)
        self.student_record.column("roomtype", width=120)

        self.student_record.pack(fill=BOTH, expand=1)

        records = self.get_all_records()

        print(records)

    def get_all_records(self):
        query= "select * from student_data"
        values = None
        rows = self.db.select(query,values)
        print('rows information', rows)
        if len(rows) != 0:
            self.student_record.delete(*self.student_record.get_children())
            for row in rows:
                self.student_record.insert('', 'end', values=(row[0], row[1], row[2], row[3], row[4], row[6], row[8], row[9], row[10]))

    def add_btn(self):
        self.root.destroy()
        tk = Tk()
        Frontend.add_students.Add(tk, self.username, self.hostelname, self.address, self.contact)

    def update_btn(self):
        self.root.destroy()
        tk = Tk()
        Frontend.update_students.Update(tk, self.username, self.hostelname, self.address, self.contact)

    def btn_dash(self):
        self.root.destroy()
        tk = Tk()
        Frontend.dashboard.Dashboard(tk,self.username,self.hostelname, self.address, self.contact)

    def prof_btn(self):
        self.root.destroy()
        tk = Tk()
        Frontend.profile.Profile(tk, self.username, self.hostelname, self.address, self.contact)

    def btn_bill(self):
        self.root.destroy()
        tk = Tk()
        Frontend.billing.Billing(tk, self.username, self.hostelname, self.address, self.contact)

    def btn_search(self):
        self.root.destroy()
        tk = Tk()
        Frontend.search_students.Search(tk, self.username, self.hostelname, self.address, self.contact)

    def btn_delete(self):
        if(self.selected_index > 0):
            self.delete_record(self.selected_index)
            self.refresh_treeview()

    def on_select(self, event):
        curItem = self.student_record.focus()
        self.selected_index = self.student_record.item(curItem)['values'][0]

    def delete_record(self, id):
        query = 'delete from student_data where student_id=%d'
        self.db.cur.execute(query%id)
        self.db.con.commit()

    def refresh_treeview(self):
        self.student_record.delete(*self.student_record.get_children())
        self.get_all_records()

# bc = Tk()
# Record(bc)
# bc.mainloop()
