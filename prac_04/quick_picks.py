import random

# Constants for the number range and count of numbers per pick
NUMBERS_PER_PICK = 6
MIN_NUMBER = 1
MAX_NUMBER = 45


def main():
    """Generate and display quick picks based on user input."""
    quick_picks_count = int(input("How many quick picks? "))

    for _ in range(quick_picks_count):
        quick_pick = generate_quick_pick()
        print(" ".join(f"{num:2}" for num in quick_pick))  # Format numbers neatly


def generate_quick_pick():
    """Generate a single quick pick with unique, sorted numbers."""
    numbers = []

    while len(numbers) < NUMBERS_PER_PICK:
        num = random.randint(MIN_NUMBER, MAX_NUMBER)
        if num not in numbers:  # Ensure uniqueness
            numbers.append(num)

    numbers.sort()  # Sort in ascending order
    return numbers


main()
