# Classes and object

# Create a car class with attributes and create instance of this class
class Car1: #example 1
    brand = None #Called class attributes/Instances
    model = None

my_car1 = Car1()
my_car1.brand = "BMW"
my_car1.model = "Q5"

class Car2: #example 2
    def __init__(self,userBrand, userModel): #The first parameter of __init__ should always be self to refer itself, __init__ is called constructor
        self.brand = userBrand #Called instance attributes
        self.model = userModel

my_car2 = Car2("Toyota", "Corolla")
print(my_car2.brand, my_car2.model)

my_car3 = Car2("TATA", "Nexon")
my_car3.brand = "Audi"
my_car3.model = "E-Tron"
print(my_car3.brand, my_car3.model)

# Add to a method to the class that displays the full name of the class(with objects)
class Car3:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def fullDetails(self):
        return f"{self.brand} {self.model}"
    
my_car4 = Car3("Tesla","Model-S")
print("Full details",my_car4.fullDetails())