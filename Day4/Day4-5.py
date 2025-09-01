#Write a program to calculate the factorial of a number.
num = int(input("Enter the number"))
factorial = 1

if num < 1:
    print("Factorial Cannot be of Negative number")

elif num == 0:
    print("Factorial of Zero is 1")

else:
    for i in range(1, num+1):
        factorial*= i
        print(f"Factorial of {num} is {factorial}")
