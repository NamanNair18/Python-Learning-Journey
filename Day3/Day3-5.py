#Check whether a given year is a leap year.
year = int(input("Enter the Year"))

if year % 400 == 0:
    print("leap year")
elif year % 100 == 0:
    print("Not a Leap Year")
elif year % 4 == 0:
    print("Leap Year")
else:
    print("Not a Leap Year")