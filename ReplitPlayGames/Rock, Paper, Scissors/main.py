from random import choice
from kidpy import *

random_choice = ['rock', 'paper', 'scissors', 'rock', 'paper', 'scissors', 'rock', 'paper', 'scissors', 'rock', 'paper', 'scissors', 'rock', 'paper', 'scissors', 'rock', 'paper', 'scissors', 'rock', 'paper', 'scissors', 'rock', 'paper', 'scissors', 'rock', 'paper', 'scissors']
print('=========================================')
print('==========Rock, paper, scissors==========')
print('=========================================')

player_choice = input('Rock, paper or scissors? ')
game_choice = choice(random_choice)

if game_choice == 'rock':
    if player_choice == 'rock':
        write('TIE')
        print('TIE')
        quit()
    elif player_choice == 'paper':
        write('Player wins!')
        print('Player wins!')
        quit()
    elif player_choice == 'scissors':
        write('Computer wins!')
        print('Computer wins!')
        quit()
    else:
        print('Something went wrong! :,( Please try again!')
        quit()

if game_choice == 'paper':
    if player_choice == 'paper':
        print('TIE')
        quit()
    elif player_choice == 'scissors':
        print('Player wins!')
        quit()
    elif player_choice == 'rock':
        print('Computer wins!')
        quit()
    else:
        print('Something went wrong! :,( Please try again!')
        quit()

if game_choice == 'scissors':
    if player_choice == 'scissors':
        print('TIE')
        quit()
    elif player_choice == 'rock':
        print('Player wins!')
        quit()
    elif player_choice == 'paper':
        print('Computer wins!')
        quit()
    else:
        print('Something went wrong! :,( Please try again!')
quit()
