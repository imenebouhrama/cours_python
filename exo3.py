amount=float(input("Total amount:"))
items=int(input("Number of items:"))
day=str(input("Day of the week:")).lower()

if day in ["monday", "tuesday", "wednesday", "thursday", "friday"] :
    remise=0.1
elif day in ["sunday","saturday"] :
    remise=0.2

if items>5 :
    remise+=0.05

x=amount*remise
amount=amount-x

print("Total price after discount:",amount,"dinars")
 
