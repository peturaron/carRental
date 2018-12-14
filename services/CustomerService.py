from repositories.CustomerRepository import CustomerRepository

class CustomerService:
    def __init__(self):
        self.__customerRepo = CustomerRepository()

    def addCustomer(self, customer):
        if self.isValidCustomer(customer):
            self.__customerRepo.addCustomer(customer)

    def isValidCustomer(self, customer):

        return True
    
    def isCustomerListed(self, email):
        for key in self.__customerRepo.getCustomerDictionary():
            if key == email:
                return True 

    def getCustomers(self):
        return self.__customerRepo.getCustomers()


    def getAllCustomers(self):
        return self.__customerRepo.getCustomers()


    def searchForCustomerInformation(self, email):
        return self.__customerRepo.getCustomerDictionary()[email]

    def unsubscribeCustomer(self, email):
        self.__customerRepo.unsubscribe(email)
       