from tkinter import *
import Frontend.records
from tkinter import ttk
from tkinter import messagebox

import model.student
import Backend.dbconnection

class Add:
    def __init__(self, root):
        self.root = root
        self.root.title("Adding students")
        self.root.geometry("1050x700")
        self.root.config(bg="purple")

        self.db= Backend.dbconnection.DBConnect()

        global icon
        icon = PhotoImage(file=r"C:\Users\ACER\Desktop\New folder\back2.png")
        rec_icon = Label(self.root, image=icon)
        rec_icon.place(x=25, y=15)

        btn_add = Button(self.root, image=icon, command=self.btn_record)
        btn_add.place(x=25, y=15)

        self.fr1 = Frame(self.root, bg="white", bd=5, relief=GROOVE)
        self.fr1.place(x=20, y=90, width=550, height=480)

        quote1 = Label(self.fr1, text="Add Student records here", font=("arial 18 bold"), fg="royalblue", \
                       bg="white").place(x=1, y=10)

        self.name = Label(self.fr1, text="Name", font=("cambria 14 bold"),bg="white", fg="navy").place(x=10, y=70)
        self.nam = Entry(self.fr1, bd=5, relief=GROOVE, width=25, font=("arial 13 bold"))
        self.nam.place(x=105, y=70)

        self.address = Label(self.fr1, text="Address", font=("cambria 14 bold"),bg="white", fg="navy").place(x=10, y=120)
        self.add = Entry(self.fr1, bd=5, relief=GROOVE, width=25, font=("arial 13 bold"))
        self.add.place(x=105, y=120)

        self.contact = Label(self.fr1, text="Contact", font=("cambria 14 bold"),bg="white", fg="navy").place(x=10, y=170)
        self.cont = Entry(self.fr1, bd=5, relief=GROOVE, width=25, font=("arial 13 bold"))
        self.cont.place(x=105, y=170)

        self.profession = Label(self.fr1, text="Profession", font=("cambria 14 bold"),bg="white", fg="navy").place(x=10, y=220)
        self.prof = Entry(self.fr1, bd=5, relief=GROOVE, width=25, font=("arial 13 bold"))
        self.prof.place(x=120, y=220)

        self.parent = Label(self.fr1, text="Parent name", font=("cambria 14 bold"),bg="white", fg="navy").place(x=10, y=270)
        self.pname = Entry(self.fr1, bd=5, relief=GROOVE, width=25, font=("arial 13 bold"))
        self.pname.place(x=135, y=270)

        self.number = Label(self.fr1, text="Parent's contact", font=("cambria 14 bold"),bg="white", fg="navy").place(x=10, y=320)
        self.pnum = Entry(self.fr1, bd=5, relief=GROOVE, width=25, font=("arial 13 bold"))
        self.pnum.place(x=170, y=320)

        self.local = Label(self.fr1, text="Local Guardain", font=("cambria 14 bold"),bg="white", fg="navy").place(x=10, y=370)
        self.guardain = Entry(self.fr1, bd=5, relief=GROOVE, width=25, font=("arial 13 bold"))
        self.guardain.place(x=170, y=370)

        self.lnumber = Label(self.fr1, text="Local Guardain's number", font=("cambria 14 bold"),bg="white", fg="navy").place(x=10, y=420)
        self.guardain_num = Entry(self.fr1, bd=5, relief=GROOVE, width=25, font=("arial 13 bold"))
        self.guardain_num.place(x=250, y=420)

        self.fr2 = Frame(self.root, bg="white", bd=5, relief=GROOVE)
        self.fr2.place(x=600, y=90, width=430, height=480)

        quote2 = Label(self.fr2, text="Add room details here", font=("arial 18 bold"), fg="royalblue", \
                       bg="white").place(x=1, y=10)

        self.room = Label(self.fr2, text="Room number ", font=("cambria 14 bold"), bg="white", fg="navy").place(x=10, y=70)
        self.num = Entry(self.fr2, bd=5, relief=GROOVE, width=15, font=("arial 13 bold"))
        self.num.place(x=10, y=100)

        self.type = Label(self.fr2, text="Room type", font=("cambria 14 bold"), bg="white", fg="navy").place(x=10,y=150)
        self.rtype = ttk.Combobox(self.fr2, values=("2-seater", "3-seater", "4-seater"), state='readonly')
        self.rtype.place(x=10, y=180)

        self.partners = Label(self.fr2, text="Room partners", font=("cambria 14 bold"), bg="white", fg="navy").place(x=10,y=230)
        self.rpartners = Entry(self.fr2, bd=5, relief=GROOVE, width=20, font=("arial 10 bold"))
        self.rpartners.place(x=10, y=260)
        self.rpartner = Entry(self.fr2, bd=5, relief=GROOVE, width=20, font=("arial 10 bold"))
        self.rpartner.place(x=215, y=260)
        self.rpartner1 = Entry(self.fr2, bd=5, relief=GROOVE, width=20, font=("arial 10 bold"))
        self.rpartner1.place(x=10, y=310)

        self.fee = Label(self.fr2, text="Room fee", font=("cambria 14 bold"), bg="white", fg="navy").place(x=10, y=370)
        self.rfee = ttk.Combobox(self.fr2, values=("9000", "9500", "10000"), state='readonly')
        self.rfee.place(x=10, y=400)

        self.fr3 = Frame(self.root, bg="white", bd=5, relief=GROOVE)
        self.fr3.place(x=250, y=600, width=500, height=70)

        btn_save = Button(self.fr3, text="Save", font=("arial", 16, "bold"), width=12, relief=GROOVE, \
                                 bd=5, bg="steelblue", fg="white", command=self.save_btn)
        btn_save.place(x=50, y=5)

        btn_clear = Button(self.fr3, text="Clear", font=("arial", 16, "bold"), width=12, \
                                    relief=GROOVE, bd=5, bg="steelblue", fg="white", command= self.clear_btn)
        btn_clear.place(x=270, y=5)


    def save_btn(self):
        name = self.nam.get()
        address = self.add.get()
        contact = self.cont.get()
        profession = self.prof.get()
        parents_name = self.pname.get()
        parents_number = self.pnum.get()
        local_guardain = self.guardain.get()
        local_guardain_number = self.guardain_num.get()
        room_number = self.num.get()
        room_type = self.rtype.get()
        room_partner1 = self.rpartners.get()
        room_partner2 = self.rpartner.get()
        room_partner3 = self.rpartner1.get()
        total_fee = self.rfee.get()

        if name == '' or address == '' or contact == '' or profession == '' or parents_name == '' or parents_number == '' or local_guardain ==''\
                or local_guardain_number == '' or room_number == '' or room_type == ''\
                or room_partner1 == '' or room_partner2 == '' or room_partner3 == '' or total_fee == '':
                    messagebox.showerror('Error', 'Please fill the empty field')
                    return

        u = model.student.Student(name, address, contact, profession, parents_name, parents_number, local_guardain, local_guardain_number, \
                                  room_number, room_type, room_partner1, room_partner2, room_partner3, total_fee)

        query = "insert into student_data(name, address, contact, profession, parents_name, parents_number, local_guardain, local_guardain_number, \
        room_number, room_type, 1st_room_partner, 2nd_room_partner, 3rd_room_partner, room_fee) \
        values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        values = (u.get_name(), u.get_address(), u.get_contact(), u.get_profession(), u.get_parents_name(), \
                  u.get_parents_number(), u.get_local_guardain(), u.get_number(),u.get_room_number(),\
                  u.get_room_type(), u.get_room_partners(), u.get_room_partner(), u.get_room_partner1(),u.get_fee())


        self.db.insert(query, values)

        messagebox.showinfo('Success', 'Data saved sucessfully!')
        self.clear_btn()


    def clear_btn(self):
        self.nam.delete(0, END)
        self.add.delete(0, END)
        self.cont.delete(0, END)
        self.prof.delete(0, END)
        self.pname.delete(0, END)
        self.pnum.delete(0, END)
        self.guardain.delete(0, END)
        self.guardain_num.delete(0, END)
        self.num.delete(0, END)
        self.rpartners.delete(0, END)
        self.rpartner.delete(0, END)
        self.rpartner1.delete(0, END)


        self.nam.insert(0, '')
        self.add.insert(0, '')
        self.cont.insert(0, '')
        self.prof.insert(0, '')
        self.pname.insert(0, '')
        self.pnum.insert(0, '')
        self.guardain.insert(0, '')
        self.guardain_num.insert(0, '')
        self.num.insert(0, '')
        self.rtype.set('')
        self.rpartners.insert(0, '')
        self.rpartner.insert(0, '')
        self.rpartner1.insert(0, '')
        self.rfee.set('')



    def btn_record(self):
        self.root.destroy()
        tk = Tk()
        Frontend.records.Record(tk)




# n = Tk()
# Add(n)
# n.mainloop()




