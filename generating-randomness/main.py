from game import Game


if __name__ == "__main__":
    introduction = '''Let\'s play a game of prediction!

- You will be prompted to input binary digits (more than 100)
- The CPU will analyze your input as to be able to predict any further inputs.
It accomplishes this by grouping digits into triads and taking note of the digit that comes afterwards.

You start the game with a virtual capital of 1000 dollars.
Each round, input more binary digits for the CPU will try to predict.
Every time the program guesses a symbol correctly, you lose one dollar.
Every time the system is wrong, you gain one dollar.
The first 3 digits are random and do not count against prediction, so input more than 3 digits.
The game ends if you lose the whole capital or input \'enough\'.

Good luck!\n'''
    
    print(introduction)
    Game(1000).play()
