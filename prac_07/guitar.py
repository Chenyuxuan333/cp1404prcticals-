"""
CP1404 Practical 07 - Guitar Class Code
Estimate: 15 minutes
Actual: 20 minutes
"""
from datetime import datetime
CURRENT_YEAR = datetime.now().year
VINTAGE_AGE = 50

class Guitar:
    """Guitar class for storing details of a guitar."""

    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of the Guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:.2f}"

    def get_age(self):
        """Get the age of the guitar."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Determine if the guitar is vintage."""
        return self.get_age() >= VINTAGE_AGE

    def __lt__(self, other):
        """Compare two guitars based on their year."""
        return self.year < other.year
