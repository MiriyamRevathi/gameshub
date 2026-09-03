import random

CODE_LENGTH = 4
MAX_GUESSES = 10
COLORS = ['red', 'blue', 'green', 'yellow', 'orange', 'purple']

def new_game():
    secret = [random.choice(COLORS) for _ in range(CODE_LENGTH)]
    return {
        'secret': secret,
        'guesses': [],
        'max_guesses': MAX_GUESSES,
        'game_over': False,
        'won': False,
        'colors': COLORS
    }

def check_guess(secret, guess):
    exact = 0
    partial = 0
    secret_remaining = []
    guess_remaining = []

    for i in range(CODE_LENGTH):
        if guess[i] == secret[i]:
            exact += 1
        else:
            secret_remaining.append(secret[i])
            guess_remaining.append(guess[i])

    for color in guess_remaining:
        if color in secret_remaining:
            partial += 1
            secret_remaining.remove(color)

    return {'exact': exact, 'partial': partial}

def make_guess(state, guess):
    if state['game_over']:
        return state

    result = check_guess(state['secret'], guess)
    state['guesses'].append({
        'colors': guess,
        'exact': result['exact'],
        'partial': result['partial']
    })

    if result['exact'] == CODE_LENGTH:
        state['game_over'] = True
        state['won'] = True
    elif len(state['guesses']) >= state['max_guesses']:
        state['game_over'] = True
        state['won'] = False

    return state
