# Use a property decorator in the class Car to make the model read-only
class Car():
    def __init__(self, brand, model):
        self.brand = brand
        self.__model = model
    
    def full_name(self):
        return f"{self.brand} {self.__model}"

    @staticmethod
    def statiq_method():
        pass

    @property #this decorator to hide the property : doubt
    def model(self):
        return self.__model

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

my_car = Car("TATA","PUNCH")
# my_car.model = "Tiago" #So we have changed the value of model, we need to stop this

print(my_car.model)