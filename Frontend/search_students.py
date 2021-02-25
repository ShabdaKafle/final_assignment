from tkinter import *
import Frontend.records
from tkinter import ttk

class Search:
    def __init__(self, root):
        self.root = root
        self.root.title("searching")
        self.root.geometry('800x500')
        self.root.config(bg="white")

        global icon
        icon = PhotoImage(file=r"C:\Users\ACER\Desktop\New folder\back2.png")
        rec_icon = Label(self.root, image=icon)
        rec_icon.place(x=10, y=10)

        self.fa = Frame(self.root, bg="purple")
        self.fa.place(x=1, y=1, width=800, height=100)

        btn_add = Button(self.fa, image=icon, command=self.btn_record)
        btn_add.place(x=15, y=15)

        self.search = Label(self.fa, text="Search by:", font=("arial 20 bold"), fg="navy", \
                    bg="purple").place(x=150, y=30)
        self.s = ttk.Combobox(self.fa, values=("ID", "Name"), state='readonly')
        self.s.place(x=300, y=38)

        self.name = Entry(self.fa, bd=5, relief=GROOVE, width=20, font=("arial 13 bold"))
        self.name.place(x=455, y=34)

        btn_search = Button(self.fa, text="Search", font=("arial", 16, "bold"), width=7, \
                            relief=GROOVE, bd=5, bg="steelblue", fg="white")
        btn_search.place(x=660, y=25)

        self.fa1 = Frame(self.root, bg="white", bd=5, relief=GROOVE)
        self.fa1.place(x=1, y=100, width=800, height=400)





    def btn_record(self):
        self.root.destroy()
        tk = Tk()
        Frontend.records.Record(tk)

# an = Tk()
# Search(an)
# an.mainloop()
