from services.BookingService import BookingService
from models.Booking import Booking
import datetime

class BookingUi:

    def __init__(self):
        self._bookingService = BookingService()

    def mainMenu(self):
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
                break
            else: 
                print("\nPlease enter valid option\n")
 
    def registerBooking(self):
        print("\nREGISTER A BOOKING\n")
        print("_"*40, "\n")
        carID = input("Car ID: ")
        inputRentDate = int(input("Beginning of rental date. Please input the number of days from today: "))
        inputReturnDate = int(input("Rental duration: "))
        rentDate, returnDate = self._bookingService.getRentalDates(inputRentDate, inputReturnDate)
        bookingStatus = "active"
        customerID = input("Customer ID: ")
        newBooking = Booking(carID, rentDate, returnDate, bookingStatus, customerID)
        self._bookingService.addBooking(newBooking)
        totalPrice = self.getPrice(carID, inputReturnDate)
        print("The total price for the booking is {}".format(totalPrice))
        
    def getPrice(self, carId, totalDays):
        price = self._bookingService.getCarPrice(carId)
        price = int(price)
        TotalPrice = price * totalDays
        return TotalPrice

    def searchForBooking(self):
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
            elif action == "2":
                self.cancelBooking(bookingId)
            elif action == "3":
                self.mainMenu()
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
            elif action == "2":
                self.getNewCar(bookingId)
            elif action == "3":
                self.mainMenu()
                break
            else:
                print("\nPlease enter valid option\n")

    def getNewRentalDates(self, bookingId):
        inputRentDate = int(input("Beginning of rental date. Please input the number of days from today: "))
        inputReturnDate = int(input("Rental duration: "))
        newRentDate, newReturnDate = self._bookingService.getRentalDates(inputRentDate, inputReturnDate)
        self._bookingService.getNewRentDateBookingList(newRentDate, newReturnDate, bookingId) 
        print("\nThe new rent date is ", newRentDate) 
        print("\nThe new rent date is ", newReturnDate)

    def getNewCar(self, bookingId):
        newCarID = input("New car ID: ") 
        self._bookingService.changeCar(bookingId, newCarID)
        print("\nCar has been changed to {} for {}\n".format(newCarID, bookingId))

    def cancelBooking(self, bookingId):
        self._bookingService.changeBookingStatus(bookingId)
        print("\nThe booking for {} has been canceled.\n". format(bookingId))

    def listBookings(self):
        print("\nLIST OF ALL BOOKINGS\n")
        print("_"*40, "\n")
        header = "{:^10}{:^10}{:^10}{:^10}{:^10}".format("Car ID", "Rent Date", "Return Date", "Rental Status", "Email")
        print(header, "\n")
        bookings = self._bookingService.getBookingList()
        for p in bookings:
            print(p)