class Car:

    def __init__(self, carId, carName, year, carType, price = 0, rentalStatus = "active"):
        self._carId = carId
        self._carName = carName
        self._year = year
        self._carType = carType
        self._price = price  #tengja price við carType og priceList
        self._rentalStatus = rentalStatus

    def __str__(self):
        return "{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}".format(self._carId, self._carName, self._year, self._carType,
            self._price, self._rentalStatus)
        
    def __repr__(self):
        return self.__str__()

    def getCarId(self):
        return self._carId

    def getCarName(self):
        return self._carName

    def getYear(self):
        return self._year

    def getCarType(self):
        return self._carType

    def getPrice(self):
        return self._price

    def getRentalStatus(self):
        return self._rentalStatus
