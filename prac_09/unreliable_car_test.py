"""
CP1404 - Test code for UnreliableCar class
"""
from prac_09.unreliable_car import UnreliableCar

def test_unreliable_car():
    """Test the UnreliableCar Class"""
    unreliable_car = UnreliableCar("Test Car", 100, 30)
    successful_drive = 0
    attempts = 100    # Number of attempts to drive
    for i in range(attempts):
        distance = unreliable_car.drive(1)
        if distance > 0:
            successful_drive += 1

    print(f"Successful drives: {successful_drive}/{attempts}")


if __name__ == "__main__":
    test_unreliable_car()
    print("Test finished.")