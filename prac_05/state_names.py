"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

CODE_TO_NAME = {
    "QLD": "Queensland",
    "NSW": "New South Wales",
    "NT": "Northern Territory",
    "WA": "Western Australia",
    "ACT": "Australian Capital Territory",
    "VIC": "Victoria",
    "TAS": "Tasmania",
    "SA": "South Australia"
}

print(CODE_TO_NAME)

while True:
    state_code = input("Enter short state: ").strip().upper()
    if not state_code:
        break
    print(f"{state_code} is {CODE_TO_NAME.get(state_code, 'Invalid state code')}")

max_length = max(map(len, CODE_TO_NAME))

for code, name in CODE_TO_NAME.items():
    print(f"{code:{max_length}} is {name}")
