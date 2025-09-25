#Write a program to show method overriding (child class redefines parent’s method).
class animal:
    def sound(self):
        print("Animal Make Sounds")
class dog(animal):
    def sound(self):
        print("Dog Makes the Sound WOOF!!!")

print(dog().sound())