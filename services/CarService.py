from repositories.CarRepository import CarRepository
import datetime

class CarService:
    def __init__(self):
        self._carRepo = CarRepository()

    def isCarListed(self, carId):
        for key in self._carRepo.getCarDictionary():
            if key == carId:
                return True

    def isCarAvailableToday(self):
        carList = []
        for dates, carId in self._carRepo.getAvailableCars().items():
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

    def priceList(self): 
        return self._carRepo.getPriceList()
    