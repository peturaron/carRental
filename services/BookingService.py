from repositories.BookingRepository import BookingRepository
import datetime

class BookingService:
    def __init__(self):
        self._bookingRepo = BookingRepository()

    def addBooking(self, booking):
        return self._bookingRepo.addBooking(booking)
        
    # def getBooking(self, searchEmail):
    #     return self._bookingRepo.getBookingDictionary()[searchEmail]

    def getBookingList(self):
        return self._bookingRepo.getBooking()

    def getBookingByReturnDate(self, returnDate):
        return self._bookingRepo.getBookingByReturnDate(returnDate) 

    def isBookingListed(self, bookingId):
        for key in self._bookingRepo.getBookingDictionary():
            if key == bookingId:
                return True

    def searchForBookingInformation(self, bookingId):
        return self._bookingRepo.getBookingDictionary()[bookingId] 

    def getRentalDates(self, inputRentDate, inputReturnDate):
        tday = datetime.date.today()
        if inputRentDate == 0:
            rentDate = tday
        elif inputRentDate != 0:
            tdelta = datetime.timedelta(days=inputRentDate)
            rentDate = tday + tdelta
        
        if inputReturnDate != 0:
            rdelta = datetime.timedelta(days=inputReturnDate)
            returnDate = rentDate + rdelta
        else:
            print("Please select one day or more: ")
        return rentDate, returnDate

    def getNewRentDateBookingList(self, newRentDate, newReturnDate, bookingId):
        newList = []
        for bookings in self._bookingRepo.getBookingList():
            for attribute in bookings:
                if bookings[4] == bookingId:
                    bookings[1] = str(newRentDate)
                    bookings[2] = str(newReturnDate)
                    newString = ":".join(bookings)
                else:
                    newString = ":".join(bookings)
            newList.append(newString)
        self._bookingRepo.readNewListToFile(newList)

    def changeCar(self, bookingId, newCarID):
        newList = []
        for bookings in self._bookingRepo.getBookingList():
            for attribute in bookings:
                if bookings[4] == bookingId:
                    bookings[0] = newCarID
                    newString = ":".join(bookings)
                else:
                    newString = ":".join(bookings)
            newList.append(newString)
        self._bookingRepo.readNewListToFile(newList)

    def changeBookingStatus(self, bookingId):
        newList = []
        for bookings in self._bookingRepo.getBookingList():
            for attribute in bookings:
                if bookings[4] == bookingId:
                    bookings[3] = "cancel"
                    newString = ":".join(bookings)
                else:
                    newString = ":".join(bookings)
            newList.append(newString)
        self._bookingRepo.readNewListToFile(newList)

    def getCarPrice(self, carId):
        return self._bookingRepo.createCarPriceDictionary()[carId]