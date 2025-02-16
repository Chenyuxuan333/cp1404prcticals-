"""cp1404 prac 3"""

# Ask for user's name and write it to name.txt
name = input("Enter your name: ")
with open("name.txt", "w") as file:
    file.write(name)

    # Read the name from name.txt and print greeting
with open("name.txt", "r") as file:
    name = file.read().strip()
print(f"Hi {name}!")

# Read the first two numbers from numbers.txt and add them
with open("numbers.txt", "r") as file:
    num1 = int(file.readline().strip())
    num2 = int(file.readline().strip())

print(num1 + num2)  # 17 + 42 = 59

# Read all numbers from numbers.txt and sum them
total = 0
with open("numbers.txt", "r") as file:
    for line in file:
        total += int(line.strip())

print(total)  # 17 + 42 + 400 = 459


