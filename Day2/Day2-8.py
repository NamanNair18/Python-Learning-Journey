#Write a program to count vowels and consonants in a string.

string = input("Enter the String:- ")
string = string.lower()

vowel = "aeiou"

vowel_count = 0
consonants_counts = 0

for ch in string:
    if ch.isalpha():
        if ch in vowel:
            vowel_count+=1
        else:
            consonants_counts+=1
print(f"Vowels:- {vowel_count}")
print(f"Consonansts:- {consonants_counts}")