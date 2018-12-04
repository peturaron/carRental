from services.CarService import CarService
from models.Car import Car

class SalesmanUi:

    def __init__(self):
        self.__car_service = CarService()

    def main_menu(self):

        action = ""
        while(action != "q"):
            print("You can do the following: ")
            print("1. Add a video")
            print("2. List all videos")
            print("press q to quit")

            action = input("Choose an option: ").lower()

            if action == "1":
                title = input("Movie title: ")
                genre = input("Genre: ")
                length = input("Length in minutes: ")
                new_car = Car(title, genre, length)
                self.__car_service.add_car(new_car)

            elif action == "2":
                cars = self.__car_service.get_cars()
                print(cars)
