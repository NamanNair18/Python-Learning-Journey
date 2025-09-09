#Write a program to read the contents of a file and display it on the screen.
f = open("text.txt", "r")
print(f.read())
f.close()