"ИНКУПСУЛЯЦИЯ"

class Person:
    def __init__(self):
        self._age = 0

    def set_age(self, age):
        if age < 0:
            print("Введите правильный возраст.")
        else:
            self._age = age

    def get_age(self):
        return f"Ваш возраст:{self._age}"

p = Person()
p.set_age(25)
#print(p.get_age())  # Вывод: 25
#p.set_age(-5)  # Должна быть ошибка или предупреждение

"НАСЛЕДОВАНИЕ"
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"I'm an animal"


class Dog(Animal):
    def speak(self):
        return "Woof"

class Cat(Animal):
    def speak(self):
        return "Meow"

dog = Dog("Buddy")
cat = Cat("Kitty")

#print(dog.name, dog.speak())  # Вывод: Buddy Woof
#print(cat.name, cat.speak())  # Вывод: Kitty Meow

"ПОЛИМОРФИЗМ"

class Vehicle:
    def move(self):
        return f"Vehicle is moving."

class Car(Vehicle):
    def move(self):
        return f"Car is driving."

class Bicycle(Vehicle):
    def move(self):
        return f"Bicycle is pedaling."

def move(vehicle):
    return vehicle.move()

car = Car()
bike = Bicycle()

#print(move(car))  # Вывод: Car is driving
#print(move(bike))  # Вывод: Bicycle is pedaling

"АБСТРАКЦИЯ"
from abc import ABC, abstractmethod
import math

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return round(math.pi * self.radius ** 2, 2)

rect = Rectangle(10, 5)
circle = Circle(7)
print(rect.area())  # Вывод: 50
print(circle.area())  # Вывод: ~153.94