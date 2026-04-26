class Book:
    def __init__(self, title, author, pages, year):
        self.title = title
        self.author = author
        self.pages = pages
        self.year = year

class Car:
    def __init__(self, name, model, year, color):
        self.name = name
        self.model = model
        self.year = year
        self.color = color

    def start(self):
        return 'Двигатель заведен'

class Fridge:
    def __init__(self, fabric, volume, model):
        self.fabric = fabric
        self.volume = volume
        self.model = model

    def open(self):
        return 'Дверца открыта'
    def close(self):
        return 'Дверца закрыта'
    def on(self):
        return 'Устройство включено'

class Person:
    def __init__(self, name, surname, age, number):
        self.name = name
        self.surname = surname
        self.age = age
        self.number = number

    def stand_up(self):
        return 'Встал'
    def sit(self):
        return 'Сел'

class House:
    def __init__(self, floors, square, rooms):
        self.floors = floors
        self.square = square
        self.rooms = rooms

    def count_price(self):
        one_m = 300
        return f'{self.square * one_m}$'

house1 = House(1, 120, 8)

print(house1.count_price())