class Car:
    wheel = 4

    def __init__(self, brand, model):
        self.brand=brand
        self.model=model

Car1 = Car("Toyota", "Fortuner")
Car2 = Car("Tata", "Safari")


print(Car1.brand, end=" ")
print(Car1.model, end=" ")
print(Car1.wheel)

print(Car2.brand, end=" ")
print(Car2.model, end=" ")
print(Car2.wheel)


Car.wheel = 6
print(Car1.model, end=" ")
print(Car1.wheel)
print(Car2.model, end=" ")
print(Car2.wheel)

Car1.wheel = 8
print(Car1.model, end=" ")
print(Car1.wheel)