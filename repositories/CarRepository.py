from models.Car import Car
#from models.Booking import Booking

class CarRepository:

    def __init__(self):
        self._cars = [] #self.getCars() 
        self._avilableCars = self.getAvilableCars()
        self._rentedCars = self.getRentedCars()
        self._carDictionary = {} #self.getCarDictionary()

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
        #Hér þarf að tengja car og booking klasana

        # if self._cars == []:
        #     with open("./data/bookings.txt", "r") as bookingFile:
        #         for line in bookingFile.readlines():
        #             carId, rentDate, returnDate, bookingStatus, customerEmail = line.split(":")
        #             #carAvilable = Booking(carId, rentDate, returnDate, bookingStatus, customerEmail)
        #             #Hér þarf að tengja booking klasann og vinna með date.  
        #             self._avilableCars.append(carAvilable)
        # return self._cars
        self._avilableCars = [["EF A45", "Toyota", "medium"], ["EF A45", "Toyota", "medium"]]
        return self._avilableCars


    def getRentedCars(self):
        #Hér þarf að tengja car og booking klasana
        self._rentedCars = ["UK M23", "Toyota"]
        return self._rentedCars

    def getCarDictionary(self):
        if self._carDictionary == {}:
            try:
                with open("./data/cars.txt", "r") as carFile:
                    #self._carDictionary = {}
                    for line in carFile.readlines():
                        carId, carName, year, carType, price, rentalStatus = line.split(":")
                        allCars = Car(carId, carName, year, carType, price, rentalStatus)
                        carKey = carId
                        attributeList = self.createAttributeList(carName, year, carType)
                        self._carDictionary[carKey] = attributeList
                    return self._carDictionary
                
            except FileNotFoundError:
                return {}

        return self._carDictionary

    def createAttributeList(self, carName, year, carType):
        a_list = [carName, year, carType]
        return a_list


##############################################################



# car_repo = CarRepository()
# cars = car_repo.getCars()
# print(cars)
