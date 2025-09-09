#Append "This is an appended line." to an existing file and then print the full content.
f= open("text.txt", "a")
f.write("\nThis is an appended Line.")
f.close()

f = open("text.txt", "r")
print(f.read())
f.close()