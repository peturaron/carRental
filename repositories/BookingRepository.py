from models.Booking import Booking

class BookingRepository:

    def __init__(self):
        self._booking = []
        
        self._bookingDictionary = {} #self.getCarDictionary()


    def addBooking(self, booking):
        # first add to file then to private list
        # active = True
        # inactive = False

        with open("./data/bookings.txt", "a+", encoding = "utf-8") as bookingFile:
            carID = booking.getCarID()
            rentDate = booking.getRentDate()
            returnDate = booking.getReturnDate()
            bookingStatus = booking.getBookingStatus()
            customerID = booking.getCustomerID()
            bookingFile.write("{}:{}:{}:{}:{}\n".format(carID, rentDate, returnDate, bookingStatus, customerID))

    def getBooking(self):
        if self._booking == []:
            with open("./data/bookings.txt", "r", encoding = "utf-8") as bookingFile:
                for line in bookingFile.readlines():
                    carID, rentDate, returnDate, bookingStatus, customerID = line.split(":")
                    newBooking = Booking(carID, rentDate, returnDate, bookingStatus, customerID)
                    self._booking.append(newBooking)

        return self._booking

    def getBookingDictionary(self):
        if self._bookingDictionary == {}:
            try:
                with open("./data/bookings.txt", "r") as bookingFile:
                    #self._bookingDictionary = {}
                    for line in bookingFile.readlines():
                        carID, rentDate, returnDate, bookingStatus, customerID = line.split(":")
                        bookingKey = carID
                        attributeList = self.createAttributeList(carID, rentDate, returnDate, bookingStatus, customerID)
                        self._bookingDictionary[bookingKey] = attributeList
                    return self._bookingDictionary
               
            except FileNotFoundError:
                return {}

    def createAttributeList(self, carID, rentDate, returnDate, bookingStatus, customerEmail):
        a_list = [carID, bookingStatus, customerEmail]
        return a_list

    def isValidBooking(self, bookingStatus):
        return bookingStatus
    
    def getBookingByReturnDate(self, returnDate):
        return returnDate