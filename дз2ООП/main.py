class Car:
    count = 0

    def __init__(self, name, mileage, country):
        self.name = name
        self.mileage = mileage
        self.country = country
        Car.count += 1

    def __eq__(self, other):
        if isinstance(other, Car):
            return self.country == other.country
        return False

    def reset_mileage(self):
        self.mileage = 0

    @classmethod
    def get_count(cls):
        return cls.count

def generate_cars(n):
    cars = []
    countries = ['США', 'Германия']
    names = ['BMW', 'Ford']
    for i in range(n):
        car = Car(names, i*1000, countries)
        cars.append(car)
    return cars

def sort_cars(cars_list):
    pass

cars = generate_cars(4)
print(Car.get_count())