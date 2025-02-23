"""
CP1404 - Practical 04
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = load_data()
    print_subjects(data)


def load_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    data = []
    input_file = open(FILENAME)
    for line in input_file:
        # print(line)  # See what a line looks like
        # print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        # print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        # print(parts)  # See if that worked
        # print("----------")
        data.append(parts)
    input_file.close()
    return data

def print_subjects(data):
    """Display subject details from the data list."""
    for subject in data:
        print(f"{subject[0]:6} is taught by {subject[1]:12} and has {subject[2]:3} students")

main()