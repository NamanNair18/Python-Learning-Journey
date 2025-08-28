#Write a program to calculate simple interest (Input: principal, rate, time).
Principal = int(input("Enter the principle Value:-"))
Rate = int(input("Enter The Rate:-"))
Time = int(input("Enter the Time period:-"))

SimpleIntrest = ( Principal * Rate * Time)/100
print(f"Simple Intrest :- {SimpleIntrest}")