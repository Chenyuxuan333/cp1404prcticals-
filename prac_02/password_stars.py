"""
cp1404 - Practical 2
password check program
"""

MIN_LENGTH = 10

def get_password():
    # Get password from user
    user_password = input("pleas enter your password: ")
    while len(user_password) < MIN_LENGTH:
        print(f"Password must be at least {MIN_LENGTH} characters long. Please try again.")
    return user_password

password = get_password()

def print_asterisks():
    # Print asterisks with length of password\
    print('*' * len(password))

print_asterisks()