# main program to run the game.

from q_a import q_list, ans_list
from helpers import *

# open_letter()
start_game()

# song: okinawa
while True:
    display_choice_qstn(0)
    player_q0_answer = q_list[0].choose_answer()
    if player_q0_answer == ans_list[0]:
        kiss(1)

        song_indicator(0)
        display_song(0)

        if q_list[0].next_qstn() == 'n':
            break
    else:
        display_incorrect_msg()

# song: turnin me up
while True:
    display_choice_qstn(1)
    player_q1_answer = q_list[1].choose_answer()
    if player_q1_answer == ans_list[1]:
        kiss(1)

        song_indicator(1)
        display_song(1)

        if q_list[1].next_qstn() == 'n':
            break
    else:
        display_incorrect_msg()

# song: love
while True:
    display_open_qstn(2)
    player_q2_answer = q_list[2].choose_answer()
    if player_q2_answer == ans_list[2]:
        kiss(2)

        song_indicator(2)
        display_song(2)

        if q_list[2].next_qstn() == 'n':
            break
    else:
        display_incorrect_msg()

# song: wait for the moment
while True:
    display_choice_qstn(3)
    player_q3_answer = q_list[3].choose_answer()
    if player_q3_answer == ans_list[3]:
        kiss(10)

        song_indicator(3)
        display_song(3)

        if q_list[3].next_qstn() == 'n':
            break
    else:
        display_incorrect_msg()


# song: this christmas
while True:
    display_open_qstn(4)
    player_q4_answer = q_list[4].choose_answer()
    if player_q4_answer == ans_list[4]:
        kiss(10)

        song_indicator(4)
        display_song(4)

        if q_list[4].next_qstn() == 'n':
            break
    else:
        display_incorrect_msg()

# song: unforgettable
while True:
    display_open_qstn(5)
    player_q5_answer = q_list[5].choose_answer()
    if player_q5_answer == ans_list[5]:
        kiss(10)

        song_indicator(5)
        display_song(5)

        if q_list[5].next_qstn() == 'n':
            break
    else:
        display_incorrect_msg()

# song: stand by me
while True:
    display_choice_qstn(6)
    player_q6_answer = q_list[6].choose_answer()
    if player_q6_answer == ans_list[6]:
        kiss(3)

        song_indicator(6)
        display_song(6)

        if q_list[6].next_qstn() == 'n':
            break
    else:
        display_incorrect_msg()

# song: aint no mountain high enough
while True:
    display_choice_qstn(7)
    player_q7_answer = q_list[7].choose_answer()
    if player_q7_answer == ans_list[7]:
        kiss(1)

        song_indicator(7)
        display_song(7)

        if q_list[7].next_qstn() == 'n':
            break
    else:
        display_incorrect_msg()

# song: send me some lovin
while True:
    display_choice_qstn(8)
    player_q8_answer = q_list[8].choose_answer()
    if player_q8_answer == ans_list[8]:
        kiss(1)

        song_indicator(8)
        display_song(8)

        if q_list[8].next_qstn() == 'n':
            break
    else:
        display_incorrect_msg()

# song: ilymtyek
while True:
    display_choice_qstn(9)
    player_q9_answer = q_list[9].choose_answer()
    if player_q9_answer == ans_list[9]:
        kiss(10)

        song_indicator(9)
        display_song(9)

        if q_list[9].next_qstn() == 'n':
            break
    else:
        display_incorrect_msg()

# song: because of you
while True:
    display_choice_qstn(10)
    player_q10_answer = q_list[10].choose_answer()
    if player_q10_answer == ans_list[10]:
        kiss(5)

        song_indicator(10)
        display_song(10)

        if q_list[10].next_qstn() == 'n':
            break
    else:
        display_incorrect_msg()

# song: im so excited
while True:
    display_choice_qstn(11)
    player_q11_answer = q_list[11].choose_answer()
    if player_q11_answer == ans_list[11]:
        kiss(1)

        song_indicator(11)
        display_song(11)

        if q_list[11].next_qstn() == 'n':
            break
    else:
        display_incorrect_msg()

# song: slow dance
while True:
    display_TF(12)
    player_q12_answer = q_list[12].choose_answer()
    if player_q12_answer == ans_list[12]:
        kiss(1)

        song_indicator(12)
        display_song(12)

        if q_list[12].next_qstn() == 'n':
            break
    else:
        display_incorrect_msg()

# song: bodyguard
while True:
    display_open_qstn(13)
    player_q13_answer = q_list[13].choose_answer()
    if player_q13_answer == ans_list[13]:
        kiss(3)

        song_indicator(13)
        display_song(13)

        if q_list[13].next_qstn() == 'n':
            break
    else:
        display_incorrect_msg()

# song: bodyguard
while True:
    display_choice_qstn(14)
    player_q14_answer = q_list[14].choose_answer()
    if player_q14_answer == ans_list[14]:
        kiss(2)

        song_indicator(14)
        display_song(14)

        break
    else:
        display_incorrect_msg()

end_main_game()
# prompt_bonus()

# # movie: the truman show
# while True:
#     display_choice_qstn(15)
#     player_q14_answer = q_list[15].choose_answer()
#     if player_q14_answer == ans_list[15]:
#         kiss(3)

#         movie_indicator(0)
#         display_movie(0)

#         break
#     else:
#         print(incorrect)

# # movie: the talented mr ripley
