COLOUR_TO_CODE = {"acid green": "#b0bf1a", "antiquewhite": "#faebd7",
            "coral": "#ff7f50", "azure": "#f0ffff",
            "blueviolet": "#8a2be2", "black": "#000000",
            "blue": "#0000ff", "brown": "#a52a2a",
            "camel": "#c19a6b", "aliceblue": "#f0f8ff"}

colour = input("Enter a colour name: ").lower()
while colour != "":
    try:
        print(f"The code of {colour} is {COLOUR_TO_CODE[colour]}")
    except KeyError:
        print("Invalid colour name")
    colour = input("Enter a colour name: ").lower()
print("Finished.")