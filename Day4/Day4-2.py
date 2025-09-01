#Print the multiplication table of a number entered by the user.
num = int(input("Enter The Number:-"))
count = 1
while count <=10:
    print(f"{count}X{num} =",count*num)
    count+=1