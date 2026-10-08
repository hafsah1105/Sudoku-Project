# Python-Sudoku-Project

A graphical Sudoku application developed in Python using Pygame.

This project was originally developed as part of my sixth-form Computer Science work. It supports both standard 9×9 Sudoku and 4×4 Sudoku, allowing users to play generated puzzles or enter their own puzzle for the program to solve.

## Features

- 9×9 classic Sudoku
- 4×4 Sudoku
- Random puzzle generation
- Graphical interface built with Pygame
- User input validation
- Check submitted answers
- Delete user-entered values
- Enter and solve your own Sudoku puzzle
- Recursive backtracking solver
- Prevents users from overwriting the original puzzle values

## How It Works

The Sudoku board is represented using a two-dimensional list.

For generated puzzles, the program creates a valid completed grid and removes selected values to create a playable puzzle.

When a user enters a number, the program checks the relevant row, column and sub-grid to determine whether the value can be placed in that position.

The solver uses recursion and backtracking. It identifies the possible values for an empty cell, tries each possible value and recursively attempts to complete the remaining grid. If a choice does not lead to a valid solution, the program backtracks and tries another value.

## Technologies

- Python
- Pygame

## Running the Project

### 1. Install Python

Python 3 is required.

### 2. Install Pygame

```bash
pip install pygame
```

### 3. Run the Application

If the Python file is named `sudoku.py`:

```bash
python sudoku.py
```

If using the original filename:

```bash
python finalsudoku.py
```

## Controls

The application includes the following options:

- **Solve** - solves the current Sudoku puzzle
- **Check** - checks the answers entered by the user
- **Delete** - removes a user-entered value from the selected cell
- **Solve Your Own** - clears the board so the user can enter their own Sudoku puzzle
- **Classic** - generates a new 9×9 Sudoku puzzle
- **4x4** - generates a new 4×4 Sudoku puzzle
- **Exit** - closes the application

Numbers can be entered using either the keyboard or the number buttons displayed in the application.

## What I Learned

This project gave me experience with:

- Python programming
- Recursion and backtracking
- Algorithmic problem-solving
- Two-dimensional data structures
- Input validation
- Building a graphical interface using Pygame
- Breaking a larger problem into smaller functions

## Future Improvements

If I were to continue developing the project, I would consider:

- Refactoring the code to reduce the use of global variables
- Separating the Sudoku logic and graphical interface into different modules
- Adding automated tests
- Improving the puzzle-generation process and introducing difficulty levels
- Improving error handling
- Further improving the user interface
