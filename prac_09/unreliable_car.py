"""
CP1404 - Unreliable Car Class Code
"""
import random
from prac_09.car import Car

class UnreliableCar(Car):
    """UnreliableCar class that inherits from Car class"""

    def __init__(self, name, fuel, reliability):
        """Initializes UnreliableCar instance"""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drives the car a certain distance if it is reliable"""
        chance = random.uniform(0, 100)
        if chance <= self.reliability:
            return super().drive(distance)
        else:
            return 0