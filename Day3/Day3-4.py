#Find the largest of three numbers entered by the user.
a = int(input("Enter The Value of a:- "))
b = int(input("Enter The Value of b:- "))
c = int(input("Enter The Value of c:- "))

if a>b and a>c :
    print(f"{a} is the Greatest number")
elif b>a and b>c:
    print(f"{b} is the Greatest number")
else:
    print(f"{c} is the Greatest number")