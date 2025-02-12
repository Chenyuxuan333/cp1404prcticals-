"""
CP1404-Practical 02
determine score status
"""
import random

EXCELLENT_SCORE =90
PASSABLE_SCORE = 50

def main():
    score = get_valid_score("Enter score: ")
    result = determine_grade(score)
    print(f"The result of {score} is: {result}")

    random_score = random.uniform(0,100)
    random_result = determine_grade(random_score)
    print(f"The result of {random_score} is: {random_result}")

def get_valid_score(prompt):
    # Error checking the user input score
    user_score = float(input(prompt))
    while user_score < 0 or user_score > 100:
        print("invalid score")
        user_score = float(input(prompt))
    return user_score

def determine_grade(number):
    # Determine the result based on score
    if number >= EXCELLENT_SCORE:
        return "Excellent"
    elif number >= PASSABLE_SCORE:
        return "Passable"
    else:
        return "Bad"

main()