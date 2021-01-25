
class AddressBook:

    def __init__(self, id=None, name=None, address=None, phone_number=None, email=None):
        self.__id = id
        self.__name = name
        self.__address = address
        self.__phone_number = phone_number
        self.__email = email

    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address):
        self.__address = address

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        self.__phone_number = phone_number

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email
