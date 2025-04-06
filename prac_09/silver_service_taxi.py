"""
CP1404 - Silver Service Taxi Class Code
"""

from prac_09.taxi import Taxi

class SilverServiceTaxi(Taxi):
    """Silver Service Taxi Class"""

    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialize a SilverServiceTaxi instance."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * fanciness

    def get_fare(self):
        """Calculate the fare for the taxi trip including the flagfall."""
        return super().get_fare() + self.flagfall

    def __str__(self):
        """Return a string representation of the SilverServiceTaxi instance."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f} and fanciness of {self.fanciness}"