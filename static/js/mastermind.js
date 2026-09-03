const COLOR_MAP = {
    red: '#e74c3c',
    blue: '#3498db',
    green: '#2ecc71',
    yellow: '#f1c40f',
    orange: '#e67e22',
    purple: '#9b59b6'
};

let currentGuess = [];
let gameOver = false;

async function newGame() {
    const res = await fetch('/api/mastermind/new', { method: 'POST' });
    const data = await res.json();
    currentGuess = [];
    gameOver = false;
    updateSlots();
    document.getElementById('history').innerHTML = '';
    document.getElementById('remaining').textContent = data.remaining;
    document.getElementById('result-message').textContent = 'Choose four colors and submit your first guess.';
    document.getElementById('result-message').className = 'result-message';
    document.getElementById('submit-btn').disabled = false;
    const att = document.getElementById('mm-attempts');
    if (att) att.textContent = '0';
}

function addColor(color) {
    if (gameOver || currentGuess.length >= 4) return;
    currentGuess.push(color);
    updateSlots();
}

function removeSlot(idx) {
    if (gameOver || idx >= currentGuess.length) return;
    currentGuess.splice(idx, 1);
    updateSlots();
}

function clearGuess() {
    currentGuess = [];
    updateSlots();
}

function updateSlots() {
    const slots = document.querySelectorAll('.mm-slot');
    slots.forEach((slot, i) => {
        if (i < currentGuess.length) {
            slot.style.background = COLOR_MAP[currentGuess[i]];
            slot.classList.add('filled');
        } else {
            slot.style.background = 'transparent';
            slot.classList.remove('filled');
        }
    });
}

async function submitGuess() {
    if (gameOver || currentGuess.length !== 4) return;

    const res = await fetch('/api/mastermind/guess', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ guess: currentGuess })
    });
    const data = await res.json();

    document.getElementById('remaining').textContent = data.remaining;
    const att = document.getElementById('mm-attempts');
    if (att) att.textContent = data.guesses ? data.guesses.length : '0';

    const history = document.getElementById('history');
    const lastGuess = data.guesses[data.guesses.length - 1];
    const row = document.createElement('div');
    row.className = 'mm-row';

    lastGuess.colors.forEach(color => {
        const peg = document.createElement('div');
        peg.className = 'mm-peg';
        peg.style.background = COLOR_MAP[color];
        row.appendChild(peg);
    });

    const fb = document.createElement('div');
    fb.className = 'mm-feedback';
    for (let i = 0; i < lastGuess.exact; i++) {
        const p = document.createElement('div');
        p.className = 'mm-feedback-peg exact';
        fb.appendChild(p);
    }
    for (let i = 0; i < lastGuess.partial; i++) {
        const p = document.createElement('div');
        p.className = 'mm-feedback-peg partial';
        fb.appendChild(p);
    }
    for (let i = 0; i < 4 - lastGuess.exact - lastGuess.partial; i++) {
        const p = document.createElement('div');
        p.className = 'mm-feedback-peg empty';
        fb.appendChild(p);
    }
    row.appendChild(fb);
    history.appendChild(row);

    currentGuess = [];
    updateSlots();

    if (data.game_over) {
        gameOver = true;
        const msg = document.getElementById('result-message');
        if (data.won) {
            msg.textContent = '🎉 You cracked the code!';
            msg.className = 'result-message win';
        } else {
            msg.textContent = '😞 Game over! The secret code was:';
            msg.className = 'result-message lose';
            if (data.secret) {
                const reveal = document.createElement('div');
                reveal.className = 'mm-secret-reveal';
                data.secret.forEach(color => {
                    const peg = document.createElement('div');
                    peg.className = 'mm-peg';
                    peg.style.background = COLOR_MAP[color];
                    reveal.appendChild(peg);
                });
                history.appendChild(reveal);
            }
        }
        document.getElementById('submit-btn').disabled = true;
    }
}

newGame();
