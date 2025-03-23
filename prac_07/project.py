"""
CP1404 Practical 07 - Project Class Code
Estimate: 20 minutes
Actual: 20 minutes
"""

from datetime import datetime

class Project:
    """Project class for storing details of a project."""

    def __init__(self, name="", start_date=None, priority=0, cost=0.0, completion_percentage=0):
        """Initialise a Project instance."""
        self.name = name
        self.start_date = start_date if start_date else datetime.now()
        self.priority = priority
        self.cost = cost
        self.completion_percentage = completion_percentage


    def __str__(self):
        """Return a string representation of the Project."""
        return f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, priority: {self.priority}, estimate: ${self.cost:.2f}, completion: {self.completion_percentage}%"


    def is_complete(self):
        """Determine if the project is complete."""
        return self.completion_percentage == 100