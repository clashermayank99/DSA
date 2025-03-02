# Create an electric car class that inherits the car class and has an additional attribute battery_size

class Car():
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def full_name(self):
        return f"{self.brand} {self.model}"

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model) #To access the attributes for super class
        self.battery_size = battery_size

my_tesla = ElectricCar("Tesla","Model S", "85kWh")
print(my_tesla.brand, my_tesla.model, my_tesla.battery_size, my_tesla.full_name())