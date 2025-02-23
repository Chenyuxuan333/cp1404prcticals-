# 1. Number list
def main():
    """Collects 5 numbers from the user and displays statistical information."""
    numbers = []

    # Get 5 numbers from the user
    for i in range(5):
        number = float(input("Number: "))  # Use float to handle decimals if needed
        numbers.append(number)

    # Display required information
    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    print(f"The average of the numbers is {sum(numbers) / len(numbers):.1f}")

main()


# 2. List of authorized usernames
usernames = [
    'jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45',
    'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState',
    'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob'
]


def main():
    """Check if the entered username is authorized."""
    username = input("Enter your username: ")

    if username in usernames:
        print("Access granted")
    else:
        print("Access denied")


main()
