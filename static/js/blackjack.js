let gameActive = false;
let bjWins = 0, bjLosses = 0, bjPushes = 0;

async function newGame() {
    const res = await fetch('/api/blackjack/new', { method: 'POST' });
    const data = await res.json();
    gameActive = !data.game_over;
    render(data);
}

async function hit() {
    if (!gameActive) return;
    const res = await fetch('/api/blackjack/hit', { method: 'POST' });
    const data = await res.json();
    gameActive = !data.game_over;
    render(data);
}

async function stand() {
    if (!gameActive) return;
    const res = await fetch('/api/blackjack/stand', { method: 'POST' });
    const data = await res.json();
    gameActive = false;
    render(data);
}

function isRedCard(cardStr) {
    return cardStr && (cardStr.includes('♥') || cardStr.includes('♦'));
}

function renderCards(container, cards) {
    if (!container) return;
    container.innerHTML = '';
    cards.forEach(card => {
        const el = document.createElement('div');
        if (card === '🂠') {
            el.className = 'bj-card facedown';
            el.textContent = '🂠';
        } else {
            el.className = 'bj-card ' + (isRedCard(card) ? 'red' : 'black');
            el.textContent = card;
        }
        container.appendChild(el);
    });
}

function render(data) {
    renderCards(document.getElementById('player-cards'), data.player_cards);
    renderCards(document.getElementById('dealer-cards'), data.dealer_cards);

    const pVal = document.getElementById('player-value');
    const dVal = document.getElementById('dealer-value');
    if (pVal) pVal.textContent = `(${data.player_value})`;
    if (dVal) dVal.textContent = data.show_dealer ? `(${data.dealer_value})` : '';

    const msg = document.getElementById('result-message');
    if (msg) msg.textContent = data.message;

    if (data.game_over) {
        const hitBtn = document.getElementById('hit-btn');
        const standBtn = document.getElementById('stand-btn');
        if (hitBtn) hitBtn.disabled = true;
        if (standBtn) standBtn.disabled = true;

        if (msg) {
            if (data.result === 'win' || data.result === 'blackjack') {
                msg.className = 'result-message win';
                bjWins++;
            } else if (data.result === 'lose' || data.result === 'bust') {
                msg.className = 'result-message lose';
                bjLosses++;
            } else {
                msg.className = 'result-message draw';
                bjPushes++;
            }
        }
        updateScores();
    } else {
        if (msg) msg.className = 'result-message';
        const hitBtn = document.getElementById('hit-btn');
        const standBtn = document.getElementById('stand-btn');
        if (hitBtn) hitBtn.disabled = false;
        if (standBtn) standBtn.disabled = false;
    }
}

function updateScores() {
    const w = document.getElementById('bj-wins');
    const l = document.getElementById('bj-losses');
    const p = document.getElementById('bj-pushes');
    if (w) w.textContent = bjWins;
    if (l) l.textContent = bjLosses;
    if (p) p.textContent = bjPushes;
}

newGame();
