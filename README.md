# Sudoku Solver

This project is an interactive Sudoku game that enables players to solve Sudoku puzzles through an intuitive graphical interface. It's constructed using the pygame library and primarily employs a backtracking algorithm for puzzle-solving, while also providing puzzle-generation capabilities.
## Features

- **Interactive Sudoku Grid**: Players can click on individual cells to select them and input numbers.
- **Temporary Number Input**: Allows players to sketch potential numbers before finalizing their decision.
- **Time Tracking**: Displays the time elapsed since the player started solving the puzzle.
- **Dynamic Difficulty Selection**: Players can choose the difficulty level for the Sudoku puzzle.
- **Auto-Solving Capability**: With the press of a key, the game can automatically solve the Sudoku puzzle.
- **Help and Instructions**: Provides a popup with game rules and instructions for new players.

## Classes and Functions

- **Cube**: Represents an individual cell in the Sudoku grid, responsible for storing the cell's value and rendering its state.
- **Grid**: Represents the main Sudoku grid. It manages the cubes, validates user inputs, and handles the puzzle-solving logic.
- **Helper Functions**:
  - `find_empty()`: Locates the first empty cell in the Sudoku grid.
  - `valid()`: Checks if a number can be validly placed in a particular cell.
  - `redraw_window()`: Updates the game display, showing the Sudoku grid, elapsed time, and strikes.
  - `format_time()`: Converts seconds into a readable time format.

## How to Play

1. Launch the game.
2. Click on an empty cell in the Sudoku grid.
3. Input a number (1-9) using the keyboard.
4. Press the RETURN key to finalize the input.
5. Use the DELETE key to clear a cell's input.
6. Click on the help button for game instructions.
7. Use the SPACE key to auto-solve the puzzle.

## Getting Started

To run the game:

```bash
python main.py
```

**Note**: Ensure you have `pygame` installed and other dependencies if necessary.

## Future Work

- Enhance graphics and user interface.
- Implement different game modes, such as a timed challenge.
- Allow users to save and load game progress.

## Contributions

Contributions, bug reports, and feature requests are welcome! Feel free to open an issue or submit a pull request.

## License

This project is open-source and available under the [MIT License](LICENSE).

## Acknowledgements

Thanks to the pygame community for their invaluable resources and tutorials.
