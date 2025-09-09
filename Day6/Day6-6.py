#Write a program to count the number of characters in a text file.

f = open("text.txt", "r")
content = f.read()  

char_count = len(content)

print(f"Total number of characters in the file: {char_count}")