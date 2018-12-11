from repositories.CarRepository import CarRepository
import datetime
#import time

class CarService:
    def __init__(self):
        self._carRepo = CarRepository()  #tilvik af klasanum fyrir neðan

    def addNewCar(self, car):
        # Eftir að útfæra, ekki hluti af kröfunum, eyða ef ekki útfært
        # if self.is_valid_car(car):
        #     self.__car_repo.add_car(car)  #köllum í fallið fyrir neðan og þar er gögnunum bætt við skrána
        return self._carRepo.addCarToFile(car)

    def is_valid_car(self, car):
        # Error check fyrir addNewCar.
        #here should be some code to
        #validate the car
        #error check, er lengdin ekki eins og hún á að vera
        #er titillinn ekki orð/valid strengur
        #ákveðið set af inputti sem er rétt sbr type
        return True

    def isCarListed(self, carId):
        for key in self._carRepo.getCarDictionary():
            if key == carId:
                return True

    def isCarAvailableToday(self):
        carList = []
        for dates, carId in self._carRepo.getAvilableCars().items():
            year = int(dates[0:4])
            month = int(dates[5:7])
            day = int(dates[-2:])
            newDate = datetime.date(year,month,day)
            nowDate = datetime.date.today()
            if nowDate < newDate:
                carList.append(carId)
        return carList

    def isCarRentedToday(self):
        carList = []
        for dates, carId in self._carRepo.getRentedCars().items():
            yearRented = int(dates[0][0:4])
            monthRented = int(dates[0][5:7])
            dayRented = int(dates[0][-2:])
            yearReturned= int(dates[1][0:4])
            monthReturned = int(dates[1][5:7])
            dayReturned = int(dates[1][-2:])
            rentDate = datetime.date(yearRented,monthRented,dayRented)
            returntDate = datetime.date(yearReturned,monthReturned,dayReturned)
            nowDate = datetime.date.today()
            if rentDate <= nowDate < returntDate:
                carList.append(carId)
        return carList


    def getAllCars(self):
        return self._carRepo.getCars()

    def searchForCarInformation(self, carId):
        return self._carRepo.getCarDictionary()[carId]    