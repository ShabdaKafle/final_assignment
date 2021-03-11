class User:
    def __init__(self, uname=None,hname=None,add=None,cont=None, passw=None):
        self.__username = uname
        self.__hostelname = hname
        self.__address = add
        self.__contact = cont
        self.__password = passw


    def set_username(self,uname):
        self.__username= uname
    def get_username(self):
        return self.__username

    def set_hostelname(self,hname):
        self.__hostelname = hname
    def get_hostelname(self):
        return self.__hostelname

    def set_address(self, add):
        self.__address = add
    def get_address(self):
        return self.__address

    def set_contact(self, cont):
        self.__contact = cont
    def get_contact(self):
        return self.__contact

    def set_password(self,passw):
        self.__password = passw
    def get_password(self):
        return self.__password

