"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
def calculate_bonus():
    try:
        while True:
            sales = float(input("Enter sales: $"))

            if sales < 0:
                print("Exiting program.")
                break

            if sales < 1000:
                bonus_rate = 0.10
            else:
                bonus_rate = 0.15

            bonus = sales * bonus_rate

            print(f"Your bonus is: ${bonus:.2f}")

    except ValueError:
        print("Invalid input. Please enter a valid number for the sales amount.")
calculate_bonus()


