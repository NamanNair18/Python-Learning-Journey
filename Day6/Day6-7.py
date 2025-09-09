#Write a program that reads a file line by line and prints each line with its line number.
f = open("text.txt", "r")

for line_n , line in enumerate(f, start=1):
    print(f"line{line_n}: {line.strip()}")