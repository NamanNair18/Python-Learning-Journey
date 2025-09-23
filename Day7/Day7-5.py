#Demonstrate Single Inheritance with an example.
class animal:
    def sound(self):
        print("Animal makes a sound")

class dog(animal):
    def barks(self):
        print("Dog Barks")

d1 = dog()
d1.barks()
d1.sound()