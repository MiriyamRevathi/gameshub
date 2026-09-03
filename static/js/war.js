let gameRunning = false;

async function newGame() {
    const res = await fetch('/api/war/new', { method: 'POST' });
    const data = await res.json();
    gameRunning = true;

    document.getElementById('player-count').textContent = data.player_count;
    document.getElementById('computer-count').textContent = data.computer_count;
    document.getElementById('round-num').textContent = '0';
    document.getElementById('player-card').textContent = '🂠';
    document.getElementById('computer-card').textContent = '🂠';
    document.getElementById('player-card').className = 'playing-card';
    document.getElementById('computer-card').className = 'playing-card';
    document.getElementById('result-message').textContent = data.message;
    document.getElementById('result-message').className = 'result-message';
    document.getElementById('draw-btn').disabled = false;
}

function isRedSuit(cardStr) {
    return cardStr && (cardStr.includes('♥') || cardStr.includes('♦'));
}

async function drawCard() {
    if (!gameRunning) return;

    const res = await fetch('/api/war/play', { method: 'POST' });
    const data = await res.json();

    const pCard = document.getElementById('player-card');
    const cCard = document.getElementById('computer-card');

    pCard.textContent = data.player_card || '🂠';
    cCard.textContent = data.computer_card || '🂠';

    pCard.className = 'playing-card ' + (isRedSuit(data.player_card) ? 'red' : 'black');
    cCard.className = 'playing-card ' + (isRedSuit(data.computer_card) ? 'red' : 'black');

    document.getElementById('player-count').textContent = data.player_count;
    document.getElementById('computer-count').textContent = data.computer_count;
    document.getElementById('round-num').textContent = data.round;

    const msg = document.getElementById('result-message');
    msg.textContent = data.message;
    if (data.result === 'win') {
        msg.className = 'result-message win';
    } else if (data.result === 'lose') {
        msg.className = 'result-message lose';
    } else {
        msg.className = 'result-message draw';
    }

    if (data.game_over) {
        gameRunning = false;
        document.getElementById('draw-btn').disabled = true;
        if (data.winner === 'player') {
            msg.className = 'result-message win';
        } else {
            msg.className = 'result-message lose';
        }
    }
}

newGame();
