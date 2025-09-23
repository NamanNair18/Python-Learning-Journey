#Write a program to create a simple class Car with attributes and methods.
class Car:
    def __init__(self, brand, model):
        self.brand=brand
        self.model=model

car1= Car("Toyota", "Fortuner")
car2= Car("Maruti", "Swift")

print(car1.brand, end=" ")
print(car1.model)

print(car2.brand, end=" ")
print(car2.model)