# Games in Python

A collection of classic board and card games built in Python to explore different libraries and concepts.

## Games

| Game | Status | UI |
|------|--------|-----|
| Rock Paper Scissors | Complete | Web |
| Mastermind | Complete | Web |
| Tic Tac Toe | Complete | Web |
| Snake | Complete | Pygame |
| War | Complete | Web |
| Blackjack | In Progress | Web |
| Tic Tac Toe (AI) | Planned | Web |
| Game of Life | Planned | TBD |

## Architecture

```
┌─────────────────────────────────────────────┐
│              Frontend (Browser)              │
│         HTML / CSS / JavaScript              │
└─────────────────┬───────────────────────────┘
                  │ API calls (JSON)
                  ▼
┌─────────────────────────────────────────────┐
│          Python Backend (Flask)              │
│            All game logic here               │
└─────────────────────────────────────────────┘
```

- **Web Games**: Flask backend serves game logic via API, frontend handles rendering and user interaction
- **Snake**: Standalone Pygame application with graphics and audio

## Folder Structure

```
python-games/
├── app.py                  # Flask application entry point
├── requirements.txt        # Python dependencies
├── README.md
│
├── games/                  # Game logic modules
│   ├── __init__.py
│   ├── rps.py              # Rock Paper Scissors
│   ├── tictactoe.py        # Tic Tac Toe
│   ├── mastermind.py       # Mastermind
│   ├── war.py              # War (card game)
│   └── blackjack.py        # Blackjack
│
├── static/                 # Frontend assets
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   ├── rps.js
│   │   ├── tictactoe.js
│   │   ├── mastermind.js
│   │   ├── war.js
│   │   └── blackjack.js
│   └── images/
│
├── templates/              # HTML templates
│   ├── base.html           # Base template
│   ├── index.html          # Home page (game selection)
│   ├── rps.html
│   ├── tictactoe.html
│   ├── mastermind.html
│   ├── war.html
│   └── blackjack.html
│
└── snake_game/             # Standalone Pygame game
    ├── main.py
    └── resources/
        ├── apple.jpg
        ├── block.jpg
        ├── bg.jpg
        ├── bg_music_1.mp3
        ├── ding.mp3
        └── crash.mp3
```

## Running the Games

### Web Games
```bash
pip install -r requirements.txt
python app.py
# Open http://localhost:5000 in your browser
```

### Snake (Pygame)
```bash
cd snake_game
pip install pygame
python main.py
```

## Tech Stack

- **Backend**: Python, Flask
- **Frontend**: HTML, CSS, JavaScript
- **Snake Game**: Python, Pygame
