#Write a program to copy contents of one file into another.

with open("text.txt", "r") as src:
    data = src.read()   

with open("destination.txt", "a") as dest:
    dest.write(data)

print("File copied successfully!")
