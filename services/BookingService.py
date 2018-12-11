from repositories.BookingRepository import BookingRepository

class BookingService:
    def __init__(self):
        self._bookingRepo = BookingRepository()

    def addBooking(self, booking):
        if self.isValidBooking(booking):
            self._bookingRepo.addBooking(booking)

    def isValidBooking(self, bookingStatus):
        return True
        # if bookingStatus == "a":
        #     return self._bookingRepo.isValidBooking(bookingStatus)

    def getBooking(self):
        return self._bookingRepo.getBooking()

    def getBookingByReturnDate(self, returnDate):
        return self._bookingRepo.getBookingByReturnDate(returnDate)
