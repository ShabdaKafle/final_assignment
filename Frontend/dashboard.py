from tkinter import *

class Dashboard:
    def __init__(self,root):
        self.root=root
        self.root.title('dashboard')
        self.root.geometry('400x400')

        lb=Label(self.root,text='welcome to dashboard',font=('arial',20,'bold'),fg='red')
        lb.pack(fill=X)