# ScrabbleGame

A complete scrabble game written in Python3 with the following features:

* challenge mode
* time limit
* point limit
* multiplayer on a single computer
* multiplayer over LAN
* playing against the computer

You can choose different options from the game interface.

If you don't know how to play Scrabble, click [here](https://scrabble.hasbro.com/en-us/rules) for rules

Clone the game and enjoy it. If you have any feedback, I would very much appreciate it.

## How to Play

### Start a game

#### Windows

Go to the _py_scrabble_gui_ folder and double click on `py_scrabble.pyw`.

#### Unix-based OS

On the terminal, `cd` into _py_scrabble_gui_ folder and run `python3 py_scrabble.pyw`. You can also run `chmod +x py_scrabble.pyw` and make the file executable.

### Blank tile

Simply place a blank tile on the spot of the letter you want to replace it with. When you submit your word, a pop-up will ask you what letter it should be replaced with.

### Challenge mode

The challenge mode is according to the double challenge rule. When activated, a player can challenge the words that the player before him or her has placed on the board. If one of the words is not valid, the previous player's turn will be passed and word points will be subtracted. If the words are valid, the turn of the player who has challenged will be passed.

### Playing against computer

Computer goes through permutations of letters on its rack and picks the valid move with the most points. A turn for computer takes about 1 minute 20 seconds (on i5 1.6 GHz with 8 GB RAM) depending on the computer.

If you want to end the game while it is computer's turn and try to close the program, you will have to wait till the computer's permutations are over, which takes about 1 minute (on i5 1.6 GHz with 8 GB RAM).
