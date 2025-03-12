"""CP1404/CP5632 Practical - Car class example."""


class Car:
    """Represent a Car object."""

    def __init__(self, name, fuel=0):
        """Initialise a Car instance."""
        self.name = name
        self.fuel = fuel
        self.odometer = 0

    def add_fuel(self, amount):
        """Add amount to the car's fuel."""
        self.fuel += amount

    def drive(self, distance):
        """Drive the car a given distance if it has enough fuel."""
        if distance > self.fuel:
            distance = self.fuel  # Car can only drive as far as fuel allows
        self.fuel -= distance
        self.odometer += distance
        return distance

    def __str__(self):
        """Return a string representation of the Car object."""
        return f"{self.name}, fuel={self.fuel}, odometer={self.odometer}"
