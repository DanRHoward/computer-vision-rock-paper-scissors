import random

game_states = ['rock','paper','scissors']

def get_computer_choice():
    computer_choice = random.choice(game_states)
    return computer_choice

def get_user_choice():
    while True:
        user_choice = input('Choose rock, paper or scissors : ').lower()
        if user_choice in game_states:
            break
        print('Your input is invalid! Please enter rock, paper or scissors : ')
    return user_choice

def get_winner(computer_choice,user_choice):
    if computer_choice == 'rock':
        if user_choice == 'rock':
            winner = 'neither'
        elif user_choice == 'paper':
            winner = 'the user'
        else:
            winner = 'the computer'
    elif computer_choice == 'paper':
        if user_choice == 'rock':
            winner = 'the computer'
        elif user_choice == 'paper':
            winner = 'neither'
        else:
            winner = 'the user'
    else:
        if user_choice == 'rock':
            winner = 'the user'
        elif user_choice == 'paper':
            winner = 'the computer'
        else:
            winner = 'neither'
    return winner

def play():
    computer_choice = get_computer_choice()
    user_choice = get_user_choice()
    winner = get_winner(computer_choice,user_choice)
    if winner == 'neither':
        return print('The game is a draw.')
    else:
        return print(f'The winner is {winner}!')

play()
while True:
    play_again = input('Would you like to play again? (y/n) : ')
    if play_again.lower() == 'y':
        play()
    elif play_again.lower() == 'n':
        break
    else:
        print('Invalid responce! Please try again. ')