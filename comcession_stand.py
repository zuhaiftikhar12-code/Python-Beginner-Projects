menu = {
    "pizza": 3.00,
    "nachos": 4.00,
    "fries": 2.50,
    "chips": 3.00,
    "soda": 3.00,
    "lemonade": 4.00,
}

cart = []
total = 0
print("-------- Menu --------")
for key, value in menu.items():
    print(f"{key:10}:${value:.2f}")
print("----------------------")
while True:
    food = input("Enter the food (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("----- Your order -----")
for item in cart:
    total += menu.get(item)
    print(item, end=" ")

print()
print("----------------------")
print(f"total bill: ${total}")
print("----------------------")
