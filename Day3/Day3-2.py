#Write a program to check whether a number is even or odd.
num = int(input("Enter the Number"))
if num > 0:
    if num % 2 == 0:
        print("Positive even number")
    else:
        print("Positive odd number")
else:
    print("Number is not positive")