class Student:
    def __init__(self, nam, add, cont, prof, pname, pnum, guardain, num, rnum, rtype, rfee,rpartners=None, rpartner=None, rpartner1=None ):
        self.__name = nam
        self.__address = add
        self.__contact = cont
        self.__profession = prof
        self.__parents_name =  pname
        self.__parents_number = pnum
        self.__local_guardain = guardain
        self.__number = num
        self.__room_number = rnum
        self.__room_type = rtype
        self.__room_partners = rpartners
        self.__room_partner = rpartner
        self.__room_partner1 = rpartner1
        self.__fee = rfee

    def set_name(self,nam):
        self.__name= nam
    def get_name(self):
        return self.__name


    def set_address(self, add):
        self.__address = add
    def get_address(self):
        return self.__address


    def set_contact(self, cont):
        self.__contact = cont
    def get_contact(self):
        return self.__contact


    def set_profession(self, prof):
        self.__profession = prof
    def get_profession(self):
        return self.__profession


    def set_parents_name(self, pname):
        self.__parents_name = pname
    def get_parents_name(self):
        return self.__parents_name


    def set_parents_number(self, pnum):
        self.__parents_number = pnum
    def get_parents_number(self):
        return self.__parents_number


    def set_local_guardain(self, guardain):
        self.__local_guardain = guardain
    def get_local_guardain(self):
        return self.__local_guardain


    def set_number(self,num):
        self.__number= num
    def get_number(self):
        return self.__number

    def set_room_number(self, rnum):
        self.__room_numbernumber = rnum
    def get_room_number(self):
        return self.__room_number


    def set_room_type(self,rtype):
        self.__room_type= rtype
    def get_room_type(self):
        return self.__room_type


    def set_room_partners(self, rpartners):
        self.__room_partners = rpartners
    def get_room_partners(self):
        return self.__room_partners


    def set_room_partner(self, rpartner):
        self.__room_partners = rpartner
    def get_room_partner(self):
        return self.__room_partner


    def set_room_partner1(self, rpartner1):
        self.__room_partner1 = rpartner1
    def get_room_partner1(self):
        return self.__room_partner1

    def set_fee(self, rfee):
        self.__fee = rfee
    def get_fee(self):
        return self.__fee
















