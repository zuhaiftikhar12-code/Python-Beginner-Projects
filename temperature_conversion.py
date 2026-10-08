temp = float(input("Enter temperature: "))
unit = input("Celcius or Fahrenheit (C/F): ")

if unit == "C":
    temp = (temp * 9) / 5 + 32
    unit = "F"
elif unit == "F":
    temp = (temp - 32) * 5 / 9
    unit = "C"
else:
    print(f"{unit} is Invalid unit")
print(f"temperature is {round(temp,2)}{unit}")
