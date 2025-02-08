# Dice Rolling Game

## Overview
This is a simple **Dice Rolling Game** where 2 to 4 players compete over multiple rounds. Each player rolls a die, and the highest roll wins the round. The player with the most wins at the end of all rounds is declared the overall winner.

## Features
- Supports **2 to 4 players**.
- Players take turns rolling a **6-sided die**.
- If a player rolls a **6**, they get an extra roll, but only their highest roll counts.
- **Leaderboard tracking** after each round.
- **Winner determination** at the end of all rounds.

## How to Play
1. Run the Python script.
2. Enter the number of players (between 2 and 4).
3. Enter names for each player.
4. Enter the number of rounds.
5. The game proceeds round by round, showing results and a leaderboard.
6. At the end of all rounds, the overall winner is announced.

## Installation
Ensure you have Python installed (version 3.x recommended).

### Steps:
1. Copy the script into a Python file (e.g., `dice_game.py`).
2. Open a terminal or command prompt and navigate to the script location.
3. Run the script using:
   ```sh
   python dice_game.py
   ```

## Code Explanation
- `roll_dice()`: Rolls a 6-sided die and returns a random number (1-6).
- `play_round(players, scores)`: Each player rolls a die, and the highest roll wins the round.
- `display_leaderboard(scores)`: Displays the current standings after each round.
- `main()`: Handles user input, starts rounds, and determines the overall winner.

## Example Output
```
Enter the number of players (2-4): 3
Enter name for Player 1: Alice
Enter name for Player 2: Bob
Enter name for Player 3: Charlie
Enter number of rounds: 5

New Round!
Alice rolled: 3
Bob rolled: 5
Charlie rolled: 6
Charlie rolled a 6! Rolling again...
Charlie rolled: 2
Winner of this round: Bob

Leaderboard:
Alice: 0 wins
Bob: 1 wins
Charlie: 0 wins
...
Congratulations Bob! You are the overall winner!
```

## Future Enhancements
- Add an **option for different types of dice** (e.g., 8-sided, 12-sided).
- Introduce **special rules or power-ups**.
- Allow **automatic replays** for rematches.

## License
This project is open-source and free to use for learning and fun!

