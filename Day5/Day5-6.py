#Write a function to find the greatest of three numbers.
def greatest(a,b,c):
    if a>b and a>c:
        print(f"{a} is the greatest number")
    elif b>a and b>c:
        print(f"{b} is the greatest number")
    else:
        print(f"{c} is the greatest number")

greatest(10,20,15)