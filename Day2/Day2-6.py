#Find the maximum and minimum element in a list without using max() or min().
lst = [3,9,5,6,1,8,2]

maximum = lst[0]
minimum = lst[0]

for num in lst:
    if num > maximum:
        maximum = num
    if num < minimum:
        minimum = num
print(f"Maximum Value:- {maximum}")
print(f"Minimum Value:- {minimum}")
