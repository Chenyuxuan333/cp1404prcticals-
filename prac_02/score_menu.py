"""
Cp1404 practical 2
"""

EXCELLENT_SCORE =90
PASSABLE_SCORE = 50
MENU =("(G)et a valid score\n"
       "(P)rint result\n"
       "(s)how stars\n"
       "(Q)uit")

def main():
    score = ""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score("Enter the score: ")
        elif choice =="p":
            if score != "":
                print(f"The result of {score} is {determine_grade(score)}")
            else:
                print("Get a valid score first.")
        elif choice == "s":
            if score != "":
                print_stars(score)
            else:
                print("Get a valid score first.")
        else:
            print("Invalid choice.")
        print("Invalid choice.")
        choice = input(">>> ").upper()
    print("Farewell!")

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

def print_stars(number):
    # print as many stars as the score
    print("*" *(int(number)))

main()