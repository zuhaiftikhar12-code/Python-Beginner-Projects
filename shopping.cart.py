foods = []
prices = []
total = 0
while True:
    food = input("Enter the food and q to quit:")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of {food}: "))
        foods.append(food)
        prices.append(price)

print("----- Your Shopping Cart -----")

for f in foods:
    print(f)

print("----- Total Bill -----")
for p in prices:
    total += p

print(f"Total bill: {total}")

# ============= 2D collections ==================
# food = ["sugar", "salt", "rice"]
# vegies = ["peas", "carrot", "jinger", "garlic"]
# fruit = ["banana", "mangoe", "watermelon"]
# items = [food, vegies, fruit]

# for i in items:
#     for j in i:
#         print(j, end=" ")
#     print()
