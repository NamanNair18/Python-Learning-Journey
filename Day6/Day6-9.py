#Write a program to merge two text files into a third file.

with open("text.txt", "r") as f1:
    data1 = f1.read()

with open("destination.txt", "r") as f2:
    data2 = f2.read()

with open("merged.txt", "a") as f3:
    f3.write(data1 + "\n" + data2)

print("Files merged successfully into merged.txt!")
