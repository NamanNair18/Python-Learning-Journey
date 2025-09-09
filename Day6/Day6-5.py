#Write a program to count the number of words in a text file.
f = open("text.txt", "r")
content = f.read()

words = content.split()

word_count = len(words)
print(f"Total No. of Words:- {word_count}")