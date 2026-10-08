operator = input("Enter the arithmatic operator (+,-,*,/): ")
num1 = int(input("Enter 1st num: "))
num2 = int(input("Enter 2nd num: "))

if operator == "+":
    result = num1 + num2
    print(f"The result = {result}")
elif operator == "-":
    result = num1 - num2
    print(f"The result = {result}")
elif operator == "*":
    result = num1 * num2
    print(f"The result = {result}")
elif operator == "/":
    result = num1 / num2
    print(f"The result = {result}")
else:
    print("Invalid operator")
