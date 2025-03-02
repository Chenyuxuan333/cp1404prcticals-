"""
Estimate: 30 mins
Actual: 25 mins
"""

FILENAME = "wimbledon.csv"
INDEX_COUNTRY = 1
INDEX_CHAMPION = 2

def main():
    data = read_file(FILENAME)
    champion_to_count, countries = process_data(data)
    display_data(champion_to_count, countries)

def read_file(filename):
    """Read data from file and return as a list of lists."""
    file = open(filename, "r", encoding="utf-8-sig")
    data = [line.strip().split(",") for line in file]
    file.close()
    return data

def process_data(data):
    """Create a dictionary of champions and a set of countries."""
    champion_to_count = {}
    countries = {record[INDEX_COUNTRY] for record in data[1:]}
    for record in data[1:]:
        champion_to_count[record[INDEX_CHAMPION]] = champion_to_count.get(record[INDEX_CHAMPION], 0) + 1
    return champion_to_count, countries

def display_data(champion_to_count, countries):
    """Display the champion win counts and the list of countries."""
    print("Wimbledon Champions:")
    for champion, count in sorted(champion_to_count.items()):
        print(f"{champion}: {count}")

    print("\nWinning Countries:")
    print(", ".join(sorted(countries)))

if __name__ == "__main__":
    main()
