"""
CP1406 - Taxi Simulator Program
"""
from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    taxis = [Taxi("Prius", 100),
             SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    total_fare = 0

    print("Let's drive!")
    print(MENU)
    choice = input(">>> ").lower()

    while choice != "q":
        if choice == "c":
            current_taxi = choose_taxi(taxis)
        elif choice == "d":
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                cost = drive_taxi(current_taxi)
                total_fare += cost
                print(f"Your {current_taxi.name} trip cost you ${cost:.2f}")
        else:
            print("Invalid option")

        print(f"Bill to date: ${total_fare:.2f}")
        print(MENU)
        choice = input(">>> ").lower()

    print(f"Total trip cost: ${total_fare:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)


def choose_taxi(taxis):
    """Choose a taxi from the list of taxis"""
    print("Taxis available: ")
    display_taxis(taxis)
    try:
        taxi_choice = int(input("Choose taxi: "))
        if 0 <= taxi_choice < len(taxis):
            return taxis[taxi_choice]
        else:
            print("Invalid taxi choice")
    except ValueError:
        print("Invalid input")
    return None


def drive_taxi(taxi):
    """Drive for a certain distance"""
    try:
        distance = float(input("Drive how far? "))
    except ValueError:
        print("Invalid input. Assuming 0 distance.")
        distance = 0

    taxi.start_fare()
    taxi.drive(distance)
    return taxi.get_fare()


def display_taxis(taxis):
    """Display all taxis in the list with their details"""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")

if __name__ == "__main__":
    main()