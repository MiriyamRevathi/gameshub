let gameActive = false;
let tttWins = 0, tttLosses = 0, tttDraws = 0;

async function newGame() {
    const res = await fetch('/api/tictactoe/new', { method: 'POST' });
    const data = await res.json();
    gameActive = true;
    updateBoard(data);
    const msg = document.getElementById('result-message');
    if (msg) {
        msg.textContent = 'Your turn — you are X.';
        msg.className = 'result-message';
    }
}

async function makeMove(pos) {
    if (!gameActive) return;

    const cell = document.querySelector(`.ttt-cell[data-pos="${pos}"]`);
    if (cell && cell.classList.contains('taken')) return;

    const res = await fetch('/api/tictactoe/move', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ position: pos })
    });
    const data = await res.json();
    updateBoard(data);
}

function updateBoard(data) {
    const cells = document.querySelectorAll('.ttt-cell');
    cells.forEach((cell, i) => {
        cell.textContent = data.board[i] || '';
        cell.className = 'ttt-cell';
        if (data.board[i]) {
            cell.classList.add('taken');
            cell.classList.add(data.board[i].toLowerCase());
        }
    });

    if (data.winning_combo) {
        data.winning_combo.forEach(i => {
            if (cells[i]) cells[i].classList.add('winner-cell');
        });
    }

    if (data.game_over) {
        gameActive = false;
        const msg = document.getElementById('result-message');
        if (data.winner === 'X') {
            msg.textContent = '🎉 You win! Great line.';
            msg.className = 'result-message win';
            tttWins++;
        } else if (data.winner === 'O') {
            msg.textContent = '💻 The AI takes this game.';
            msg.className = 'result-message lose';
            tttLosses++;
        } else {
            msg.textContent = "🤝 Draw game — no more moves remain.";
            msg.className = 'result-message draw';
            tttDraws++;
        }
        updateScores();
    }
}

function updateScores() {
    const pEl = document.getElementById('ttt-player-score');
    const aiEl = document.getElementById('ttt-ai-score');
    const dEl = document.getElementById('ttt-draw-score');
    if (pEl) pEl.textContent = tttWins;
    if (aiEl) aiEl.textContent = tttLosses;
    if (dEl) dEl.textContent = tttDraws;
}

newGame();
