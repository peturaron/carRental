class Car:

    def __init__(self, title, genre, length):
        self.__title = title
        self.__genre = genre
        self.__length = length

    def __str__(self):
        return "{},{},{}".format(self.__title, self.__genre, self.__length)

    def __repr__(self):
        return self.__str__()

    def get_title(self):
        return self.__title

    def get_genre(self):
        return self.__genre

    def get_length(self):
        return self.__length
