class Transport:
    def __init__(self):
        self.coord_X = 0
        self.coord_Y = 0

class Car(Transport):
    def __init__(self):
        self.type = "Car"

    def move(self,X,Y):
        self.coord_X = X
        self.coord_Y = Y