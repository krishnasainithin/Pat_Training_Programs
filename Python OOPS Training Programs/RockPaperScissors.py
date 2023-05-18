import random

CHOICES = ['rock','paper','scissors']


def get_player_choice():
    """Get user input and validate it is one of the choices above"""
    player_choice = None
    while player_choice is None:
        player_choice = input('Choices: \nRock \nPaper \nScissors \n\nPick: ')
        if player_choice.lower() not in CHOICES:
            player_choice = None
    return player_choice.lower()


def get_computer_choice():
    """Have the computer pick one of the valid choices at random"""
    computer_choice = random.randint(0, 2)
    computer_choice = CHOICES[computer_choice]
    return computer_choice


def is_draw(player_choice, computer_choice):
    """Check if game was a draw"""
    if player_choice == computer_choice:
        return True


def print_winner(player_choice, computer_choice):
    """Check to see who won"""
    if player_choice == 'rock' and computer_choice == 'scissors':
        print('Player wins!')
    elif player_choice == 'scissors' and computer_choice == 'paper':
        print('Player wins!')
    elif player_choice == 'paper' and computer_choice == 'rock':
        print('Player wins!')
    else:
        print('Computer wins!')
        print('%s beats %s' % (computer_choice, player_choice))


def play_game():
    """play the game"""
    player_choice = get_player_choice()
    computer_choice = get_computer_choice()
    if is_draw(player_choice, computer_choice):
        print("It's a draw, both players picked %s: " % player_choice)
    else:
        print("Computer picked: %s" % computer_choice)
        print("Player picked: %s" % player_choice)
        print_winner(player_choice, computer_choice)


if __name__ == "__main__":
    play_game()