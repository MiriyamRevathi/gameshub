from flask import Flask, render_template, request, jsonify, session, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
import sqlite3
import os

from games import rps, tictactoe, mastermind, war, blackjack

app = Flask(__name__)
app.secret_key = 'python-games-secret-key-2026'

# ─── Database ─────────────────────────────────────────────────────────

DATABASE = os.path.join(os.path.dirname(__file__), 'users.db')

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

init_db()

# ─── Auth Helpers ─────────────────────────────────────────────────────

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Please log in to access this page.', 'warning')
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function

def get_current_user():
    if 'user_id' in session:
        conn = get_db()
        user = conn.execute('SELECT * FROM users WHERE id = ?', (session['user_id'],)).fetchone()
        conn.close()
        return user
    return None

@app.context_processor
def inject_user():
    return {'current_user': get_current_user()}

# ─── Auth Routes ──────────────────────────────────────────────────────

@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'user_id' in session:
        return redirect(url_for('index'))

    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '')

        if not username or not password:
            flash('Please fill in all fields.', 'error')
            return render_template('login.html')

        conn = get_db()
        user = conn.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()
        conn.close()

        if user and check_password_hash(user['password_hash'], password):
            session['user_id'] = user['id']
            session['username'] = user['username']
            flash(f'Welcome back, {user["username"]}!', 'success')
            next_url = request.args.get('next', url_for('index'))
            return redirect(next_url)
        else:
            flash('Invalid username or password.', 'error')

    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if 'user_id' in session:
        return redirect(url_for('index'))

    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '')
        confirm_password = request.form.get('confirm_password', '')

        errors = []
        if not username or not email or not password:
            errors.append('All fields are required.')
        if len(username) < 3:
            errors.append('Username must be at least 3 characters.')
        if len(password) < 6:
            errors.append('Password must be at least 6 characters.')
        if password != confirm_password:
            errors.append('Passwords do not match.')
        if '@' not in email or '.' not in email:
            errors.append('Please enter a valid email address.')

        if errors:
            for error in errors:
                flash(error, 'error')
            return render_template('register.html')

        conn = get_db()
        existing = conn.execute(
            'SELECT id FROM users WHERE username = ? OR email = ?',
            (username, email)
        ).fetchone()

        if existing:
            flash('Username or email already exists.', 'error')
            conn.close()
            return render_template('register.html')

        password_hash = generate_password_hash(password)
        conn.execute(
            'INSERT INTO users (username, email, password_hash) VALUES (?, ?, ?)',
            (username, email, password_hash)
        )
        conn.commit()

        user = conn.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()
        conn.close()

        session['user_id'] = user['id']
        session['username'] = user['username']
        flash(f'Account created! Welcome, {username}!', 'success')
        return redirect(url_for('index'))

    return render_template('register.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out.', 'success')
    return redirect(url_for('index'))

# ─── Home ────────────────────────────────────────────────────────────

@app.route('/')
def index():
    return render_template('index.html')

# ─── Rock Paper Scissors ─────────────────────────────────────────────

@app.route('/rps')
@login_required
def rps_page():
    return render_template('rps.html')

@app.route('/api/rps/play', methods=['POST'])
def rps_play():
    data = request.get_json()
    choice = int(data.get('choice', 0))
    result = rps.play(choice)
    return jsonify(result)

# ─── Tic Tac Toe ─────────────────────────────────────────────────────

@app.route('/tictactoe')
@login_required
def tictactoe_page():
    return render_template('tictactoe.html')

@app.route('/api/tictactoe/new', methods=['POST'])
def tictactoe_new():
    state = tictactoe.new_game()
    session['ttt'] = state
    return jsonify(state)

@app.route('/api/tictactoe/move', methods=['POST'])
def tictactoe_move():
    data = request.get_json()
    position = int(data.get('position', 0))
    state = session.get('ttt', tictactoe.new_game())
    state = tictactoe.make_move(state, position)
    session['ttt'] = state
    return jsonify(state)

