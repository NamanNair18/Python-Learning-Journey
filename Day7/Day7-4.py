#Create a class with public, protected, and private members and access them.
class Student:
    def __init__(self, name, marks, age):
        self.name = name
        self._marks = marks
        self.__age = age

    def get_info(self):
            return f"Name: {self.name}, Marks: {self._marks}, Age: {self.__age}"
        
    def get_age(self):
            return self.__age
        
    def set_age(self, age):
            if age>0:
                self.__age = age
            else:
                print("invalid age")

s1 = Student("Naman", 85, 21)

print(s1.name)
print(s1._marks)
print(s1.get_age())

s1.set_age(20)
print(s1.get_info())
        

