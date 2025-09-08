#Write a function that takes a string and returns it reversed.
def reversed_string(string):
    rever_string = ""
    for i in range (len(string)-1,-1,-1):
        rever_string+=string[i]

reversed_string() 
