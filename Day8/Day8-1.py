#Create a Person class and inherit a Student class from it. Add methods to show details.
class person:
    def detail(self):
        print("Resident Of Cloral Woods.")

class student(person):
    def college(self):
        print("Student of JLU")


obj = student()
obj.detail()
obj.college()