#Write a program to create a new text file and write "Hello, Python!" into it.
f = open("text.txt", "x")
f.write("Hello, Python!")
f.close()

f = open("text.txt", "r")
print(f.read())
f.close()