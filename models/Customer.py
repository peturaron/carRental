class Customer:

    def __init__(self, email, name, dateOfBirth, gender, dateOfReg, payMethod):
        self.__email = email
        self.__name = name
        self.__dateOfBirth = dateOfBirth
        self.__gender = gender
        self.__dateOfReg = dateOfReg
        self.__payMethod = payMethod

    def __str__(self):
        return "{},{},{},{},{},{}".format(self.__email, self.__name, self.__dateOfBirth, self.__gender, self.__dateOfReg, self.__payMethod)

    def __repr__(self):
        return self.__str__()

    def get_email(self):
        return self.__email

    def get_name(self):
        return self.__name

    def get_dateOfBirth(self):
        return self.__dateOfBirth

    def get_gender(self):
        return self.__gender

    def get_dateOfReg(self):
        return self.__dateOfReg

    def get_payMethod(self):
        return self.__payMethod
