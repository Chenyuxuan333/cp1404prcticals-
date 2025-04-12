"""
CP1404/CP5632 Practical
Testing code using assert and doctest
"""

import doctest
from prac_06.car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between.
    >>> repeat_string("hi", 2)
    'hi hi'
    >>> repeat_string("Python", 3)
    'Python Python Python'
    """
    return " ".join([s] * n)


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    >>> is_long_word("hello", 5)
    True
    """
    return len(word) >= length  # Changed from > to >= to pass the test


def format_as_sentence(phrase):
    """
    Format a phrase as a proper sentence starting with capital and ending with full stop.
    >>> format_as_sentence('hello')
    'Hello.'
    >>> format_as_sentence('It is an ex parrot.')
    'It is an ex parrot.'
    >>> format_as_sentence('this needs formatting')
    'This needs formatting.'
    """
    # Capitalize first letter
    sentence = phrase.capitalize()
    # Add full stop if needed
    if sentence[-1] not in ".!?":
        sentence += "."
    return sentence


def run_tests():
    """Run the tests on the functions."""
    # Test repeat_string
    assert repeat_string("Python", 1) == "Python"
    assert repeat_string("hi", 2) == "hi hi"

    # Test Car class
    # Test default fuel
    default_car = Car()
    assert default_car.fuel == 0, "Default fuel not set correctly"

    # Test passed fuel value
    custom_fuel_car = Car(fuel=10)
    assert custom_fuel_car.fuel == 10, "Custom fuel not set correctly"

    # Test odometer
    assert default_car._odometer == 0, "Car does not set odometer correctly"


if __name__ == "__main__":
    run_tests()
    doctest.testmod()