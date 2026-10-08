principal = 0
rate = 0
time = 0

while True:
    principal = float(input("Enter the principal amount: "))
    if principal < 0:
        print("principle amount can't be less than zero")
    else:
        break

while True:
    rate = float(input("Enter the  interest rate: "))
    if rate < 0:
        print("interest rate can't be less than zero")
    else:
        break

while True:
    time = int(input("Enter the time in years: "))
    if time < 0:
        print("time can't be less than zero")
    else:
        break
print(f"principal: {principal}")
print(f"rate: {rate}")
print(f"time: {time}")
total = principal * pow((1 + rate / 100), time)
print(f"total compound interset after {time} years : ${total:.2f}")
