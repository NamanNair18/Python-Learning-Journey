#Demonstrate Multiple Inheritance with an example.
class ClassA:
    def methodA(self):
        print("Class A")

class ClassB:
    def methodB(self):
        print("Class B")

class ClassC(ClassA, ClassB):
    def methodC(self):
        print("Class C")

obj = ClassC()
obj.methodA()
obj.methodB()
obj.methodC()

