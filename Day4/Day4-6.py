#Create a simple number guessing game
secret_num = 25
print("Guess a number between 1-100")

while True:
    guess = int(input("Enter The Guess:-"))

    if guess<secret_num:
        print("Guessed number is to low..")
    elif guess>secret_num:
        print("Guessed number is to high...")
    else:
        print("Congeadulations You guessed the Right Number.....")