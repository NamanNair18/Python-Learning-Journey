#Check if a string is a palindrome.
string = input("Enter the String:- ")

string = string.lower()

reversed_string ="" 
for i in range(len(string)-1,-1,-1):
    reversed_string += string[i]

if string == reversed_string:
    print("Yes, It's a Palindrome")
else:
    print("No, it's Not a plaindrome ")