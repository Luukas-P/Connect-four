# Connect Four Game

A classic Connect Four game implementation with a graphical user interface built using Python and Tkinter.

## Description

This is a two-player Connect Four game where players take turns dropping colored pieces into a 6x7 grid. The objective is to be the first player to connect four of your pieces vertically, horizontally, or diagonally.

Note: This was my first larger Python project, created while learning to program on my first ever programming course. It represents my introduction to object-oriented programming, GUI development with Tkinter, and game logic implementation.

## Features

- **Customizable Player Colors**: Each player can choose their own piece color using a color picker
- **Score Tracking**: Keeps track of wins for both players across multiple games
- **Interactive GUI**: Clean and intuitive interface built with Tkinter
- **Game Rules**: Built-in rules display accessible from the menu
- **Random Starting Player**: Each new game randomly selects which player goes first
- **Draw Detection**: Automatically detects when the board is full with no winner

## Requirements

- Python 3.x
- Tkinter (usually included with Python)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/connect-four-game.git
cd connect-four-game
```

2. Ensure you have Python 3 installed:
```bash
python --version
```

3. Tkinter should be included with your Python installation. If not, install it:
   - **Ubuntu/Debian**: `sudo apt-get install python3-tk`
   - **macOS**: Included with Python
   - **Windows**: Included with Python

## How to Play

1. Run the game:
```bash
python connect_four.py
```

2. Both players must select their piece colors by clicking the "Player 1 Color" and "Player 2 Color" buttons

3. Once both colors are selected, the game begins

4. Click on the column where you want to drop your piece

5. The piece will fall to the lowest available position in that column

6. Continue taking turns until one player connects four pieces or the board fills up (draw)

7. After each game, the score updates automatically and a new game begins

## Game Rules

- The game is played on a 6x7 grid
- Players take turns dropping their pieces from the top
- Pieces occupy the lowest free space in the selected column
- The goal is to connect four pieces vertically, horizontally, or diagonally
- The first player to connect four pieces wins

## Project Structure

```
connect-four-game/
├── connect_four.py    # Main game file
└── README.md          # This file
```

## Classes

- **Player**: Represents a player with name, color, and score attributes
- **Board**: Manages the game board state and piece rendering
- **ConnectFour**: Main game class that handles game logic, GUI, and player interactions

## Menu Options

- **Rules**: Displays the game rules in a popup window
- **Quit**: Exits the game

## Notes

- Colors cannot be changed once both players have selected them
- The game window is fixed size and cannot be resized
- Player who starts each round is randomly selected
- Score persists across multiple rounds until the application is closed

## License

This project is open source and available under the MIT License.
