from services.CustomerService import CustomerService
from models.Customer import Customer
from repositories.CustomerRepository import CustomerRepository

class CustomerUi:

    def __init__(self):
        self.__customerService = CustomerService()
        self.__customerRepo = CustomerRepository()

    def main_menu(self):

        action = ""
        while(action != "4"):

            print("Customers: \n ")
            print("1. Register a customer")
            print("2. List all customers")
            print("3. Search for customer")
            print("4. Main menu")

            action = input("\nChoose an option: ").lower()

            if action == "1":
                email = input("Email address: ")
                name = input("Full name: ")
                dateOfBirth = input("Date of birth: ")
                gender = input("(M/F): ")
                dateOfReg = input("Date of registration: ")
                payMethod = input("(Cash/Card): ")

                newCustomer = Customer(email, name, dateOfBirth, gender, dateOfReg, payMethod)
                self.__customerService.addCustomer(newCustomer)

            elif action == "2":
                counter = 1;
                customers = self.__customerService.getCustomers()

                for customer in customers:
                    printString = repr(counter) + ". " + repr(customer)
                    print(repr(counter) + ". \n" + repr(customer))
                    counter += 1

            elif action == "3":
                print("\nSEARCH FOR A CUSTOMER\n")
                print("_"*40, "\n")
                name = input("Customer email (email): ")

                customerInfo = self.__customerService.searchForCustomerInformation(name)
                for attribute in customerInfo:
                    print(attribute)

            else:
                print("\nPlease enter a valid number\n")
