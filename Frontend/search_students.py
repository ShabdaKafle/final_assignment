from tkinter import *
from tkinter import messagebox
import Frontend.records
from tkinter import ttk
import Backend.dbconnection


class Search:
    def __init__(self, root, user_id=None, username=None, hostelname=None, address=None, contact=None):
        self.root = root
        self.user_id =user_id
        self.username = username
        self.hostelname = hostelname
        self.address = address
        self.contact = contact

        self.root.title("searching")
        self.root.geometry('1000x700')
        self.root.config(bg="white")

        global icon
        icon = PhotoImage(file=r"C:\Users\ACER\Desktop\New folder\back2.png")
        rec_icon = Label(self.root, image=icon)
        rec_icon.place(x=10, y=10)

        self.fa = Frame(self.root, bg="purple")
        self.fa.place(x=1, y=1, width=1000, height=100)

        btn_add = Button(self.fa, image=icon, command=self.btn_record)
        btn_add.place(x=15, y=15)

        self.selected = StringVar()
        optns = ["Id","Name"]
        self.selected.set("Select")

        self.search = Label(self.fa, text="Search by:", font=("arial 20 bold"), fg="navy", \
                    bg="purple").place(x=150, y=30)
        self.s = OptionMenu(self.fa, self.selected,*optns)
        self.s.place(x=300, y=38)
        self.name = Entry(self.fa, bd=5, relief=GROOVE, width=20, font=("arial 13 bold"))
        self.name.place(x=455, y=34)

        btn_search = Button(self.fa, text="Search", font=("arial", 16, "bold"), width=7, \
                            relief=GROOVE, bd=5, bg="steelblue", fg="white",command=self.serch)
        btn_search.place(x=660, y=25)

        self.fa1 = Frame(self.root, bg="white", bd=5, relief=GROOVE)
        self.fa1.place(x=1, y=100, width=1000, height=600)

        scroll_x = Scrollbar(self.fa1, orient=HORIZONTAL)
        scroll_y = Scrollbar(self.fa1, orient=VERTICAL)
        self.student_record = ttk.Treeview(self.fa1, columns=(
            "id", "name", "address", "contact", "profession", "parentsnum", "localnum", "roomnum", "roomtype"), \
                                      xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
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

        self.student_record['show'] = 'headings'

        self.student_record.column("id", width=60)
        self.student_record.column("roomnum", width=120)
        self.student_record.column("roomtype", width=120)

        self.student_record.pack(fill=BOTH, expand=1)

    def serch(self,item, index):

        item = self.name.get()
        if item == '':
            messagebox.showerror('Error', 'Please fill the search field')
            return

        option = self.selected.get()
        query = "select * from student_data where user_id={}".format(self.user_id)
        if option == "Id":
            index = 0
        elif option == "Name":
            index = 1
        self.db = Backend.dbconnection.DBConnect()
        record = self.db.select(query)
        for i in record:
            if (option == 'Name' and i[index] == item) or (option == 'Id' and i[index] == int(item)):
                item = i
                self.student_record.delete(*self.student_record.get_children())
                self.student_record.insert('', 'end', values=(item[0], item[1], item[2], item[3], item[4], item[6], item[8], item[9], item[10]))

            elif not item:
                print("User not found")
                messagebox.showerror("Error", "Not found!")


    def btn_record(self):
        self.root.destroy()
        tk = Tk()
        Frontend.records.Record(tk, self.user_id,self.username, self.hostelname, self.address, self.contact)

# an = Tk()
# Search(an)
# an.mainloop()
