class Customer:

    def __init__(self, email, name, dateOfBirth, gender, dateOfReg, payMethod):
        self.__email = email
        self.__name = name
        self.__dateOfBirth = dateOfBirth
        self.__gender = gender
        self.__dateOfReg = dateOfReg
        self.__payMethod = payMethod

    def __str__(self):
        return "Email: {}\nName: {}\nDate of Birth: {}\nGender: {}\nDate of Registration: {} \nPayment method: {}\n".format(self.__email, self.__name, self.__dateOfBirth, self.__gender, self.__dateOfReg, self.__payMethod)

    def __repr__(self):
        return self.__str__()

    def getEmail(self):
        return self.__email

    def getName(self):
        return self.__name

    def getDateOfBirth(self):
        return self.__dateOfBirth

    def getGender(self):
        return self.__gender

    def getDateOfReg(self):
        return self.__dateOfReg

    def getPayMethod(self):
        return self.__payMethod
