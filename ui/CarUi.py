from services.CarService import CarService
from models.Car import Car
from repositories.CarRepository import CarRepository  #sett inn til að ná í lista af available cars.eyða þegar lagað

class CarUi:

    def __init__(self):
        self._carService = CarService()
        self._carRepo = CarRepository()

    def mainMenu(self):
        action = ""
        while(action != "3"):
            print("\nCAR MENU")
            print("_"*40, "\n")
            carMenu = "\t{:<30}\n\t{:<30}\n\t{:<30}\n\t{:<30}\n\t{:<30}\n\t{:<30}\n\t{:<30}\n\t{:<30}\n\t".format(
                "1 - View available cars", "2 - View rented cars", "3 - View all cars", "4 - Return a car",
                "5 - Search for a car", "6 - View price list", "7 - Register new car", "8 - Main menu")
            print(carMenu)
            
            action = input("Choose an option: ")
            print()
            if action == "1":
                self.availableCars()
            elif action == "2":
                self.rentedCars()
            elif action == "3":
                self.displayAllCars()
            elif action == "4":
                self.returnCar()
            elif action == "5":
                self.searchForCar()
            elif action == "6":
                self.displayPriceList()
            elif action == "7":
                self.addNewCar()
            elif action == "8":
                break
            else: 
                print("\nCar - ERROR\n")

    def availableCars(self):
        print("\nAVAILABLE CARS")
        print("_"*40, "\n")
        header = "{:^10}{:^10}{:^10}".format("Car ID", "Name", "Type")
        print(header, "\n")
        #Hér þarf að kalla á lista af lausum bílum. Tengja car og booking klasana
        #Eftirfarandi kóði er til prufu, er ekki listi úr database.
        avilableCars = self._carRepo.getAvilableCars()
        for car in avilableCars:
            for attribute in car:
                attribute = "{:^10}".format(attribute)
                print(attribute, end="")
            print()

    #Hér mætti raða bílunum eftir stærð eða láta velja alla/small/medium/large áður en bílarnir eru kallaðir fram

        self.backToCarMenu()

    def rentedCars(self):
        print("\nRENTED CARS\n")
        print("_"*40, "\n")
        header = "{:^10}{:^10}".format("Car ID", "Name")
        print(header, "\n")
        #Hér þarf að kalla á lista af rented cars. Tengja car og booking klasana
        #Eftirfarandi kóði er til prufu, er ekki listi úr database.
        rentedCars = self._carRepo.getRentedCars()
        for car in rentedCars:
            car = "{:^10}".format(car)
            print(car, end="")

        self.backToCarMenu()

    def displayAllCars(self):
        print("\nALL REGISTERED CARS AT NORDIC CAR RENTAL\n")
        print("_"*40, "\n")
        header = "{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}".format("Car ID", "Name", "Year", "Type", "Price", "Rental Status")
        print(header, "\n")
        #Hér prentast listinn skv. formati í car class: def __repr__(self).
        #Prentast sem listi en ekki stökin úr listanum.  þarf að skoða.
        cars = self._carService.getAllCars()
        # for car in cars:
        #     #car = "{:<10}".format(car)
        #     print(car, end="")
        print(cars)

        self.backToCarMenu()
        self.mainMenu()


    def returnCar(self):
        print("\nRETURN A CAR\n")
        print("_"*40, "\n")
        carId = input("License plate (car ID): ")

        #Þennan klasa á eftir að útfæra
        #Hér þarf að sækja booking og skila.  Breyta status í inactive.

        # carName = input("Car name: ")
        # carType = input("Car type: ")

        self.backToCarMenu()

    def searchForCar(self):
        #Þennan klasa má útfæra eins fyrir search customer og search booking.
        print("\nSEARCH FOR A CAR\n")
        print("_"*40, "\n")
        carId = input("License plate (car ID): ")

        carInfo = self._carService.searchForCarInformation(carId)
        for attribute in carInfo:
            print(attribute)
        
        self.backToCarMenu()


    def displayPriceList(self):
        print("\nPRICE LIST\n")
        print("_"*40, "\n")
        #Þennan klasa á eftir að útfæra.

    def addNewCar(self):
        print("\nADD NEW CAR\n")  
        print("_"*40, "\n")
        carId = input("License plate (car ID): ")  #villuprófa?
        carName = input("Car name: ").title()  #villuprófun: á bara að vera str.
        year = input("Year: ")
        carType = input("Car type(small/medium/large): ").lower()   #villuprófun: ef ekki small/medium/large þá villa.  þetta er tengist price og því mikilvægt.
        #carMilage = int(input("Milage(km): "))    #Ekki breyta

        newCar = Car(carId, carName, year, carType)
        self._carService.addNewCar(newCar)
        
        self.backToCarMenu()

    def backToCarMenu(self):
        print("\n","_"*40, "\n")
        print("{}\n".format("b - Back to Car menu"))
        back = "yes"
        while back != "b":
            back = input("Choose an option: ").lower()
            if back == "b":
                #self.mainMenu()
                break
            else:
                print("Please choose valid option.")


    #Eftir að útfæra Function til að velja breyta/remove car.

##############################################################
# car = CarUi()
# car.mainMenu()