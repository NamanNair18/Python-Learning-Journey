#A user enters their name and age. Print:
#"Hello <name>, you will turn 100 years old in the year <YYYY>". 
from datetime import date

name = (input("Enter Your Name:- "))
age = int(input("Enter Your Age:- "))

current_year = date.today().year
years_to_100 = 100 - age
year_turn_100 = current_year + years_to_100

print(f"Hello {name}, you will turn 100 year old in the year {year_turn_100} ")