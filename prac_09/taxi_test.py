"""
CP1404 - Test code for Taxi Class

"""
from prac_09.taxi import Taxi

my_taxi = Taxi("Prius 1", 100, 1.23)

# Drive the taxi 40 km. Expected output: 40 km driven, 60 km fuel left
my_taxi.drive(40)
# Print the taxi's details. Expected output: Prius 1, fuel=60, odometer=40
print(my_taxi)
# Print the taxi's fare. Expected output: Fare: $49.20
print(f"Fare: ${my_taxi.get_fare():.2f}")

# Reset and drive another 100 km. Expected output: 100 km driven, 0 km fuel left
my_taxi.start_fare()
my_taxi.drive(100)
# Print the taxi's details. Expected output: Prius 1, fuel=0, odometer=100
print(my_taxi)
# Print the taxi's fare. Expected output: Fare: $123.00
print(f"Fare: ${my_taxi.get_fare():.2f}")