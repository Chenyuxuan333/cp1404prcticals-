num_items = int(input("Numbers of items: "))

total_price = 0

for i in range(num_items):
    price = float(input(f"Price of item: "))
    total_price += price

if total_price > 100:
    total_price *= 0.9

print(f"Total price for {num_items} items is ${total_price:.2f}")