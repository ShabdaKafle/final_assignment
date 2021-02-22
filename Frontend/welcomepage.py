from tkinter import *
import Frontend.loginpage
import Frontend.registerpage
from PIL import Image, ImageTk

class Welcome:
    def __init__(self, fpage):
        self.fpage = fpage
        self.fpage.title("Main page")
        self.fpage.geometry("800x500")
        self.fpage.config(bg="white")

        self.frame1 = Frame(self.fpage, bg= "purple")
        self.frame1.place(x=1, y=1, width=800, height=60)
        quote1 = Label(self.frame1, text="Welcome To Hostel Billing System", font=("arial 20 bold"), fg="steelblue",\
                       bg="purple").place(x=160, y=10)


        self.frame2 = Frame(self.fpage,bg="purple", bd= 5, relief=GROOVE)
        self.frame2.place(x=1, y=70, width=350, height=430)

        global hostel
        hostel = PhotoImage(file="hostel1.png")
        das = Label(self.frame2, image=hostel)
        das.place(x=60, y=90)

        quote2 = Label(self.frame2, text="Feels like second home", font=("arial 15 bold"), fg="steelblue", \
                       bg="purple").place(x=50, y=300)

        self.frame3 = Frame(self.fpage, bg="white", bd=5, relief=GROOVE)
        self.frame3.place(x=355, y=70, width=445, height=430)

        reg1 = Label(self.frame3, text="Already registered?", font=("arial", 18, "bold"), fg="darkblue",\
                     bg="white").place(x=14, y=235)
        log1 = Label(self.frame3, text="Are you a new User?", font=("arial", 18, "bold"), fg="darkblue",\
                     bg="white").place(x=14, y=140)

        self.signinbtn = Button(self.frame3, text="Log in", font=("times new roman", 14, "bold"), bd=5, bg="purple", \
                                fg="white", relief=RAISED, command=self.btn_signin).place(x=270, y=230)
        self.signupbtn = Button(self.frame3, text="Sign up", font=("times new roman", 14, "bold"), bd=5, bg="purple", \
                                fg="white", relief=RAISED, command=self.btn_signup).place(x=270, y=135)

    def btn_signin(self):
        tk = Toplevel()
        Frontend.loginpage.Login_Page(tk)

    def btn_signup(self):
        tk = Toplevel()
        Frontend.registerpage.Register_Page(tk)

'''ab = Tk()
Welcome(ab)
ab.mainloop()'''