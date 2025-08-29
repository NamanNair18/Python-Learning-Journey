#Concatenate two lists and remove duplicates.
number = [1,2,3,4,5]
even_number = [2,4,6,8,10]

combined_list = list(set(number+even_number))#first make it a set then covert it back to list 
print(combined_list)