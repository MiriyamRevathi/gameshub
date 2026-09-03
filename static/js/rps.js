let wins = 0, losses = 0, draws = 0;
const emojis = ['✊', '✋', '✌️'];

async function play(choice) {
    const res = await fetch('/api/rps/play', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ choice })
    });
    const data = await res.json();

    document.getElementById('player-choice').textContent = emojis[data.player_choice];
    document.getElementById('computer-choice').textContent = emojis[data.computer_choice];

    const msg = document.getElementById('result-message');
    if (data.result === 'win') {
        msg.textContent = `You win! ${data.player_label} beats ${data.computer_label}`;
        msg.className = 'result-message win';
        wins++;
    } else if (data.result === 'lose') {
        msg.textContent = `You lose! ${data.computer_label} beats ${data.player_label}`;
        msg.className = 'result-message lose';
        losses++;
    } else {
        msg.textContent = `Draw! Both chose ${data.player_label}`;
        msg.className = 'result-message draw';
        draws++;
    }

    document.getElementById('wins').textContent = wins;
    document.getElementById('losses').textContent = losses;
    document.getElementById('draws').textContent = draws;
}
