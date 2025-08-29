#Rotate a list by k positions.
lst = [1,2,3,4,5]
k = 2

n = len(lst)
k = k%n

rotated = [0]*n

for i in range(n):
    rotated[(i+k)%n]=lst[i]

print("original lst", lst)
print( f"List after rotating by {k} positions (right):", rotated)
