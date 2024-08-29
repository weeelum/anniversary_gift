"""Define helper functions."""

from pathlib import Path
from classSong import *
from classQuestion import *
from songs import *
from movies import *
from q_a import q_list

correct = "Correct!"
incorrect = "\nIncorrect. Try again!"
kiss_count = 0
kiss_emoji = "😚"
kiss_bank = []
completed_playlist = []

"""Function to open starting letter before game begins."""
def open_letter():
    while True:
        view = input("You've got a letter! Enter 'view' to view the message: ")
        if view == "view":
            start_path = Path("starting_msg.txt")
            starting_msg = start_path.read_text()
            print(starting_msg)
            break
        else:
            print("There's no other functionality here! Do the thing!")

"""Function to take player input to start game."""
def start_game():
    while True:
        start_game = input("\nEnter 'start' to begin the game: ")
        if start_game == "start":
            break

"""Function to end main game."""
def end_main_game():
    while True:
        end_main_game = input(
            "\nEnter 'finished' to end the game and print out a list of "
            "all the songs you've collected! "
        )
        if end_main_game == 'finished':
            display_playlist()
            break

"""Add kisses to global var kiss_count"""
def add_kisses(kiss):
    global kiss_count
    kiss_count += kiss
    if kiss == 1:
        print(
            f"Correct! {kiss} kiss has been deposited into your kiss bank."
        )
    elif kiss > 1:
        print(
            f"Correct! {kiss} kisses have been deposited into your kiss "
            "bank."
        )

"""Function to update and display kiss balance."""
def display_kiss_balance():
    global kiss_count
    if kiss_count == 1:
        print(
            f"You have {kiss_count} kiss in the bank.\n"
        )
    elif kiss_count > 1:
        print(
            f"You now have {kiss_count} kisses in the bank.\n"
        )

"""Add kiss emoji to kiss_bank."""
def append_kiss(num):
    global kiss_bank
    global kiss_emoji
    for num in kiss_bank:
        kiss_emoji
    kiss_bank.append(kiss_emoji)

"""Wraps up add_kisses(), display_kiss_balance(), and append_kiss() in
one neat function."""
def kiss(num):
    add_kisses(num)
    display_kiss_balance()
    # append_kiss(num)

"""Header for song indicator."""
def song_indicator(num):
    num += 1
    print(f"Song #{num} is:")

"""Header for movie indicator."""
def movie_indicator(num):
    num += 1
    print(f"Movie #{num} is:")

"""Show which song has just been revealed."""
def display_song(num):
    song_list[num].display_song()

"""Show which movie has just been revealed."""
def display_movie(num):
    movie_list[num].display_movie()

"""Print out unique message for each song/answer."""
def display_correct_msg():
    print(correct)

"""Print out unique message for each incorrect answer."""
def display_incorrect_msg():
    print(incorrect)

"""Loop through and print all song dictionaries for completed
playlist."""
def display_playlist():
    song_num = 1
    print("\n\n\nHere's the complete playlist! Enjoy :)")
    for song in complete_playlist:
        print(f"\nSong #{song_num}:")
        song_num += 1
        for key, value in song.items():
            print(f"{key}: {value}")

"""Display kiss bank at end of game."""
def display_kiss_bank():
    global kiss_count
    print(f"Here are all {kiss_count} kisses you've accumulated:")
    print(f"{kiss_bank}")

"""Display multiple choice question."""
def display_choice_qstn(num):
    q_list[num].display_choice_qstn()

"""Display open question."""
def display_open_qstn(num):
    q_list[num].display_open_qstn()

"""Display true/false question."""
def display_TF(num):
    q_list[num].display_TF()

"""Take player answer input and return the value."""
def set_player_ans(num):
    q_list[num].choose_answer()
    return q_list[num].choose_answer()

"""Ask player if they want to start bonus section."""
def prompt_bonus():
    while True:
        bonus = input(
            "\nWould you like to play the bonus game for some extra goodies?\n"
            "Enter 'y' to begin or 'q' to quit: "
        )

        if bonus == 'y':
            print(
                "\nGreat! All you have to do is fill in the movie quotes! Let's "
                "begin.\n"
                "If you need some hints, check imdb.com 😉\n"
            )
            begin_bonus()
            break
        elif bonus == 'q':
            print("goodbye")
            break

"""Initiate bonus rounds."""
def begin_bonus():
    pass

# prompt_bonus()