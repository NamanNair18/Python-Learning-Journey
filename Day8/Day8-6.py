#Create an example to demonstrate polymorphism using a common method across multiple classes.
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!!"

class Cat(Animal):
    def speak(self):
        return "Meow!!!"

class Duck(Animal):
    def speak(self):
        return "Kwak!!!"
    
def sound_animal(animal):
    print(animal.speak())

dog = Dog()
cat = Cat()
duck = Duck()

sound_animal(dog)
sound_animal(cat)
sound_animal(duck)