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
