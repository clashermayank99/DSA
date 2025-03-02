# Modify the car class to encapsulate the brand attributes, making it private, and provide a Getter method for it
class Car():
    def __init__(self, brand, model):
        self.__brand = brand #dunder to make attribute private, only class members can access it
        self.model = model

    def get_brand(self):
        return self.__brand
    # def chai_brand(self):

    
    def full_name(self):
        return f"{self.__brand} {self.model}"
    
my_car = Car("TATA","SAFARI")
# print(my_car.__brand) #Since we are using dunder we can't access it directly
print(my_car.get_brand()) #Now we can access it through the method