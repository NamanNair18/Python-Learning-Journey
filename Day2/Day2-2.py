#Take a string input from the user and print its first and last character.

string = input("Enter The Input:-")

char_lst = list(string)
print(f"First Character :- {char_lst[0]}")
print(f"Last Character :- {char_lst[-1]}")