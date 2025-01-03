# Tic-Tac-Toe
Simple Tic-Tac-Toe game in Python

Overview

This is a simple implementation of the classic Tic Tac Toe game in Python. The game allows two players to play alternately and determines the winner or declares a draw based on the rules of the game. The moves and results of each game are saved in a text file for record-keeping.

Features

Two-player game: Player 1 uses X and Player 2 uses O.
Interactive gameplay with real-time board updates.
Automatic detection of winning conditions.
Records game details including date, time, moves, and results to a file (game_data_new.txt).


Gameplay Instructions

The game begins by displaying a welcome message and the initial game board.
Players take turns to choose a position (1-9) to place their marker (X or O) on the board.
The game checks for invalid moves and prompts the player to choose again if necessary.
The game ends when one player wins or all positions are filled, resulting in a draw.
The result and moves are saved in the game_data_new.txt file.

Code Breakdown

Functions:
save_game_data(moves, result):
Saves game details (date, time, moves, and result) to game_data_new.txt.
welcome():
Displays a welcome message and the initial game board.
dimension_change(arr):
Converts the 2D board array into a 1D list for easier winning condition checks.
winning(wins):
Checks if a player has met any winning conditions.
board(arr):
Displays the current state of the board.
player1() and player2():
Handles moves for Player 1 and Player 2 respectively.
play():
Orchestrates the game flow, manages turns, checks for winners, and saves game data.


Saving Game Data:
The save_game_data(moves, result) function is responsible for handling file operations.
It opens a file named game_data_new.txt in append mode ("a"), ensuring previous game records are not overwritten.
The following details are written to the file:
The current date and time using datetime.now().
A list of all moves made by the players.
The result of the game (e.g., Player 1 wins, Player 2 wins, or Draw).
A separator (= repeated 30 times) to differentiate game records.
