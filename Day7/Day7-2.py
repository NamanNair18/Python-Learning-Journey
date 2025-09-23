#Write a program with a constructor to initialize object values.
class Student:
    def __init__(self, name, age):
        self.name=name
        self.age=age

s1 = Student("Naman", 20)
s2 = Student("Ricky", 21)

print(s1.name, end=":- ")
print(s1.age)

print(s2.name, end=":- ")
print(s2.age)

