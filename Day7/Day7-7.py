#Demonstrate Polymorphism by overriding a method in the child class.
class Animal:
    def speak(self):
         return "Animal Speaks"

class duck(Animal):
    def speak(self):
        return "Kwaks!!!"

print(duck().speak())