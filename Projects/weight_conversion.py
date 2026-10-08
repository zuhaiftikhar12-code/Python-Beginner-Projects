weight=float(input("Enter the weight: "))
unit=input("kilograms or pounds (K/L): ")
if unit=="K":
    weight=weight*2.205
    print(f"weight is {round(weight,2)} lbs")
elif unit=="L":
    weight/=2.205
    print(f"weight is {round(weight,2)} kg")
else:
    print(f"{unit}  is invalid unit")