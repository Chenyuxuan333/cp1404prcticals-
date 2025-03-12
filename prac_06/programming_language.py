class ProgrammingLanguage:
    """Represent a programming language with its characteristics."""

    def __init__(self, name, typing, reflection, year):
        """Initialize a programming language instance."""
        self.name = name
        self.typing = typing  # "Static" or "Dynamic"
        self.reflection = reflection  # True or False
        self.year = year

    def is_dynamic(self):
        """Return True if the language is dynamically typed, otherwise False."""
        return self.typing.lower() == "dynamic"

    def __str__(self):
        """Return a formatted string representation of the programming language."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"
