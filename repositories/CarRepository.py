from models.Car import Car

class CarRepository:

    def __init__(self):
        self._cars = [] 
        self._avilableCars = {}
        self._rentedCars = {}
        self._carDictionary = {} 
        self._priceList = []

    def addCarToFile(self, car):
        try:
            with open("./data/cars.txt", "a+") as carsFile:
                carId = car.getCarId()
                carName = car.getCarName()
                year = car.getYear()
                carType = car.getCarType()
                price = car.getPrice()
                rentalStatus = car.getRentalStatus()
                carsFile.write("{}:{}:{}:{}:{}:{}\n".format(carId, carName, year, carType, price, rentalStatus))
        except FileNotFoundError:
                print("File {} not found".format("./data/cars.txt"))

    def getCars(self):
        self._cars == []
        try:
            with open("./data/cars.txt", "r") as carFile:
                for line in carFile.readlines():
                    carId, carName, year, carType, price, rentalStatus = line.split(":")
                    newCar = Car(carId, carName, year, carType, price, rentalStatus)
                    self._cars.append(newCar)
        
        except FileNotFoundError:
            return []
        return self._cars

    def getAvailableCars(self):
        try:
            with open("./data/bookings.txt", "r") as bookingFile:
                self._avilableCars = {}
                for line in bookingFile.readlines():
                    carId, rentDate, returnDate, bookingStatus, customerEmail = line.split(":")
                    key = (rentDate, carId)
                    value = [carId]
                    self._avilableCars[key] = value
                    
                self.newDict = {}
                self.aList = []
                for keys, values in self._avilableCars.items():
                    keys = keys[0]
                    if keys in self.newDict:
                        self.dateList = self.newDict[keys]
                        self.dateList.append(values)
                    else:
                        self.dateList = [values]
                        self.newDict[keys] = self.dateList
                return self.newDict
        except FileNotFoundError:
            return {}
        

    def getRentedCars(self):
        self._rentedCars = {}
        try:
            with open("./data/bookings.txt", "r") as bookingFile:
                self._rentedCars = {}
                for line in bookingFile.readlines():
                    carId, rentDate, returnDate, bookingStatus, customerEmail = line.split(":")

                    valueList = [carId]
                    if (rentDate, returnDate) not in self._rentedCars:
                        self._rentedCars[(rentDate, returnDate)] = valueList
                    else:
                        valueList.append(carId)
                        self._rentedCars[(rentDate, returnDate)] = valueList


                    # if (rentDate, returnDate) not in self._rentedCars:
                    #     self._rentedCars[(rentDate, returnDate)] = carId
                    # else:
                    #     self._rentedCars[(rentDate, returnDate)].add(carId)
                
        except FileNotFoundError:
            return {}
        return self._rentedCars

    def getCarDictionary(self):
        self._carDictionary = {}
        try:
            with open("./data/cars.txt", "r") as carFile:
                for line in carFile.readlines():
                    carId, carName, year, carType, price, rentalStatus = line.split(":")
                    carKey = carId
                    attributeList = self.createAttributeList(carName, year, carType)
                    self._carDictionary[carKey] = attributeList
                return self._carDictionary
            
        except FileNotFoundError:
            return {}

        return self._carDictionary

    def createAttributeList(self, carName, year, carType):
        aList = [carName, year, carType]
        return aList

    def getPriceList(self):
        self._priceList = []
        try:
            with open("./data/price.txt", "r", encoding = "utf-8") as priceFile:
                for line in priceFile.readlines():
                    carType, price = line.strip().split(":")
                    attributes = [carType, price] 
                    self._priceList.append(attributes) 
        except FileNotFoundError:
            return []
        return self._priceList

