from models.Booking import Booking

class BookingRepository:

    def __init__(self):
        self._booking = []
        self._bookingDictionary = {}
        self._carPriceDict = {}
        self._customerDictionary = {}
        self._priceList = []

    def addBooking(self, booking):
        with open("./data/bookings.txt", "a+", encoding = "utf-8") as bookingFile:
            carID = booking.getCarID()
            rentDate = booking.getRentDate()
            returnDate = booking.getReturnDate()
            bookingStatus = booking.getBookingStatus()
            customerID = booking.getCustomerID()
            bookingFile.write("{}:{}:{}:{}:{}\n".format(carID, rentDate, returnDate, bookingStatus, customerID))

    def getBooking(self):
        if self._booking == []:
            try:
                with open("./data/bookings.txt", "r", encoding = "utf-8") as bookingFile:
                    for line in bookingFile.readlines():
                        carID, rentDate, returnDate, bookingStatus, customerID = line.strip().split(":")
                        newBooking = Booking(carID, rentDate, returnDate, bookingStatus, customerID)
                        self._booking.append(newBooking)
            except FileNotFoundError:
                return []
        return self._booking

    def getBookingList(self):
        if self._booking == []:
            try:
                with open("./data/bookings.txt", "r", encoding = "utf-8") as bookingFile:
                    for line in bookingFile.readlines():
                        carID, rentDate, returnDate, bookingStatus, customerID = line.strip().split(":")
                        newBooking = [carID, rentDate, returnDate, bookingStatus, customerID]
                        self._booking.append(newBooking)
            except FileNotFoundError:
                return []

        return self._booking

    def readNewListToFile(self, newList):
        myFile = open("./data/bookings.txt", "w", encoding = "utf-8")
        for line in newList:
            myFile.write(line)
            myFile.write("\n")
        myFile.close()

    def getBookingDictionary(self):
        try:
            with open("./data/bookings.txt", "r") as bookingFile:
                for line in bookingFile.readlines():
                    carID, rentDate, returnDate, bookingStatus, customerID = line.strip().split(":")
                    bookingKey = customerID
                    attributeList = self.createAttributeList(carID, rentDate, returnDate, bookingStatus)
                    self._bookingDictionary[carID] = attributeList
                    self._bookingDictionary[bookingKey] = [carID, rentDate, returnDate, bookingStatus]
                return self._bookingDictionary
               
        except FileNotFoundError:
            return {}

    def createAttributeList(self, carID, rentDate, returnDate, bookingStatus):
        a_list = [carID, rentDate, returnDate, bookingStatus]
        return a_list

    def isValidBooking(self, bookingStatus):
        return bookingStatus
    
    def getBookingByReturnDate(self, returnDate):
        return returnDate

    def createCarPriceDictionary(self):
        self._carPriceDict = {}
        try:
            with open("./data/cars.txt", "r", encoding = "utf-8") as carFile:
                for line in carFile.readlines():
                    carId, name, year, carType, price, rentalStatus = line.strip().split(":")
                    self._carPriceDict[carId] = price
        except FileNotFoundError:
            return []
        return self._carPriceDict

    def createCustomerDictionaryForBooking(self):
        self._customerDictionary = {}
        try:
            with open("./data/customers.txt", "r", encoding = "utf-8") as customerFile:
                for line in customerFile.readlines():
                    customerID, name, dateOfBirth, gender, dateOfReg, payMethod, cardNo, status = line.strip().split(":")
                    self._customerDictionary[customerID] = [name, dateOfBirth, gender, dateOfReg, payMethod, cardNo, status]  
        except FileNotFoundError:
            return []
        return self._customerDictionary
