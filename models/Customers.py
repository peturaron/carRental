class Customers:
    
    def __init__(self, email, name, phone, status, dateOfBirth):
        self.__email = email
        self.__name = name
        self.__phone = phone
        self.__status = status
        self.__dateOfBirth = dateOfBirth


    def __str__(self):
        return "{},{},{}".format(self.__email, self.__name, self.__phone, self.__status, self.__dateOfBirth)
    
    def __repr__(self):
        return self.__str__()

    def getEmail(self):
        return self.__email
    
    def getName(self):
        return self.__name
    
    def getPhone(self):
        return self.__phone
    
    def getUserStatus(self):
        return self.__status
    
    def getDateOfBirth(self):
        return self.__dateOfBirth
