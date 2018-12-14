from services.CustomerService import CustomerService
from models.Customer import Customer
from repositories.CustomerRepository import CustomerRepository
from os import system, name
from time import sleep

import datetime
import re

class CustomerUi:

    def __init__(self):
        self.__customerService = CustomerService()
        self.__customerRepo = CustomerRepository()

    def customerMenu(self):

        action = ""
        while(action != "5"):
            self.clear()
            print("\nCUSTOMER MENU") 
            print("_"*40,"\n")
            customerMenu = "\t{:<30}\n\t{:<30}\n\t{:<30}\n\t{:<30}\n\t{:<30}\n\t".format("1 - Register a customer", 
                                                                                     "2 - List all customer", 
                                                                                     "3 - Search for a customer",
                                                                                     "4 - Unsubscribe customer", 
                                                                                     "5 - Return to main menu")
            print(customerMenu)

            action = input("\nChoose an option: ").lower()

            if action == "1":
                self.createCustomer()
            elif action == "2":
                self.viewAllCustomers() 
            elif action == "3":
                self.searchForCustomer()
                break
            elif action == "4":
                self.unsubscribeCustomer()
                break
            elif action == "5":
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
        cardNumber = self.validCardNumber() 
        subscription = "active"
 
        newCustomer = Customer(email, name, dateOfBirth, gender, dateOfReg, payMethod, cardNumber, subscription)
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
        print("Please enter the customers date of birth in date-month-year format(e.g. 12-01-1999)" )
        while True:
            birthDate = input("Date of birth: ")
            dateValidated = datetime.datetime.strptime(birthDate,"%d-%m-%Y").date()
            if dateValidated:
                return dateValidated
            else:
                print("Invalid format. Please enter the date-month-year")

    def validGender(self):
        while True:
            option = input("Please enter M for male or F for Female: ").lower()
            validGender = re.search("m", option) or re.search("f", option)
            if validGender:
                return option
            
    def validPayment(self):
        while True:
            option = input("Write 'Cash' or 'Card' depending on the customer: ").lower()
            validPayment = re.search("cash", option) or re.search("card", option)
            if validPayment:
                return option

    def validCardNumber(self):
        cardPattern='^([0-9]{4})-?([0-9]{4})-?([0-9]{4})-?([0-9]{4})$'
        while True:
            customerCard = input("Please enter the customers card number for insurance: ")
            validCard = re.match(cardPattern, customerCard)
            if validCard:
                return customerCard
            else:
                print("Invalid Credit Card please try again.")

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
        action = ""
        while True:
            email = input("Customer email (email): ")
            if self.__customerService.isCustomerListed(email) == True:
                customerInfo = self.__customerService.searchForCustomerInformation(email)
                self.clear()
                print("Name: " + customerInfo[0])
                print("\nEmail: " + customerInfo[1])
                print("\nDate of birth: " + customerInfo[2])
                break
            else:
                print("Email not found. The search is case sensitive")
        while(action != "2"):
            self.lineInHeader()
            print("\n1. Unsubscribe customer")
            print("\n2. Return to Customer menu")
            action = input("Choose an option: ")
            if(action == "1"):
                print("email-----" + email)
                self.__customerService.unsubscribeCustomer(email)
                break

    def unsubscribeCustomer(self):
        actionBar = "\t{:<30}\n\t{:<30}\n\t".format("1 - Yes", "2 - No")
        email = ""
        while(email != "b"):
            email = input("Enter b to return to Main menu.\nCustomer email (email): ")
            if self.__customerService.isCustomerListed(email) == True:
                print("Are you sure you want to unsubscribe " + email)
                print(actionBar)
                action = input("\nChoose an option: ").lower()
                if action == "1":
                    self.__customerService.unsubscribeCustomer(email)
                    print("Customer has been unsubscribed.\nReturning to Main menu")
                    sleep(2)
                    break
                elif action == "2":
                    print("Returning to Main menu")
                    sleep(2)
                    break
                else:
                    print("Invalid option.")
            elif(email == "b"):
                print("Returning to Main menu")
                sleep(2)
                break
            else:
                print("Email not found. The search is case sensitive")      

    def backToCustomerMenu(self):
        print()
        self.lineInHeader()

        print("{}\n".format("b - Back to Customer menu"))
        back = "yes"
        while back != "b":
            back = input("Choose an option: ").lower()
            if back == "b":
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