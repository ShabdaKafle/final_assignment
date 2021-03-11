class Bill:
    def __init__(self, name=None, dat=None, rtype=None, month=None, fee=None, num=None):
        self.__bill_number = num
        self.__date = dat
        self.__student_name = name
        self.__room_type = rtype
        self.__months = month
        self.__total_fee = fee

    def set_bill_num(self, num):
        self.__bill_number = num
    def get_bill_num(self):
        return self.__bill_number


    def set_date(self, dat):
        self.__date = dat
    def get_date(self):
        return self.__date


    def set_name(self, name):
        self.__student_name = name
    def get_name(self):
        return self.__student_name


    def set_room(self, rtype):
        self.__room_type = rtype
    def get_room(self):
        return self.__room_type


    def set_month(self, month):
        self.__months = month
    def get_month(self):
        return self.__months


    def set_fees(self, fee):
        self.__total_fee = fee
    def get_fees(self):
        return self.__total_fee
