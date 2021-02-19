from tkinter import *

class Welcome:
    def __init__(self, fpage):
        self.fpage = fpage
        self.fpage.geometry("700x500")


        self.frame1 = Frame(self.fpage)
        self.frame1.place(x=200, y=350, width=350, height=350)
        #quote1 = Label(self.frame1, text="'YOUR BANKING PROBLEMS, OUR SOLUTIONS!'", fg="blue").place(x=9, y=10)


        log1 = Label(self.frame1, text="Are you a new user?", font=("times new roman", 20), fg="blue").place(x=0, y=0)
        self.signupbtn = Button(self.fpage, text="Sign up", font=("times new roman", 14, "bold"), bd=5, bg="black",fg="white", relief=RAISED).place(x=450, y=240)


        '''self.frame2 = Frame(self.fpage)
        self.frame2.place(x=200, y=350, width=300, height=100)'''
        reg1 = Label(self.frame1, text="Already registered?", font=("times new roman", 20), fg="blue").place(x=5,y=20)
        self.signinbtn = Button(self.fpage, text="Log in", font=("times new roman", 14, "bold"), bd=5, bg="black", fg="white", relief=RAISED).place(x=453, y=357)


ab = Tk()
Welcome(ab)
ab.mainloop()