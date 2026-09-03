import random

SUITS = ['♠', '♥', '♦', '♣']
RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

def card_value(card):
    rank = card['rank']
    if rank in ('J', 'Q', 'K'):
        return 10
    elif rank == 'A':
        return 11
    return int(rank)

def hand_value(hand):
    total = sum(card_value(c) for c in hand)
    aces = sum(1 for c in hand if c['rank'] == 'A')
    while total > 21 and aces > 0:
        total -= 10
        aces -= 1
    return total

def card_label(card):
    return f"{card['rank']}{card['suit']}"

def create_deck(num_decks=1):
    deck = [{'rank': r, 'suit': s} for _ in range(num_decks) for s in SUITS for r in RANKS]
    random.shuffle(deck)
    return deck

def new_game():
    deck = create_deck()
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]

    p_val = hand_value(player_hand)
    state = {
        'deck': deck,
        'player_hand': player_hand,
        'dealer_hand': dealer_hand,
        'player_value': p_val,
        'dealer_value': hand_value(dealer_hand),
        'game_over': False,
        'result': None,
        'message': 'Your move: hit for another card or stand.',
        'show_dealer': False
    }

    if p_val == 21:
        state['show_dealer'] = True
        d_val = hand_value(dealer_hand)
        if d_val == 21:
            state['game_over'] = True
            state['result'] = 'push'
            state['message'] = 'Both have Blackjack! Push.'
        else:
            state['game_over'] = True
            state['result'] = 'blackjack'
            state['message'] = 'Blackjack! You win!'

    return state

def hit(state):
    if state['game_over']:
        return state

    deck = list(state['deck'])
    player_hand = list(state['player_hand'])
    player_hand.append(deck.pop())
    p_val = hand_value(player_hand)
    new_state = {**state, 'deck': deck, 'player_hand': player_hand, 'player_value': p_val}

    if p_val > 21:
        new_state['game_over'] = True
        new_state['result'] = 'bust'
        new_state['message'] = f'Bust! You went over with {p_val}.'
        new_state['show_dealer'] = True
        new_state['dealer_value'] = hand_value(state['dealer_hand'])
    elif p_val == 21:
        return stand(new_state)

    return new_state

def stand(state):
    if state['game_over']:
        return state

    deck = list(state['deck'])
    dealer_hand = list(state['dealer_hand'])

    while hand_value(dealer_hand) < 17:
        dealer_hand.append(deck.pop())

    d_val = hand_value(dealer_hand)
    p_val = state['player_value']

    new_state = {
        **state,
        'deck': deck,
        'dealer_hand': dealer_hand,
        'dealer_value': d_val,
        'game_over': True,
        'show_dealer': True
    }

    if d_val > 21:
        new_state['result'] = 'win'
        new_state['message'] = f'Dealer busts with {d_val}! You win!'
    elif d_val > p_val:
        new_state['result'] = 'lose'
        new_state['message'] = f'Dealer has {d_val} vs your {p_val}. Dealer wins.'
    elif p_val > d_val:
        new_state['result'] = 'win'
        new_state['message'] = f'You have {p_val} vs dealer\'s {d_val}. You win!'
    else:
        new_state['result'] = 'push'
        new_state['message'] = f'Both have {p_val}. Push!'

    return new_state
