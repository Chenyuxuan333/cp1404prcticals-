"""
CP1404/CP5632 - Practical
Capitalist Conrad wants a stock price simulator for a volatile stock.
The price starts off at $1.00, and, at the end of every day there is
a 50% chance it increases by 0 to 17.5%, and
a 50% chance that it decreases by 0 to 5%.
If the price rises above $100, or falls below $1, the program should end.
The price should be displayed to the nearest cent (e.g. $33.59, not $33.5918232901)
"""
import random

MAX_INCREASE = 0.175  # 17.5%
MAX_DECREASE = 0.05  # 5%
MIN_PRICE = 1.00
MAX_PRICE = 100.00
INITIAL_PRICE = 10.00
FILENAME = "stock_prices.txt"

out_file = open(FILENAME, 'w')
price = INITIAL_PRICE
day = 0
print(f"Initial price: ${price:,.2f}", file=out_file)

while MIN_PRICE <= price <= MAX_PRICE:
    day += 1
    if random.randint(0, 1) == 0:
        price_change = random.uniform(0, MAX_INCREASE)
        price *= (1-price_change)
    else:
        price_change = random.uniform(0, MAX_DECREASE)
        price *= (1-price_change)

    print(f"On day {day} price is: ${price:.2f}", file=out_file)

out_file.close()
print(f"Simulation complete. Result saved to {FILENAME}.")