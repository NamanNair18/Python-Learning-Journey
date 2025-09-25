#Demonstrate single inheritance and multiple inheritance with simple examples.
class A:
    def methodA(self):
        return "Class A"
    
class B(A):#single inheritance
    def methodB(self):
        return "Class B"
    
class C(B):#Multiple inheritance
    def methodC(self):
        return "Class C"

obj1 = B()
obj2 = C()

print(obj1.methodB())
print(obj1.methodA())

print(obj2.methodA())
print(obj2.methodB())
print(obj2.methodC())