import random

EMPTY = ''
PLAYER_X = 'X'
PLAYER_O = 'O'

WIN_COMBOS = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],
    [0, 3, 6], [1, 4, 7], [2, 5, 8],
    [0, 4, 8], [2, 4, 6]
]

def new_game():
    return {
        'board': [EMPTY] * 9,
        'current_player': PLAYER_X,
        'winner': None,
        'game_over': False
    }

def check_winner(board):
    for combo in WIN_COMBOS:
        a, b, c = combo
        if board[a] and board[a] == board[b] == board[c]:
            return board[a]
    if all(cell != EMPTY for cell in board):
        return 'draw'
    return None

def make_move(state, position):
    board = list(state['board'])
    if state['game_over'] or board[position] != EMPTY:
        return state

    board[position] = PLAYER_X
    winner = check_winner(board)
    if winner:
        return {
            'board': board,
            'current_player': PLAYER_O,
            'winner': winner,
            'game_over': True,
            'winning_combo': _get_winning_combo(board) if winner not in (None, 'draw') else None
        }

    empty = [i for i, cell in enumerate(board) if cell == EMPTY]
    if empty:
        comp_move = _get_best_move(board, empty)
        board[comp_move] = PLAYER_O
        winner = check_winner(board)
        if winner:
            return {
                'board': board,
                'current_player': PLAYER_X,
                'winner': winner,
                'game_over': True,
                'winning_combo': _get_winning_combo(board) if winner not in (None, 'draw') else None
            }

    return {
        'board': board,
        'current_player': PLAYER_X,
        'winner': None,
        'game_over': False,
        'winning_combo': None
    }

def _get_winning_combo(board):
    for combo in WIN_COMBOS:
        a, b, c = combo
        if board[a] and board[a] == board[b] == board[c]:
            return combo
    return None

def _get_best_move(board, empty):
    for pos in empty:
        test = list(board)
        test[pos] = PLAYER_O
        if check_winner(test) == PLAYER_O:
            return pos

    for pos in empty:
        test = list(board)
        test[pos] = PLAYER_X
        if check_winner(test) == PLAYER_X:
            return pos

    if 4 in empty:
        return 4

    corners = [i for i in [0, 2, 6, 8] if i in empty]
    if corners:
        return random.choice(corners)

    return random.choice(empty)
