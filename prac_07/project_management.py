"""
CP1404 Practical 07 - Project Management Client Code
Estimate: 60 minutes
Actual: 60 minutes
"""

from datetime import datetime
from project import Project

AFFIRMATIVES = ["Y", "YES", "OK"]

def main():
    """Main function to manage projects."""
    filename = "projects.txt"
    projects = load_projects(filename)
    print(f"Loaded {len(projects)} projects from {filename}.")

    display_menu()
    choice = input(">>> ").strip().upper()

    while choice != "Q":
        if choice == "L":
            projects = load_projects(filename)
        elif choice == "S":
            save_projects(filename, projects)
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            filter_projects_by_date(projects)
        elif choice == "A":
            add_new_project(projects)
        elif choice == "U":
            update_project(projects)
        else:
            print("Invalid choice. Please enter valid menu option.")

        display_menu()
        choice = input(">>> ").strip().upper()

    save_option = input(f"Would you like to save to {filename}? ").strip().upper()
    if save_option.upper() in AFFIRMATIVES:
        save_projects(filename, projects)
    print("Thank you for using custom-built project management system.")


def display_menu():
    """Display menu options."""
    print("- (L)oad projects\n"
          "- (S)ave projects\n"
          "- (D)isplay projects\n"
          "- (F)ilter projects by date\n"
          "- (A)dd new project\n"
          "- (U)pdate project\n"
          "- (Q)uit")


def load_projects(filename):
    """Load projects from the file."""
    projects = []
    try:
        with open(filename, 'r') as file:
            next(file)
            for line in file:
                name, start_date, priority, cost, completion_percentage = line.strip().split('\t')
                project = Project(name, datetime.strptime(start_date, "%d/%m/%Y").date(),
                                  int(priority), float(cost), int(completion_percentage))
                projects.append(project)
    except FileNotFoundError:
        print(f"File {filename} not found.")
    return projects


def save_projects(filename, projects):
    """Save projects to the file."""
    with open(filename, 'w') as file:
        for project in projects:
            file.write(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t{project.priority}\t{project.cost}\t{project.completion_percentage}\n")
    print(f"Projects saved to {filename}.")


def display_projects(projects, filtered=False):
    """Display the projects."""
    if not projects:
        print("No projects to display.")
        return
    if not filtered:
        incomplete_projects = [project for project in projects if not project.is_complete()]
        completed_projects = [project for project in projects if project.is_complete()]
        print("Incomplete projects:")
        for project in incomplete_projects:
            print(f"  {project}")
        print("Completed projects:")
        for project in completed_projects:
            print(f"  {project}")
    else:
        for project in projects:
            print(f"  {project}")


def filter_projects_by_date(projects):
    """Filter projects by start date."""
    date_str = input("Show projects that start after date (dd/mm/yy): ")
    try:
        start_date = datetime.strptime(date_str, "%d/%m/%Y").date()
        filtered_projects = [project for project in projects if project.start_date >= start_date]
        display_projects(filtered_projects, filtered=True)
    except ValueError:
        print("Invalid date format.")


def add_new_project(projects):
    """Add a new project to the list."""
    print("Let's add a new project")
    name = input("Name: ").strip()
    while any(project.name == name for project in projects):
        print("Project already exists.")
        name = input("Name: ").strip()

    start_date = get_valid_date("Start date (dd/mm/yyyy): ")
    priority = get_valid_priority("Priority: ")
    cost = get_valid_cost("Cost estimate: $")
    completion_percentage = get_valid_number("Percent complete: ")

    new_project = Project(name, start_date, priority, cost, completion_percentage)
    projects.append(new_project)


def update_project(projects):
    """Update an existing project."""
    for i, project in enumerate(projects):
        print(f"{i} {project}")

    try:
        index_number = int(input("Project choice: "))
        if 0 <= index_number < len(projects):
            project = projects[index_number]
            print(f"{project}")
            new_completion_percentage = get_valid_number("New Percentage: ")
            if new_completion_percentage != "":
                project.completion_percentage = new_completion_percentage
            new_priority = get_valid_priority("New Priority: ")
            if new_priority != "":
                project.priority = new_priority
        else:
            print("Invalid choice. Index out of range.")
    except ValueError:
        print("Invalid input. Please enter a number.")


def get_valid_date(prompt):
    """Get a valid date from user."""
    date_str = input(prompt)
    while date_str != "":
        try:
            return datetime.strptime(date_str, "%d/%m/%Y").date()
        except ValueError:
            print("Invalid date format. Please use dd/mm/yyyy.")
            date_str = input(prompt)


def get_valid_number(prompt):
    """Get a valid number from user."""
    number = input(prompt)
    while number != "":
        try:
            number = int(number)
            if number < 0:
                print("Number must be greater than 0.")
            else:
                return number
        except ValueError:
            print("Invalid input. Please enter a number.")
        number = input(prompt)


def get_valid_cost(prompt):
    """Get a valid cost from user."""
    cost = input(prompt)
    while cost != "":
        try:
            cost = float(cost)
            if cost < 0:
                print("Cost must be greater than 0.")
            else:
                return cost
        except ValueError:
            print("Invalid input. Please enter a number.")
        cost = input(prompt)


def get_valid_priority(prompt):
    """Get a valid priority from user."""
    priority = input(prompt)
    while priority != "":
        try:
            priority = int(priority)
            if 1 <= priority <= 10:
                return priority
            else:
                print("Priority must be between 1 and 10.")
        except ValueError:
            print("Invalid input. Please enter a number.")
        priority = input(prompt)


if __name__ == "__main__":
    main()