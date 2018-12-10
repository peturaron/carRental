from models.Customer import Customer

class CustomerRepository:

    def __init__(self):
        self.__customers = []
        self._customerDictionary = {} #self.getCustomerDictionary()

    def addCustomer(self, customer):
        # first add to file then to private list
        with open("./data/customers.txt", "a+", encoding = "utf-8") as customersFile:
            email = customer.getEmail()
            name = customer.getName()
            dateOfBirth = customer.getDateOfBirth()
            gender = customer.getGender()
            dateOfReg = customer.getDateOfReg()
            payMethod = customer.getPayMethod()
            customersFile.write("{}:{}:{}:{}:{}:{}\n".format(email, name, dateOfBirth, gender, dateOfReg, payMethod))

    def getCustomers(self):
        if self.__customers == []:
            with open("./data/customers.txt", "r", encoding = "utf-8") as customerFile:
                for line in customerFile.readlines():
                    email, name, dateOfBirth, gender, dateOfReg, payMethod = line.split(":")
                    newCustomer = Customer(email, name, dateOfBirth, gender, dateOfReg, payMethod)
                    self.__customers.append(newCustomer)
        return self.__customers

    def getCustomerDictionary(self):
        if self._customerDictionary == {}:
            try:
                with open("./data/customers.txt", "r") as customerFile:
                    #self._carDictionary = {}
                    for line in customerFile.readlines():
                        email, name, dateOfBirth, gender, dateOfReg, payMethod = line.split(":")
                        allCustomers = Customer(email, name, dateOfBirth, gender, dateOfReg, payMethod)
                        customerKey = email
                        attributeList = self.createAttributeList(email, name, dateOfBirth)
                        self._customerDictionary[customerKey] = attributeList
                    return self._customerDictionary

            except FileNotFoundError:
                return {}

        return self._customerDictionary

    def createAttributeList(self, email, name, dateOfBirth):
        list = [email, name, dateOfBirth]
        return list
