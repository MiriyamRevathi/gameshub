import random

def play(player_choice):
    labels = ['Rock', 'Paper', 'Scissors']
    emojis = ['🪨', '📄', '✂️']
    computer_choice = random.randint(0, 2)

    if player_choice == computer_choice:
        result = 'draw'
    elif (player_choice == 0 and computer_choice == 2) or \
         (player_choice == 1 and computer_choice == 0) or \
         (player_choice == 2 and computer_choice == 1):
        result = 'win'
    else:
        result = 'lose'

    return {
        'player_choice': player_choice,
        'computer_choice': computer_choice,
        'player_label': f'{emojis[player_choice]} {labels[player_choice]}',
        'computer_label': f'{emojis[computer_choice]} {labels[computer_choice]}',
        'result': result
    }
