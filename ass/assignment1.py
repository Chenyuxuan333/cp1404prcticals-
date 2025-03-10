"""
Name: CHENYUXUAN
Date started: 01/03/2025
GitHub URL: https://github.com/cp1404-students/a1-2025-1-Chenyuxuan333.git
"""
from operator import itemgetter

# Constants
FILENAME = "songs.csv"
LEARNED_INDICATOR = "l"
UNLEARNED_INDICATOR = "u"
UNLEARNED_SYMBOL = "*"


def main():
    """Main function to manage the song list."""
    print("Song List Manager 1.0 - by CHENYUXUAN")
    songs = load_songs_from_file(FILENAME)
    print(f"{len(songs)} songs loaded.")

    while True:
        display_menu()
        choice = input(">>> ").upper()

        if choice == "D":
            display_song_list(songs)
        elif choice == "A":
            add_new_song(songs)
        elif choice == "C":
            mark_song_as_learned(songs)
        elif choice == "Q":
            save_songs_to_file(songs, FILENAME)
            print("Make some music!")
            break
        else:
            print("Invalid menu choice. Please try again.")


def display_menu():
    """Display the main menu options."""
    print("Menu:")
    print("D - Display songs")
    print("A - Add new song")
    print("C - Complete a song")
    print("Q - Quit")


def load_songs_from_file(filename):
    """Load songs from a CSV file."""
    songs = []
    try:
        with open(filename, "r") as file:
            for line in file:
                title, artist, year, learned = line.strip().split(",")
                songs.append([title, artist, int(year), learned])
    except FileNotFoundError:
        print(f"Error: {filename} not found. Starting with an empty song list.")
    return songs


def save_songs_to_file(songs, filename):
    """Save songs to a CSV file."""
    with open(filename, "w") as file:
        for song in songs:
            file.write(f"{song[0]},{song[1]},{song[2]},{song[3]}\n")
    print(f"{len(songs)} songs saved to {filename}.")


def display_song_list(songs):
    """Display the list of songs sorted by year and title."""
    sorted_songs = sorted(songs, key=itemgetter(2, 0))
    for i, song in enumerate(sorted_songs, 1):
        title, artist, year, learned = song
        learned_status = " " if learned == LEARNED_INDICATOR else f"{UNLEARNED_SYMBOL} "
        print(f"{i}. {learned_status}{title} by {artist} ({year})")

    learned_count = sum(1 for song in songs if song[3] == LEARNED_INDICATOR)
    unlearned_count = len(songs) - learned_count
    print(f"{learned_count} songs learned, {unlearned_count} songs still to learn.")


def add_new_song(songs):
    """Add a new song to the list."""
    title = get_non_empty_input("Title: ")
    artist = get_non_empty_input("Artist: ")
    year = get_positive_integer_input("Year: ")

    songs.append([title, artist, year, UNLEARNED_INDICATOR])
    print(f"{title} by {artist} ({year}) added to the song list.")


def mark_song_as_learned(songs):
    """Mark a song as learned."""
    unlearned_songs = [song for song in songs if song[3] == UNLEARNED_INDICATOR]
    if not unlearned_songs:
        print("No more songs to learn!")
        return

    print("Enter the number of a song to mark as learned.")
    sorted_songs = sorted(songs, key=itemgetter(2, 0))

    try:
        song_number = get_positive_integer_input(">>> ")
        while song_number < 1 or song_number > len(sorted_songs):
            print("Invalid song number. Please try again.")
            song_number = get_positive_integer_input(">>> ")

        selected_song = sorted_songs[song_number - 1]
        if selected_song[3] == LEARNED_INDICATOR:
            print(f"You have already learned {selected_song[0]}.")
        else:
            for i, song in enumerate(songs):
                if song[0] == selected_song[0] and song[1] == selected_song[1] and song[2] == selected_song[2]:
                    songs[i][3] = LEARNED_INDICATOR
                    print(f"{selected_song[0]} by {selected_song[1]} learned.")
                    return
    except ValueError:
        print("Invalid input. Please enter a valid number.")


def get_non_empty_input(prompt):
    """Get non-empty input from the user."""
    while True:
        user_input = input(prompt).strip()
        if user_input:
            return user_input
        print("Input cannot be blank. Please try again.")


def get_positive_integer_input(prompt):
    """Get a positive integer input from the user."""
    while True:
        user_input = input(prompt).strip()
        if user_input.isdigit() and int(user_input) > 0:
            return int(user_input)
        print("Invalid input. Please enter a positive integer.")


if __name__ == "__main__":
    main()
