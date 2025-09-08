#Create a function to check whether a string is a palindrome.
reversed_string=""
def palindrome(a: str):
    a = a.lower()
    if a == a[::-1]:
        print("Palindrome")
    else:
        print("not palindrome")
        
palindrome("Naman")