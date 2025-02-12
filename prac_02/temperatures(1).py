"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""
from prac_1.temperatures import celsius, fahrenheit

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)
choice = input(">>> ").upper()

def convert_c_to_f(number):
    # convert Celsius to Fahrenheit
    convert_fahrenheit = number * 9.0 / 5 + 32
    return convert_fahrenheit

def convert_f_to_c(number):
    # convert fahrenheit to celsius
    convert_celsius = 5 / 9 * (number - 32)
    return convert_celsius

while choice != "Q":
    if choice == "C":
        celsius = float(input("Celsius： "))
        fahrenheit = convert_c_to_f(celsius)
        print(f"Result: {fahrenheit:.2f} F")
    elif choice == "F":
        # convert F to C and display the result
        fahrenheit = float(input("Fahrenheit: "))
        celsius = convert_f_to_c(fahrenheit)
        print(f"Result: {celsius:.2f} ℃")
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you!")
