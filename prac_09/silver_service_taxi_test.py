"""
CP1404 - Silver Service Taxi Class Test Code
"""
from prac_09.silver_service_taxi import SilverServiceTaxi

def test_silver_service_taxi():
    """Test the SilverServiceTaxi Class"""
    fancy_taxi = SilverServiceTaxi("Fancy Taxi", 200, 2)

    # Start fare and drive 18km.
    fancy_taxi.start_fare()
    fancy_taxi.drive(18)

    # Calculate the fare
    fare = fancy_taxi.get_fare()
    print(f"Fare for {fancy_taxi.name} after driving 18km: ${fare:.2f}")

    # Check fare calculation
    assert round(fare, 2) == 48.80, f"Expected fare: $48.80, got: ${fare:.2f}"


if __name__ == "__main__":
    test_silver_service_taxi()
    print("Test finished.")