from services.CarService import CarService
from services.BookingService import BookingService
from models.Car import Car
from os import system, name
from time import sleep
import datetime

class CarUi:

    def __init__(self):
        self._carService = CarService()
        self._bookingService = BookingService()

    def mainMenu(self):
        action = ""
        while(action != "7"):
            self.clear()
            print("\nCAR MENU")
            self.lineInHeader()
            carMenu = "\t{:<30}\n\t{:<30}\n\t{:<30}\n\t{:<30}\n\t{:<30}\n\t{:<30}\n\t{:<30}\n\t".format(
                "1 - View available cars", "2 - View rented cars", "3 - View all cars", "4 - Return a car",
                "5 - Search for a car", "6 - View price list", "7 - Main menu")
            print(carMenu)
            
            action = input("Choose an option: ")
            print()
            if action == "1":
                self.availableCars()
                self.backToCarMenu()
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
                self.clear()
                break
            else: 
                print("\nCar - ERROR\n")

    def availableCars(self):
        self.clear()
        print("\nAVAILABLE CARS:", datetime.date.today())
        self.lineInHeader()
        header = "\n{:<10}{:<10}{:<10}{:<10}".format("Car ID", "Name", "Year", "Type")
        print(header)
        carsAvailableToday = self._carService.isCarAvailableToday()
        for carId in carsAvailableToday:
            #print(carId, end = "")
            for i in carId:
                for j in i:
                    print(j, end = "")
                    carInfo = self._carService.searchForCarInformation(j)
                    for attribute in carInfo:
                        attribute = "{:^10}".format(attribute)
                        print(attribute, end = "")
            print()

    def rentedCars(self):
        self.clear()
        print("\nRENTED CARS:", datetime.date.today())
        self.lineInHeader()
        header = "\n{:<10}{:<10}{:<10}{:<10}".format("Car ID", "Name", "Year", "Type")
        print(header)
        carsRentedToday = self._carService.isCarRentedToday()
        for carId in carsRentedToday:
            for i in carId:
                print(i, end = "")
                carInfo = self._carService.searchForCarInformation(i)
                for attribute in carInfo:
                    attribute = "{:^10}".format(attribute)
                    print(attribute, end = "")
                print()
        self.backToCarMenu()

    def displayAllCars(self):
        self.clear()
        print("\nALL REGISTERED CARS AT NORDIC CAR RENTAL")
        self.lineInHeader()
        header = "{:>10}{:>10}{:>10}{:>10}{:>10}{:>20}".format("Car ID", "Name", "Year", "Type", "Price", "Rental Status")
        print(header, "\n")
        cars = self._carService.getAllCars()
        for car in cars:
            print(car, end="")
        self.backToCarMenu()
        self.mainMenu()

    def returnCar(self):
        self.clear()
        print("\nRETURN A CAR")
        self.lineInHeader()
        while True:
            carId = input("License plate (car ID): ")
            if self._carService.isCarListed(carId) == True:
                self._bookingService.returnCar(carId)
                print("\nThe car has been returned")
                break
            else:
                print("Please enter valid car Id.")
         
        self.backToCarMenu()

    def searchForCar(self):
        self.clear()
        print("\nSEARCH FOR A CAR")
        self.lineInHeader()
        while True:
            carId = input("License plate (car ID): ")
            if self._carService.isCarListed(carId) == True:
                header = "\n{:^10}{:^10}{:^10}".format("Name", "Year", "Type")
                print(header, "\n")
                carInfo = self._carService.searchForCarInformation(carId)
                for attribute in carInfo:
                    attribute = "{:^10}".format(attribute)
                    print(attribute, end = "")
                break
            else:
                print("Please enter valid car Id.")
        
        self.backToCarMenu()


    def displayPriceList(self):
        self.clear()
        print("\nPRICE LIST\n")
        header = "{:^10}{:^10}".format("Car type", "Price")
        print(header)
        self.lineInHeader()
        for price in self._carService.priceList():
            print("{:^10}{:^10}".format(price[0], price[1]))
        self.backToCarMenu()

    def lineInHeader(self):
        print("_"*80, "\n")

    def backToCarMenu(self):
        print()
        self.lineInHeader()
        print("{}\n".format("b - Back to Car menu"))
        back = "yes"
        while back != "b":
            back = input("Choose an option: ").lower()
            if back == "b":
                break
            else:
                print("Please enter valid option.")

    def clear(self): 
        # Virkni fyrir windows 
        if name == 'nt': 
            _ = system('cls') 
        #  Virkni fyrir Mac 
        else: 
            _ = system('clear')