# ─── Mastermind ───────────────────────────────────────────────────────

@app.route('/mastermind')
@login_required
def mastermind_page():
    return render_template('mastermind.html')

@app.route('/api/mastermind/new', methods=['POST'])
def mastermind_new():
    state = mastermind.new_game()
    public = {k: v for k, v in state.items() if k != 'secret'}
    public['remaining'] = state['max_guesses'] - len(state['guesses'])
    session['mm'] = state
    return jsonify(public)

@app.route('/api/mastermind/guess', methods=['POST'])
def mastermind_guess():
    data = request.get_json()
    guess = data.get('guess', [])
    state = session.get('mm')
    if not state:
        state = mastermind.new_game()

    state = mastermind.make_guess(state, guess)
    session['mm'] = state

    public = {k: v for k, v in state.items() if k != 'secret'}
    public['remaining'] = state['max_guesses'] - len(state['guesses'])
    if state['game_over'] and not state['won']:
        public['secret'] = state['secret']
    return jsonify(public)

# ─── War ──────────────────────────────────────────────────────────────

@app.route('/war')
@login_required
def war_page():
    return render_template('war.html')

@app.route('/api/war/new', methods=['POST'])
def war_new():
    state = war.new_game()
    session['war'] = state
    return jsonify({
        'player_count': len(state['player_deck']),
        'computer_count': len(state['computer_deck']),
        'message': state['message'],
        'game_over': False,
        'round': 0
    })

@app.route('/api/war/play', methods=['POST'])
def war_play():
    state = session.get('war')
    if not state:
        state = war.new_game()
    state = war.play_round(state)
    session['war'] = state
    return jsonify({
        'player_card': state.get('player_card'),
        'computer_card': state.get('computer_card'),
        'result': state.get('result'),
        'message': state.get('message'),
        'game_over': state['game_over'],
        'winner': state.get('winner'),
        'round': state.get('round', 0),
        'player_count': state.get('player_count', len(state['player_deck'])),
        'computer_count': state.get('computer_count', len(state['computer_deck']))
    })

# ─── Blackjack ────────────────────────────────────────────────────────

@app.route('/blackjack')
@login_required
def blackjack_page():
    return render_template('blackjack.html')

def _blackjack_state_to_json(state):
    player_cards = [blackjack.card_label(c) for c in state['player_hand']]
    if state['show_dealer']:
        dealer_cards = [blackjack.card_label(c) for c in state['dealer_hand']]
        dealer_value = state['dealer_value']
    else:
        dealer_cards = [blackjack.card_label(state['dealer_hand'][0]), '🂠']
        dealer_value = blackjack.card_value(state['dealer_hand'][0])

    return {
        'player_cards': player_cards,
        'dealer_cards': dealer_cards,
        'player_value': state['player_value'],
        'dealer_value': dealer_value,
        'game_over': state['game_over'],
        'result': state.get('result'),
        'message': state['message'],
        'show_dealer': state['show_dealer']
    }

@app.route('/api/blackjack/new', methods=['POST'])
def blackjack_new():
    state = blackjack.new_game()
    session['bj'] = state
    return jsonify(_blackjack_state_to_json(state))

@app.route('/api/blackjack/hit', methods=['POST'])
def blackjack_hit():
    state = session.get('bj')
    if not state:
        state = blackjack.new_game()
    state = blackjack.hit(state)
    session['bj'] = state
    return jsonify(_blackjack_state_to_json(state))

@app.route('/api/blackjack/stand', methods=['POST'])
def blackjack_stand():
    state = session.get('bj')
    if not state:
        state = blackjack.new_game()
    state = blackjack.stand(state)
    session['bj'] = state
    return jsonify(_blackjack_state_to_json(state))

if __name__ == '__main__':
    app.run(debug=True, port=5000)
