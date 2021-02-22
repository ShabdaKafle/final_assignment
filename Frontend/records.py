from tkinter import *

class Record:
    def __init__(self, root):
        self.root = root
        self.root.title("records")
        self.root.geometry('750x550')
        self.root.config(bg="white")


        self.frame = Frame(self.root, bg="purple", bd=5, relief=FLAT)
        self.frame.place(x=1, y=70, width=200, height=480)

        self.fram = Frame(self.root, bg= "white", bd=5, relief=GROOVE)
        self.fram.place(x=230, y=70, width= 520, height=480)

        self.fr = Frame(self.fram, bg="purple")
        self.fr.place(x=1, y=1, width=508, height=40)

        quote1 = Label(self.fr, text="Student records", font=("arial 15 bold"), fg="steelblue", \
                       bg="purple").place(x=1, y=1)



bc = Tk()
Record(bc)
bc.mainloop()
