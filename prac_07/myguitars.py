"""
CP1404 Practical 07 - Client code for Guitar class
Estimate: 30 minutes
Actual: 25 minutes
"""

from guitar import Guitar

def main():
    guitars = load_guitars("guitars.csv")
    print("My guitars are: ")
    display_guitars(guitars)

    if input("Do you want to add a new guitar? (y/n): ").strip().lower() == "y":
        add_new_guitar(guitars)

    guitars.sort()
    print("\nSorted guitars by year: ")
    display_guitars(guitars)
    save_guitars("guitars.csv", guitars)


def load_guitars(filename):
    """Load guitars from a CSV file."""
    guitars = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                name, year, cost = line.strip().split(',')
                guitar = Guitar(name, int(year), float(cost))
                guitars.append(guitar)
    except FileNotFoundError:
        print(f"File {filename} not found.")

    return guitars


def display_guitars(guitars):
    """Display the guitars in dynamic formatting method."""
    if guitars:
        name_width = max(len(guitar.name) for guitar in guitars)
        year_width = max(len(str(guitar.year)) for guitar in guitars)
        cost_width = max(len(f"${guitar.cost:,.2f}") for guitar in guitars)
        for guitar in guitars:
            print(f"{guitar.name:<{name_width}} ({guitar.year:<{year_width}}), ${guitar.cost:>{cost_width}}")
    else:
        print("No guitars to display.")


def save_guitars(filename, guitars):
    """Save guitars to a CSV file."""
    with open(filename, 'w') as file:
        for guitar in guitars:
            file.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")
    print(f"\nGuitars list saved to {filename}.")


def add_new_guitar(guitars):
    """Add a new guitar to the list."""
    name = input("Enter guitar name: ").strip()
    while any(guitar.name == name for guitar in guitars):
        print("Guitar already exists.")
        name = input("Enter guitar name: ").strip()

    while name != "":
        try:
            year = int(input("Enter guitar year: "))
            cost = float(input("Enter guitar cost: "))
        except ValueError:
            print("Invalid input. Please enter numeric values for year and cost.")
            continue

        new_guitar = Guitar(name, year, cost)
        guitars.append(new_guitar)
        print(f"{new_guitar} added.")
        name = input("Enter guitar name: ").strip()

if __name__ == "__main__":
    main()