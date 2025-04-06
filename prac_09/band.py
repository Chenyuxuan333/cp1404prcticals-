"""
CP1404 - Band class code
"""
class Band:
    """Band Class containing a collection of musicians."""

    def __init__(self, name=""):
        """Initialise a Band instance."""
        self.name = name
        self.musicians = []

    def add(self, musician):
        """Add a musician to the band."""
        self.musicians.append(musician)

    def __str__(self):
        """Return a string representation of the band."""
        return f"{self.name} ({', '.join(str(musician) for musician in self.musicians)})"

    def play(self):
        """Return a string of what instrument each musician is playing"""
        return "\n".join(musician.play() for musician in self.musicians)