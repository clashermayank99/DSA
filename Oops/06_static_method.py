# Static methos is also called decorators
# Add a static method to the car class that returns a general description of a car.

class Car():
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def general_description1(self):
        return "Cars are means of transport."
    def general_description2():
        return "Cars are means of transport.."
    
    @staticmethod # learn about these
    def statiq_method():
        pass
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(selfresult):
        return "Electric Charge"
my_car = Car("TATA","Nexon")
print(my_car.general_description1()) #At instance level method can only be accessed with self
print(Car.general_description2()) #At Class level methods can be accessed only without self

# Learn static method again in python from scratch
# Here is the learning - statiq method is a normal method which is defined inside a class and can be accessed independently, so we dont need to use self
class Math():
    def __init__(self, num1):
        self.num1 = num1
    def addTwoNums(self, n):
        self.num1 = self.num1 + n
    @staticmethod
    def add(a, b):
        return a+b

a = Math(5)
print(a.num1)
a.addTwoNums(6)
print(a.num1)

# calling statiq method
print(a.add(10,20))
print(Math.add(20,30))