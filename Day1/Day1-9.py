#A shopkeeper gives 18% GST on a product. Take cost price as input, calculate final price including GST.
CostPrice = int(input("Enter the Cost Price:- "))
GstRate = 0.18

GSTAmount = CostPrice * GstRate
FinalPrice = CostPrice + GSTAmount
print("GST Rate :- 18% ")
print(f"GST Amount({GSTAmount}) = Cost Price({CostPrice}) X GST Rate({GstRate}) ")
print(f"Final PRice({FinalPrice}) = Cost Price({CostPrice}) + GST Amount({GSTAmount})")