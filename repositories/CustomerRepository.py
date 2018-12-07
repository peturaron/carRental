from models.Customer import Customer

class CustomerRepository:

    def __init__(self):
        self.__customers = []

    def addCustomer(self, customer):
        # first add to file then to private list
        with open("./data/customers.txt", "a+", encoding = "utf-8") as customersFile:
            email = customer.getEmail()
            name = customer.getName()
            dateOfBirth = customer.getDateOfBirth()
            gender = customer.getGender()
            dateOfReg = customer.getDateOfReg()
            payMethod = customer.getPayMethod()
            customersFile.write("{},{},{},{},{},{}\n".format(email, name, dateOfBirth, gender, dateOfReg, payMethod))

    def getCustomers(self):
        if self.__customers == []:
            with open("./data/customers.txt", "r", encoding = "utf-8") as customerFile:
                for line in customerFile.readlines():
                    email, name, dateOfBirth, gender, dateOfReg, payMethod = line.split(",")
                    newCustomer = Customer(email, name, dateOfBirth, gender, dateOfReg, payMethod)
                    self.__customers.append(newCustomer)

        return self.__customers