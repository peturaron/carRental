from repositories.CarRepository import CarRepository


class CarService:
    def __init__(self):
        self._carRepo = CarRepository()  #tilvik af klasanum fyrir neðan

    def addNewCar(self, car):
        # if self.is_valid_car(car):
        #     self.__car_repo.add_car(car)  #köllum í fallið fyrir neðan og þar er gögnunum bætt við skrána
        return self._carRepo.addCarToFile(car)

    def is_valid_car(self, car):
        #here should be some code to
        #validate the car
        #error check, er lengdin ekki eins og hún á að vera
        #er titillinn ekki orð/valid strengur
        #ákveðið set af inputti sem er rétt sbr type
        return True

    def getAllCars(self):
        return self._carRepo.getCars()

    def searchForCarInformation(self, carId):
        return self._carRepo.getCarDictionary()[carId]

    