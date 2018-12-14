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
                break
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
        actionBar = "\t{:<30}\n\t{:<30}\n\t".format("1 - Yes", "2 - No")
        valid = False
        while(valid != True):
            email = input("\nEmail address: ")
            name = input("\nFull name: ") 
            print("\nPlease enter the customers date of birth in date-month-year format(e.g. 12-01-1999)" )
            dateOfBirth = input("Date of birth: ")
            gender = input("\nPlease enter M for male or F for Female: ").lower()
            dateOfReg = (datetime.date.today())
            payMethod = self.getPayMethod()
            cardNumber = input("\nPlease enter the customers card number for insurance(use '-' between each four digit combination): ")
            subscription = "active"
            self.clear()

            newCustomer = Customer(email, name, dateOfBirth, gender, dateOfReg, payMethod, cardNumber, subscription)
            if self.__customerService.addCustomer(newCustomer):
                valid = True
                break
            else:
                print("Do you want to try again?\n" + actionBar)
                action = input("\nChoose an option: ").lower()
                if action == "1":
                    valid = False
                elif action == "2":
                    print("Returning to Main menu")
                    sleep(2)
                    break
                else:
                    print("Invalid option.")

    def getPayMethod(self):
        payMethod =input("\nWrite 'Cash' or 'Card' depending on the customer: ").lower()
        return payMethod

    def viewAllCustomers(self):
        self.clear()
        counter = 1
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
            print("\n2. Change customer")
            print("\n3. Return to Main menu")
            action = input("Choose an option: ")
            if(action == "1"):
                self.__customerService.unsubscribeCustomer(email)
                break
            elif(action == "2"):
                self.changeCustomer(email)
                break
            elif(action == "3"):
                print("Returning to Main menu")
                sleep(2)
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

    def changeCustomer(self, email):
        valid = False
        print("_"*40, "\n")
        action = ""
        while(action != "3"):
            changeMenu = "\t{:<30}\n\t{:<30}\n".format(
                    "1 - Change payment method", "2 - Back to Booking Menu")
            print(changeMenu)
            action = input("Choose an option: ")
            print()
            if action == "1":   
                while(valid != True):
                    payMethod = self.getPayMethod()
                    if self.__customerService.validPayment(payMethod):
                        self.__customerService.changePayMethod(payMethod, email)
                        valid = True
                    else:
                        valid = False
                print("The payment method has changed to {}".format(payMethod))
                break
            elif action == "2":
                self.customerMenu()
                break
            else:
                print("\nPlease enter valid option\n")

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