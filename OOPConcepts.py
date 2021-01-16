class Animal:
    def __init__(self, type, name, color):
        self.type = type  # public
        self._name = name  # protected
        self.__color = color  # private

    def eat(self):
        print(self._name + " eat something")

    def set_color(self, color):
        if (color == "red"):
            self.__color = color
        else:
            return 0

    def get_color(self):
        return self.__color


class Cat(Animal):
    def __init__(self,tail, ear, eyes):
        self.color_tail = tail
        self.color_ear = ear
        self.color_eyes = eyes

    def eat(self):
        print(self._name + " eat fish meat")
        super().eat()  # eat for Animal(parent)


cat1 = Cat("white", "white", "black")
animal = Animal("Cat", "Jun", "White")
animal.set_color("red")
print(animal.get_color())

cat1.get_color()
cat1.set_color()

animal.eat()
cat1.eat()






