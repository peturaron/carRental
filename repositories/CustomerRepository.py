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
            cardNumber = customer.getCardNumber()
            subscription = customer.getSubscription()
            customersFile.write("{}:{}:{}:{}:{}:{}:{}:{}\n".format(email, name, dateOfBirth, gender, dateOfReg, payMethod, cardNumber, subscription))

    def getCustomers(self):
        if self.__customers == []:
            with open("./data/customers.txt", "r", encoding = "utf-8") as customerFile:
                for line in customerFile.readlines():
                    email, name, dateOfBirth, gender, dateOfReg, payMethod, cardNumber, subscription = line.split(":")
                    newCustomer = Customer(email, name, dateOfBirth, gender, dateOfReg, payMethod, cardNumber, subscription)
                    self.__customers.append(newCustomer)
        return self.__customers

    def getCustomerDictionary(self):
        if self._customerDictionary == {}:
            try:
                with open("./data/customers.txt", "r", encoding = "utf-8") as customerFile:
                    #self._carDictionary = {}
                    for line in customerFile.readlines():
                        email, name, dateOfBirth, gender, dateOfReg, payMethod, cardNumber, subscription = line.strip().split(":")
                        allCustomers = Customer(email, name, dateOfBirth, gender, dateOfReg, payMethod, cardNumber, subscription)
                        customerKey = email
                        attributeList = self.createAttributeList(name, email, dateOfBirth)
                        self._customerDictionary[customerKey] = attributeList
                    return self._customerDictionary

            except FileNotFoundError:
                return {}

        return self._customerDictionary

    def createAttributeList(self, name, email, dateOfBirth):
        list = [name, email, dateOfBirth]
        return list

    def unsubscribe(self, email):
            customerList = []
            with open("./data/customers.txt", "r", encoding = "utf-8") as customerFile:
                for line in customerFile.readlines():
                    customerRow = line.strip().split(":") 
                    customerList.append(customerRow)
                for customerX in range(len(customerList)):
                    if customerList[customerX][0] == email:
                        customerList[customerX][7] = "inactive"
                        break   
            self.readNewListToFile(customerList)
            return


    def readNewListToFile(self, newList):
        with open("./data/customers.txt", "w", encoding = "utf-8") as customersFile:
            for singleCustomer in newList:
                    email = singleCustomer[0]
                    name = singleCustomer[1]
                    dateOfBirth = singleCustomer[2]
                    gender = singleCustomer[3]
                    dateOfReg = singleCustomer[4]
                    payMethod = singleCustomer[5]
                    cardNumber = singleCustomer[6]
                    subscription = singleCustomer[7]
                    customersFile.write("{}:{}:{}:{}:{}:{}:{}:{}\n".format(email, name, dateOfBirth, gender, dateOfReg, payMethod, cardNumber, subscription))
            return
