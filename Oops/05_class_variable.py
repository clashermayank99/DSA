# Add a class variable to Car that keeps track of the number of cars created.
class Car():
    total_car = 0
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        Car.total_car += 1

    def full_name(self):
        return f"{self.brand} {self.model}"
    
my_car = Car("Audi", "E-Tron")
my_car2 = Car("BMW", "Q3")
print(my_car.total_car)

test = Car("test","test")
print(test.total_car) # instance atrribute, incorrect way it may give wrong value
print(Car.total_car) # class atribute, We should always use class attributes instaed of instance attributes for these operations