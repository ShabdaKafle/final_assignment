from tkinter import *
import Frontend.loginpage
import Frontend.registerpage

class Welcome:
    def __init__(self, fpage):
        self.fpage = fpage
        self.fpage.title("Main page")
        self.fpage.geometry("900x500")
        self.fpage.config(bg="black")

        self.frame1 = Frame(self.fpage, bg= "black")
        self.frame1.place(x=1, y=1, width=900, height=60)
        quote1 = Label(self.frame1, text="'Welcome To Hostel Billing System'", font=("arial 20 bold"), fg="blue", bg="black").place(x=200, y=10)




        # making a signin button
        self.frame2 = Frame(self.fpage, bg ="black")
        self.frame2.place(x=200, y=150, width=300, height=280)

        reg1 = Label(self.frame2, text="Already registered?", font=("times new roman", 20, "bold"), fg="green", bg="black").place(x=14,y=215)
        log1 = Label(self.frame2, text="Are you a new User?", font=("times new roman", 20, "bold"), fg="green",bg="black").place(x=3, y=120)

        self.signinbtn = Button(self.fpage, text="Log in", font=("times new roman", 14, "bold"), bd=5, bg="dark red",
                                fg="white", relief=RAISED, command=self.btn_signin).place(x=453, y=357)
        self.signupbtn = Button(self.fpage, text="Sign up", font=("times new roman", 14, "bold"), bd=5, bg="dark red",
                           fg="white", relief=RAISED, command=self.btn_signup).place(x=453, y=260)


    def btn_signin(self):
        tk = Toplevel()
        Frontend.loginpage.Login_Page(tk)

    def btn_signup(self):
        tk = Toplevel()
        Frontend.registerpage.Register_Page(tk)

'''ab = Tk()
Welcome(ab)
ab.mainloop()'''