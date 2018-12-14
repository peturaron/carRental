from services.BookingService import BookingService
from models.Booking import Booking
from ui.CarUi import CarUi
from services.CarService import CarService
import datetime
from os import system, name
from time import sleep

class BookingUi:

    def __init__(self):
        self._bookingService = BookingService()
        self._carUi = CarUi()
        self._carService = CarService()

    def mainMenu(self):
        self.clear()
        action = ""
        while(action != "4"):
            print("\nBOOKING MENU")
            print("_"*40, "\n")
            bookingMenu = "\t{:<30}\n\t{:<30}\n\t{:<30}\n\t{:<30}\n".format(
                "1 - Register a booking", "2 - Search for a booking", "3 - List all bookings", "4 - Main menu")
            print(bookingMenu)

            action = input("Choose an option: ")
            print()
            if action == "1":
                self.registerBooking()
            elif action == "2":
                self.searchForBooking()
            elif action == "3":
                self.listBookings()
            elif action == "4":
                self.clear()
                break
            else: 
                print("\nPlease enter valid option\n")
 
    def registerBooking(self):
        self.clear()
        print("\nNew BOOKING\n")
        print("_"*40, "\n")
        customerID = self.customerMenu()
        self.clear()
        print("Customer ID: ", customerID)
        carID = self.availableCarMenu()
        self.clear()
        print("RENTAL DATES")
        print("_"*40, "\n")
        inputRentDate = self.getInitialRentDate()
        inputReturnDate = self.getInitalReturnDate()
        rentDate, returnDate = self._bookingService.getRentalDates(inputRentDate, inputReturnDate)
        bookingStatus = "active"
        self.clear()
        print("PAYMENT")
        print("_"*40, "\n")
        totalPrice = self.getPrice(carID, inputReturnDate)
        print("\nThe total price for the booking is {} kr\n".format(totalPrice))
        totalPrice = self.getAddtionalInsurance(totalPrice, inputReturnDate)
        self.printCustomer(customerID)
        print("\nThe total price for the booking including additional insurance is {} kr\n".format(totalPrice))
        while True:
            saveBooking = input("Book this car? (y/n) ").lower()
            if saveBooking == "y":
                newBooking = Booking(carID, rentDate, returnDate, bookingStatus, customerID)
                self._bookingService.addBooking(newBooking)
                break
            elif saveBooking == "n":
                self.clear()
                break
            else:
                print("Please enter valid option\n")

    def printCustomer(self, customerID):
        customerInfo = self._bookingService.getCustomerDict(customerID)
        print("Booking information for {}:".format(customerID))
        for customer in customerInfo:
            print(customer) 

    def customerMenu(self):
        action = ""
        while (action != "3"):
            availableCustomerMenu = "\n\t{:<30}\n\t{:<30}\n\t{:<30}\n".format(
                    "1 - View list of registered customers", "2 - Enter customer ID", "3 - Back to Booking menu")
            print(availableCustomerMenu)
            action = input("Choose an option: ")
            print()
            if action == "1":
                self.clear()
                print("ALL CUSTOMERS")
                self.lineInHeader()
                for customer in self._bookingService.getCustomerInformationForBooking().keys():
                    print("{}".format(customer))
                while True:
                    customerID = input("\nCustomer ID: ")
                    if self._bookingService.isCustomerListed(customerID) == True:
                        break
                    else:
                        print("Please enter valid Customer ID")
                return customerID
            elif action == "2":
                while True:
                    customerID = input("\nCustomer ID: ")
                    if self._bookingService.isCustomerListed(customerID) == True:
                        break
                    else:
                        print("Please enter valid customer ID")
                return customerID
            elif action == "3":
                self.mainMenu()
                break
            else: 
                print("\nPlease enter valid option\n")

    def availableCarMenu(self):
        action = ""
        while(action != "3"):
            availableCarMenu = "\n\t{:<30}\n\t{:<30}\n\t{:<30}\n".format(
                    "1 - View list of available cars", "2 - Enter car ID", "3 - Back to Booking menu")
            print(availableCarMenu)
            action = input("Choose an option: ")
            print()
            if action == "1":
                self._carUi.availableCars()
                while True:
                    carID = input("\nCar ID: ")
                    if self._carService.isCarListed(carID) == True:
                        break
                    else:
                        print("Please enter valid car ID")
                return carID
            elif action == "2":
                while True:
                    carID = input("\nCar ID: ")
                    if self._carService.isCarListed(carID) == True:
                        break
                    else:
                        print("Please enter valid car ID")
                return carID
            elif action == "3":
                self.mainMenu()
                break
            else: 
                print("\nPlease enter valid option\n")

    def getInitialRentDate(self):
        while True:
            inputRentDate = input("Beginning of rental date. Please enter the number of days from today: ")
            if self._bookingService.isRentDateValid(inputRentDate) is not True:
                print("Invalid entry, please enter zero day or more: ")
            else:
                inputRentDate = int(inputRentDate)
                return inputRentDate

    def getInitalReturnDate(self):
        while True:
            inputReturnDate = input("Rental duration: ")
            if self._bookingService.isReturnDateValid(inputReturnDate) is not True:
                print("Invalid entry, please select one day or more: ")
            else:
                inputReturnDate = int(inputReturnDate)
                return inputReturnDate

    def getPrice(self, carId, totalDays):
        price = self._bookingService.getCarPrice(carId)
        price = int(price)
        TotalPrice = price * totalDays
        return TotalPrice

    def getAddtionalInsurance(self, price, inputReturnDate):
        insurancePerDay = 1500
        while True:
            extraInsurance = input("Do you want to add additional insurance (y/n)?").lower()
            if extraInsurance == "y":
                self.clear()
                print("BOOKING INFORMAION")
                print("_"*40, "\n")
                insuranceCost = insurancePerDay * inputReturnDate
                totalPrice = price + insuranceCost
                return totalPrice
            elif extraInsurance == "n":
                self.clear()
                print("BOOKING INFORMAION")
                print("_"*40, "\n")
                return price
            else:
                print("\nPlease enter valid option\n")

    def searchForBooking(self):
            self.clear()
            print("\nSEARCH FOR A BOOKING")
            print("_"*40, "\n")
            while True:
                bookingId = input("Customer email: ")
                if self._bookingService.isBookingListed(bookingId) == True:
                    bookingInfo = self._bookingService.searchForBookingInformation(bookingId)
                    for attribute in bookingInfo:
                        print(attribute)
                    break
                else:
                    print("Please enter valid Customer email.")
            self.searchBookingMenu(bookingId)
                
    def searchBookingMenu(self, bookingId):
        print("_"*40, "\n")
        action = ""
        while(action != "3"):
            searchBookingMenu = "\t{:<30}\n\t{:<30}\n\t{:<30}\n".format(
                    "1 - Change a booking", "2 - Cancel a booking", "3 - Back to Booking Menu")
            print(searchBookingMenu)
            action = input("Choose an option: ")
            print()
            if action == "1":
                self.changeBooking(bookingId)
                break
            elif action == "2":
                self.cancelBooking(bookingId)
                break
            elif action == "3":
                self.mainMenu()
                break
            else:
                print("\nPlease enter valid option\n")

    def changeBooking(self, bookingId):
        print("_"*40, "\n")
        action = ""
        while(action != "3"):
            cancelMenu = "\t{:<30}\n\t{:<30}\n\t{:<30}\n".format(
                    "1 - Change rental dates", "2 - Change car", "3 - Back to Booking Menu")
            print(cancelMenu)
            action = input("Choose an option: ")
            print()
            if action == "1":   
                self.getNewRentalDates(bookingId)
                break
            elif action == "2":
                self.getNewCar(bookingId)
                break
            elif action == "3":
                self.mainMenu()
                break
            else:
                print("\nPlease enter valid option\n")

    def getNewRentalDates(self, bookingId):
        self.clear()
        print("CHANGE RENTAL DATES")
        print("_"*40, "\n")
        inputRentDate = int(input("Beginning of rental date. Please input the number of days from today: "))
        inputReturnDate = int(input("Rental duration: "))
        newRentDate, newReturnDate = self._bookingService.getRentalDates(inputRentDate, inputReturnDate)
        self._bookingService.getNewRentDateBookingList(newRentDate, newReturnDate, bookingId) 
        print("\nThe new rent date is ", newRentDate) 
        print("The new rent date is ", newReturnDate, "\n")
        self.backToBookingMenu()
        self.clear()

    def getNewCar(self, bookingId):
        self.clear()
        print("CHANGE CAR")
        print("_"*40, "\n")
        newCarID = self.availableCarMenu()
        self._bookingService.changeCar(bookingId, newCarID)
        print("\nCar has been changed to {} for {}\n".format(newCarID, bookingId))
        self.backToBookingMenu()
        self.clear

    def cancelBooking(self, bookingId):
        print("\nCANCEL BOOKING\n")
        print("_"*40, "\n")
        self._bookingService.changeBookingStatus(bookingId)
        print("\nThe booking for {} has been canceled.\n". format(bookingId))
        self.backToBookingMenu()
        self.clear()

    def listBookings(self):
        print("\nLIST OF ALL BOOKINGS\n")
        print("_"*40, "\n")
        header = "{:^10}{:^10}{:^10}{:^10}{:^10}".format("Car ID", "Rent Date", "Return Date", "Rental Status", "Email")
        print(header, "\n")
        bookings = self._bookingService.getBookingList()
        for p in bookings:
            print(p)
        self.backToBookingMenu()
        self.clear()

    def clear(self): 
        # Virkni fyrir windows 
        if name == 'nt': 
            _ = system('cls') 
        #  Virkni fyrir Mac 
        else: 
            _ = system('clear')
 
    def backToBookingMenu(self):
        print()
        self.lineInHeader()
        print("{}\n".format("b - Back to Booking menu"))
        back = "yes"
        while back != "b":
            back = input("Choose an option: ").lower()
            if back == "b":
                break
            else:
                print("Please enter valid option.")

    def lineInHeader(self):
        print("_"*80, "\n")