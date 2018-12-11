class Booking:
    
    def __init__(self, carID, rentDate, returnDate, bookingStatus, customerID):
        self._carID = carID
        self._rentDate = rentDate
        self._returnDate = returnDate
        bookingStatus = "active"
        self._bookingStatus = bookingStatus
        self._customerID = customerID


    def __str__(self):
        return "{}:{}:{}:{}:{}".format(self._carID, self._rentDate, self._returnDate, self._bookingStatus, self._customerID)

    def __repr__(self):
        return self.__str__()

    def getCarID(self):
        return self._carID

    def getRentDate(self):
        return self._rentDate

    def getReturnDate(self):
        return self._returnDate

    def getBookingStatus(self):
        return self._bookingStatus

    def getCustomerID(self):
        return self._customerID

