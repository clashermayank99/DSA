# Create two classes Battery and Engine, and let the ElectricCar class inherit from both, demonstrating multiple inheritence.

class Car():
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
class Battery():
    def battery_info(self):
        return "Battery 50kWh"
        
class Engine():
    def engine_info(self):
        return "Engine V8"

class ElectricCar(Car, Battery, Engine):
    pass

my_tesla = ElectricCar("Tesla", "Model-S")
print(my_tesla.battery_info())
print(my_tesla.engine_info())