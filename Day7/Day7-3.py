#Demonstrate the difference between instance methods, class methods, and static methods.
class Student:
    college = "JLU"

    def __init__(self, name, marks):
        self.name=name
        self.marks=marks
        
    @classmethod
    def show_college(cls):
        return f"college is {cls.college}"
    
    def show_name(self):
        return f"name: {self.name}"
    
    @staticmethod
    def is_pass(marks):
        return marks >= 45

s1 = Student("naman", 83)
s2  =Student("Ricky", 40)

print(Student.show_college())
print(s1.show_name())
print(Student.is_pass(s1.marks))
print(s2.show_name())
print(Student.is_pass(s2.marks))

    