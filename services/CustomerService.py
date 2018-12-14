from repositories.CustomerRepository import CustomerRepository
from repositories.BookingRepository import BookingRepository

import re
import datetime

class CustomerService:
    def __init__(self):
        self.__customerRepo = CustomerRepository()

    def addCustomer(self, customer):
        if self.isValidCustomer(customer):
            self.__customerRepo.addCustomer(customer)
            return True
        else:
            return False

    def isValidCustomer(self, customer):
        email = self.validEmail(customer.getEmail())
        name = self.validName(customer.getName())
        dateOfBirth = self.validDateOfBirth(customer.getDateOfBirth())
        gender = self.validGender(customer.getGender())
        payMethod = self.validPayment(customer.getPayMethod())
        cardNumber = self.validCardNumber(customer.getCardNumber())
        subscription = self.validSubscription(customer.getSubscription())

        if((email == True) and (name == True) and (dateOfBirth == True) and 
           (gender == True) and (payMethod == True) and (cardNumber  == True) and (subscription == True)):
            print("Valid")
            return True
        else:
            return False
            
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
    
    def validEmail(self, email):
        if re.search(r"[^@]+[^@]+\.[^@]", email):
            return True
        else:
            print("Invalid email address please try again.")
            return False

    def validName(self, name):
        if len(name) > 50 or len(name) < 1:
            print("Invalid. maximum character length is 50 and the minimum is 1")
            return False
        elif all(letters.isalpha() or letters.isspace() for letters in name):
            return True
        else:
            print("Invalid name must only use letters")
            return False

    def validDateOfBirth(self, day):
        try:
            dateValidated = datetime.datetime.strptime(day,"%d-%m-%Y").date()
            if dateValidated:
                return True
        except ValueError:
            print("Invalid format. Please enter the date-month-year")
            return False

    def validGender(self, gender):
        genderValid = re.search("m", gender) or re.search("f", gender)
        if genderValid:
            return True
        else:
            print("Invalid entry for gender")
            return False

    def validPayment(self, option):
        validPayment = re.search("cash", option) or re.search("card", option)
        if validPayment:
            return True
        else:
            print("Invalid entry for payment method")
            return False

    def validCardNumber(self, customerCard):
        cardPattern='^([0-9]{4})-?([0-9]{4})-?([0-9]{4})-?([0-9]{4})$'
        validCard = re.match(cardPattern, customerCard)
        if validCard:
            return True
        else:
            print("Invalid card number.")
            return False

    def validSubscription(self, subscription):
        if(subscription == "active"):
            return True
        else:
            return False
       
    def changePayMethod(self, payMethod, email):
        newList = []
        for persons in self.__customerRepo.createCustomerListFromFile():
            for attribute in persons:
                if persons[0] == email:
                    persons[5] = payMethod
                    newString = ":".join(persons)
                else:
                    newString = ":".join(persons)
            newList.append(newString)
        self.__customerRepo.addChangedCustomerInfoToFile(newList)
