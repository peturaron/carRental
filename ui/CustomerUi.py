from services.CustomerService import CustomerService
from models.Customer import Customer
import os

class CustomerUi:

    def __init__(self):
        self.__customerService = CustomerService()

    def main_menu(self):

        action = ""
        while(action != "3"):
           
            print("Customers: \n ")
            print("1. Register a customer")
            print("2. List all customers") #A eftir ad breyta 2 i search for a customer
            print("3. Main menu")

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
