from repositories.BookingRepository import BookingRepository
import datetime

class BookingService:
    def __init__(self):
        self._bookingRepo = BookingRepository()

    def addBooking(self, booking):
        return self._bookingRepo.addBooking(booking)

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

    def isRentDateValid(self, inputRentDate):
        if inputRentDate.isdigit():
            if int(inputRentDate) >= 0:
                return True

    def isReturnDateValid(self, inputReturnDate):
        if inputReturnDate.isdigit():
            if int(inputReturnDate) >= 1:
                return True

    def getRentalDates(self, inputRentDate, inputReturnDate):
        tday = datetime.date.today()
        if inputRentDate == 0:
            rentDate = tday
        elif inputRentDate != 0:
            tdelta = datetime.timedelta(days=inputRentDate)
            rentDate = tday + tdelta
        
        rdelta = datetime.timedelta(days=inputReturnDate)
        returnDate = rentDate + rdelta

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

    def getCustomerInformationForBooking(self):
        return self._bookingRepo.createCustomerDictionaryForBooking()

    def isCustomerListed(self, customerID):
        for customer in self._bookingRepo.createCustomerDictionaryForBooking().keys():
            if customer == customerID:
                return True

    def getCustomerDict(self, customerID):
        return self._bookingRepo.createCustomerDictionaryForBooking()[customerID]

    def getAvailableCarDict(self):
        return self._bookingRepo.getAvailableCars()