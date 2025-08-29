#Find the second largest element in a list.
number = [1,2,3,4,5]

largest = second_largest = float('-inf')

for num in number:
    if num > largest:
        second_largest = largest
        largest = num
    elif num> second_largest and num != largest:
        second_largest = num
print("largest Element:- ", largest)
print("Second largest Element:- ", second_largest)