import random as rnd
import numpy


class Transport:
    def __init__(self):
        self._coord_X = 0
        self._coord_Y = 0

    @property
    def coord_X(self):
        return self._coord_X

    @property
    def coord_Y(self):
        return self._coord_Y

    @coord_X.getter
    def coord_X(self):
        return self._coord_X

    @coord_Y.getter
    def coord_Y(self):
        return self._coord_Y

    @coord_X.setter
    def coord_X(self, X):
        if X >= -10 and X <= 10:
            self._coord_X = X

    @coord_Y.setter
    def coord_Y(self, Y):
        if Y >= -10 and Y <= 10:
            self._coord_Y = Y


class Car(Transport):
    def __init__(self):
        self.type = "Car"
        self._coord_X = 0
        self._coord_Y = 0
        self.is_dead = False
        self.id = False

    def move(self, X, Y):
        self._coord_X = X
        self._coord_Y = Y

    def boom(self):
        i = 0
        while True:
            x = rnd.randint(-10, 10)
            y = rnd.randint(-10, 10)
            i += 1
            if x == self._coord_X and y == self._coord_Y:
                print("Number of combinations = " + str(i))
                print("BOOOOMMM !!!!!!!")
                self.is_dead = True
                break


class Road:
    def __init__(self):
        self.road = numpy.zeros((20, 20))
        self.car_list = []

    def prindRoad(self):
        print(self.road)

    def set_car(self, car):
        car.id = len(self.car_list)
        self.car_list = car
        self.road[car.coord_X][car.coord_Y] = 1


car1 = Car()
road1 = Road()
road1.set_car(car1)
road1.prindRoad()
# Класс транспорт и класс машина.
# Машина может ехать по координатам.
# У машины должно быть от 5 характеристик.
# Машину можно взорвать динамитом.
