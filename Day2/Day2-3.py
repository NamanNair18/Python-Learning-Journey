#Write a program to reverse a string without using built-in functions.

string = input("Enter the String:- ")

reversed_string ="" 

for i in range(len(string)-1,-1,-1):
    reversed_string += string[i]
print(f"Reversed String:- {reversed_string}")