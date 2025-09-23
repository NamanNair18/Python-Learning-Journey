class dog:
    def __init__(self, name):
        self.name=name
    
    def display_name(self):
        print(f"Dog's Name:- {self.name}")

class labrador(dog): #Single Inheritance
    def sound(self):
        print("Labrador Woof")

class guideDog(labrador): #Multi-level Inheritance
    def guide(self):
        print(f"{self.name} guide the Way!")

class friendly:
    def greet(self):
        print("Friendly")

class GoldenRetriever(dog, friendly): #Multiple Inheritance
    def sound(self):
        print("Golden Retriver Barks")

lab = labrador("Buddy")
lab.display_name()
lab.sound()

guide_Dog = guideDog("Max")
guide_Dog.display_name() 
guide_Dog.guide()

retriver = GoldenRetriever("Rick")
retriver.display_name()
retriver.greet()
retriver.sound()
