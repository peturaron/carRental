from services.CustomerService import CustomerService
from models.Customer import Customer
from repositories.CustomerRepository import CustomerRepository

import datetime
import re

class CustomerUi:

    def __init__(self):
        self.__customerService = CustomerService()
        self.__customerRepo = CustomerRepository()

    def customerMenu(self):

        action = ""
        while(action != "4"):
            print("\nCUSTOMER MENU") 
            print("_"*40,"\n")
            mainMenu = "\t{:<30}\n\t{:<30}\n\t{:<30}\n\t{:<30}\n\t".format("1 - Register a customer", 
                                                                           "2 - List all customer", 
                                                                           "3 - Search for a customer", 
                                                                           "4 - Return to main menu")
            print(mainMenu)

            action = input("\nChoose an option: ").lower()

            if action == "1":
                self.createCustomer()
            elif action == "2":
                self.viewAllCustomers()
                
            elif action == "3":
                print("\nSEARCH FOR A CUSTOMER\n")
                print("_"*40, "\n")
                name = input("Customer email (email): ")

                customerInfo = self.__customerService.searchForCustomerInformation(name)
                for attribute in customerInfo:
                    print(attribute)

            else:
                print("\nPlease enter a valid number\n")

    def createCustomer(self): 
        email = self.validEmail()
        name = self.validName()
        dateOfBirth = self.validDateOfBirth()
        gender = self.validGender()
        dateOfReg = (datetime.date.today())
        payMethod = self.validPayment()

        newCustomer = Customer(email, name, dateOfBirth, gender, dateOfReg, payMethod)
        self.__customerService.addCustomer(newCustomer)
    
    def validEmail(self):
        while True:
            email = input("Email address: ")
            emailIsValid = re.search(r"[^@]+[^@]+\.[^@]", email)
            if emailIsValid:
                return email
            else:
                print("Invalid email address please try again.")

    def validName(self):
        while True:
            name = input("Full name: ")
            if len(name) > 50 or len(name) < 1:
                print("Invalid. maximum character length is 50 and the minimum is 1")
            elif all(letters.isalpha() or letters.isspace() for letters in name):
                return name
            else:
                print("Invalid. Name must only use letters")
         
    def validDateOfBirth(self):
        while True:
            try:
                print("Please enter the customers date of birth in date-month-year format(e.g. 12-01-1999)" )
                birthDate = input("Date of birth: ")
                dateValidated = datetime.datetime.strptime(birthDate,"%d-%m-%Y").date()
            except ValueError:
                print("Invalid format. Please enter the date-month-year")
            else:    
                return dateValidated
    def validGender(self):
        while True:
            try:
                option = input("Please enter M for male or F for Female: ").lower()
                validGender = re.search("m", option) or re.search("f", option)
                if validGender:
                    return option
            except ValueError as e:
                    print(e)
    def validPayment(self):
        while True:
            try:
                option = input("Write 'Cash' or 'Card' depending on the customer: ").lower()
                validPayment = re.search("cash", option) or re.search("card", option)
                if validPayment:
                    return option
            except ValueError as e:
                    print(e)
                
    def viewAllCustomers(self):
        counter = 1;
        customers = self.__customerService.getCustomers()
        print("\nCUSTOMERS") 
        print("_"*40,"\n")
        for customer in customers:
            print(repr(counter) + ". " + repr(customer))
            counter += 1