from models.Car import Car

class CarRepository:

    def __init__(self):
        self.__cars = []

    def add_car(self, car):
        # first add to file then to private list
        with open("./data/cars.txt", "a+") as cars_file:
            title = car.get_title()
            genre = car.get_genre()
            length = car.get_length()
            cars_file.write("{},{},{}\n".format(title, genre, length))

    def get_cars(self):
        if self.__cars == []:
            with open("./data/cars.txt", "r") as car_file:
                for line in car_file.readlines():
                    title, genre, length = line.split(",")
                    new_car = Car(title, genre, length)
                    self.__cars.append(new_car)

        return self.__cars
