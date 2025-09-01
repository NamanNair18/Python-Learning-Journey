#Print the sum of first N natural numbers (user input N).
N = int(input("Enter The Number:- "))

i = 1
total  = 0
while i<=N:
    total+=i
    print(total)
    i+=1