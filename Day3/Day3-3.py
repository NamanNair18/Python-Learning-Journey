#Take a user’s age as input and print if they are Child, Teen, Adult, or Senior.
age = int(input("Enter Your Age:- "))

if age >=0 and age <=12:
    print("You Are a Child")
elif age>=13 and age<=19:
    print("You are a Teen")
elif age>=20 and age<=59:
    print("You are a Adult")
elif age>=60:
    print("You are A senior")
else:
    print("invalid Age")