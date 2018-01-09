class Cards():
    def __init__(self, year, month,type):
        self.__year = year
        self.__month = month
        self.__type = type

    def get_year(self):
        return self.__year
    def get_month(self):
        return self.__month
    def get_type(self):
        return self.__type

    def set_firstname(self, year):
        self.__year = year
    def set_month(self, month):
        self.__month = month
    def set_age(self, type):
        self.__type = type


