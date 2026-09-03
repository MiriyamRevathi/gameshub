import random

SUITS = ['♠', '♥', '♦', '♣']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
RANK_VALUES = {r: i for i, r in enumerate(RANKS)}

def create_deck():
    deck = [{'rank': r, 'suit': s} for s in SUITS for r in RANKS]
    random.shuffle(deck)
    return deck

def card_label(card):
    return f"{card['rank']}{card['suit']}"

def compare_cards(card1, card2):
    v1 = RANK_VALUES[card1['rank']]
    v2 = RANK_VALUES[card2['rank']]
    if v1 > v2:
        return 1
    elif v2 > v1:
        return -1
    return 0

def new_game():
    deck = create_deck()
    mid = len(deck) // 2
    return {
        'player_deck': deck[:mid],
        'computer_deck': deck[mid:],
        'player_card': None,
        'computer_card': None,
        'war_pile': [],
        'result': None,
        'game_over': False,
        'winner': None,
        'round': 0,
        'message': 'Draw a card to begin the battle.'
    }

def play_round(state):
    if state['game_over']:
        return state

    p_deck = list(state['player_deck'])
    c_deck = list(state['computer_deck'])
    war_pile = list(state.get('war_pile', []))

    if not p_deck:
        return {**state, 'game_over': True, 'winner': 'computer',
                'message': 'Computer wins! You ran out of cards.'}
    if not c_deck:
        return {**state, 'game_over': True, 'winner': 'player',
                'message': 'You win! Computer ran out of cards.'}

    p_card = p_deck.pop(0)
    c_card = c_deck.pop(0)

    result = compare_cards(p_card, c_card)

    if result == 1:
        p_deck.extend(war_pile)
        p_deck.extend([p_card, c_card])
        message = f"You played {card_label(p_card)} vs {card_label(c_card)} — You win this round!"
        war_pile = []
    elif result == -1:
        c_deck.extend(war_pile)
        c_deck.extend([p_card, c_card])
        message = f"You played {card_label(p_card)} vs {card_label(c_card)} — Computer wins this round!"
        war_pile = []
    else:
        war_pile.extend([p_card, c_card])
        face_down = min(3, len(p_deck), len(c_deck))
        for _ in range(face_down):
            if p_deck and c_deck:
                war_pile.append(p_deck.pop(0))
                war_pile.append(c_deck.pop(0))
        message = f"WAR! Both played {card_label(p_card)} — {face_down} cards added to the pot!"

    game_over = False
    winner = None
    if not p_deck and not war_pile:
        game_over = True
        winner = 'computer'
        message = 'Computer wins! You ran out of cards.'
    elif not c_deck and not war_pile:
        game_over = True
        winner = 'player'
        message = 'You win! Computer ran out of cards.'

    return {
        'player_deck': p_deck,
        'computer_deck': c_deck,
        'player_card': card_label(p_card),
        'computer_card': card_label(c_card),
        'war_pile': war_pile,
        'result': 'win' if result == 1 else 'lose' if result == -1 else 'war',
        'game_over': game_over,
        'winner': winner,
        'round': state['round'] + 1,
        'message': message,
        'player_count': len(p_deck),
        'computer_count': len(c_deck)
    }
