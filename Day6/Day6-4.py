#Write a program to count the number of lines in a text file.
f = open("text.txt", "r")
lines = f.readlines()
print("Total no. of lines:- ", len(lines))