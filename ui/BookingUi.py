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

            action = input("Choose an option: ").lower()
            print()
            if action == "1":
                self.registerBooking()
            elif action == "2":
                self.searchBooking()
            elif action == "3":
                self.listBookings()
            elif action == "4":
                break
            else: 
                print("\nBooking - ERROR\n")
        

            
    def registerBooking(self):
        print("\nREGISTER A BOOKING\n")
        print("_"*40, "\n")
        tday = datetime.date.today()
        carID = input("Car ID: ")
        inputRentDate = int(input("Beginning of rental date. Please input the number of days from today: "))
        if inputRentDate == 0:
            rentDate = tday
        elif inputRentDate != 0:
            tdelta = datetime.timedelta(days=inputRentDate)
            rentDate = tday + tdelta
        inputReturnDate = int(input("Rental duration: "))
        if inputReturnDate != 0:
            rdelta = datetime.timedelta(days=inputReturnDate)
            returnDate = rentDate + rdelta
        else:
            print("Please select one day or more: ")
        bookingStatus = input("Status - (a)ctive or (c)ancel: ") #þetta þarf að útfæra betur
        customerID = input("Customer ID: ")
        #price = price listi
        

        newBooking = Booking(carID, rentDate, returnDate, bookingStatus, customerID)
        self._bookingService.addBooking(newBooking)
        

    def searchBooking(self):
        print("\nSEARCH FOR A BOOKING\n")
        print("_"*40, "\n")
        searchEmail = input("Customer email: ")
        bookingInfo = self._bookingService.getBooking(searchEmail)
        for attribute in bookingInfo:
            print(attribute)



    def listBookings(self):
        print("\nLIST ALL BOOKINGS\n")
        print("_"*40, "\n")
        header = "{:^10}{:^10}{:^10}{:^10}{:^10}".format("Car ID", "Rent Date", "Return Date", "Rental Status", "Email")
        print(header, "\n")
        bookings = self._bookingService.getBooking()
        for p in bookings:
            print(p)
            # {:^10}{:^10}{:^10}{:^10}{:^10}".format("Car ID", "Rent Date", "Return Date", "Rental Status", "Email")


    # def cancelBooking(self):
    #     searchEmail = input("Email: ")
    #     with open("data/Bookings.txt", "a+") as f:
    #         searchFile = f.readlines()
    #     for line in searchFile:
    #         if searchEmail in line: 
    #             if bookingStatus == "active":
    #                 bookingStatus = "cancel" #veit að þetta virkar ekki - á eftir að útfæra
    #     print("This is the current booking status: ", bookingStatus)
    # #self.backToBookingMenu()

    # def changeBooking(self):
    #     a_list = []
    #     searchEmail = input("Email: ")
    #     with open("data/Bookings.txt", "a+") as f:
    #         searchFile = f.readlines()
    #     for line in searchFile:
    #         a_list.append(line)
            
                

        # def backToBookingMenu(self):
        #     print("\n","_"*40, "\n")
        # print("{}\n".format("b - Back to booking menu"))
        # back = "yes"
        # while back != "b":
        #     back = input("Choose an option: ").lower()
        #     if back == "b":
        #         #self.mainMenu()
        #         break
        #     else:
        #         print("Please choose valid option.")