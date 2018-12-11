from models.Car import Car
#from models.Booking import Booking

class CarRepository:

    def __init__(self):
        self._cars = [] 
        self._avilableCars = {}
        self._rentedCars = {}
        self._carDictionary = {} 

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
        if self._cars == []:
            try:
                with open("./data/cars.txt", "r") as carFile:
                    for line in carFile.readlines():
                        carId, carName, year, carType, price, rentalStatus = line.split(":")
                        newCar = Car(carId, carName, year, carType, price, rentalStatus)
                        self._cars.append(newCar)
            
            except FileNotFoundError:
                return []
        return self._cars

    def getAvilableCars(self):
        if self._avilableCars == {}:
            try:
                with open("./data/bookings.txt", "r") as bookingFile:
                    self._avilableCars = {}
                    for line in bookingFile.readlines():
                        carId, rentDate, returnDate, bookingStatus, customerEmail = line.split(":")
                        if rentDate not in self._avilableCars:
                            self._avilableCars[rentDate] = carId
                        else:
                            self._avilableCars[rentDate].add(carId)
                    
            except FileNotFoundError:
                return {}
        return self._avilableCars

    def getRentedCars(self):
        if self._rentedCars == {}:
            try:
                with open("./data/bookings.txt", "r") as bookingFile:
                    self._rentedCars = {}
                    for line in bookingFile.readlines():
                        carId, rentDate, returnDate, bookingStatus, customerEmail = line.split(":")
                        if (rentDate, returnDate) not in self._rentedCars:
                            self._rentedCars[(rentDate, returnDate)] = carId
                        else:
                            self._rentedCars[(rentDate, returnDate)].add(carId)
                    
            except FileNotFoundError:
                return {}
        return self._rentedCars

    def getCarDictionary(self):
        if self._carDictionary == {}:
            try:
                with open("./data/cars.txt", "r") as carFile:
                    #self._carDictionary = {}
                    for line in carFile.readlines():
                        carId, carName, year, carType, price, rentalStatus = line.split(":")
                        #allCars = Car(carId, carName, year, carType, price, rentalStatus)
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



##############################################################
