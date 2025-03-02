# Class inheritence and isinstance() dunction
# Problem : Demonstrate the use isinstance() to check if my_tesla is and instance of Car or ElectricCar
class Car():
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def full_details(self):
        return f"{self.brand} {self.model}"
    def fuel_type(self):
        return "Petrol or Diesel"

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    def fuel_type(self):
        return "Electricity"

my_tesla = ElectricCar("Tesla", "Model S", "85kWh")

print(isinstance(my_tesla, Car))
print(isinstance(my_tesla, ElectricCar))