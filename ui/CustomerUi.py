from services.CustomerService import CustomerService
from models.Customer import Customer
from repositories.CustomerRepository import CustomerRepository
from os import system, name

import datetime
import re


class CustomerUi:

    def __init__(self):
        self.__customerService = CustomerService()
        self.__customerRepo = CustomerRepository()

    def customerMenu(self):

        action = ""
        while(action != "4"):
            self.clear()
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
                self.searchForCustomer()
            elif action =="4":
                break
            else:
                print("Error wrong input!\n")

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
        self.clear()
        counter = 1;
        customers = self.__customerService.getCustomers()
        print("\nCUSTOMERS") 
        print("_"*40,"\n")
        for customer in customers:
            print(repr(counter) + ". " + repr(customer))
            counter += 1
        self.backToCustomerMenu()

    def searchForCustomer(self):
        self.clear()
        print("\nSEARCH FOR A CUSTOMER\n")
        self.lineInHeader()
        while True:
            email = input("Customer email (email): ")
            if self.__customerService.isCustomerListed(email) == True:
                customerInfo = self.__customerService.searchForCustomerInformation(email)
                print("Name: " + customerInfo[0])
                print("\nEmail: " + customerInfo[1])
                print("\nDate of birth: " + customerInfo[2])
                break
            else:
                print("Email not found. The search is case sensitive")
                
        
        self.backToCustomerMenu()

    def backToCustomerMenu(self):
        print()
        self.lineInHeader()

        print("{}\n".format("b - Back to Customer menu"))
        back = "yes"
        while back != "b":
            back = input("Choose an option: ").lower()
            if back == "b":
                #self.mainMenu()
                #sleep(2)
                break
            else:
                print("Please choose valid option.")

    def lineInHeader(self):
        print("_"*80, "\n")

    def clear(self): 
        # Virkni fyrir windows 
        if name == 'nt': 
            _ = system('cls') 
        #  Virkni fyrir Mac 
        else: 
            _ = system('clear')